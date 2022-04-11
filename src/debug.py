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

dstate = DebugState()

def print_state():
    print("\r", end="")
    # print("[F2]Kazalar:" + ("1" if _crashes_enabled else "0"), end=" ")
    # print("[F3]Limitler:" + ("1" if _limits_enabled else "0"), end=" ")
    # print("[F8]SınırsızKaynak:" + ("1" if _infinite_supply else "0"), end=" ")
    print("[F6-F7]IKA-ID:" + str(dstate.controlling_ugv), end=" ")
    print("[ad]SuBasinci:" + str(dstate.fire_hose_pressure), end=" ")
    print("[zxcvbn]SuYonu:" + str(dstate.fire_hose_dir), end=" ")
    print("", end="", flush=True)

# Key names for reference
#  'backspace', 'caps_lock', 'cmd', 'cmd_r', 'ctrl', 'ctrl_l', 'ctrl_r', 'delete', 
#  'down', 'end', 'enter', 'esc', 'f1'
#  'home', 'insert', 'left', 'media_next', 'media_play_pause', 'media_previous', 
#  'media_volume_down', 'media_volume_mute', 'media_volume_up', 'menu', 'num_lock', 
#  'page_down', 'page_up', 'pause', 'print_screen', 'right', 'scroll_lock', 'shift', 
#  'shift_r', 'space', 'tab', 'up']

def update_firehose():
    global dstate
    cmd_ugv.align_firehose(dstate.controlling_ugv, dstate.fire_hose_dir[0], dstate.fire_hose_dir[1], dstate.fire_hose_dir[2])


def update_keyboard_control():
    global dstate
    if keyboard.get_key_down('f2'):
        dstate.crashes_enabled = not dstate.crashes_enabled
        cmd_debug.crash_enabled(dstate.crashes_enabled)
    if keyboard.get_key_down('f3'):
        dstate.limits_enabled = not dstate.limits_enabled
        cmd_debug.limits_enabled(dstate.limits_enabled)
    if keyboard.get_key_down('f4'):
        dstate.show_nodes = not dstate.show_nodes
        cmd_debug.show_nodes(dstate.show_nodes)
    if keyboard.get_key_down('f5'):
        dstate.show_limits = not dstate.show_limits
        cmd_debug.show_limits(dstate.show_limits)
    if keyboard.get_key_down('f8'):
        dstate.infinite_supply = not dstate.infinite_supply
        cmd_debug.infinite_supply(dstate.infinite_supply)
    if keyboard.get_key_down('f6'):
        dstate.controlling_ugv -= 1
        if dstate.controlling_ugv < 1:
            dstate.controlling_ugv = 1
    if keyboard.get_key_down('f7'):
        dstate.controlling_ugv += 1

    if keyboard.get_key_down('e'):
        cmd_ugv.start_motor(dstate.controlling_ugv)
    if keyboard.get_key_down('q'):
        cmd_ugv.stop_motor(dstate.controlling_ugv)

    if keyboard.get_key_down('+'):
        cmd_ugv.set_gear(dstate.controlling_ugv, True)
    if keyboard.get_key_down('-'):
        cmd_ugv.set_gear(dstate.controlling_ugv, False)

    if keyboard.get_key_down('o'):
        cmd_ugv.set_handbrake(dstate.controlling_ugv, True)
    if keyboard.get_key_down('l'):
        cmd_ugv.set_handbrake(dstate.controlling_ugv, False)

    if keyboard.get_key_down('0'):
        cmd_ugv.set_turn_choice(dstate.controlling_ugv, 0)
    if keyboard.get_key_down('1'):
        cmd_ugv.set_turn_choice(dstate.controlling_ugv, 1)

    if keyboard.get_key_down('t'):
        cmd_ugv.start_supply(dstate.controlling_ugv, dstate.subject_station, dstate.cmd_interop.SUPPLY_FUEL)
    if keyboard.get_key_down('g'):
        cmd_ugv.start_supply(dstate.controlling_ugv, dstate.subject_station, dstate.cmd_interop.SUPPLY_WATER)
    if keyboard.get_key_down('y'):
        cmd_ugv.stop_supply(dstate.controlling_ugv, cmd_interop.SUPPLY_FUEL)
    if keyboard.get_key_down('h'):
        cmd_ugv.stop_supply(dstate.controlling_ugv, cmd_interop.SUPPLY_WATER)

    # Firehose pressure
    if keyboard.get_key_down('d'):
        dstate.fire_hose_pressure += 0.5
        cmd_ugv.adjust_firehose(dstate.controlling_ugv, dstate.fire_hose_pressure)
    if keyboard.get_key_down('a'):
        dstate.fire_hose_pressure -= 0.5
        if dstate.fire_hose_pressure < 0:
            _fire_hose_pressure = 0
        cmd_ugv.adjust_firehose(dstate.controlling_ugv, _fire_hose_pressure)

    # Firehose direction
    if keyboard.get_key_down('z'):
        dstate.fire_hose_dir[0] -= 1
        update_firehose()
    if keyboard.get_key_down('x'):
        dstate.fire_hose_dir[0] += 1
        update_firehose()
    if keyboard.get_key_down('c'):
        dstate.fire_hose_dir[1] -= 1
        update_firehose()
    if keyboard.get_key_down('v'):
        dstate.fire_hose_dir[1] += 1
        update_firehose()
    if keyboard.get_key_down('b'):
        dstate.fire_hose_dir[2] -= 1
        update_firehose()
    if keyboard.get_key_down('n'):
        dstate.fire_hose_dir[2] += 1
        update_firehose()

    if keyboard.get_key_down('f11'):
        dstate.subject_station -= 1
        if dstate.subject_station < 1:
            dstate.subject_station = 1
    if keyboard.get_key_down('f12'):
        dstate.subject_station += 1

    cmd_ugv.set_throttle(dstate.controlling_ugv, 1 if keyboard.get_key('w') else 0)
    cmd_ugv.set_brake(dstate.controlling_ugv, 1 if keyboard.get_key('s') else 0)