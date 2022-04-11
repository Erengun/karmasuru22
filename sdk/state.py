from sdk import cmd_interop

def update_state():
    msg = cmd_interop.receive_message()

    