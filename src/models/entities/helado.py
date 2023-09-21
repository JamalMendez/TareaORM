class Helado():
    def __init__(self,id, store_id=None, EMPLOYEE_id=None, date=None, flavor=None, is_season_flavor=None, quantity=None) -> None:
        self.id = id
        self.store_id = store_id
        self.EMPLOYEE_id = EMPLOYEE_id
        self.date = date
        self.flavor = flavor
        self.is_season_flavor = is_season_flavor
        self.quantity = quantity

    def toJSON(self):
        return{
            'id' : self.id,
            'store_id' : self.store_id,
            'EMPLOYEE_id' : self.EMPLOYEE_id,
            'date' : self.date,
            'flavor' : self.flavor,
            'is_season_flavor' : self.is_season_flavor,
            'quantity' : self.quantity,
        }