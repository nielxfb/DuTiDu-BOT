from flask import Flask, request, abort
from dotenv import load_dotenv
from util.commands import commands
from datas.load import FileLoader

import os

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

load_dotenv()

app = Flask(__name__)
file_loader = FileLoader()

configuration = Configuration(access_token=os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))


@app.route("/webhook", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

def check_command(messages):
    for command in commands:
        if messages[0] in command['aliases']:
            print(messages[1:])
            return command['handler'](messages[1:])
    return ""

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    messages = event.message.text.split(' ')
    response = check_command(messages)
    if response == "":
        return
    
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=response)]
            )
        )

if __name__ == "__main__":
    app.run()