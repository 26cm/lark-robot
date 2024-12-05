import json
import re
from database_query import query_phone_addresses
from message_sender import send_message
import lark_oapi as lark

# 正则表达式匹配手机号码（格式：11位数字，通常以1开头）
phone_pattern = re.compile(r'\b1\d{10}\b')

def do_p2_im_message_receive_v1(data: lark.im.v1.P2ImMessageReceiveV1) -> None:
    try:
        print(f'[ do_p2_im_message_receive_v1 access ], data: {lark.JSON.marshal(data, indent=4)}')

        message_content = data.event.message.content
        parsed_content = json.loads(message_content)
        message_text = parsed_content.get('text', '未找到消息内容')

        # 检测是否包含手机号码
        match = phone_pattern.search(message_text)
        if match:
            phone_number = match.group()
            print(f"检测到手机号码: {phone_number}")

            # 执行查询功能
            results = query_phone_addresses(phone_number)
            if results is not None:
                reply_text = f"{phone_number}用户有效的信息有：\n"
                for row in results:
                    reply_text += f"{row[0]}, {row[1]}\n"
                chat_id = data.event.message.chat_id
                send_message(chat_id, reply_text)
            else:
                print("查询失败或无结果")
        else:
            print("未检测到手机号码")
    except (json.JSONDecodeError, AttributeError) as e:
        print(f"处理消息失败: {e}")
