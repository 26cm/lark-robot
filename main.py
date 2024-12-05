import lark_oapi as lark
from event_dispatcher import create_event_handler
from config import APP_ID, APP_SECRET

def main():
    event_handler = create_event_handler()
    cli = lark.ws.Client(APP_ID, APP_SECRET,
                         event_handler=event_handler,
                         log_level=lark.LogLevel.DEBUG)
    cli.start()

if __name__ == "__main__":
    main()
