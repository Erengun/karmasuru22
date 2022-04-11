
class Fire:
    FIRE_ID = None
    FIRE_LOCATION = []
    FIRE_RADIUS = None
    FIRE_STRENGTH_FACTOR  = None
    FIRE_GROWING_SPEED = None
    FIRE_MAXIMUM_STRENGTH_FACTOR = None
    FIRE_STRENGTH = None
    FACTOR_SPEED = None

    def get_data(self, data):
        self.FIRE_ID = data[0]
        self.FIRE_LOCATION = data[1]
        self.FIRE_RADIUS = data[2]
        self.FIRE_STRENGTH_FACTOR = data[3]
        self.FIRE_GROWING_SPEED = data[4]
        self.FIRE_MAXIMUM_STRENGTH_FACTOR = data[5]
        self.FIRE_STRENGTH = data[6]
        self.FACTOR_SPEED = data[7]
