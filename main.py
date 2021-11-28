from asyncio import TimeoutError
from discord import Client

from utils.message_embed import usage_embed_maker, y2e_embed_maker, e2y_embed_maker
from utils.timeline import Timeline


TIMELINE_DATA_PATH = 'timeline_data.csv'
CHOICE_EMOJIS: list = ['\N{Regional Indicator Symbol Letter A}', '\N{Regional Indicator Symbol Letter B}', '\N{Regional Indicator Symbol Letter C}', '\N{Regional Indicator Symbol Letter D}']  # [🇦, 🇧, 🇨, 🇩]

client = Client()
timeline = Timeline(TIMELINE_DATA_PATH)


@client.event
async def on_ready():
    print('スタートしました！')


@client.event
async def on_message(message):
    if message.content.startswith('/omaeda'):
        channel = message.channel
        arg = message.content.split()

        if len(arg) == 1:
            await message.channel.send(embed=usage_embed_maker())
            return

        if arg[1].lower() == 'y2e':
            # 下準備
            tgt_timestamp = timeline.get_timestamp()
            options = timeline.get_option_from_timestamp(tgt_timestamp)
            answer = options.index(tgt_timestamp)

            # 問題を埋め込みで表示
            question_message = await channel.send(embed=y2e_embed_maker(tgt_timestamp[0], options))

            # 選択肢ボタンを表示
            for index in range(4):
                await question_message.add_reaction(CHOICE_EMOJIS[index])

            # 選択ボタンを押すのを待ち、処理をする
            def check(reaction, user):
                return str(reaction.emoji) in CHOICE_EMOJIS

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
                if user == message.author and CHOICE_EMOJIS.index(reaction.emoji) == answer:
                    await channel.send('<@{}>！正解です！'.format(user.id))
                else:
                    await channel.send('<@{}>！不正解です！正解は{}でした！'.format(user.id, CHOICE_EMOJIS[answer]))
            except TimeoutError:
                await channel.send('時間切れですー！乙デェス')
            
            return

        if arg[1].lower() == 'e2y':
            # 下準備
            tgt_timestamp = timeline.get_timestamp()
            options = timeline.get_option_from_timestamp(tgt_timestamp)
            answer = options.index(tgt_timestamp)

            # 問題を埋め込みで表示
            question_message = await channel.send(embed=e2y_embed_maker(tgt_timestamp[1], options))

            # 選択肢ボタンを表示
            for index in range(4):
                await question_message.add_reaction(CHOICE_EMOJIS[index])

            # 選択ボタンを押すのを待ち、処理をする
            def check(reaction, user):
                return str(reaction.emoji) in CHOICE_EMOJIS

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
                if user == message.author and CHOICE_EMOJIS.index(reaction.emoji) == answer:
                    await channel.send('<@{}>！正解です！'.format(user.id))
                else:
                    await channel.send('<@{}>！不正解です！正解は{}でした！'.format(user.id, CHOICE_EMOJIS[answer]))
            except TimeoutError:
                await channel.send('時間切れですー！乙デェス')

            return

        if arg[1].lower() == 's':
            return


# BOTスターーとおおお！！
TOKEN = input('M.A.が起きたぞおおお！！おはよお！Discord botのIDを教えてちょ！')
client.run(TOKEN)
