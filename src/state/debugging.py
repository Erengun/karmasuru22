
class Debugging:
    IGNORE_CRASHES = False
    SPEED_LIMIT = False
    INFINITE_SUPPLY = False

    def get_data(self, data):
        self.IGNORE_CRASHES = data[0]
        self.SPEED_LIMIT = data[1]
        self.INFINITE_SUPPLY = data[2]