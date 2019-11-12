import random
import sys
import os

class Room:
    __name = ""
    __directions = ["", "", "", ""]
    __text = ""
    
    def __init__(self, name, dir1, dir2, dir3, dir4, text):
        self.__name = name
        self.__directions = [dir1, dir2, dir3, dir4]
        self.__text = text
    
    def getName(self):
        return self.__name
    
    def getText(self):
        return self.__text
    
    def getDir(self, direction):
        return self.__directions[direction]

def __main__():
    print("hello world!")
    # Top 3 rooms
    topLeft = Room("top left", "no", "yes", "no", "yes",
                   "You are in the top left room")
    topCenter = Room("top center", "no", "yes", "yes", "yes",
                     "You are in the top center room")
    topRight = Room("top right", "no", "yes", "yes", "no",
                    "You are in the top right room")
    
    # Middle 3 rooms
    middleLeft = Room("middle left", "yes", "yes", "no", "yes",
                      "You are in the middle left room")
    middleCenter = Room("middle center", "yes", "yes", "yes", "yes",
                        "You are in the middle center room")
    middleRight = Room("middle right", "yes", "yes", "yes", "no",
                       "You are in the middle right room")
    
    # Bottom 3 rooms
    bottomLeft = Room("bottom left", "yes", "no", "no", "yes",
                      "You are in the bottom left room")
    bottomCenter = Room("bottom center", "yes", "no", "yes", "yes",
                        "You are in the bottom center room")
    bottomRight = Room("bottom right", "yes", "no", "yes", "no",
                       "You are in the bottom right room")
    
    rooms = [topLeft, topCenter, topRight,
             middleLeft, middleCenter, middleRight,
             bottomLeft, bottomCenter, bottomRight]
    
    current = 4
    done = 0
    print "To move (l)eft, (r)ight, (u)p, (d)own, (q)uit\n"
    while (not(done)):
        print "    ****", rooms[current].getName(), "****    "
        print(rooms[current].getText())
        print "-----------------------------------"
        c = raw_input("Which direction do you want to go? ")
        if c == 'u':
            result = rooms[current].getDir(0);
            if result == 'yes':
                current -= 3
            else:
                print "\nYou can't go that way."
        elif c == 'd':
            result = rooms[current].getDir(1);
            if result == 'yes':
                current += 3
            else:
                print "\nYou can't go that way."
        elif c == 'l':
            result = rooms[current].getDir(2);
            if result == 'yes':
                current -= 1
            else:
                print "\nYou can't go that way."
        elif c == 'r':
            result = rooms[current].getDir(3);
            if result == 'yes':
                current += 1
            else:
                print "\nYou can't go that way."
        elif c == 'q':
            print "\nGoodbye"
            done += 1
        else:
            print "That was not a valid input. Try again."
        print "\n"


if __name__ == "__main__":
    __main__()
