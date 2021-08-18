import random
import time

import requests
from nonebot import on_command, CommandSession
from nonebot.permission import *
import json
from aiocqhttp import MessageSegment

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
        await session.send(MessageSegment.at(int(execuser_name))+"今天您签到过了，无法签到了呢")
        return

    #给予经验
    give_jy=random.randint(200,350)
    if state==1:
        give_jy=random.randint(360,420)
    if not(execuser_name in content["users"]):
        content["users"][execuser_name]={"lv":0,"jy":0}
    content["users"][execuser_name]["jy"]+=give_jy


    content["sign"]["people"].append(execuser_name)

    with open("ct.json","w") as f:
        json.dump(content,f)

    if state==0:
        await session.send(MessageSegment.at(int(execuser_name))+f"签到成功"+MessageSegment.face(101)+f'\n你获得了{give_jy}经验~，你现在有{content["users"][execuser_name]["jy"]}经验'+MessageSegment.face(101)+f"\n今日有{len(content['sign']['people'])}人签到")
    if state==1:
        await session.send(MessageSegment.at(int(execuser_name)) + f"你是今天第一个签到的人"+MessageSegment.face(101)+f'\n获得了{give_jy}经验~~，你现在有{content["users"][execuser_name]["jy"]}经验')
