#region Print
'''
print(5)
print(-5)
print(3.14)
print(100000)
print(5 + 3)
print(5 * 10)
print(3 * (3+1))
print('풍선')
print("나비")
print('ㄹㅇㅋㅋ')
print('ㄹㅇㅋㅋ'* 4)
print(1>10)
print(1<10)
print(True)
print(False)
print(not 1>10)
print(not 1<10)
'''
#endregion
#region Variable
'''
name = "정수용"
sex = "남"
age = 24
hight = 178
weight = 73
is_adult = age >= 20

print("내이름은" , name)
print("나이는" , age , "이고")
print("어른인가?" , is_adult)
'''
#endregion
#region Quiz1
'''
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")
'''
#endregion
#region Calculation
'''
print(2**10)
print(100//5)
'''
#endregion
#region Maxminrandom
'''
print(abs(-1))      #절댓값
print(pow(2, 4))    #지수
print(max(5, 10))   #최댓값
print(min(1, 5))    #최솟값
print(round(3.14))  #반올림
print(round(3.99))
print(round(3.14))  
from math import *  #math 라이브러리
print(floor(3.99))  #내림
print(ceil(3.14))   #올림
print(sqrt(16))     #제곱근
'''
'''
from random import *

print(random())             #0.0 ~ 1.0미만
print(random() *10)         #0.0 ~ 10.0미만
print(int(random() *10))    #0 ~ 10미만  

print(randrange(1, 46))     #1 ~ 46미만
print(randrange(1, 45))     #1 ~ 45
'''
#endregion
#region Quiz2
'''
from random import *

print("오프라인 스터디 모임 날짜는 매월"+ str(randrange(4, 29)) +"일로 선정되었습니다")
'''
#endregion
#region Sentence
'''
se = '가나다라마바사'
se2 = "가나다라마바사"
se3 = """
가나다라마바사
아자차카타파하
에헤
"""
print(se)
print(se2)
print(se3)
'''
#endregion
#region Slicing
'''
per = "980119-1118011"

print("성별 : " + per[7])
print("생년 : " + per[0:2])         #0 ~ 2 직전까지
print("월 : " + per[2:4])
print("일 : " + per[4:6])
print("생년월일 : " + per[:6])      #처음부터
print("뒷자리 : " + per[7:])        #끝까지
print("뒷자리 : " + per[-7:])       #뒤부터
'''
#endregion
#region Sentence_function
'''
python = "Python is Greatn"
print(python.lower())       #전부 소문자
print(python.upper())       #전부 대문자
print(python[0].isupper())  #해당글자 논리
print(len(python))          #문자열 길이
print(python.replace("Python", "Java")) #치환

print(index)
index = python.index("n", index + 1) #그다음번째
print(index)
print(python.find("java"))  #문자찾기(없다면 -1을 반환)
print(python.count("n"))    #문자횟수
'''
#endregion
#region Sentence_format
'''
print("%d" % 30)
print("%s" % "정수용")
print("%c" % "a")

print("%s" % 30)
print("%s %s" % ("하나", "둘"))

print("{}".format(20))
print("{} {}".format(20, 10))
print("{1} {0}".format(20, 10))

print("{color} {age}".format(age = 20, color = "하나"))

age = 20
color = "하나"
print(f"{color} {age}")

print("\"\"\"\"")
print("\\")
#\r = 커서를 앞으로
print("asdasd\rdddddddd")
#\b = 백스페이스
#\t = 탭
'''
#endregion
#region Quiz3
'''
site = "https://www.naver.com"
site_1 = site[site.index(".") + 1:site.index(".",site.index(".") + 1)]

PW = site_1[:3] + str(len(site_1)) + str(site_1.count('e')) + "!"
print(site_1)
print(PW)
'''
#endregion
#region List
'''
subway = [0,2,3]
print(subway.index(2))
subway.append(4)
print(subway)
subway.insert(1,1)
print(subway)

print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

subway.append(1)
print(subway.count(1))

num = [3,4,2,5,1]
num.sort()
print(num)

num.reverse()
print(num)

# num.clear()
# print(num)

num.extend(subway)
print(num)
'''
#endregion
#region Cabinet
'''
cabinet = {3:"정수용", 100:"홍길동"}

# print(cabinet[3])   #값이 없는경우 프로그램 종료
# print(cabinet[100])

# print(cabinet.get(3)) #값이 없는경우 넘어감

print(3 in cabinet)
print(5 in cabinet)

cabinet[50] = "신규"
print(cabinet)

del cabinet[100]  # 지우기
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)
'''
#endregion
#region Tuple
'''
menu = ("제육", "라면")
print(menu[0])
print(menu[1])

name, age, hobby = "정수용", 24, "코딩"
print(name, age, hobby)
'''
#endregion
#region Set
#중복 안됨, 순서 없음
'''
my_set = {1,2,3,3,3}
print(my_set)

java = {"갑", "을", "병", "정"}
python = set(["을", "정"])
#교집합
print(java & python)
print(java.intersection(python))
#합집합
print(java | python)
print(java.union(python))
#차집합
print(java - python)
print(java.difference(python))
#추가
python.add("무")
print(python)
#삭제
java.remove("을")
print(java)
'''
#endregion
#region Change
'''
menu = {"커피", "우유", "쥬스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))
'''
#endregion
#region Quiz4
'''
from random import *
ID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#ID = range(1, 21) 1부터 20까지 숫자를 생성
#ID = list(ID) list형으로 변환
shuffle(ID)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : ", ID.pop())
print("커피 당첨자 : ", sample(ID, 3))
print("-- 축하합니다 --")
print(ID)
'''
#endregion
#region If
'''
weather = input("today weather?")
if weather == "rain" or weather == "snow":
    print("umbrella")
elif weather == "dust":
    print("mask")
else:
    print("-")

temp = int(input("temp?"))

if 30 <= temp:
    print("too hot")
elif 10 <= temp < 30:
    print("good")
else:
    print("too cold")
'''
#endregion
#region For
'''
for ex in range(6):
    print("number : {0}".format(ex))
for ex in [0,1,2,3,4,5]:
    print("number : {0}".format(ex))
for ex in range(1,6):
    print("number : {0}".format(ex))

user = ["A","B","C"]
for customer in user:
    print("{0}, thanks.".format(customer))
    '''
#endregion
#region While
'''
user = "A"
index = 5
while index >= 1:
    print("{0}, ready. {1} number.".format(user, index))
    index -= 1
    if index == 0:
        print("user no.")
lndex = 1
while True:
    print("{0}, ready. {1} number.".format(user, lndex))
    lndex += 1
    if lndex == 5:
        print("user no.")
        break
    '''
#endregion
#region Continue
'''
absent = [2, 5]
for student in range(1,11):
    if student in absent:
        continue
    print("{0} student".format(student))
    '''
#endregion
#region One_Line_For
'''
students = range(1,6)
print(students)
students = [i+100 for i in students]
print(students)

students = ["QWRDASF", "QWFD AWEQWE", " QWES"]

students = [i.lower() for i in students]
print(students)

students = [len(i) for i in students]
print(students)
'''
#endregion
#region Quiz5
'''
from random import *
matching = 0
for coustomer_matching in range(50):
    i = randrange(5, 51)
    if i <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(coustomer_matching,i))
        matching += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(coustomer_matching,i))
print("총 탑승 승객 : {0}명".format(matching))
'''
#endregion
#region Function
'''
balance = 0
money = 0
def open_account():             #intro
    print("new account.")

def deposit(balance, money):    #입금함수
    print("balance : {0}$".format(balance + money))
    return balance + money

def withdraw(balance, money):   #출금함수
    if balance < money:
        print("insufficient cash. balance : {0}$".format(balance))
        return balance
    else:
        print("balance : {0}$".format(balance - money))
        return balance - money

open_account()
balance = deposit(balance, 1000)
balance = withdraw(balance, 300)
print(balance)
'''
#endregion
#region Default
'''
def profile(name, age = 24, sex = "female"):
    print("name : {0}\nage : {1}\nsex : {2}".format(name, age, sex))
profile(name = "정수용", sex = "male")
'''
#endregion
#region Variable_factor
'''
def profile(name, age, sex, *language):
    print("name : {0}\nage : {1}\nsex : {2}".format(name, age, sex))
    for i in language:
        print(i, end = " ")
    print()
profile("정수용", 24,  "male", "Java", "C", "C++", "Python")
'''
#endregion
#region Local_Global
'''
gun = 10
def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[func in]remain guns : {0}".format(gun))

print("total guns : {0}".format(gun))
checkpoint(2)
print("remain guns : {0}".format(gun))
'''
#endregion
#region Quiz6
'''
def std_weight(height, sex):
    if sex == "남자":
        return pow(height/100, 2) * 22
    elif sex == "여자":
        return pow(height/100,2) * 21
sex = input("성별입력(\"남자\" or \"여자\")")
height = int(input("키 입력(cm)"))
weight = round(std_weight(height, sex), 2)
print("키{0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, sex, weight))
'''
#endregion
#region Input_Output
'''
import sys
print("Java", "Python","JavaScript", sep = ", ", end = "?")
print("-???")
print("Java", "Python","JavaScript", file = sys.stdout)#표준출력
print("Java", "Python","JavaScript", file = sys.stderr)#표준에러

score = {"국어":90, "수학":100, "영어":70}
for subject, score in score.items():
    #print(subject, score)
    print(subject.ljust(9), str(score).rjust(4), sep = ":")#좌우정렬

for num in range(1, 21):
    print("대기번호 : " +str(num).zfill(3))# 빈공간 0으로 채우기

answer = input("input anyone. : ")
print(type(answer))#입력할땐 다  string으로 저장
print("input things : " + answer)
'''
#endregion
#region Output
'''
print("{0: >10}".format(500))   #빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >+10}".format(500))  #양수일땐 +,  음수일땐 -
print("{0: >+10}".format(-500))
print("{0:_<+10}".format(500))  #왼쪽정렬, 양수음수표시, 빈칸대신_, 자릿수확보
print("{0:+,}".format(1000000000000000000000))  #3자리마다 콤마
print("{0:^<+30,}".format(100000000000000))     #3자리마다 콤마, 왼쪽정렬, 양수음수표시, 빈칸대신^, 자릿수확보
print("{0:f}".format(5/3))  #소숫점 출력
print("{0:.2f}".format(5/3))  #소숫점 셋째자리에서 반올림해서 출력
'''
#endregion
#region File_Input
'''
score_file = open("score.txt","w", encoding = "utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()
'''
'''
score_file = open("score.txt","a", encoding = "utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()
'''
'''
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()
'''
'''
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") #한줄만 읽기
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()
'''
'''
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()
'''
'''
score_file = open("score.txt", "r", encoding="utf8")# list에 정리하기
lines = score_file.readlines()
for line in lines:
    print(line, end="")

score_file.close()
'''
#endregion
#region Pickle
'''
import pickle

profile_file = open("profile.pickle", "wb")
profile = {"이름":"정수용", "나이":24, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()
'''
'''
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # prifile에 있는 정보를 file로 불러오기
print(profile)
profile_file.close()
'''
#endregion
#region With
'''
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
'''
'''
with open("study.txt", "w", encoding="utf8") as study_file:#파일 쓰기
    study_file.write("study hard.")

with open("study.txt", "r", encoding="utf8") as study_file:#파일 읽기
    print(study_file.read())
'''
#endregion
#region Quiz7
'''
for i in range(1,51):
    with open(f"{i}주차.txt", "w", encoding="utf8") as report_file:
        report_file.write(f"""
        - {i} 주차 주간보고 -
        부서 : 
        이름 : 
        업무 요약 : 
        """)
'''
#endregion
#region Class
'''
from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛이 생성되었습니다.")
    
    def move(self, location):
        print("[지상유닛이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name}이(가) 파괴되었습니다.")

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. 공격력 {self.damage}")

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중유닛이동]")
        self.fly(self.name, location)

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def strampack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")


class Tank(AttackUnit):
    seize_developed = False
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.seize_mode = True
        
        else:
            print(f"{self.name} : 시즈모드를 해제합니다.")
            self.damage /= 2
            self.seize_mode = False

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == False:
            print(f"{self.name} : 클로킹 모드를 설정합니다.")
            self.clocked = True
        
        else:
            print(f"{self.name} : 클로킹 모드를 해제합니다.")
            self.clocked = False

def game_start():
    print("Computer : 한수요")

def game_over():
    print("Computer : GG ")
    print("SYSTEM : 상대가 나갔습니다.")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("탱크 시즈모드 개발완료.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.strampack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5, 100))

game_over()
'''
#endregion
#region Quiz8
'''
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")

house = []
gangnam_apt = House("강남", "아파트", "매매", "10억", "2010년")
mapo_off = House("마포", "오피스텔", "전세", "5억", "2007년")
songpa_vil = House("송파", "빌라", "월세", "500/50", "2000년")

house.append(gangnam_apt)
house.append(mapo_off)
house.append(songpa_vil)
print(f"총 {len(house)}대의 매물이 있습니다.")
for house in house:
    house.show_detail()
'''
#endregion
#region Try
'''
try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("num1 : ")))
    nums.append(int(input("num2 : ")))
    #nums.append(int(nums[0]/nums[1]))

    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError:
    print("에러가 발생했습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 오류")
    print(err)
    '''
#endregion
#region Error
'''
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한자리 나누기 계산기")
    num1 = int(input("1num : "))
    num2 = int(input("2num : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f"입력값 : {num1}, {num2}")
    print(f"{num1} / {num2} = {num1 / num2}")
except ValueError:
    print("error")
except BigNumberError as err:
    print("Big number Error")
    print(err)
finally:
    print("Bye")
    '''
#endregion
#region Quiz9
'''
class SoldOutError(Exception):
    pass
chicken = 10
wating = 1
while(True):
    try:
        print(f"[남은 치킨 : {chicken}]")
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order <= 0:
            raise ValueError
        if order > chicken:
            print("재료가 부족합니다.")
        else:
            print(f"[대기번호 {wating}] {order} 마리 주문이 완료되었습니다.")
            wating += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
'''
#endregion
#region Module
'''
import theater_module
theater_module.price(3)
theater_module.price_moring(4)
theater_module.price_soldier(5)
'''
'''
import theater_module as mv
mv.price(3)
mv.price_moring(4)
mv.price_soldier(5)
'''
'''
from theater_module import*
price(3)
price_moring(4)
price_soldier(5)
'''
'''
from theater_module import price, price_moring
price(3)
price_moring(4)
try:
    price_soldier(5)
except NameError as err:
    print(err)
'''
'''
from theater_module import price_soldier as price
price(5)
'''
#endregion
#print("hi")