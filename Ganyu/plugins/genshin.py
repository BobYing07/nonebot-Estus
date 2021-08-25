from nonebot import CommandSession
from nonebot import on_command
from nonebot.permission import *
from Ganyu.service.limit import *
from random import choice

_chat_flmt = FreqLimiter(3)
_chat_flmt_notice = choice(["666您就是pvp大蛇是吧", "冷静1下", "阿伟，你又在调戏机器人欸，休息一下吧", "你怎么这么逊哦，天天调戏机器人"])
__plugin_name__ = "原神"
__plugin_usage__ = r"""输入 /胡桃，/温迪 
即可模仿原神内的角色"""





@on_command("wendi", aliases=("巴巴托斯", "温迪"), permission=EVERYBODY, only_to_me=False)
async def wind(session: CommandSession):
    await session.send("诶嘿")
    await session.send("做点正事吧，巴巴托斯")
    return

@on_command("hutao", aliases=("胡桃", "往生堂堂主"), permission=EVERYBODY, only_to_me=False)
async def hutao(session: CommandSession):
    try:
        bye = str(session.get('bye',prompt="来生意啦！请输入你想要迫害的彬彬:"))
        if len(str(bye).split(" ")) >= 2:
            await session.send("请直接输入迫害对象")
            return
        bye= str(bye)
    except ValueError and TypeError:
        await session.send("异常")
        return


    await session.send(
        "大" + bye + "病了，"
        "二" + bye + "瞧。"
        "三" + bye + "采药，"
        "四" + bye + "熬。"
        "五" + bye + "死了，"
        "六" + bye + "抬。"
        "七" + bye + "却说："
    )
    await session.send("'别想投胎哦~'")