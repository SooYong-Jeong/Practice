class TU:
    def  __init__(self):
        self.TU = 0

    def Input_ID(self):
        print("Input Your ID : ")
        self.ID = input()

    def Input_Name(self):
        print("Input Your Name : ")
        self.Name = input()

    def print_ID_name(self):
        print(f"Your ID is {self.Id}, and your name is {self.Name}")

JSY = TU()

JSY.Input_ID()
JSY.Input_Name()
JSY.print_ID_name()