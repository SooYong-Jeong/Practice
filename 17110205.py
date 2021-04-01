class TU:   #학생정보 클래스
    def  __init__(self):
        self.TU = 0

    def Input_ID(self): #학번 입력 함수
        print("Input Your ID : ")
        self.ID = input()

    def Input_Name(self):   #이름 입력 함수
        print("Input Your Name : ")
        self.Name = input()

    def print_ID_name(self):    #학번, 이름 출력 함수
        print(f"Your ID is {self.ID}, and your name is {self.Name}")

JSY = TU()

JSY.Input_ID()
JSY.Input_Name()
JSY.print_ID_name()