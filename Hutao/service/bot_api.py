#oding = utf-8
# -*- coding:utf-8 -*-
import json
import random

mj=60*60
money_name = 'Beimo coin'
def get_content():
    with open("ct.json", 'r') as f:
        return json.load(f)

def write_content(content):
    with open("ct.json", 'w') as f:
        json.dump(content, f)

def create_per(user_num):
    content = get_content()
    user_num = str(user_num)
    content["users"][user_num] = {"lv": 0, "jy": 0, "money": 0,"data":[],"bag":{},"tl":10}
    write_content(content)



def add_money(add_num, user_num):
    content=get_content()
    user_num = str(user_num)
    if not (user_num in content["users"]):
        create_per(user_num)
        content=get_content()
    content["users"][user_num]["money"] += add_num
    write_content(content)


def sub_money(sub_num, user_num):
    content = get_content()
    user_num = str(user_num)
    if not (user_num in content["users"]):
        create_per(user_num)
        content=get_content()
    content["users"][user_num]["money"] -= sub_num
    write_content(content)


def get_money(user_num):
    content = get_content()
    user_num = str(user_num)
    if not (user_num in content["users"]):
        create_per(user_num)
        content=get_content()
    return content["users"][user_num]["money"]

def add_jy(add_num, user_num):
    content = get_content()
    user_num = str(user_num)
    if not (user_num in content["users"]):
        create_per(user_num)
        content = get_content()
    content["users"][user_num]["jy"] += add_num
    write_content(content)

def get_jy(user_num):
    content = get_content()
    user_num = str(user_num)
    if not (user_num in content["users"]):
        create_per(user_num)
        content = get_content()
    return content["users"][user_num]["jy"]

def add_per_data(user_num,data):
    content = get_content()
    user_num = str(user_num)
    if not (user_num in content["users"]):
        create_per(user_num)
        content = get_content()
    content["users"][user_num]["data"].append(data)
    write_content(content)

def sub_per_data(user_num,data_num):
    content = get_content()
    user_num = str(user_num)
    if not (user_num in content["users"]):
        create_per(user_num)
        content = get_content()
    if len(content["users"][user_num]["data"]) >= data_num:
        return 400
    content["users"][user_num]["data"].pop(data_num)
    write_content(content)

def get_per_data(user_num):
    content = get_content()
    user_num = str(user_num)
    if not (user_num in content["users"]):
        create_per(user_num)
        content = get_content()
    return content["users"][user_num]["data"]

def add_qj_xf_data(user_num):
    content = get_content()
    user_num = str(user_num)
    content["p_not_jj"].append(user_num)
    write_content(content)

def sub_qj_xf_data(user_num):
    content = get_content()
    user_num = str(user_num)
    if not (user_num in content["p_not_jj"]):
        return 401
    content["p_not_jj"].pop(content["p_not_jj"].index(user_num))
    write_content(content)

def get_qj_xf_data():
    content = get_content()
    return content["p_not_jj"]

def set_now_melon_t(price):
    # get some contents
    content = get_content()
    price = int(price)
    #set some data
    content['melon_price']=price
    #save
    write_content(content)

def add_melon_t(user_num):
    #get some contents
    content = get_content()
    user_num=str(user_num)
    #set some data
    content["melon_t"][user_num]={"melon_p":100,"melon_num":0,"j":{}}
    #save
    write_content(content)


def add_melon_j_num(user_num,add_num,j):
    #get some contents
    content = get_content()
    user_num=str(user_num)
    add_num=int(add_num)
    j=str(j)
    if not(j in content["melon_t"][user_num]["j"]):
        content["melon_t"][user_num]["j"][j]=0
    #set some data
    content["melon_t"][user_num]["j"][j]+=add_num
    #save
    write_content(content)

def sub_melon_j_num(user_num,sub_num,j):
    #get some contents
    content = get_content()
    user_num=str(user_num)
    sub_num=int(sub_num)
    j=str(j)
    if not(j in content["melon_t"][user_num]["j"]):
        content["melon_t"][user_num]["j"][j]=0
    #set some data
    content["melon_t"][user_num]["j"][j]-=sub_num
    #save
    write_content(content)

def get_melon_j_num(user_num,j):
    #get some contents
    content = get_content()
    user_num=str(user_num)
    j = str(j)
    if not(j in content["melon_t"][user_num]["j"]):
        return 0
    return content["melon_t"][user_num]["j"][j]


def get_melon_t():
    #get some contents
    content = get_content()

    return content["melon_t"]

def is_have_melon_t(user_num):
    user_num=str(user_num)
    if user_num in get_melon_t():
        return True
    return False

def set_melon_t_price(user_num,set_num):
    #get some contents
    content = get_content()
    user_num=str(user_num)
    set_num=int(set_num)
    #set some data
    content["melon_t"][user_num]["melon_p"]=set_num
    #save
    write_content(content)

def get_melon_t_price(user_num):
    #get some contents
    content = get_content()
    user_num=str(user_num)

    return content["melon_t"][user_num]["melon_p"]

def add_melon_num(add_num,user_num):
    #get some contents
    content = get_content()
    user_num=str(user_num)
    add_num=int(add_num)

    content["melon_t"][user_num]["melon_num"]+=add_num

    write_content(content)

def sub_melon_num(sub_num, user_num):
    # get some contents
    content = get_content()
    user_num = str(user_num)
    sub_num = int(sub_num)

    content["melon_t"][user_num]["melon_num"] -= sub_num

    write_content(content)

def get_melon_num(user_num):
    # get some contents
    content = get_content()
    user_num = str(user_num)

    return content["melon_t"][user_num]["melon_num"]

def ads_get_list():
    content = get_content()
    items=[]
    ks=[]
    for i in content["ads"]:
        items.append(i)
        ks.append(content["ads"][i])
    return f"\n{'-'*10+'广告'+'-'*10}\n"+random.choices(items,weights=ks)[0]

def add_ads(ggc,w):
    content = get_content()
    content["ads"][ggc]=w
    write_content(content)

def bag_add(user_id,name,num):
    content = get_content()
    user_id=str(user_id)
    if not(name in content["melon_t"][user_id]["j"]):
        content["users"][user_id]["bag"][name]=0
    content["users"][user_id]["bag"][name]+=num
    write_content(content)

def bag_sub(user_id,name,num):
    content = get_content()
    user_id=str(user_id)
    if not(name in content["melon_t"][user_id]["j"]):
        content["users"][user_id]["bag"][name]=0
    if content["users"][user_id]["bag"][name]<num:
        return 1
    content["users"][user_id]["bag"][name]-=num
    write_content(content)

def bag_get(user_id,name):
    content = get_content()
    user_id=str(user_id)
    if not(name in content["melon_t"][user_id]["j"]):
        content["users"][user_id]["bag"][name]=0
    return content["users"][user_id]["bag"][name]

def tl_get(user_id):
    content = get_content()
    user_id=str(user_id)

    return content["users"][user_id]["tl"]

def getted(user_id,item):
    content = get_content()
    user_id = str(user_id)
    return content['life'][user_id]['items'][item]