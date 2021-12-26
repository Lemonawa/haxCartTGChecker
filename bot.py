import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import random
from telegram.ext import Updater,CommandHandler

updater = Updater("<YOUR_TOKEN>")
dispatcher = updater.dispatcher

def getParams():
    ua = UserAgent()
    params = dict(
        headers = {'User-Agent': ua.random},
    )
    return params

def getSoup(url,encoding="utf-8",**params):
    reponse = requests.get(url,**params)
    reponse.encoding = encoding
    soup = bs(reponse.text,'lxml')
    return soup

def getWebpage():
    global eu1,eu2,eu3,eu4,eu5,eu6,eu7,eu8,eu9,eu10,eumid1,euovz,id1,usla,all
    params = getParams()
    soup = getSoup("https://hax.co.id/data-center/",**params)
    allVPS = soup.find_all('h1')
    eu1 = allVPS[0].string.replace(' VPS', '')
    eu2 = allVPS[1].string.replace(' VPS', '')
    eu3 = allVPS[2].string.replace(' VPS', '')
    eu4 = allVPS[3].string.replace(' VPS', '')
    eu5 = allVPS[4].string.replace(' VPS', '')
    eu6 = allVPS[5].string.replace(' VPS', '')
    eu7 = allVPS[6].string.replace(' VPS', '')
    eu8 = allVPS[7].string.replace(' VPS', '')
    eu9 = allVPS[8].string.replace(' VPS', '')
    eu10 = allVPS[9].string.replace(' VPS', '')
    eumid1 = allVPS[10].string.replace(' VPS', '')
    id1 = allVPS[11].string.replace(' VPS', '')
    usla = allVPS[12].string.replace(' VPS', '')
    euovz = str(int(allVPS[13].string.replace(' VPS', '')) + int(allVPS[14].string.replace(' VPS', '')) + int(allVPS[15].string.replace(' VPS', '')) + int(allVPS[16].string.replace(' VPS', '')) + int(allVPS[17].string.replace(' VPS', '')))
    all = allVPS[18].string.replace(' VPS', '')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="您好，欢迎使用Hax库存查询监控bot！\n我能够帮你拿到hax官网上的库存信息，并把他们发送到你的Telegram会话中\nGithub: @isaka-blog    TG: @misakanetcn")

def ping(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pong~")

def get(update, context):
    getWebpage()
    context.bot.send_message(chat_id=update.effective_chat.id, text="我获取到网页了！下面是Hax VPS目前的库存情况：\nEU-1: "+eu1+"\nEU-2: "+eu2+"\nEU-3: "+eu3+"\nEU-4: "+eu4+"\nEU-5: "+eu5+"\nEU-6: "+eu6+"\nEU-7: "+eu7+"\nEU-8: "+eu8+"\nEU-9: "+eu9+"\nEU-10: "+eu10+"\nEU-Mid-1: "+eumid1+"\nID-1: "+id1+"\nUS-LA: "+usla+"\nEU-OpenVZ: "+euovz+"\n开通的VPS: "+all+"\nNote: EU1-EU10、EU-Mid-1 为KVM区，ID-1 和 US-LA 为LXC区")

Start = CommandHandler('start', start)
Ping = CommandHandler('ping', ping)
Get = CommandHandler('get', get)
dispatcher.add_handler(Ping)
dispatcher.add_handler(Start)
dispatcher.add_handler(Get)

updater.start_polling()
