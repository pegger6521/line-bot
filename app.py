#要載入LINE官方的SDK: Software development kit 軟體開發套件
#使用他寫好的FUNCTION
#我們必須要用LINE寫好的SDK來做一個聊天機器人
#我們要寫一個伺服器(就是寫web app)如下
#用FLASK來架設伺服器

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('FF2FR7fuZdmdybomJ1Fqq42KvJ/rGtdntM84Es/hgU/RxByYSfsVKLoQO5MEKL9JMZCcJWSCUKLZU4Zji4szGflIuBjAqXrbaGlFNusMNUY32PlkT38VYoMnKH67qXZ44/pbcBchl4KLfAPDF50JIAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('868424d97ac619571e20cc5ee0862869')

#例如:當有人在網址(路徑)的地方輸入"www.line-bot.com/callback"時, 就會執行下面的程式碼
#這裡就是: 把訊息從LINE官方伺服器轉介到我們的WEB APP的程式碼
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

#這裡是在: 回覆使用者傳來的訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = '你吃飯了嗎'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()
