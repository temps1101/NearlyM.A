import asyncio
from threading import Thread
import discord

from timeline import Timeline
from question_embedder import y2e_embed_maker


TOKEN = ''
TIMELINE_DATA_PATH = 'timeline_data.csv'

HELP_EMBED = discord.Embed(title="M.A.だよ。", description="コマンド一覧を教えてあげるー！", color=0xff6a00)
HELP_EMBED.add_field(name="/omaeda y2e", value="その時代に起こった出来事を答える問題を出す。", inline=False)
HELP_EMBED.add_field(name="/omaeda e2y", value="出来事が起こった時代を応える問題を出す", inline=True)
HELP_EMBED.add_field(name="/omaeda o", value="四つの選択肢を年代順に並べる問題を出す。ABCDを順番にリアクションしてね。", inline=True)

client = discord.Client()
timeline = Timeline(TIMELINE_DATA_PATH)


@client.event
async def on_message(message):
    if message.content.startswith('/omaeda'):
        channel = message.channel
        arg = message.content.split()
        if len(arg) == 1:
            await message.channel.send(embed=HELP_EMBED)
        if arg[1].lower() == 'y2e':
            year_event_pair = timeline.get_year_event_pair()
            suggestions = timeline.get_suggestions_from_year_event_pair(year_event_pair)
            question_message = await channel.send(embed=y2e_embed_maker(year_event_pair[0], suggestions))
            answer =  suggestions.index(year_event_pair)

            for i in range(4):
                await question_message.add_reaction(['\N{Regional Indicator Symbol Letter A}', '\N{Regional Indicator Symbol Letter B}', '\N{Regional Indicator Symbol Letter C}', '\N{Regional Indicator Symbol Letter D}'][i])

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ['\N{Regional Indicator Symbol Letter A}', '\N{Regional Indicator Symbol Letter B}', '\N{Regional Indicator Symbol Letter C}', '\N{Regional Indicator Symbol Letter D}']
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
                if ['\N{Regional Indicator Symbol Letter A}', '\N{Regional Indicator Symbol Letter B}', '\N{Regional Indicator Symbol Letter C}', '\N{Regional Indicator Symbol Letter D}'].index(reaction.emoji) == answer:
                    await channel.send('<@{}>！正解です！'.format(user.id))
                else:
                    await channel.send('<@{}>！不正解です！正解は{}でした！'.format(user.id, ['\N{Regional Indicator Symbol Letter A}', '\N{Regional Indicator Symbol Letter B}', '\N{Regional Indicator Symbol Letter C}', '\N{Regional Indicator Symbol Letter D}'][suggestions.index(year_event_pair)]))
            except asyncio.TimeoutError:
                await channel.send('時間切れですー！乙デェス')

    if arg.lower() == 'e2y':
        year_event_pair = timeline.get_year_event_pair()
        suggestions = timeline.get_suggestions_from_year_event_pair(year_event_pair)


# BOTスターーとおおお！！
#job = Thread(target=client.run, args=(TOKEN,))
#job.start()
client.run(TOKEN)