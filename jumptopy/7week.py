Tkinter : 파이썬에서 그래픽 사용자 인터페이스 (GUI; Graphical user interface)를 개발할 때 필요한 모듈

GUI : 사용자가 그래픽을 통해 프로그램과 상호작용할 수 있는 환경
-> 즉, 사용자가 일으키는 Event 기반의 프로그래밍 구조

Python설치 시 기본적으로 내장되어있는 표준 라이브러리

Tkinter Programming 개요
1. TK 객체 생성 및 RootWindow 생성
2. Window내에 위치할 다양한 Widget, 구성요소 생성
3. 생성된 객체들을 Window 내에 배치

from tkinter import *
window = Tk()
## 이 부분에서 화면을 구성하고 처리 ##
window.mainloop()

레이블(Label) : 문자를 표현할 수 있는 위젯
레이블에 글자 대신 이미지 넣기 : PhotoImage()는 GIF 파일만 지원, JPEG나 BMP 등은 지원하지 않음

버튼(Button) : 마우스로 클릭하면 눌리는 효과와 함께 지정한 작업 실행
ex : 버튼을 누르면 파이썬 IDLE이 종료되는 코드

체크버튼 : 켜고 끄는 데 사용하는 위젯
라디오버튼 : 여러개 중에서 하나를 선택하는데 사용하는 위젯
수평정렬 : 수평으로 정렬하는 방법. pack()함수의 옵션 중 side=LEFT,RIGHT
수직정렬 : pack()함수의 옵션 중 수직으로 정렬하는 방법 : side=TOP,BOTTOM
폭 조정 : pack()함수의 옵션 중에서 윈도창 폭에 맞추는 방법 fill=X
위젯 사이의 여백 조절 : pack()함수의 옵션 중에서 위젯 사이에 여백 주는 방법 : padx=픽셀값 또는 pady=픽셀값
위젯 내부의 여백 조절 : pack()함수의 옵션 중에서 위젯 내부에 여백 주는 방법 : ipadx=픽셀값 또는 ipady=픽셀값
고정 위치에 배치 : 위젯을 고정 위치에 배치하려면 pack()대신 place()함수 사용

마우스 이벤트가 처리형식
def 이벤트처리함수(event):
    # 이 부분에 마우스 이벤트가 발생할 때 작동할 내용 작성

위젯.bind("마우스이벤트", 이벤트처리함수)

키보드이벤트
Enter를 처리하려면 <Key> 대신 <Return>을 사용
대,소문자 등도 구분해서 처리 가능
소문자 r은 <Key> 대신에 r을 사용해 처리
일반키를 누를 때 주의할 점은 SpaceBar는 <Space>로, <는 <less>로 사용

대화상자의 생성과 사용
tkinter.simpledialog 모듈을 임포트 한 후 askinteger()및 askstring()등을 사용

