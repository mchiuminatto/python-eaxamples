class House:
    def __init__(self, address, house_key, **rooms) -> None:
        self.address = address
        self.__house_key = house_key
        self.__locked = True
        self._rooms = dict()

        for room, desc in rooms.items():
            self._rooms[room.replace("_", " ").lower()] = desc

    def unlock_house(self, house_key):
        if self.__house_key == house_key:
            self.__locked = False

        else:
            raise RuntimeError("Wrong key! Could not unloock house.")
        
    def explore(self, room):
        if self.__locked:
            raise RuntimeError("Cannot explore locked house")
        
        try:
            return f"The {room.lower()} is {self._rooms[room.lower()]}. "
        except KeyError as e:
            raise KeyError(f"No room {room}") from e
        
    def lock_house(self):
        self.__locked = True
        print("House locked!")


    
class HouseShowing:

    def __init__(self, house: House, house_key):
        self.house: House = house
        self.House_key = house_key

    def __enter__(self):
        self.house.unlock_house(self.House_key)
        return self
    
    def show(self, room):
        print(self.house.explore(room))

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Sorry about that.")
        self.house.lock_house()
        
    

house = House("123 Anywhere Street", 
              house_key=1803,
              living_room="spacious",
              office="bright",
              bedroom="cozy",
              bathroom="small",
              kitchen="modern")


# case ok
with HouseShowing(house, 1803) as showing:
    showing.show("Living Room")
    showing.show("bedroom")
    showing.show("kitchen")


# case room not found
# with HouseShowing(house, house_key=1803) as showing:
#     showing.show("Living Room")
#     showing.show("bedroom")
#     showing.show("porch")

# case house locked
# with HouseShowing(house, house_key=9999) as showing:
#     showing.show("Living room")
#     showing.show("bedroom")
#     showing.show("porch")
