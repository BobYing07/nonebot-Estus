from nonebot import on_command,CommandSession
from nonebot.permission import *



@on_command('weather',aliases=('天气','查询天气'),permission=EVERYBODY,only_to_me=False)
async def weather(session:CommandSession):
    city = session.get('city',prompt='你要查询哪个城市的天气呢?')
    await session.send("您查询的城市是：" + city)



@weather.args_parser
async def _(session:CommandSession):
    if session.is_first_run:
        return

    session.args['city'] = session.current_arg_text
