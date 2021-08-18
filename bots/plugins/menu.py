#coding = utf-8
# -*- coding:utf-8 -*-
"""
author:Beimo
Date:2021/8/18
plugin:menu
"""
from nonebot import on_command, CommandSession
from nonebot.permission import *


@on_command('menu',aliases=('菜单','面板'),only_to_me=False,permission=EVERYBODY)
async def menu(session:CommandSession):
    await session.send(
        "--------菜单--------\n"
        "1.签到(sign)\n"
        "2.每日一句（daily)\n"
        "3.复读机(echo)\n"
        "4.游戏(尾随 + @某人)\n"
        "5.禁言(群主管理专用 ban)\n"
        "6.制裁（全体成员可用 judge)\n"
        "其他插件正在更新中\n"
        "--------**------------"
                       )
