from nonebot import on_command, CommandSession
from nonebot.permission import *
from nonebot import CQHttpError

@on_command("my_chat",aliases=("查询群信息","群信息","查群"),permission=EVERYBODY,only_to_me=False)
async def my_chat(session:CommandSession):
    group_id = str(session.ctx['group_id'])
    try:
        member_list = await session.bot.get_group_member_list(
            group_id=group_id
        )
        group_name = await session.bot.get_group_info(
            group_id=group_id,
            type="group_name"
        )
        current_talkative = await session.bot.get_group_honor_info(
            group_id=group_id,
            talkative_id='user_id',
            type="current_talkative"
        )
    except CQHttpError:
        await session.send("出现错误，无法获取")
        return
    await session.send(f"您正在查询{group_name}c{group_id})的信息"
                       f'群内人数：{len(member_list)}人\n'
                       f'本日龙王：{current_talkative}\n'
                       )