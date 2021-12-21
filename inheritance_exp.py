# Parent class
class Property_Types(object):
    print("In super class")
    # Constructor

    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability

    def display(self):
        print("\nIn parent class display method")
        print("Name:", self.name)
        print("Availability:", self.price)
        print("Price:", self.availability)

# Child Class 1
class Private_room(Property_Types):
    print("In subclass private room")
    str1 = 'Private room'
    def __int__(self, name, price, availability, room_id):
        self.room_id = room_id

        # calling parent class constructor
        Property_Types.__init__(self,name, price, availability)

    print("\n In private room child class")

room = input("Enter room Name:")
availability = int(input("Enter Availability:"))
price = int(input("Enter Price:"))

# Creating a Object of child class
private_room_obj = Private_room(room, availability, price)

private_room_obj.display()

# Child Class 2
class Entire_Home(Property_Types):
    print("In subclass Entire_Home")
    str = "Sweet Home"
    def __int__(self, name, price, availability, home_id):
        self.home_id = home_id

        # calling parent class constructor
        Property_Types.__init__(self,name, price, availability)

    print("\n In Entire_Home child class")

room = input("Enter Home Name:")
availability = int(input("Enter Availability:"))
price = int(input("Enter Price:"))

class Shared(Private_room, Entire_Home):
    def __int__(self):
        print("Calling constructor of private room and Entire Home subclasses")
        Private_room.__init__(self, price, availability)
        self.price=price
        self.availability=availability


        Entire_Home.__init__(self, price, availability)
        self.price = price
        self.availability = availability

        print("Shared room class formed from 2 classes Private room & EntireHome by Multiple Inheritance")

    def shared_display(self):
        print("Got attribute from one parent class:", private_room_obj.str1)
        print("Got attribute from one parent class:", shared_obj.str)

# Creating a Object of child class
shared_obj = Shared(room, availability, price)
shared_obj.shared_display()

