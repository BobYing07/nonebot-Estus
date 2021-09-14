import random
import json
import requests
from nonebot import on_command, CommandSession
from nonebot.permission import *
from aiocqhttp import MessageSegment



@on_command('setu',aliases=("色图","涩图","二刺螈"),permission=EVERYBODY,only_to_me=False)
async def setu(session:CommandSession):
    urls = {
        "https://api.vvhan.com/api/acgimg?type=json":"imgurl",
        "https://api.dongmanxingkong.com/suijitupian/acg/1080p/index.php?return=json":"imgurl",
        "http://api.easys.ltd/api/api/api.php?return=json":"imgurl"
    }
    url = random.choice(list(urls.keys()))
    url = json.loads(requests.get(url).content.decode("utf-8-sig"))[urls[url]].strip("/")
    await session.send(MessageSegment.image(url))