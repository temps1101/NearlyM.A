from asyncio import TimeoutError
from os import getenv

from discord import Client

from utils.message_embed import usage_embed_maker, y2e_embed_maker, e2y_embed_maker, s_embed_maker
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
            await channel.send(embed=usage_embed_maker())
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
                return user == message.author and str(reaction.emoji) in CHOICE_EMOJIS

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
                if CHOICE_EMOJIS.index(reaction.emoji) == answer:
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
                return user == message.author and str(reaction.emoji) in CHOICE_EMOJIS

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
                if CHOICE_EMOJIS.index(reaction.emoji) == answer:
                    await channel.send('<@{}>！正解です！'.format(user.id))
                else:
                    await channel.send('<@{}>！不正解です！正解は{}でした！'.format(user.id, CHOICE_EMOJIS[answer]))
            except TimeoutError:
                await channel.send('時間切れですー！乙デェス')

            return

        if arg[1].lower() == 's':
            # 下準備
            sort_tgt_timestamps, mixed_tgt_timestamps = timeline.get_sort_tgt()
            answer = [mixed_tgt_timestamps.index(timestamp) for timestamp in sort_tgt_timestamps]
            user_answer = list()

            # 問題を埋め込みで表示
            await channel.send(embed=s_embed_maker(mixed_tgt_timestamps))

            # 並び替えの入力を受ける
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in CHOICE_EMOJIS
            while len(user_answer) != 4:
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                    user_answer.append(CHOICE_EMOJIS.index(reaction.emoji))

                except TimeoutError:
                    await channel.send('時間切れですー！乙デェス')
                    return

            if user_answer == answer:
                await channel.send('<@{}>！正解です！'.format(user.id))
            else:
                await channel.send('<@{}>！不正解です！正解は{}→{}→{}→{}でした！'.format(user.id, *[CHOICE_EMOJIS[idx] for idx in answer]))


client.run(getenv('DISCORD_BOT_TOKEN'))
