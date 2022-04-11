from sdk import cmd_interop
from state import 






    
        

class State:
    debugging = Debugging()
    # def __init__():
    #     debugging = Debugging()

state = State()


def print_state_debugging():
    print(f"ign: {state.debugging.IGNORE_CRASHES}")
    print(f"spd: {state.debugging.SPEED_LIMIT}")
    print(f"inf sup: {state.debugging.INFINITE_SUPPLY}")

def print_state():
    #print_state_debugging()
    print("Heyo")

def update_state():
    global state
    msg = cmd_interop.receive_message()

    # print_state()
    if (not msg):
        #print("No message!")
        return
    key = msg['msg']
    data = msg['data']
    
    if (key == "debugging"):
        state.debugging.get_data(data)
    if (key == "ugv-data"):
        state.ugv.get_data(data)
    # if (key == "debugging"):
    #     state.debugging.get_data(data)
    
        

    
