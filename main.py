from sdk import cmd_debug
from sdk import cmd_ugv
from sdk import cmd_interop
from src import keyboard
from src import debug
from src import runner
from src import state
import time
import colored_traceback.auto 
from colorama import init # For windows colored output support

init()

cmd_interop.init_socket()
EXECUTABLE_FOLDER="sim"
EXECUTABLE_NAME="KARMASIM.exe"

runner.run_program(EXECUTABLE_FOLDER, EXECUTABLE_NAME)

while True:
    keyboard.perform_update()
    time.sleep(0.01)

    #debug.print_state()
    debug.update_keyboard_control()

    #if (keyboard.get_key_down("a")):
    state.update_state()
        #state.print_state()

