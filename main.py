from sdk import cmd_debug
from sdk import cmd_ugv
from sdk import cmd_interop
from src import keyboard
from src import debug_keys
from src import runner
import time

EXECUTABLE_FOLDER="sim"
EXECUTABLE_NAME="KARMASIM.exe"

runner.run_program(EXECUTABLE_FOLDER, EXECUTABLE_NAME)

while True:
    keyboard.perform_update()
    time.sleep(0.01)

    # Deneme
    debug_keys.print_state()
    debug_keys.update_keys()
