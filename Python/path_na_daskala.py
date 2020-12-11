from enum import Enum

map = [[1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]

def print_map(map):
    for row in map:
        print(row)
    print()

class Type(Enum):
    TREE = 1
    PLAYER = 2
    OLD = 3
        
class Player:
    def __init__(self, x, y, map):
        self.x = x
        self.y = y
        self.map = map
        self.map_size = len(map)
        self.update_player_pos()
        
    def update_player_pos(self):
        self.map[self.y][self.x] = Type.PLAYER
        print_map(self.map)

    def move_left(self):
        print("want to go left")
        if self.x - 1 < 0:
            print("Too left!")
            return False
        if map[self.y][self.x - 1] == 1 or map[self.y][self.x - 1] == Type.OLD:
            return False
        self.map[self.y][self.x] = Type.OLD
        self.x -= 1
        print("moving left")
        self.update_player_pos()
        return True

    def move_right(self):
        print("want to go right")
        if self.x + 1 >= self.map_size:
            print("Too right!")
            return False
        if map[self.y][self.x + 1] == 1 or map[self.y][self.x + 1] == Type.OLD:
            return False
        self.map[self.y][self.x] = Type.OLD
        self.x += 1
        print("moving right")
        self.update_player_pos()
        return True

    def move_up(self):
        print("want to go up")
        if self.y - 1 < 0:
            print("Too high!")
            return False
        if map[self.y - 1][self.x] == 1 or map[self.y - 1][self.x] == Type.OLD:
            return False
        self.map[self.y][self.x] = Type.OLD
        self.y -= 1
        print("moving up")
        self.update_player_pos()
        return True

    def move_down(self):
        print("want to go down")
        if self.y + 1 > self.map_size:
            print("Too low!")
            return False
        if map[self.y + 1][self.x] == 1 or map[self.y + 1][self.x] == Type.OLD:
            return False
        self.map[self.y][self.x] = Type.OLD
        self.y += 1
        print("moving down")
        self.update_player_pos()
        return True

    def setEndpoint(self, endpoint_y, endpoint_x):
        self.endpoint_y = endpoint_y
        self.endpoint_x = endpoint_x

    def move(self):
        if self.x > self.endpoint_x:
            if self.move_left():
                return
        if self.x < self.endpoint_x:
            if self.move_right():
                return
        if self.y > self.endpoint_y:
            if self.move_up():
                return
        if self.y < self.endpoint_y:
            if self.move_down():
                return   

        if self.move_left():
            return
        elif self.move_right():
            return
        elif self.move_up():
            return
        elif self.move_down():
            return

        print("NO WAY")
        return -1

player = Player(1, 0, map)
player.setEndpoint(2, 0)

print("Start")

while True:
    if player.move() == -1:
        break




