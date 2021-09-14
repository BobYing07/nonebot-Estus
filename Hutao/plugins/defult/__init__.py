#oding = utf-8
# -*- coding:utf-8 -*-
from nonebot import RequestSession
from nonebot import on_notice, NoticeSession, on_request
import pathlib
import nonebot
from .news import *

__plugin_name__ = "基础指令"
__plugin_usage__ = r"""一些基础些础指令
希望人没事
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



@on_command("goobul",aliases=("圈钱工作室","goobul工作室"),only_to_me=False,permission=EVERYBODY)
async def goobul(session:CommandSession):
    await session.send("No one can master Python Linux,Python Linux can make money and ignore GNU\n——goobul")






@on_command("about",aliases=("关于","主人"),only_to_me=False,permission=EVERYBODY)
async def about(session:CommandSession):
    await session.send("你不知道吗？往生堂第七十七代堂主就是胡桃我啦\n"
                       "目前版本：v0.0.1\n"
                       "主人QQ：20203491392\n"
                       "机器人QQ：2581249284\n"
                       "机器人交流群：769394903\n"
                       "联系主人：2023491392@qq.com\n"
                       "Github链接：\nhttps://github.com/Ganyu2007/nonebot-Hutao\n"
                       "友情链接：\nOnebot-YBOT，新一代qq机器人，基于Onebot实现与Nonebot库\nhttps://github.com/HeyYubadboy/YBOT \n"
                       )

bot = nonebot.get_bot()
sid = 2581249284

@on_request('friend')
async def auto_add_friend(session: RequestSession):
    await session.bot.set_friend_add_request(flag=session.event['flag'],self_id=sid,approve=True)
    await bot.send_private_msg(user_id=session.event['flag'],message="已自动添加好友",self_id=sid)

@on_request('group')
async def auto_add_group(session: RequestSession):
    await session.bot.set_group_add_request(flag=session.event['flag'],self_id=sid,approve=True,sub_type=session.event['sub_type'])
    await bot.send_group_msg(group_id=session.event['group_id'],message="已自动同意入群",self_id=session.event['self_id'])


@on_notice('group_increase')
async def _(session: NoticeSession):
    await session.send('有人进群了！')

@on_command('usage', aliases=("菜单","menu","用途","使用方法"),only_to_me=False,permission=EVERYBODY)
async def _(session: CommandSession):
    # 获取设置了名称的插件列表
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))

    arg = session.current_arg_text.strip().lower()
    if not arg:
        # 如果用户没有发送参数，则发送功能列表
        await session.send(
            '胡桃支持功能：\n'
            '=================\n'
            + '\n'.join(p.name for p in plugins)
            + "\n=================\n"
            + "输入 '/menu + 插件名称' 查看插件详情\n"
        )
        return

    # 如果发了参数则发送相应命令的使用帮助
    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)