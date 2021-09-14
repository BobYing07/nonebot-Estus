from nonebot import on_command,CommandSession
from nonebot.permission import *
from asyncio import sleep

__plugin_name__ = "原神"
__plugin_usage__ = r"""输入 /胡桃
即可模仿原神内的角色"""



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
    await sleep(1)
    await session.send("'别想投胎哦~'")