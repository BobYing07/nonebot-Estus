import nonebot
from nonebot import on_command, CommandSession
from nonebot.permission import *

@on_command('usage', aliases=("菜单","menu","用途","使用方法"),only_to_me=False,permission=EVERYBODY)
async def _(session: CommandSession):
    # 获取设置了名称的插件列表
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))

    arg = session.current_arg_text.strip().lower()
    if not arg:
        # 如果用户没有发送参数，则发送功能列表
        await session.send(
            'Ganyu-bot支持功能：\n'
            '=================\n'
            + '\n'.join(p.name for p in plugins)
            + "\n=================\n"
            + "输入 '/menu + 插件名称' 查看插件详情\n"
            + "基于Onebot的机器人Ganyu\n")
        return

    # 如果发了参数则发送相应命令的使用帮助
    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)
