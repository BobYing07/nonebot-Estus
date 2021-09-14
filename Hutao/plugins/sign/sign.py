import random
import time

from nonebot import on_command, CommandSession
from nonebot.permission import *
from aiocqhttp import MessageSegment
from Ganyu.service.bot_api import *


money_name="Beimo Coin"


@on_command('sign', aliases=('sign','签到','打卡'),only_to_me=False,permission=EVERYBODY)
async def sign(session: CommandSession):
    execuser_name=str(session.ctx["sender"]["user_id"])
    with open("ct.json","r") as f:
        content=json.load(f)

    state=0

    d=time.strftime("%Y/%m/%d",time.localtime())
    if content["sign"]["data"]!=d:
        content["sign"]["data"]=d
        content["sign"]["people"]=list()
        state = 1
    if execuser_name in content["sign"]["people"]:
        await session.send(MessageSegment.at(int(execuser_name))+"签过了你个沙比")
        return

    content["sign"]["people"].append(execuser_name)

    with open("ct.json", "w") as f:
        json.dump(content, f)

    if not (execuser_name in content["users"]):
        create_per(execuser_name)

    #给予经验
    give_jy=random.randint(200,350)
    if state==1:
        give_jy=random.randint(360,420)
    add_jy(give_jy,execuser_name)

    # 给予货币
    give_money = random.randint(200, 350)
    if state == 1:
        give_money = random.randint(360, 420)
    add_money(give_money,execuser_name)