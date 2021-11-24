## Matplotlib
Python에서 데이터를 차트나 플롯으로 그려주는 라이브러리 패키지로 가장 많이 사용되는 시각화 패키지
Line Plot, Bar Chart, Pie Chart, Box Plot, Scatter Plot 등

Matplotlib 설치 : Pip install matplotlib

## Pyplot
matplotlib.pyplot 모듈은 MATLAB과 비슷하게 명령어 스타일로 동작하는 함수의 모음
각각의 함수를 사용해서 간편하게 그래프를 만들고 변화를 줄 수 있음
그래프 영역을 만들고, 몇개의 선을 표현하고, 레이블로 꾸미는 등의 일을 할 수 있음

기본 그래프 그리기
pyplot.plot() 함수에 하나의 숫자 리스트를 입력
plot() 함수는 리스트의 값들이 y 값들이라고 가정하고, x값[0,1,2,3]을 자동으로 만들어냄
matplotlib.pyplot 모듈의 show() 함수는 그래프를 화면에 나타나도록 함
plot() 함수는 다양한 기능을 포함하고 있어서, 임의의 개수의 인자를 받을 수 있음

스타일 지정하기
x, y값 인자에 대해 선의 색상과 형태를 지정하는 포맷 문자열(Format string)을 세번째 인자에 입력 가능
포맷 문자열 'ro'는 빨간색('red')의 원형('o') 마커를 의미
'b-'는 파란색('blue')의 실선('-')을 의미
matplotlib.pyplot 모듈의 axis() 함수를 이용해서 축의 범위 [xmin, xmax, ymin, ymax]를 지정

Matplotlib에서는 일반적으로 NumPy array를 이용
np.arrange() 함수는 (시작, 끝, 간격)으로 구성되어 있음
다양한 스타일을 갖는 여러 개의 곡선을 하나의 그래프로 나타냄

축 레이블 설정하기
xlabel(), ylabel() 함수에 문자열을 입력

축 레이블 여백 설정하기
xlabel(), ylabel() 함수의 labelpad 파라미터는 축 레이블의 여백(Padding)을 지정
x축 레이블에 대해서 15pt, y축 레이블에 대해서 20pt 만큼의 여백을 지정

축 레이블 폰트 설정하기
xlabel(), ylabel() 함수의 fontdict 파라미터를 사용하면 축 레이블의 폰트 스타일을 설정할 수 있음
'family', 'color', 'weight', 'size'와 같은 속성을 사용해서 축 레이블 텍스트를 설정 가능

축 레이블 위치 지정
xlabel() 함수의 loc 파라미터는 x축 레이블의위치를 지정
({'left', 'center', 'right'})
ylabel() 함수의 loc 파라미터는 y축 레이블의 위치를 지정
({'bottom', 'center', 'top'} )
이 파라미터는 Matplotlib 3.3 이후 버전부터 적용

범례 표시
범례(Legend)는 그래프에 데이터의 종류를 표시하기 위한 텍스트
matplotlib.pyplot 모듈의 legend() 함수를 사용해서 그래프에 범례를 표시할 수 있음
그래프 영역에 범례를 나타내기 위해서는 우선 plot() 함수에 label 문자열을 지정하고, matplotlib.pyplot 모듈의 legend() 함수를 호출

범례 위치 지정
legend() 함수의 loc 파라미터를 이용해서 범례가 표시될 위치를 설정할 수 있음
loc 파라미터를 숫자 쌍 튜플로 지정하면, 해당하는 위치가 범례가 표시
loc = (0.0, 0.0)은 데이터 영역의 왼쪽 아래, loc=(1.0,1.0)은 데이터 영역의 오른쪽 위 위치
loc 파라미터에 여러 숫자 쌍을 입력하면서 범례 위치를 확인

범례 열 개수 지정
legend() 함수의 ncol 파라미터는 범례에 표시될 텍스트의 열의 개수를 지정
기본적으로 범례 텍스트는 1개의 열로 표시
ncol=2로 지정하면 아래 두번째 그림과 같이 표시

범례 테두리 꾸미기
frameon 파라미터는 범례 텍스트 상자의 테두리를 표시할지 여부를 지정
frameon=False로 지정하면 테두리가 표시되지 않음
shadow 파라미터를 사용해서 텍스트 상자에 그림자를 표시할 수 있음
축 범위 지정
matplotlib.pyplot 모듈의 xlim(), ylim(), axis() 함수를 사용하면 그래프의 X, Y축이 표시되는 범위를 지정
xlim() 함수에 xmin, xmax 값을 각각 입력하거나 리스트 또는 튜플의 형태로 입력
ylim() 함수에 ymin, ymax 값을 각각 입력하거나 리스트 또는 튜플의 형태로 입력
입력값이 없으면 데이터에 맞게 자동으로 범위를 지정
axis() 함수에 [xmin, xmax, ymin, ymax]의 형태로 x,y축의 범위를 지정
axis() 함수에 입력한 리스트 (또는 튜플)는 반드시 네 개의 값(xmin, xmax, ymin, ymax)이 있어야 함
입력값이 없으면 데이터에 맞게 자동으로 범위를 지정

선 종류 지정
Matplotlib에서 선의 종류를 지정하는 가장 간단한 방법은 포맷 문자열을 사용하는 것
plot() 함수의 linestyle 파라미터 값을 직접 지정할 수 있음
'-'(Solid), '--'(Dashed), ':'(Dotted), '-.'(Dash-dot)

선 끝 모양 지정
plot() 함수의 solid_capstyle, dash_capstyle를 사용해서 선의 끝모양을 지정할 수 있음
각각 'butt', 'round'로 지정하면 둥근 끝모양이 나타남
