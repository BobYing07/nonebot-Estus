#oding = utf-8
# -*- coding:utf-8 -*-

from nonebot import on_command, CommandSession
from nonebot.permission import *
from nonebot import on_notice, NoticeSession
import requests

__plugin_name__ = "基础指令"
__plugin_usage__ = r"""
一些Ganyu-bot的基础指令
/echo + 语言 -- 复读
/daily --每日一句
/about --关于
"""

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
    url = 'http://open.iciba.com/dsapi'
    res = requests.get(url)
    content_e = res.json()['content']
    content_c = res.json()['note']
    return [content_c, content_e]






@on_command("about",aliases=("关于","主人"),only_to_me=False,permission=EVERYBODY)
async def about(session:CommandSession):
    await session.send("nonebot-Ganyu是基于Onebot的QQ机器人\n"
                       "目前版本：alpha v1.0.1 beta\n"
                       "主人QQ：20203491392\n"
                       "机器人QQ：2581249284\n"
                       "机器人交流群：769394903\n"
                       "联系主人：2023491392@qq.com\n"
                       "Github链接：\nhttps://github.com/Ganyu2007/nonebot-Ganyu\n"
                       "友情链接：\nOnebot-YBOT，新一代qq机器人，基于Onebot实现与Nonebot库\nhttps://github.com/HeyYubadboy/YBOT \n"
                       )