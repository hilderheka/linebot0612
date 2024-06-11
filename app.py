# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, MessageTemplateAction, ButtonsTemplate
import random


# 填入你的 Channel Access Token 和 Channel Secret
#line_bot_api = LineBotApi('EZeAPTZN8Q5hwz6GtaV2w9RtwkYLYlE1Ln2cAEmxPmie3ywJRrRWorPGgnfsw8AGVOqxPGCccviBKBTaViNjee4+TKWHtzHi9C/g0fdod4Ijbx3u04T0ccoVnHmixs25Cjm0z/wb9ACynP/NVEzO1AdB04t89/1O/w1cDnyilFU=')
#handler = WebhookHandler('65725ea67526524bc5709481ae2eebaf')
import os
line_bot_api = LineBotApi(os.environ.get('Channel_Access_Token'))
handler = WebhookHandler(os.environ.get('Channel_Secret'))

# 隨機回復的句子列表
responses = [
    "書籍是人類進步的階梯。 — 高爾基",
    "讀萬卷書，行萬里路。 — 中國諺語",
    "書中自有黃金屋，書中自有顏如玉。 — 宋真宗",
    "一本好書，就是一個好朋友。 — 歐內斯特·海明威",
    "讀書破萬卷，下筆如有神。 — 杜甫",
    "知識就是力量。 — 培根",
    "讀書之法，在循序而漸進，熟讀而精思。 — 朱熹",
    "開卷有益。 — 宋代諺語",
    "讀書使人充實，思考使人深邃，交談使人清晰。 — 弗朗西斯·培根",
    "不讀書的人，思想就會停止。 — 狄德羅",
]

@app.route("/callback", methods=['POST'])
def callback():
    # 獲取請求的簽名
    signature = request.headers['X-Line-Signature']
    # 獲取請求的主體
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "佳言美句":
        reply_message = random.choice(responses)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_message)
        )

if __name__ == "__main__":
    app.run()
