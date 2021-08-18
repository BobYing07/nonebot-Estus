from nonebot import on_command, CommandSession

@on_command('echo',aliases=("重复","复读机"),only_to_me=False)
async def echo(session: CommandSession):
    await session.send(session.state.get('message') or session.current_arg)
