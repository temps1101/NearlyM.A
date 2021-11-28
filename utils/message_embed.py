from discord import Embed
from . import CHOICE_EMOJIS


def usage_embed_maker() -> Embed:
    '''ほぼM.A.botの使い方の説明の埋め込みを取得するための関数

    Returns:
        Embed: ほぼM.A.botの使い方の説明の埋め込み
    '''
    embed = Embed(title="M.A.だよ。", description="コマンド一覧を教えてあげるー！", color=0xff6a00)
    embed.add_field(name="/omaeda y2e", value="その時代に起こった出来事を答える問題を出す。", inline=False)
    embed.add_field(name="/omaeda e2y", value="出来事が起こった時代を応える問題を出す", inline=False)
    embed.add_field(name="/omaeda o", value="四つの選択肢を年代順に並べる問題を出す。ABCDを順番にリアクションしてね。", inline=False)

    return embed


def y2e_embed_maker(year: str, options: list) -> Embed:
    '''y2e機能の問題を表示するときの埋め込みを取得するための関数

    Args:
        year (str): 問題となる対象の西暦
        options (list): 選択肢が含まれたリスト

    Returns:
        Embed: y2e機能の問題を表示するときの埋め込み
    '''
    embed = Embed(title='M.A.だよ。', description='***問題：{}に起こった出来事を答えなさい。***'.format(year), color=0xff6a00)
    for i in range(4):
        choice_emoji = CHOICE_EMOJIS[i]
        embed.add_field(name=choice_emoji, value=options[i][1], inline=False)
    embed.set_footer(text="↓ここから選んだ記号を押してね↓")

    return embed


def e2y_embed_maker(event: str, options: list) -> Embed:
    '''e2y機能の問題を表示するときの埋め込みを取得するための関数

    Args:
        event (str): 問題となる対象の出来事
        options (list): 選択肢が含まれたリスト

    Returns:
        Embed: e2ey機能の問題を表示するときの埋め込み
    '''
    embed = Embed(title='M.A.だよ。', description='***問題：{}が起こった西暦OR時代を答えなさい。***'.format(event), color=0xff6a00)
    for i in range(4):
        choice_emoji = CHOICE_EMOJIS[i]
        embed.add_field(name=choice_emoji, value=options[i][0], inline=False)
    embed.set_footer(text="↓ここから選んだ記号を押してね↓")

    return embed
