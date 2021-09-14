from nonebot import on_command,CommandSession
from nonebot.permission import *
from aiocqhttp import MessageSegment
from Ganyu.service.bot_api import *

@on_command("store",aliases=("商店","买东西"),permission=EVERYBODY,only_to_me=False)
async def store(session:CommandSession):
        un = session.event['user_id']
        items = ['DR钻戒','以理服人','五星律师',"士力架"]
        cost = [114514,1919,1000,100]
        dr = f"{items[0]} ——可以用来求婚 售价：{cost[0]} {money_name}"
        yi_li_fu_ren = f"{items[1]} ——打架获胜概率翻倍 售价：{cost[1]} {money_name}"
        lawyer = f"{items[2]} ——进监狱免费保释 售价：{cost[2]} {money_name}"
        shi_li_jia = f"{items[3]} ——据说是彬彬在超商抢的，吃完之后有特异功能 售价：{cost[3]} {money_name}"




        await session.send("*-*-*-*-*-甘雨の奇妙小商店-*-*-*-*-*\n"
                           f"{dr}\n"
                           f"{yi_li_fu_ren}\n"
                           f"{lawyer}\n"
                           f"{shi_li_jia}\n"
                           )


        get_item = session.get("get_item",prompt=f"{MessageSegment.at(un)}请问需要什么呢：")


        if get_item not in items:
            await session.send("您要的东西，甘雨这没有哦~")
            return


        elif get_item in items:
            if get_item == items[0]:    #dr
                item = items[0]
                cost = cost[0]
                if get_money(un) < cost:
                    await session.send(MessageSegment.at(un) + "没钱给👴爪巴")
                    return
                else:
                    await session.send(MessageSegment.at(un) + f"成功使用{cost}{money_name}购买{get_item}")
                    sub_money(cost,un)    #后面将获得的item加入json
                    getted(un,item)
                    return

            elif get_item == items[1]:  #以理服人
                item = items[1]
                cost = cost[1]
                if get_money(un) < cost:
                    await session.send(MessageSegment.at(un) + "没钱给👴爪巴")
                    return

                else:
                    await session.send(MessageSegment.at(un) + f"成功使用{cost} {money_name}购买{get_item}")
                    sub_money(cost,un)
                    getted(item)
                    return

            elif get_item == items[2]:  #五星律师
                item = items[2]
                cost = cost[2]
                if get_money(un) < cost:
                    await session.send(MessageSegment.at(un) + "没钱给👴爪巴")
                    return
                else:
                    await session.send(MessageSegment.at(un) + f"成功使用{cost} {money_name}购买{get_item}")
                    sub_money(cost,un)
                    getted(item)
                    return

            elif get_item == items[3]:  #士力架
                item = items[3]
                cost = cost[3]
                if get_money(un) < cost:
                    await session.send(MessageSegment.at(un) + "没钱给👴爪巴")
                    return
                else:
                    await session.send(MessageSegment.at(un) + f'成功使用{cost} {money_name}购买{get_item}')
                    sub_money(cost,un)
                    getted(item)
                    return


