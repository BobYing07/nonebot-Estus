#oding = utf-8
# -*- coding:utf-8 -*-
import asyncio
import time

from nonebot import on_command, CommandSession
from nonebot.permission import *
from aiocqhttp import MessageSegment

judged_persons=[]
judge_var={}

@on_command('judge_apply', aliases=('裁决申请','申请裁决'),only_to_me=False,permission=EVERYBODY)
async def judge_apply(session: CommandSession):
    if len(session.event["message"])!=2:
        await session.send(message=MessageSegment.at(session.event['user_id']) + '请输入"裁决申请 类型 @某人"或者"申请裁决 类型 @某人"')
        return
    p1 = str(session.event["message"][0]).split(" ")[1]
    p2 = session.event["message"][1]
    if p2["type"] != "at":
        await session.send(message=MessageSegment.at(session.event['user_id'])+'请输入"裁决申请 类型 @某人"或者"申请裁决 类型 @某人"')
        return
    if p1=="禁言":
        judge_var[str(p2['data']['qq'])] = {"yes": 0, "no": 0, "class": "禁言"}
    elif p1=="踢出":
        judge_var[str(p2['data']['qq'])] = {"yes": 0, "no": 0, "class": "禁言"}
    else:
        await session.send(MessageSegment.at(session.event['user_id']) + "类型只有禁言和踢出")
        return
    await session.send(MessageSegment.at(session.event['user_id']) + "成功申请裁决\n" + '输入"支持裁决 @被裁决人"支持裁决\n' + '输入"反对裁决 @被裁决人"反对裁决\n' + "裁决将在3分钟后判决")

    @on_command('test', aliases=('test'), only_to_me=False, permission=EVERYBODY)
    async def test(session: CommandSession):
        print("1233123123")


    try:
        asyncio.ensure_future(test)
    except TypeError:
        pass


    asyncio.get_event_loop().run_forever()


@on_command('judge_apply_yes', aliases=('支持裁决'),only_to_me=False,permission=EVERYBODY)
async def judge_apply_yes(session: CommandSession):
    if len(session.event["message"])!=2:
        await session.send('请输入"支持裁决 @被裁决人"')
        return
    at_p = session.event["message"][1]
    if at_p["type"] != "at":
        await session.send('请输入"支持裁决 @被裁决人"')
        return
    await session.send(MessageSegment.at(session.event['user_id'])+"成功支持裁决")