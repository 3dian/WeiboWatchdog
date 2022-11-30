from datetime import datetime

from WeiboBot import Bot, Chat, Weibo, Comment

cookies = "__bid_n=183eb0ee103b9cea1e4207; FPTOKEN=30$McBBDBeCQt3rM9ihBItEq41qvp0pyf4t0hbNg8lb5NpxL7QGheGGeAsGtKUAsv3HF4AbP37dM5yWTLACokxYcqNo/bvIBqkf4+JewKT848xL5nnRc+dW8socUgx0Kxhq/aOEJdORH4TyQWMiUEZoas2MVeRkmmhZl/rpnnuAzO3XIVlY56QZJeDfVTxM/4XRO5BJZJ8Z3wjyaDAhtNIOi44vXkNzi5LazpXTFzzUU0lUUDf2T8GLJJSYvHUzRms7AzUA5MUVUry7sLxrZr/Q4uB0lm8Xgk0tZMhczWoEznArENVeEpe36TcjSC4X4vR9sG86bllf0zEdTI1ZtR9j2rUFun6qBlr2wmMO8fJxXGYeElYAdzYHoZ6J1BgDvMvv|UjEzCP79YzIrxRQmZX4GWD5s8pyQEgRWdVFrtTLnTlU=|10|5958a098f108efce9a827550041417e9; WEIBOCN_FROM=1110006030; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFc7RlZHqFNwG-QGQIKVhQm5JpX5K-hUgL.Fo24Sh-ReKep1KB2dJLoIpzLxKBLB.eL1KnLxKqL1heLBK5t; _T_WM=45933065706; MLOGIN=1; XSRF-TOKEN=c0d56e; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E7%2588%25B1%25E5%259B%25BD%26fid%3D1076035894492633%26uicode%3D10000011; SCF=AnhClORMcCoVnCi78R6avLpWs7JkEPnllov39MMnrpb4R7sqWGGEOIKKx-Yzz-210Uwp7DArn4cTpHBJgfbxXN8.; SUB=_2A25OcyHpDeRhGedH71cZ8S3NwjiIHXVtnE-hrDV6PUJbktANLUyskW1NULX5Cpav1PDSjbmBrbaj7cIfnfEJUNnv; SSOLoginState=1668764089; ALF=1671356089"
myBot = Bot(cookies=cookies)


@myBot.onNewMsg  # 被私信的时候触发
async def on_msg(chat: Chat):
    for msg in chat.msg_list:  # 消息列表
        print(f"{msg.sender_screen_name}:{msg.text}")


@myBot.onNewWeibo  # 首页刷到新微博时触发
async def on_weibo(weibo: Weibo):
    if weibo.original_weibo is None:  # 是原创微博
        print("find new", f"{weibo.text}")


@myBot.onMentionCmt  # 提及我的评论时触发
async def on_mention_cmt(cmt: Comment):
    print("on_mention_cmt", f"{cmt.text}")


# @myBot.onTick  # 每次循环触发
# async def on_tick():
    # print(datetime.now())

if __name__ == '__main__':
    myBot.run()