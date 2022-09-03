# -*- coding:utf-8 -*-
"""
@author: Lee.poch
@file:Auto_push_main.py
@software:PyCharm
@time:2022/09/03 
"""
import requests
import yaml
import time
from bs4 import BeautifulSoup
from cqhttp import CQHttp
import schedule


def send_msg(str):
    bot = CQHttp(api_root='http://xxxx:5700/') # go-cqhttp 监听地址
    QQ = '' # 接受推送QQ号
    bot.send_private_msg(user_id=QQ, message='Time:' + time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime()) + '\n' + 'Info:' + '\n' + f'{str}')


def loadYml(ymlFileName='config.yml'):
    with open(ymlFileName, 'r', encoding="utf-8") as file:
        item = yaml.load(file, Loader=yaml.FullLoader)
        return item


def log(log):
    Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"{Time}" + "\t" + f"|||{log}|||")
    log = None


def sign(user):
    url_flusheh = 'http://zhcx.scitc.com.cn/weixin/UpdateUserInfor.php'
    url_get = f"http://zhcx.scitc.com.cn/weixin/HealthAdd.php?code={user['code']}&state=123"
    url_post = 'http://zhcx.scitc.com.cn/weixin/HealthAdd.php'
    header_flusheh = {
        "Host": "zhcx.scitc.com.cn",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; ANA-AN00 Build/HUAWEIANA-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3185 MMWEBSDK/20220105 Mobile Safari/537.36 MMWEBID/371 MicroMessenger/8.0.19.2080(0x2800133B) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "X-Requested-With": "com.tencent.mm",
        "Referer": url_get,
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": user['Cookie']
    }
    header_get = header_flusheh
    header_post = header_flusheh

    def flusheh():
        resp_flusheh = requests.get(url_flusheh, headers=header_flusheh)
        html_flusheh = resp_flusheh.text
        soup_flusheh = BeautifulSoup(html_flusheh, 'html.parser')
        try:
            ation = soup_flusheh.find_all(
                'div', {'class': 'weui-cell my-weui-cell'})[0]
            log(ation)
            # send_msg('用户Cookie存活')
        except:
            log("用户信息获取失败")
            send_msg('用户Cookie过期')

    def submit():
        str_msg = "智慧川信提醒:" + "\n" + '用户名：' + user['username'] + '\n'

        def get_value():
            resp_get = requests.get(url_get, headers=header_get)
            html = resp_get.text
            log(html)
            soup = BeautifulSoup(html, 'html.parser')
            token = "NULL"
            demo = "NULL"
            demo_id = "NULL"
            try:
                token = soup.find('input', id='token')["value"]
                demo = soup.find_all('input', type="hidden")[1]["value"]
                demo_id = soup.find_all('input', type="hidden")[1]["id"]
            except:
                send_msg(str_msg + "页面获取失败")
            return token, demo, demo_id

        parameter = get_value()
        log(parameter)
        IncomingValue = {
            'token': parameter[0],
            'InSchoolYN': user['InSchool'],
            'GoOutYN': user['GoOutYN'],
            'Temperature': '36.6',
            'Info': '',
            'HealthAction': '正常　',
            'HealthMa': '绿码',
            'YiMiao_JiaQiang_YN': 'null',
            'Other': '',
            'LoadTimes': '811',
            'latitude': user['lat'],
            'longitude': user['lon'],
            'speed': '0.0',
            'accuracy': '35.0',
            'networkType': 'wifi',
            'Content': '',
            # 'yzm': "yzm",
            'action': 'save',
            parameter[2]: parameter[1]
        }
        print(IncomingValue)
        resp_post = requests.post(
            url_post, data=IncomingValue, headers=header_post, timeout=5)
        txt = str(resp_post.text)
        str_msg = str_msg + txt[5:16]
        print(str_msg)
        send_msg(str_msg)
        log(resp_post.text)
    schedule.every(20).minutes.do(flusheh)
    # schedule.every(18).seconds.do(flusheh)
    schedule.every(1).day.at("07:00").do(submit)
    while True:
        schedule.run_pending()
        time.sleep(3)


def main():
    config = loadYml()
    print(config)
    for user in config['users']:
        sign(user)


if __name__ == '__main__':
    main()
