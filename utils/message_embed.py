from discord import Embed


CHOICE_EMOJIS: list = ['\N{Regional Indicator Symbol Letter A}', '\N{Regional Indicator Symbol Letter B}', '\N{Regional Indicator Symbol Letter C}', '\N{Regional Indicator Symbol Letter D}']  # [ð¦, ð§, ð¨, ð©]


def usage_embed_maker() -> Embed:
    '''ã»ã¼M.A.botã®ä½¿ãæ¹ã®èª¬æã®åãè¾¼ã¿ãåå¾ããããã®é¢æ°

    Returns:
        Embed: ã»ã¼M.A.botã®ä½¿ãæ¹ã®èª¬æã®åãè¾¼ã¿
    '''
    embed = Embed(title="M.A.ã ãã", description="ã³ãã³ãä¸è¦§ãæãã¦ãããã¼ï¼", color=0xff6a00)
    embed.add_field(name="/omaeda y2e", value="ãã®æä»£ã«èµ·ãã£ãåºæ¥äºãç­ããåé¡ãåºãã", inline=False)
    embed.add_field(name="/omaeda e2y", value="åºæ¥äºãèµ·ãã£ãæä»£ãå¿ããåé¡ãåºã", inline=False)
    embed.add_field(name="/omaeda s", value="åã¤ã®é¸æè¢ãå¹´ä»£é ã«ä¸¦ã¹ãåé¡ãåºããABCDãé çªã«ãªã¢ã¯ã·ã§ã³ãã¦ã­ã", inline=False)

    return embed


def y2e_embed_maker(year: str, options: list) -> Embed:
    '''y2eæ©è½ã®åé¡ãè¡¨ç¤ºããã¨ãã®åãè¾¼ã¿ãåå¾ããããã®é¢æ°

    Args:
        year (str): åé¡ã¨ãªãå¯¾è±¡ã®è¥¿æ¦
        options (list): é¸æè¢ãå«ã¾ãããªã¹ã

    Returns:
        Embed: y2eæ©è½ã®åé¡ãè¡¨ç¤ºããã¨ãã®åãè¾¼ã¿
    '''
    embed = Embed(title='M.A.ã ãã', description='***åé¡ï¼{}ã«èµ·ãã£ãåºæ¥äºãç­ããªããã***'.format(year), color=0xff6a00)
    for i in range(4):
        choice_emoji = CHOICE_EMOJIS[i]
        embed.add_field(name=choice_emoji, value=options[i][1], inline=False)
    embed.set_footer(text="âããããé¸ãã è¨å·ãæ¼ãã¦ã­â")

    return embed


def e2y_embed_maker(event: str, options: list) -> Embed:
    '''e2yæ©è½ã®åé¡ãè¡¨ç¤ºããã¨ãã®åãè¾¼ã¿ãåå¾ããããã®é¢æ°

    Args:
        event (str): åé¡ã¨ãªãå¯¾è±¡ã®åºæ¥äº
        options (list): é¸æè¢ãå«ã¾ãããªã¹ã

    Returns:
        Embed: e2yæ©è½ã®åé¡ãè¡¨ç¤ºããã¨ãã®åãè¾¼ã¿
    '''
    embed = Embed(title='M.A.ã ãã', description='***åé¡ï¼{}ãèµ·ãã£ãè¥¿æ¦ORæä»£ãç­ããªããã***'.format(event), color=0xff6a00)
    for i in range(4):
        choice_emoji = CHOICE_EMOJIS[i]
        embed.add_field(name=choice_emoji, value=options[i][0], inline=False)
    embed.set_footer(text="âããããé¸ãã è¨å·ãæ¼ãã¦ã­â")

    return embed


def s_embed_maker(timestamps: list):
    '''sæ©è½ã®åé¡ãè¡¨ç¤ºããã¨ãã®åãè¾¼ã¿ãåå¾ããããã®é¢æ°

    Args:
        timestamps (str): ä¸¦ã³æ¿ãã®åè£

    Returns:
        Embed: sæ©è½ã®åé¡ãè¡¨ç¤ºããã¨ãã®åãè¾¼ã¿
    '''
    embed = Embed(title='M.A.ã ãã', description='***åé¡ï¼ä¸ã®åºæ¥äºãä¸¦ã³æ¿ããªããã***', color=0xff6a00)
    for i in range(4):
        choice_emoji = CHOICE_EMOJIS[i]
        embed.add_field(name=choice_emoji, value=timestamps[i][1], inline=False)

    embed.set_footer(text="âå·¦ããå³ã¸æä»£ãæ°ãããªãããã«è¨å·ãä¸¦ã³æ¿ãã¦ã­ï¼â")

    return embed
