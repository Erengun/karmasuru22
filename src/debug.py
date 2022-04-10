from sdk import cmd_ugv
from sdk import cmd_debug
from sdk import cmd_interop
from src import keyboard

class DebugState:
    crashes_enabled = True
    limits_enabled = True
    show_nodes = False
    show_limits = False
    infinite_supply = False

    controlling_ugv = 1
    fire_hose_dir = [0, 0, 1]
    fire_hose_pressure = 0
    subject_station = 1

state = DebugState()

def print_state():
    print("\r", end="")
    # print("[F2]Kazalar:" + ("1" if _crashes_enabled else "0"), end=" ")
    # print("[F3]Limitler:" + ("1" if _limits_enabled else "0"), end=" ")
    # print("[F8]SınırsızKaynak:" + ("1" if _infinite_supply else "0"), end=" ")
    print("[F6-F7]IKA-ID:" + str(state.controlling_ugv), end=" ")
    print("[ad]SuBasinci:" + str(state.fire_hose_pressure), end=" ")
    print("[zxcvbn]SuYonu:" + str(state.fire_hose_dir), end=" ")
    print("", end="", flush=True)

# Key names for reference
#  'backspace', 'caps_lock', 'cmd', 'cmd_r', 'ctrl', 'ctrl_l', 'ctrl_r', 'delete', 
#  'down', 'end', 'enter', 'esc', 'f1'
#  'home', 'insert', 'left', 'media_next', 'media_play_pause', 'media_previous', 
#  'media_volume_down', 'media_volume_mute', 'media_volume_up', 'menu', 'num_lock', 
#  'page_down', 'page_up', 'pause', 'print_screen', 'right', 'scroll_lock', 'shift', 
#  'shift_r', 'space', 'tab', 'up']

def update_firehose():
    global state
    cmd_ugv.align_firehose(state.controlling_ugv, state.fire_hose_dir[0], state.fire_hose_dir[1], state.fire_hose_dir[2])


def update_keyboard_control():
    global state
    if keyboard.get_key_down('f2'):
        state.crashes_enabled = not state.crashes_enabled
        cmd_debug.crash_enabled(state.crashes_enabled)
    if keyboard.get_key_down('f3'):
        state.limits_enabled = not state.limits_enabled
        cmd_debug.limits_enabled(state.limits_enabled)
    if keyboard.get_key_down('f4'):
        state.show_nodes = not state.show_nodes
        cmd_debug.show_nodes(state.show_nodes)
    if keyboard.get_key_down('f5'):
        state.show_limits = not state.show_limits
        cmd_debug.show_limits(state.show_limits)
    if keyboard.get_key_down('f8'):
        state.infinite_supply = not state.infinite_supply
        cmd_debug.infinite_supply(state.infinite_supply)
    if keyboard.get_key_down('f6'):
        state.controlling_ugv -= 1
        if state.controlling_ugv < 1:
            state.controlling_ugv = 1
    if keyboard.get_key_down('f7'):
        state.controlling_ugv += 1

    if keyboard.get_key_down('e'):
        cmd_ugv.start_motor(state.controlling_ugv)
    if keyboard.get_key_down('q'):
        cmd_ugv.stop_motor(state.controlling_ugv)

    if keyboard.get_key_down('+'):
        cmd_ugv.set_gear(state.controlling_ugv, True)
    if keyboard.get_key_down('-'):
        cmd_ugv.set_gear(state.controlling_ugv, False)

    if keyboard.get_key_down('o'):
        cmd_ugv.set_handbrake(state.controlling_ugv, True)
    if keyboard.get_key_down('l'):
        cmd_ugv.set_handbrake(state.controlling_ugv, False)

    if keyboard.get_key_down('0'):
        cmd_ugv.set_turn_choice(state.controlling_ugv, 0)
    if keyboard.get_key_down('1'):
        cmd_ugv.set_turn_choice(state.controlling_ugv, 1)

    if keyboard.get_key_down('t'):
        cmd_ugv.start_supply(state.controlling_ugv, state.subject_station, state.cmd_interop.SUPPLY_FUEL)
    if keyboard.get_key_down('g'):
        cmd_ugv.start_supply(state.controlling_ugv, state.subject_station, state.cmd_interop.SUPPLY_WATER)
    if keyboard.get_key_down('y'):
        cmd_ugv.stop_supply(state.controlling_ugv, cmd_interop.SUPPLY_FUEL)
    if keyboard.get_key_down('h'):
        cmd_ugv.stop_supply(state.controlling_ugv, cmd_interop.SUPPLY_WATER)

    # Firehose pressure
    if keyboard.get_key_down('d'):
        state.fire_hose_pressure += 0.5
        cmd_ugv.adjust_firehose(state.controlling_ugv, state.fire_hose_pressure)
    if keyboard.get_key_down('a'):
        state.fire_hose_pressure -= 0.5
        if state.fire_hose_pressure < 0:
            _fire_hose_pressure = 0
        cmd_ugv.adjust_firehose(state.controlling_ugv, _fire_hose_pressure)

    # Firehose direction
    if keyboard.get_key_down('z'):
        state.fire_hose_dir[0] -= 1
        update_firehose()
    if keyboard.get_key_down('x'):
        state.fire_hose_dir[0] += 1
        update_firehose()
    if keyboard.get_key_down('c'):
        state.fire_hose_dir[1] -= 1
        update_firehose()
    if keyboard.get_key_down('v'):
        state.fire_hose_dir[1] += 1
        update_firehose()
    if keyboard.get_key_down('b'):
        state.fire_hose_dir[2] -= 1
        update_firehose()
    if keyboard.get_key_down('n'):
        state.fire_hose_dir[2] += 1
        update_firehose()

    if keyboard.get_key_down('f11'):
        state.subject_station -= 1
        if state.subject_station < 1:
            state.subject_station = 1
    if keyboard.get_key_down('f12'):
        state.subject_station += 1

    cmd_ugv.set_throttle(state.controlling_ugv, 1 if keyboard.get_key('w') else 0)
    cmd_ugv.set_brake(state.controlling_ugv, 1 if keyboard.get_key('s') else 0)