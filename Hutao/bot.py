from os import path
import nonebot
from Hutao import bot_config

if __name__ == '__main__':
    nonebot.init(bot_config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), '', 'plugins'),
        'Hutao.plugins'
    )


    nonebot.run()
