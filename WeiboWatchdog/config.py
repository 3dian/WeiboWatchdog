import json
import os

cookies = "WEIBOCN_FROM=1110006030; loginScene=102003; SUB=_2A25Og0mjDeRhGedI7VUW8i_LyzuIHXVtjFfrrDV6PUJbkdAKLWvdkW1NVvZkIBK2nt2ASB9yIEOl3gzxAIjnGxdV; _T_WM=80586365866; XSRF-TOKEN=83f14e; MLOGIN=1; mweibo_short_token=cf2d2e791c; M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174%26uicode%3D20000174"  # m.weibo.cn cookie
bark_key = ""  #
special_users = []  # 只转发的用户
ai_key = "wTW18mCGFmI9N2POHBfws126"  # 百度云人体识别api key 如果这个和下面的ai_secret为空，则不进行人体识别
ai_secret = "pdFKuewCguRUBcPKenyavxcsZ9mb9Kqq"  # 百度云人体识别api secret
is_repost = True  # 是否转发
is_upload = False  # 是否上传图片
is_screenshot = False  # 是否自动截图（需要自行配置chromedriver）
owner = 0  # 管理员ID
is_debug = False

default_config = {
    "cookies": cookies,
    "bark_key": bark_key,
    "special_users": special_users,
    "ai_key": ai_key,
    "ai_secret": ai_secret,
    "is_repost": is_repost,
    "is_upload": is_upload,
    "is_screenshot": is_screenshot,
    "owner": owner,
    "is_debug": is_debug
}

if not os.path.exists("config.json"):
    with open("config.json", "w") as f:
        f.write(json.dumps(default_config, indent=4))

with open("config.json", "r") as f:
    config = json.loads(f.read())
    for k, v in default_config.items():
        if k not in config:
            config[k] = v
    for k, v in config.items():
        globals()[k] = v

with open("config.json", "w") as f:
    f.write(json.dumps(config, indent=4))
