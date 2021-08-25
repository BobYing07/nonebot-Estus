from nonebot.permission import *
from nonebot import on_command,CommandSession
from aiocqhttp import MessageSegment
import requests

@on_command("知乎日报",aliases=("daily-news","zhihu","news"),permission=EVERYBODY,only_to_me=False)
async def zhihu(session:CommandSession):
    STORY_URL_FORMAT = 'https://daily.zhihu.com/story/{}'
    resp = requests.get(
        'https://news-at.zhihu.com/api/4/news/latest',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }
    )
    data = resp.json()
    stories = data['stories']
    reply = ''
    for story in stories:
        url =  STORY_URL_FORMAT.format(story['id'])
        title = story['title']
        reply += f'\n{title}\n{url}\n'
    await session.send(MessageSegment.at(session.ctx['user_id']) + reply)

