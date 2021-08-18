#oding = utf-8
# -*- coding:utf-8 -*-

import random,json
from nonebot import on_command, CommandSession
from nonebot.permission import *
from aiocqhttp import MessageSegment

s_save={}
mj=60*60
p_not_jj=[]
money_name="YM"

def add_money(add_num,user_num):
    with open("ct.json",'r') as f:
        content=json.load(f)
    user_num=str(user_num)
    if not(user_num in content["user"]):
        content["users"][user_num]
    content["users"][user_num]+=add_num
    with open("ct.json",'w') as f:
        json.dump(content, f)

def get_money(user_num):
    with open("ct.json",'r') as f:
        content=json.load(f)
    user_num=str(user_num)
    return content["user"][user_num]


@on_command('qj_with_person', aliases=('跟踪',"尾随"),only_to_me=False,permission=EVERYBODY)
async def qj_with_person(session: CommandSession):
    if len(session.event["message"])!=2:
        await session.send(MessageSegment.at(session.event['user_id']) + '请输入"强奸 @某人"')
        return
    p=session.event["message"][1]
    if p["type"] != "at":
        await session.send(MessageSegment.at(session.event['user_id'])+'请输入"跟踪 @某人"')
        return
    pn=p['data']['qq']
    state=random.choices([1,2,3],weights=[5,3,3])[0]
    if state==1:
        await session.send(MessageSegment.at(session.event['user_id'])+"已成功跟踪，输入强奸 @某人")
        s_save[session.event['user_id']]=[pn,1]
    if state==2:
        await session.send(MessageSegment.at(session.event['user_id'])+"Ta发现你了，把你揍了一顿，住院3分钟")
        await session.bot.set_group_ban(group_id=session.event['group_id'],user_id=session.event['user_id'],duration=3*mj,self_id=session.event['self_id'])
    if state==3:
        await session.send(MessageSegment.at(session.event['user_id'])+"你居然能把人跟没了，然后你发现你背后有警察，被拘留2分钟")
        await session.bot.set_group_ban(group_id=session.event['group_id'], user_id=session.event['user_id'],
                                        duration=2 * mj, self_id=session.event['self_id'])

@on_command('qj_qj', aliases=('强奸'),only_to_me=False,permission=EVERYBODY)
async def qj_qj(session: CommandSession):
    execuser_name = int(session.ctx["sender"]["user_id"])
    if execuser_name in p_not_jj:
        await session.send(MessageSegment.at(session.event['user_id']) + '鸡鸡都没有，强奸墙角去吧')
        return
    if len(session.event["message"])!=2:
        await session.send(MessageSegment.at(session.event['user_id']) + '请输入"强奸 @某人"')
        return
    p = session.event["message"][1]
    if p["type"] != "at":
        await session.send(MessageSegment.at(session.event['user_id']) + '请输入"强奸 @某人"')
        return
    pn = p['data']['qq']
    if execuser_name in s_save:
        state = random.choices([1, 2, 3], weights=[6, 2, 2])[0]
        if state == 1:
            add_m=random.randint(300,460)
            add_money(add_m,session.event['user_id'])
            await session.send(MessageSegment.at(session.event['user_id']) + f"已成功强奸{MessageSegment.at(pn)}\n你得到了{add_m}{money_name},现在有{get_money(session.event['user_id'])}{money_name}")
            s_save.pop(session.event['user_id'])
        if state == 2:
            await session.send(MessageSegment.at(session.event['user_id']) + "Ta发现你了，把你揍了一顿，住院3分钟")
            await session.bot.set_group_ban(group_id=session.event['group_id'], user_id=session.event['user_id'],
                                            duration=3 * mj, self_id=session.event['self_id'])
        if state == 3:
            await session.send(MessageSegment.at(session.event['user_id']) + "Ta反客为主，把你的鸡鸡拽下来了")
            p_not_jj.append(session.event['user_id'])
    else:
        state = random.choices([1, 2], weights=[2, 8])[0]
        if state==1:
            add_m = random.randint(300, 460)
            add_money(add_m, session.event['user_id'])
            await session.send(MessageSegment.at(session.event[
                                                     'user_id']) + f"已成功强奸{MessageSegment.at(pn)}\n你得到了{add_m}{money_name},现在有{get_money(session.event['user_id'])}{money_name}")
            s_save.pop(session.event['user_id'])
        if state==2:
            await session.send(MessageSegment.at(session.event['user_id']) + f"你被拘留了，原因是光天化日直接扑上去强奸{MessageSegment.at(pn)}")
            await session.bot.set_group_ban(group_id=session.event['group_id'], user_id=session.event['user_id'],
                                            duration=2 * mj, self_id=session.event['self_id'])