from nonebot import on_command,CommandSession
from nonebot.permission import *
from aiocqhttp import MessageSegment
from asyncio import sleep
from Ganyu.service.bot_api import *

@on_command("fishing",aliases=("钓鱼","我要钓鱼"),only_to_me=False,permission=EVERYBODY)
async def fishing(session:CommandSession):
    un =session.event['user_id']
    little_fish_value = random.randint(100,150)
    big_fish_value = random.randint(200,300)



    await session.send(MessageSegment.at(session.ctx['user_id']) + "您正在钓鱼")
    await sleep(10)
    s1 = session.send("哎呀，鱼被吓跑了，你什么也没钓到")
    s2 = session.send("你放了个屁，鱼被熏死了")
    s3 = session.send("你的鱼都被群主收走了，获得了个寂寞")
    s4 = session.send(f"恭喜钓上一条小鱼，价值{little_fish_value} {money_name}!")
    s5 = session.send(f"wow!一条鲜美的大鱼，您获得了{big_fish_value} {money_name}!")


    state = random.choice([s1,s2,s3,s4,s5])
    await session.send(MessageSegment.at(session.ctx['user_id']) + state)
    if state == s4:
        add_money(little_fish_value,un)
    if state == s5:
        add_money(big_fish_value,un)

