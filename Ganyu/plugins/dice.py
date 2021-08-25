from nonebot import on_command, CommandSession
from nonebot.permission import *
from aiocqhttp import MessageSegment
import random

__plugin_name__ = "骰子"
__plugin_usage__ = """骰娘插件：
输入/dice即可游玩
"""


@on_command("dice",aliases=("骰子","随机"),permission=EVERYBODY,only_to_me=False)
async def dice(session:CommandSession):
    point = ['1','2','3','4','5','6']
    a = random.choice(point)
    await session.send(MessageSegment.at(session.ctx['user_id']) + "分数是：" + a)
