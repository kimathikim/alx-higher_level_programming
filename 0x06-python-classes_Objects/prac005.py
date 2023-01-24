#!/usr/bin/python3
class square:

    def __init__(self, height="0", weight="0"):
        self.height = height
        self.weight = weight

    @property
    def height(self):
        print("Retrieving height")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Enter numbers only!!!")

    @property
    def weight(self):
        print("Retrieving weight")
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        if value.isdigit():
            self.__weight = value
        else:
            print("Enter numbers only!!!")
    
    def getArea(self):
        return int(self.__height) * int(self.__weight)
    
def main():
    sq = square()

    height = input("Height: ")
    weight = input("Width: ")

    sq.height  = height
    sq.weight = weight

    print("Height :",sq.height)
    print("Width,height :", sq.weight)

    print("The area is :",sq.getArea())

main()