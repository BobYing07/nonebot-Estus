from .ban import *
from .group_info import *
from Hutao.service.limit import *
from random import choice
_chat_flmt = FreqLimiter(3)
_chat_flmt_notice = choice(["666您就是pvp大蛇是吧", "冷静1下", "阿伟，你又在调戏机器人欸，休息一下吧", "你怎么这么逊哦，天天调戏机器人"])
__plugin_name__ = "群聊管理"
__plugin_usage__ = r"""使用该命令前请设置机器人为管理员
否则无法实现群聊管理
目前支持的功能有：禁言，查询人数
正在开发：龙王，给予头衔
"""