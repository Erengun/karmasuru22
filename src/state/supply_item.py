
class SupplyItem:
    supply_type = None
    value = None
    capacity = None
    refill_speed = None
    transfer_speed = None

    def get_data(self, data):
        self.supply_type = data[0]

        self.value = data[1]
        self.capacity = data[2]
        self.refill_speed = data[3]
        self.transfer_speed = data[4]