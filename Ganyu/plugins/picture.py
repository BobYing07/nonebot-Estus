#coding = utf-8
# -*- coding:utf-8 -*-
__plugin_name__ = '随机图片'
__plugin_usage__ = '发生随机二次元图片'

from nonebot import on_command, CommandSession
from aiocqhttp import MessageSegment
from nonebot.permission import *

@on_command('picture',aliases=('陈睿','图片'),only_to_me=False,permission=EVERYBODY)
async def picture(session:CommandSession):
    await session.send(message=MessageSegment.image(file="https://img.xjh.me/random_img.php"))


