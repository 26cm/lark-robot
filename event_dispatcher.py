import lark_oapi as lark
from message_handler import do_p2_im_message_receive_v1

def create_event_handler() -> lark.EventDispatcherHandler:
    event_handler = lark.EventDispatcherHandler.builder("", "") \
        .register_p2_im_message_receive_v1(do_p2_im_message_receive_v1) \
        .register_p1_customized_event("这里填入你要自定义订阅的 event 的 key，例如 out_approval", lambda data: print(f'[ do_customized_event access ], type: message, data: {lark.JSON.marshal(data, indent=4)}')) \
        .build()
    return event_handler
