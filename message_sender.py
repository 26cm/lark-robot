# sender.py
import json
import lark_oapi as lark
from lark_oapi.api.im.v1 import *
from config import APP_ID, APP_SECRET

def send_message(chat_id: str, text: str) -> None:
    """发送消息到指定群聊"""
    try:
        client = lark.Client.builder() \
            .app_id(APP_ID) \
            .app_secret(APP_SECRET) \
            .log_level(lark.LogLevel.DEBUG) \
            .build()

        request = CreateMessageRequest.builder() \
            .receive_id_type("chat_id") \
            .request_body(CreateMessageRequestBody.builder()
                .receive_id(chat_id)
                .msg_type("text")
                .content(json.dumps({"text": text}))
                .build()) \
            .build()

        response = client.im.v1.message.create(request)

        if not response.success():
            lark.logger.error(
                f"消息发送失败, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
            return

        print("消息发送成功")
    except Exception as e:
        print(f"发送消息时发生错误: {e}")
