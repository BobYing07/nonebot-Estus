#coding = utf-8
# -*- coding:utf-8 -*-
"""
author:Beimo
Date:2021/8/18
plugin:pause and start
"""
from nonebot import on_command, CommandSession
from nonebot.permission import *
from aiocqhttp import MessageSegment
@on_command('pause',aliases=("stop","停止"),only_to_me=False,permission=(SUPERUSER,GROUP_OWNER,GROUP_ADMIN))
async def pause(session:CommandSession):
    session.pause(message=MessageSegment.at(session.ctx['user_id']) + "您成功停止了机器人")


@on_command('start',aliases=("continue","启动"),only_to_me=False,permission=(SUPERUSER,GROUP_OWNER,GROUP_ADMIN))
async def start(session:CommandSession):
    session.send("开发中")