# id = index
# range = diameter
from src.state.supply_item import SupplyItem

class Station:
    index = None
    location = None
    diameter = None
    vehicle_capacity = None
    supply_items = []

    def get_data(self, data):
        self.index = data[0]
        self.location = data[1]
        self.diameter = data[2]
        self.vehicle_capacity = data[3]

        items_data = data[4]
        for item_data in items_data:
            new_item = SupplyItem()
            new_item.get_data(item_data)
            self.supply_items.append(new_item)

        



        