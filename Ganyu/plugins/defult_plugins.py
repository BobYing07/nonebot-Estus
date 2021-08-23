#oding = utf-8
# -*- coding:utf-8 -*-
"""
Author:Beimo
Date:2021/8/21 00:13
集合了一些基础指令
有复读，欢迎，每日一句和面板
"""

from nonebot import on_command, CommandSession
from nonebot.permission import *
from nonebot import on_notice, NoticeSession
import requests

@on_command('echo',aliases=("重复","复读机"),only_to_me=False,permission=EVERYBODY)
async def echo(session: CommandSession):
    await session.send(session.state.get('message') or session.current_arg)



@on_notice('group_increase')
async def _(session: NoticeSession):
    await session.send('欢迎新群员')



@on_command('daily', aliases=('每日一句',"每天一句"),only_to_me=False)
async def daily(session: CommandSession):
    daily_send = await get_daily()
    await session.send(daily_send[0])
    await session.send(daily_send[1])


async def get_daily():
    daily_sentence = get_content()
    return daily_sentence

def get_content():
    url = 'http://www.weather.com.cn/data/cityinfo/101190408.html'
    res = requests.get(url)
    content_e = res.json()['content']
    content_c = res.json()['note']
    return [content_c, content_e]





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
        "7.游戏(/尾随 + @某人)\n"
        "其他插件正在更新中\n"
        "--------**------------"
                       )
