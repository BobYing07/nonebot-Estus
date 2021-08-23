# -*- coding:utf-8 -*-
from nonebot import on_command, CommandSession
from nonebot.permission import *

mj=60*60

@on_command('ban', aliases=('ban','禁言'),only_to_me=False,permission=SUPERUSER)
async def ban(session: CommandSession):
    try:
        qqn=str(session.get('data', prompt='你想禁言哪个人，请输入Ta的qq号'))
        if len(str(qqn).split(" ")) >= 2:
            await session.send("请直接输入qq号")
            return
        qqn=int(qqn)
    except ValueError:
        await session.send("异常：qq号错误或此人不存在")
        return
    try:
        qqt=int(session.get('data2', prompt='禁言时长(分钟)'))
    except ValueError:
        await session.send("请输入整数")
        return





    if str(qqn)==str(session.ctx['self_id']):
        await session.send("请勿输入自己的qq号")
        return
    await session.bot.set_group_ban(
        group_id=session.ctx['group_id'],user_id=qqn,duration=qqt*mj,self_id=session.ctx['self_id']
    )
    await session.send("成功禁言")



@ban.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['data'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要禁言的qq号不能为空，请重新输入')
    session.state[session.current_key] = stripped_arg

@ban.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['data2'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要禁言的时长不能为空，请重新输入')
    session.state[session.current_key] = stripped_arg



@on_command('kick', aliases=('kick','踢出'),only_to_me=False,permission=(SUPERUSER,GROUP_OWNER))
async def kick(session: CommandSession):
    try:
        qqn=str(session.get('data', prompt='你想移除哪个人，请输入Ta的qq号'))
        if len(str(qqn).split(" ")) >= 2:
            await session.send("请直接输入qq号")
            return
        qqn=int(qqn)
    except ValueError:
        await session.send("异常：qq号错误或此人不存在")
        return


    if str(qqn)==str(session.ctx['self_id']):
        await session.send("请勿输入自己的qq号")
        return
    await session.bot.set_group_kick(group_id=session.ctx['group_id'],user_id=qqn,self_id=session.ctx['self_id'])
    await session.send("成功移除")


@ban.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['data'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要踢出的qq号不能为空，请重新输入')
    session.state[session.current_key] = stripped_arg



@on_command('pardon',aliases=('解禁','解除禁言'),only_to_me=False,permission=(SUPERUSER,GROUP_OWNER))
async def pardon(session:CommandSession):
    try:
        qqn=str(session.get('data', prompt='你想解禁哪个人，请输入Ta的qq号'))
        if len(str(qqn).split(" ")) >= 2:
            await session.send("请直接输入qq号")
            return
    except ValueError:
        await session.send("异常：qq号错误或此人不存在")
        return

    if str(qqn)==str(session.ctx['self_id']):
        await session.send("请勿输入自己的qq号")
        return

    await session.bot.set_group_ban(
        group_id=session.ctx['group_id'], user_id=qqn, duration=0, self_id=session.ctx['self_id']
    )





