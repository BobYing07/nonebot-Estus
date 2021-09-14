from Hutao.service.limit import *
from .sign import *
from random import choice
_chat_flmt = FreqLimiter(3)
_chat_flmt_notice = choice(["666您就是pvp大蛇是吧", "冷静1下", "阿伟，你又在调戏机器人欸，休息一下吧", "你怎么这么逊哦，天天调戏机器人"])
__plugin_name__ = "签到系统"
__plugin_usage__ = "签到获取Beimo coin"