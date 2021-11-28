import discord


def y2e_embed_maker(year, suggestions):
    embed = discord.Embed(title='M.A.だよ。', description='***問題：{}に起こった出来事を答えなさい。***'.format(year), color=0xff6a00)
    for i in range(4):
        cuur_emoji = [':regional_indicator_a:', ':regional_indicator_b:', ':regional_indicator_c:', ':regional_indicator_d:'][i]
        embed.add_field(name=cuur_emoji, value=suggestions[i][1], inline=False)
    embed.set_footer(text="↓ここから選んだ記号を押してね↓")

    return embed


