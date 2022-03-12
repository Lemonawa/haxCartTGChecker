# -*- coding: utf-8 -*-
import re
from random import choice
import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater,CommandHandler

updater = Updater("<YOUR BOT TOKEN>")
dispatcher = updater.dispatcher

class Hax:
    @staticmethod
    def get_ua(brower_name):
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.30 Safari/537.36"
        return useragent

    def check(self, url):
        headers = {
            "User-Agent": self.get_ua("Safari"),
            "Content-type": "application/json",
        }
        datas = requests.get(url, headers=headers).text
        return datas

    def get_server_info(self):
        html_text = self.check("https://hax.co.id/data-center")
        soup = BeautifulSoup(html_text, "html.parser")
        zone_tags = soup("h5", class_="card-title mb-4")
        sum_tags = soup("h1", class_="card-text")
        vps_dict = dict(map(lambda x, y: [x.text, y.text], zone_tags, sum_tags))
        return vps_dict

    def get_data_center(self):
        html_text = self.check("https://hax.co.id/create-vps")
        soup = BeautifulSoup(html_text, "html.parser")
        center_list = [x.text for x in soup("option", value=re.compile(r"^[A-Z]{2,}-"))]
        center_str = "\n".join(center_list)
        return center_list, center_str

    def main(self):
        vps_dict = self.get_server_info()
        vps_str = ""
        for k, v in vps_dict.items():
            vps_str += str(k) + "\t" + str(v) + "\n"
        srv_stat = f"[🛰Opened Server Statistics / 已开通的服务器数据]\n{vps_str}\n\n"
        center_list, center_str = self.get_data_center()
        data_center = (
            f"[🚩Currently available data centers / 当前可开通的数据中心]\n{center_str}\n\n"
        )
        eu_mid1 = (
            "[♨Special Focus / 特别关注]\nEU Middle Specs (KVM + SSD) are NOT available now.\t暂时没有库存。"
            if "EU Middle Specs" not in center_str
            else "CHECK https://hax.co.id/create-vps NOW!!! EU Middle Specs (KVM + SSD) are available now.\t有库存！"
        )
        msg = srv_stat + data_center + eu_mid1
        return msg

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="欢迎使用Hax库存查询监控bot！\n我能够帮你拿到hax官网上的库存信息，并把他们发送到你的Telegram会话中\n输入 /help 获取帮助列表\nGithub: Misaka-blog    TG: @misakanetcn")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hax 库存查询监控BOT 帮助菜单\n/help 显示本菜单\n/get 获取当前库存情况\n/ping 检测bot存活状态")

def ping(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pong~")

def get(update, context):
    res = Hax().main()
    context.bot.send_message(chat_id=update.effective_chat.id, text=res)

Start = CommandHandler('start', start)
Ping = CommandHandler('ping', ping)
Get = CommandHandler('get', get)
Help = CommandHandler('help', help)
dispatcher.add_handler(Ping)
dispatcher.add_handler(Start)
dispatcher.add_handler(Get)
dispatcher.add_handler(Help)

updater.start_polling()
