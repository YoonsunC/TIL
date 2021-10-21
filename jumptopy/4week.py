# 객체 지향 프로그래밍(Object Oriented Programming, OOP) : 함수처럼 어떤 기능을 함수 코드에 묶어 두는 것이 아니라, 그런 기능을 묶은 하나의 단일 프로그램을 객체라고 하는 코드에 넣어 다른 프로그래머가 재사용할 수 있도록 하는, 컴퓨터 공학의 오래된 프로그래밍 기법 중 하나  
# 객체(object) : 실생활에 존재하는 실제적인 물건 또는 개념 ex)심판,선수,팀  
# 속성(attribute) : 객체가 가지고 있는 변수 ex)선수의 이름, 포지션, 소속팀  
# 행동(action) : 객체가 실제로 작동할 수 있는 함수, 메서드 ex)공을 차다, 패스하다  

# 클래스를 사용하면 편리하게 코드 작성 가능  

# 클래스(class) : 객체가 가져야 할 기본 정보를 담은 코드  
# 클래스는 일종의 설계도 코드  
# 실제로 생성되는 객체를 인스턴스(instance)라고 함  

# 잘 만든 붕어빵틀(클래스) -> 새로운 종류의 다양한 붕어빵(인스턴스)  

# 파이썬에서 클래스를 선언하기 위한 기본 코드 템플릿  
# class SoccerPlayer(object):  
# 클래스예약어 클래스 이름 상속받는 객체명  

# 클래스의 이름을 선언할 때 첫글자, 중간글자가 대문자  
# snake_case : 띄어쓰기 부분에 '_'를 추가하여 변수의 이름 지정 (파이썬 함수, 변수명에 사용)  
# CamelCase : 띄어쓰기 부분에 대문자를 사용하여 변수의 이름 지정 (낙타의 혹 / 파이썬 클래스명에 사용)  

# 속성의 선언 : __init__() 이라는 예약함수 사용  
# __init__() : 이 클래스에서 사용할 변수를 정의하는 함수  
# __init__() 함수의 첫번째 매개변수는 반드시 self 변수를 사용해야 함.  
# self 변수는 클래스에서 생성된 인스턴스에 접근하는 예약어  
# self 뒤의 매개변수들은 실제로 클래스가 가진 속성(축구 선수의 이름, 포지션, 등번호)  
# 이 값들은 실제 생성된 인스턴스에 할당됨  
# 할당되는 코드는 self.name=name  

# 함수는 이 클래스가 의미하는 어떤 객체가 하는 다양한 동작을 정의할 수 있음  
# if) 축구선수 - 등번호 교체라는 행동  
# 클래스 내에서의 함수도 기존 함수와 크게 다르지 않음 - 함수의 이름을 쓰고 매개변수를 사용하면 됨  
# 가장 큰 차이점 -> self를 매개변수에 반드시 넣어야 함 / self가 있어야만 실제로 인스턴스가 사용할 수 있는 함수로 선언됨  

# _의 쓰임 : _1개 -> 이후로 쓰이지 않을 변수에 특별한 이름을 부여하고 싶지 않을 때  
#         : _2개 -> 특수한 예약 함수나 변수에 사용 ex) __str__ / __init__()  
#         __str() : 클래스로 인스턴스를 생성했을 때, 그 인스턴스 자체를 print()함수로 화면에 출력하면 나오는 값  

# 인스턴스 호출법 : yoonsun = SoccerPlayer("yoonsun", "MF", 10):  
#                 객체명      클래스 이름     __init__함수 interface, 초깃값  
# yoonsun이라는 인스턴스가 기존 SoccerPlayer의 클래스를 기반으로 생성되는 것 확인 가능  
# 이 yoonsun이라는 인스턴스 자체가 SoccerPlayer 클래스에서 self에 할당된다  

# 클래스를 사용하는 이유  
# : 자신이 만든 코드가 데이터 저장뿐 아니라 데이터를 변환하거나 데이터베이스에 저장하는 등의 역할이 필요할 때  
# 이것을 리스트와 함수로 각각 만들어 공유하는 것보다 하나의 객체로 생성해 다른 사람들에게 배포한다면 손쉽게 사용 가능  
# 또한 코드를 더 손쉽게 선언 가능  

# 노트북 프로그램 만들기 설계  
# - 노트를 정리하는 프로그램  
# - 사용자는 노트에 콘텐츠를 적을 수 있음  
# - 노트는 노트북에 삽입됨  
# - 노트북은 타이틀이 있음  
# - 노트북은 노트가 삽입될 때 이미지를 생성, 최대 300페이지까지 저장 가능  
# - 300페이지를 넘기면 노트를 더는 삽입하지 못함  

# Note 클래스
# class Note(object):
#     def __init__(self, contents=None): # 노트를 만들어놓고 빌 수도 있으므로 None
#         self.contents = contents #contents를 self로 만듦
    
#     def write_contents(self,contents):
#         self.contents = contents #컨텐츠가 입력한 컨텐츠로 변경되도록 하는 함수

#     def remove_all(self): 
#         self.contents = "" #컨텐츠를 지우기 위해 공백

#     def __str__(self):
#         return self.contents #컨텐츠를 반환

class NoteBook(object):
    def __init__(self, title): # init함수 안에 아래 세가지 정보 입력
        self.title = title
        self.page_number = 1
        self.notes = {} #노트를 딕셔너리 형태로 설계

    def add_note(self, note, page = 0): #새로운 노트를 노트북에 삽입
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number]=note
                self.page_number += 1
            else: 
                self.notes = {page : note}
                self.page_number += 1
        else: #페이지 300페이지 이상
            print("페이지가 모두 채워졌다.")

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않는다.")

    def get_number_of_pages(self):
        return len(self.notes.keys())

#notebook_client.py
from notebook import Note
from notebook import NoteBook
good_sentence = ""세상 사는 데 도움이 되는 명언""

#notebook.py

객체지향 프로그래밍의 특징  
상속(inheritance) : 무엇인가를 내려받는 것. 부모 클래스에 정의된 속성과 메서드를 자식 클래스가 물려받아 사용하는 것  
class라는 예약어 다음 클래스명으로 Person을 쓰고 object를 입력.  
-> object가 Person 클래스의 부모 클래스  
class Person(object):
    pass  
상속이 진행될수록 부모 클래스에 대해 각 클래스의 기능이 구체화되도록 부모 객체에는 일반적인 기능을, 자식 객체에는 상세한 기능을 넣어야 함  
같은 일을 하는 메서드이지만 부모 객체보다 자식 객체가 더 많은 정보를 줄 수 있음 -> 부모 클래스의 메서드를 재정의  

다형성(polymorphism): 같은 이름의 메서드가 다른 기능을 할 수 있도록 하는 것  

가시성(visibility) : 객체의 정보를 볼 수 있는 레벨을 조절하여 객체의 정보 접근을 숨기는 것.
파이썬에서는 가시성이라고 하지만 핵심 개념은 캡슐화(encapsulation)와 정보은닉(information hiding)
파이썬의 가시성 사용방법에 대한 예시 코드
- Product 객체를 Inventory 객체에 추가
- Inventory에는 오직 Product 객체만 들어감
- Inventory에 Product가 몇 개인지 확인 필요 
- Inventory에 Product items는 직접 접근이 불가