import json
import os
import traceback
from datetime import datetime

import pytz
import requests


# 获取北京时间
def get_beijing_time():
    target_timezone = pytz.timezone('Asia/Shanghai')
    # 获取当前时间
    return datetime.now().astimezone(target_timezone)


# 格式化时间
def format_now():
    return get_beijing_time().strftime("%Y-%m-%d %H:%M:%S")


def get_wx_access_token():
    # 获取access token的url
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(
        appID.strip(), appSecret.strip())
    response = requests.get(url).json()
    print(response)
    access_token = response.get('access_token')
    return access_token


def send_message(user_mi, step, success, message):
    body = {
        "touser": openId.strip(),
        "template_id": templateId.strip(),
        "url": "https://weixin.qq.com",
        "data": {
            "date": {
                "value": format_now()
            },
            "account": {
                "value": user_mi
            },
            "step": {
                "value": step
            },
            "success": {
                "value": "True" if success else "False"
            }
        }
    }
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(get_wx_access_token())
    print(requests.post(url, json.dumps(body)).text)


if __name__ == "__main__":
    wx_config = dict()
    try:
        if os.environ.__contains__("WX_CONFIG") is False:
            print("未配置WX_CONFIG变量，无法发送消息")
        else:
            wx_config = dict(json.loads(os.environ.get("WX_CONFIG")))
            appID = wx_config.get("APP_ID")
            appSecret = wx_config.get("APP_SECRET")
            openId = wx_config.get("OPEN_ID")
            templateId = wx_config.get("TEMPLATE_ID")
            send_message('1', '2', True, '3')
    except:
        traceback.print_exc()
        exit(1)
