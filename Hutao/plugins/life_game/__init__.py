from Hutao.service.limit import *
from random import choice
from .fishing import *
from .store import *
_chat_flmt = FreqLimiter(3)
_chat_flmt_notice = choice(["666您就是pvp大蛇是吧", "冷静1下", "阿伟，你又在调戏机器人欸，休息一下吧", "你怎么这么逊哦，天天调戏机器人"])
__plugin_name__ = "生活大冒险"
__plugin_usage__ = r"""正在开发的一款游戏
工作 钓鱼 卖瓜
结婚 搞事 生娃
本游戏应有尽有"""
#这一块的命令有问题啊啊啊啊
#下个版本修改