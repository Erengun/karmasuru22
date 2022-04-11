from enum import Enum

class Ugv:
    id = -1
    is_active = None
    
    # Motor
    motor_state = None
    motor_start_time = None
    motor_stop_time = None
    respawn_time = None

    # Fuel
    fuel_capacity = None
    fuel_solace = None
    fuel_consumption_add = None
    fuel_consumption_multiply = None
    fuel_consumption_throttle_multiply = None

    water_capacity = None
    position = []
    edge = None
    hermit_value = None
    turn_choice = None
    throttle = None
    brake = None
    forward_gear = None
    handbrake = None
    fuel_value = None
    water_value = None
    attached_fuel_station_id = None
    attached_water_station_id= None
    firehose_dir = []
    firehose_pressure = None

class UgvError:
    errors = []
    def get_data(self, data):
        error_data = {
            "id":data[0],
            "error_code":data[1]
        }
        self.errors.append(error_data)


error_dict = {
    1:"UNSPECIFIED",
    2:"TRY_AGAIN_LATER",
    3:"VEHICLE_IN_MOTION",
    4:"VEHICLE_TOO_FAST",
    5:"MOTOR_IS_NOT_STARTED",
    6:"MOTOR_IS_NOT_STOPPED",
    7:"OUT_OF_FUEL",
    8:"STATION_NOT_FOUND",
    9:"ALREADY_ATTACHED_FOR_THIS_SUPPLY_TYPE",
    10:"STATION_NOT_SERVING_SUPPLY_TYPE",
    11:"STATION_OUT_OF_RANGE",
    12:"STATION_OUT_OF_CAPACITY",
    13:"STATION_NOT_ATTACHED_YET"
}

def error_to_string(err_code):
    return error_dict[err_code]
    