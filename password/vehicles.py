class Vehicle:
    def __init__(self, name, model, gas_left, mileage, max_speed):
        self.name = name
        self.model = model
        self.gas_left = gas_left
        self.mileage = mileage
        self.max_speed = max_speed
    
    def reload_gas(self):
        if self.gas_left == 0:
            self.gas_left += 100
            print("Added gas..")
    
class Car(Vehicle):
    def __init__(self, name, model, gas_left, mileage, max_speed, wheels, wheel_company, company_made, destination, current_location):
        super.__init__(name, model, gas_left, mileage, max_speed)
        self.wheels = 4
        self.wheel_company = wheel_company
        self.company_made = company_made
        self.destination = destination
        self.current_location = current_location
    
    def sound(self):
        return "Beep beep"
    
    def get_company(self):
        return self.company_made
    
    def check_if_arrived(self):
        if self.destination == self.current_location:
            print("Arrived to the destination..")
        
    
class Plane(Vehicle):
    def __init__(self, name, model, gas_left, mileage, max_speed, air_route, current_location, people, max_people, ticket_price):
        super().__init__(name, model, gas_left, mileage, max_speed)
        self.air_route = air_route
        self.current_location = current_location
        self.people = people
        self.max_people = max_people
        self.ticket_price = ticket_price
    
    def get_air_route(self):
        return self.air_route
    
    def buy_ticket(self):
        if len(self.people) == self.max_people:
            print("no ticket left")
        else:
            name = input("Your name:")
            print("Buying..")
            self.people.append(name)
 
