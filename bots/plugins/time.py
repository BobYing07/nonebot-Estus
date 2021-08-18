#coding = utf-8
# -*- coding:utf-8 -*-
"""
author:Beimo
Date:2021/8/18
Plugin:random_pic
"""
import nonebot
from nonebot import on_command, CommandSession
from nonebot import scheduler
from nonebot import session
from aiocqhttp import MessageSegment
from nonebot.permission import *

@nonebot.scheduler.scheduled_job(
    'cron',
    # year=None,
    # month=None,
    # day=None,
    # week=None,
    day_of_week="mon,tue,wed,thu,fri",
    hour=7,
    # minute=None,
    # second=None,
    # start_date=None,
    # end_date=None,
    # timezone=None,
)
async def _():
    await session.bot.send_group_msg(message="早上好")