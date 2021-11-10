# 윈도우 운영체제 구조  
윈도우는 크게 유저모드와 커널모드로 구성되어 운영되며, 그 구조는 추상화의 개념으로 상위레벨과 하위레벨의 구조에 대한 영향을 받지 않고 서로의 상호작용 할 수 있도록 구성됨  
## 윈도우 아키텍처  
윈도우 NT 아키텍처  
- 두개의 메인 구성요소로 구성으로 설계  
- 리소스 자원의 낭비를 줄여 여러 부분으로 쪼개어 설계된 구조  
- 유저모드  
> 필수 서브시스템(Integral Subsystem)  
>> 보안, 워크스테이션 서비스, 서버 서비스로 구성  
>> 보안 : 계정권한관리, 인증관리 등  
>> 워크스테이션 서비스 : 컴퓨터가 네트워크로 접근을 제공  
>> 서버 서비스 : 컴퓨터가 네트워크 서비스를 제공  
> 환경 서브시스템  
>> OS/2, WIN32, POSIX 등의 환경에 맞는 어플리케이션을 운용할 수 있도록 지원  
- 커널모드  
> 하드웨어의 접근과 보호된 메모리 내에 실행되고 있는 코드와 컴퓨터의 시스템 자원 모두 접근하는 영역  
> 스케쥴링, 메모리 관리, 하드웨어와의 상호 작용 등의 역할 수행  
> 내부구조  
>> Executive  
>>> 모든 사용자 모드 하위 시스템과 상호작용  
>>> I/O Manager, the Security Reference Monitor, the Object Manager, the IPC Manager, the Virtual Memory Manager(VMM), a PnP Manager and Power Manager의 항목을 포함  
>>> I/O Manager : 유저모드 서브시스템과 상호작용하는 디바이스를 관리  
>>> the Security Reference Monitor(SRM) : 보안 필수 서브시스템의 보안 규칙을 시행하기 위한 주요 권한을 모니터링  
>>> IPC Manager : 서버와 클라이언트 사이의 상호작용관리를 담당  
>>> Virtual Memory Manager : 가상 메모리 관리  
>>> Process Manager : 프로세스 생성 및 삭제 등의 관리  
>>> PnP Manager : 장치 로드 시 Plug & Play 기능 관리  
>>> Power Manager : 전원과 관련 이벤트 관리 수행  
>>> Window Manager : 윈도우의 화면ㅇ르 그리는 역할 수행  
>>> GDI(Graphics Device Interface) : 폰트 랜더링과 팔레트, 곡선, 직선 등의 라인을 그리는 작업 수행  

>> (마이크로)커널  
>>> HAL과 Executive 사이에서 멀티프로세서 동기화, 충돌 관리, 예외 관리 등의 역할 수행  
>>> OS 부팅시 필요한 장치 드라이버를 초기화 하는 등의 역할 수행  

>> 커널 모드 드라이버  
>>> 하드웨어 장치와의 상호 작용을 수행할 수 있도록 중간자 역할  
>>> 최상위, 중간, 하위 레벨 드라이버로 구분되어 구성  

>> Hardware Abstraction Layer(HAL)  
>>> 물리적 하드웨어와 운영체제의 나머지 부분 사이에 위치  
>>> 하드웨어의 차이를 숨기고 커널이 실행되는 일관된 플랫폼을 제공  

# 윈도우 주요 프로세스  
프로세스를 이해하기 전 용어에 대한 의미를 먼저 파악한다.  
## 프로세스의 이해  
용어의 의미  
- 프로그램 : 하드디스크 등에 저장되어 있는 실행코드  
- 프로세스 : 연속적으로 실행되고 있는 컴퓨터 프로그램의 작은 단위  
- 스레드 : 프로세스에서 작업의 최소 단위  
- 세션  
: 윈도우 내에 어플리케이션이 동작하기 위해서는 실행하고 있는 세션이 필요  
: 윈도우의 세션은 일종의 사용자를 뜻하며 Session 0부터 시작  
: 윈도우 Vista 이전 버전에서는 처음 로그인한 사용자를 Session 0으로 정의  
: Vista 이후부터 Session0은 단지 시스템 프로세스와 서비스 실행에서만 동작하는 공간으로 정의하고 이후 로그인 사용자에게 각 세션 번호를 부여  

여러 프로세스들 중에서는 중요한 프로세스가 존재한다. 제시된 프로세스는 http://digitalforensics.sans.org의 사이트를 기준으로 작성되었으며 비정상적인 행위를 탐지하기 위해 중요한 프로세스들의 집합으로 구성되었다.  
## 윈도우 주요 프로세스  
프로세스 종류(Windows 7)  
- System : 대부분의 커널 모드 스레드를 담당  
- smss.exe  
: Session Manager Process 의미  
: 새로 생성되는 세션을 담당  
: csrss.exe 프로세스 시작  
: wininit.exe에서 생성되는 Session 0을 초기화  
: winlogon.exe에서 생성되는 Session 1 이상의 새 세션을 초기화  
- wininit.exe  
: Session 0에서 백그라운드로 실행  
: services.exe, lsass.exe, lsm.exe 실행  
- taskhost.exe  
: 윈도우 작업을 위한 프로세스  
: 모든 DLL 기반 서비스나 그룹서비스의 호스트를 제공  
- Isass.exe  
: 로컬 보안 인증 서브시스템 서버 프로세스  
: 유저의 인증을 위한 프로세스  
- csrss.exe  
: Client/Server Run-Time Subsystem으로 윈도우 서브시스템을 위한 유저모드의 프로세스  
: 프로세스와 스레드 등을 관리하는 등의 역할  
- services.exe : 서비스와 작업 스케줄을 관리하는 프로세스  
- svchost.exe  
: 윈도우 서비스의 호스트 프로세스  
: DLL을 이용한 서비스가 실행하도록 제공  
: 여러개의 프로세스를 생성할 수 있음  
- lsm.exe  
: Local Session Manager  
: 터미널 서비스, 원격 데스크탑 등의 세션들이 효율적으로 스위칭 될 수 있는 역할 수행  
: smss.exe와 같이 새로 세션이 이루어질 때 실행  
- winlogon.exe : 사용자 계정의 로그온과 로그오프 상태를 관리하는 프로세스  
- explorer.exe : 사용자가 파일을 접근하도록 기능을 제공하는 프로세스  
- iexplorer.exe : explorer 프로세스로부터 실행된 프로세스  

프로세스 종류(Windows 10)  
- 윈도우 7과 유사하나 추가적으로 주요한 프로세스가 존재  
- RuntimeBroker.exe  
: 제한된 UWP(Universal Windows Platform)앱과 전체 Windows API간의 프록시 역할을 수행  
: UWP - Windows 10, Windows 10 모바일, 엑스박스원 등에서 실행할 유니버설 앱의 개발을 돕기 위한 것  
- taskhostw.exe : 윈도우7에서의 taskhost.exe와 역할이 동일하며 파일 이름만 다름  
- lsaiso.exe  
: lsass.exe가 기능을 대부분 수행하나 계정 자격 증명을 안전하게 저장하는 중요한 역할을 할 때 사용되는 프로세스  
: 하드웨어 가상화 기술을 통해 다른 프로세스와 분리된 컨텍스트에서 실행하여 안정성을 보장  
: 원격 인증을 요구할 경우, RPC 채널을 사용하여 요청을 프록시 수행  

# 윈도우 주요 서비스  
윈도우에는 구동을 위한 서비스가 존재한다. 사용자가 간섭하지 않으며 신체의 장기와 같이 운영체제가 잘 구동될 수 있도록 도와주는 역할을 수행한다.  
## 윈도우 서비스 개요  
서비스란?  
- 오랜 시간 실행되며 특정한 기능을 수행하는 실행파일  
- 사용자의 간섭이 없음  
- 보통의 경우 윈도우 운영체제가 시동될 때 실행  
- 유닉스 또는 리눅스의 데몬과 개념이 유사  
서비스 실행계정  
- Local System  
- Local Service  
- Network Service  

## 윈도우 주요 서비스  
서비스 확인방법  
1. 제어판 -> 관리도구 -> 서비스 실행 또는 <Ctrl+Alt+Del> 실행중인 서비스 확인  
2. 윈도우키+R -> services.msc 입력 후 엔터  
3. CMD에서 net start 입력 / 특정 서비스 확인 방법 : net start | find /i "서비스명"  

주요 서비스  
- Logical Logging Manager  
: MS-SQL 서버와 마이크로소프트 메일 서버, IIS, 터미널 서비스, 파일 및 인쇄 서비스 등의 서버 제품에 대한 클라이언트의 접근 라이센스 사용을 추적  
- Network Connections  
: 시스템에 관련된 모든 네트워크에 대한 서비스를 제공하며, 이에 대한 상태를 표시하며, 서비스 중지시 네트워크에 대한 모든 접속이 불가능  
- NTLM(NT LAN Manager) Security Support Provider  
: LTLM을 이용한 인증 서비스를 제공, 윈도우 2000의 경우에는 NTLM2를 이용하나, 다른 운영체제와의 호환을 위해 필요  
- Plug and Play(PNP)  
: PNP는 하드웨어에 대한 자동 인식과 설정을 도와주는 서비스, 최근의 윈도우 시스템에서는 PNP 서비스를 중지시킬 경우 운영체제 자체가 불안정해짐  
- Server  
: RPC(Remote Procedure Call) 지원 및 파일, 인쇄 등을 위한 자원 공유를 제공  
- Workstation  
: 네트워크 연결 및 통신을 제공, 클라이언트 측의 네트워크 구성에 영향을 미치는 서비스  
- Removable Storage  
: 이동식 미디어 드라이브에 대한 연결을 제공  
- Security Accounts Manager(SAM)  
: 계정 인증에 관련된 서비스  
- WMI(Windows MAnagement Instrumentation)  
: 시스템의 관리 정보를 제공하는 서비스, WMI는 응용 프로그램과 서비스가 생성하는 관리 이벤트를 포함하여 응용 프로그램 서비스에 접근 정보를 제공  
- Windows Management Instrumentation Driver Extensions  
: WMI 정보를 등록한 모든 드라이버를 추적하여 알림  
: 서비스 중지 시 클라이언트가 드라이버의 WMI 정보에 접근 못함  
- Application Management  
: 응용 프로그램의 설치, 제거와 같은 서비스 제공  
: 서비스를 중지 시 프로그램을 추가하거나 제거할 수 없음  
- Remote Procedure Call(RPC)  
: RPC(원격제어를 위한 프로세스 통신)에 관련된 서비스를 제공  

## 윈도우 주요 서비스(선택)  
- ClipBook  
: 흔히 사용하는 편집 기술인 Copy&Paste를 지원하기 위한 서비스  
- COM+ (an extension to the Component Object Model)Event System  
: Com(Component Object Model)은 프로그램의 컴포넌트 객체들을 개발하고 지원하기 위한 하부기관 구조로, 인터페이스 교섭과 언제쯤 객체가 시스템에서 제거될 수 있는지를 판단  
: 라이선스, 이벤트 서비스 등을 제공  
- Computer Browser  
: 네트워크에 있는 컴퓨터의 최신 목록을 유지하고, 요청하는 프로그램에게 목록을 제공  
- Distributed Link Tracking(DLT) Client  
: 네트워크 도메인의 여러 컴퓨터에 걸쳐있거나 하나의 컴퓨터에 있는 NTFS 파일 시스템 사이의 링크를 유지 및 관리, 대상 파일의 이름이 바뀌거나 이동된 후에도 바로가기와 OLE(Object Linking and Embedding)링크가 계속 작동  
- Distributed Link Tracking(DLT) Server  
: 볼륨간에 이동한 파일을 추적할 수 있도록 도메인 내의 각 볼륨에 대한 정보를 저장  
: 도메인 내의 각 도메인 컨트롤러에서 실행  
: 서비스 중지시 DLT 클라이언트 서비스가 유지 및 관리하는 링크의 안정성이 시간이 지날수록 낮아짐  
- Distributed Transaction Coordinator  
: 데이터베이스, 메시지 대기열, 파일 시스템, 트랜잭션 보호 리소스 관리자 등 여러 리소스 관리자와 여러 컴퓨터 시스템간의 분산된 트랜잭션을 조정  
- File Replication  
: 자동 파일 복제 서비스, 여러 서버에 존재하는 파일을 복사 및 관리하여 동기화  
- Internet Authentication Service(IAS)  
: VPN(Virtual Private Network)장비, RAS(Remote Access Server) 장비 또는 무선 LAN, WAN 네트워크에 접속하는 사용자의 인증, 권한부여, 감사 및 계정작업을 수행  
- Intersite Messaging(ISM)  
: 윈도우 서버간에 메시지를 주고받을 수 있음  
- Logical Disk Manager  
: 이동식 하드디스크 등을 이용하면 PNP 이벤트가 발생하는데, 이를 관찰하고 Logical Disk Manager Administrative Service에 볼륨 및 디스크 정보를 전달  
- Logical Disk Manager Administrative Service  
: 이 서비스는 드라이브나 파티션을 구성하거나 새로운 드라이버가 검색된 경우에만 시작  
: 동적 디스크 구성이 변경될 때마다 또는 MMC(Microsoft Management Console) 스냅인이 실행될 때 활성화, MMC는 시작버튼의 실행창에서 mmc를 입력하면 실행되며, 시스템 관리용 응용프로그램을 중앙에서 제어할 수 있도록 해주는 프로그램  
- Message Queuing(MSMQ)  
: 윈도우용 분산 메시지 응용 프로그램을 만들기 위한 메시징 인프라 및 개발 툴  
- Remote Procedure Call(RPC) Locator  
: RPC 클라이언트에 대한 이름 서비스를 제공  
- Simple TCP/IP Services  
: TCP/IP 계층에서 사용되는 간단한 프로토콜의 묶음에 대한 지원  
- TCP/IP NetBIOS Helper  
: NetBIOS를 이용해 이름을 확인할 수 있도록 하는 서비스  
- Trivial FTP Daemon  
: TFTP(Trivial File Transfer Protocol) 프로토콜을 지원하는 서비스로 원격 설치시 이용  

# 윈도우 레지스트리의 이해  
레지스트리는 윈도우 운영체제 내에 여러 설정값들을 담은 일종의 데이터베이스이다. 리눅스에서 각 설정값을 파일로 담고있는것과는 다르게 차이점을 가지고 있다.  
## 레지스트리 개요  
레지스트리란?  
- 32/64bit 아키텍처에서 윈도우 운영체제의 설정과 선택항목을 담고있는 데이터베이스  
- 하드웨어, 소프트웨어, 사용자 PC 선호도, 중요 시스템 정보 등에 대한 설정이 포함  
- 이전에는 윈도우 프로그램 내부에 ini 파일이 사용(ini 등의 설정파일이 포함되어 레지스트리에 영향이되지않고 설치되는 프로그램들을 포터블형식의 설치파일이라 함)  
구성  
- 키  
: 윈도우의 폴더와 유사한 형태  
: 레지스트리 안에 경로와 같은 개념으로 사용  
- 값  
: 키 안에 담겨있는 이름 또는 자료  
: 여러 키로부터 참조될 수 있음  
- 구성  
: 레지스트리 편집기 실행 : 윈도우키+R -> regedit 입력후 엔터  
: 레지스트리 편집기에서 아래 그림과 같이 확인가능  
: 좌측에는 키로 이루어진 특정경로를 의미하며, 우측에는 값을 의미하는 실제 데이터값이 출력  

레지스트리는 크게 5가지로 구분되어 각 데이터가 분류된다.  
## 윈도우 레지스트리의 이해  
주요 레지스트리 구조  
- 윈도우 내 레지스트리는 주요 키를 크게 5가지로 분류  
: HKEY_CLASSES_ROOT - 등록된 응용프로그램의 정보를 보관  
: HKEY_CURRENT_USER - 현재 로그인한 사용자의 설정값 보관  
: HKEY_LOCAL_MACHINE - 컴퓨터의 모든 사용자의 설정값 보관  
: HKEY_USERS - 컴퓨터에서 사용중인 각 사용자의 프로파일에 대한 설정값을 보관  
: HKEY_CURRENT_CONFIG - 실행시간에 수집한 자료를 보관  

레지스트리의 값은 숫자별로 각 정의가 구분되어있다.  

## 윈도우 레지스트리 명령어  
REG 명령어  
- REG QUERY   
: 지정한 레지스트리 키나 그 하위 트리의 값을 표시  
- REG ADD  
: 레지스트리에 키나 값 이름 또는 값을 추가하거나 기존의 값을 수정  
- REG DELETE  
: 레지스트리에서 지정한 키나 값을 삭제  
- REG COPY  
: 레지스트리의 트리를 복사  
- REG SAVE  
: 레지스트리 트리의 저장  
: 지정한 하위 키 이하의 트리를 지정된 파일에 저장  
- REG RESTORE  
: REG SAVE로 저장한 레지스트리를 로컬 컴퓨터의 지정한 트리에 복원  
- REG LOAD  
: REG SAVE로 저장한 레지스트리를 원래와는 다른 장소에 로드/복원  
- REG UNLOAD  
: REG LOAD로 읽어들인 레지스트리의 섹션을 삭제  
- REG COMPARE  
: 지정한 2곳의 레지스트리 트리를 비교해서 그 차이점 혹은 같은 부분을 표시  
- REG EXPORT  
: 지정한 키나 항목(과 그 값)을 파일에 씀  
- REG IMPORT  
: REG EXPORT로 쓴 레지스트리 값을 로컬 컴퓨터에 다시 불러옴  
- REG FLAGS  
: 윈도우 비스타 이후부터 적용된 레지스트리 가상화 플래그를 설정  

윈도우의 계정관리는 크게 계정과 그룹의 형태로 서로 권한과 역할을 구분하여 사용한다. 또한 계쩡과 그룹은 각 고유한 속성을 가지고 있으며 그 값에 따라 관리할 수 있다.  
## 윈도우 계정의 이해  
윈도우 계정 분류  
- 계정과 그룹  
: 계정(User)와 그룹(Group)으로 구성되며 역할에 권한을 제어  
: 계정명과 그룹명은 고유하며 중복되지 않음  
: 각 계정명은 여러 그룹에 종속될 수 있음  
: 고유한 계정명 외에 식별할 수 있는 SID(Security ID) 존재  
: 계정 속성 값  
> Name : 도메인 속성이 지정하는 도메인의 윈도우 사용자 계정  
> PasswordChangeable : 사용자가 암호변경 가능여부  
> Password Expires : 패스워드 계정 만료여부  
> PasswordRequired 패스워드가 반드시 지정되어야 하는지 여부  
> SID : 계정 고유 ID  
> SIDType : SID의 유형  
> Caption : 계정의 도메인과 계정이름  
> Description : 계정 설명  
> Disabled : 계정 활성화 여부  
> Domain : 윈도우 도메인 이름  
> FullName : 로컬 계정의 전체이름  
> InstallDate : 계정이 설치된 일자  
> LocalAccount : 로컬 컴퓨터 계정 여부 확인  
> Lockout : 윈도우 시스템의 잠김 설정 여부 확인  
> Name : 도메인 속성이 지정하는 도메인의 윈도우 사용자 계정  
> Status : 객체의 현재상태  

윈도우의 계정은 크게 3개의 계정으로 분류되며, 각 계정의 단계에 따라 역할이 각각 다르게 수행된다.  
윈도우 계쩡은 세가지 분류로 분리  
- Local System, Network Service, Local Service  
: 시스템에 중요 자원이나 관리를 위한 계정  
: 서비스, 시스템에 중요 프로세스를 실행하는 주체  
- Administrator  
: 운영체제의 응용프로그램 레벨에서의 관리자  
: 프로그램 설치 등을 수행할 때 주로 권한을 필요로하는 계정  
- User or Guest  
: 최소한의 권한을 가진 일반 사용자 또는 게스트 계정  
: 윈도우 중요파일이나 프로그램에서의 중요 폴더 접근이 제한된 계정  

## 윈도우 운영체제 부팅 순서  
POST(Power On Self Test) - ROM BIOS - 부트로드 실행 - NTLDR - NTDETECT.COM - ntoskrnl.exe  

POST와 ROM BIOS 과정은 대부분 초기 디바이스에 대한 상태여부를 확인하는 목적을 가진다. 이후 부트로드를 통해 운영체제의 필요한 설정을 로드한다.
POST  
- 순서  
: 변환된 전기적 흐름은 CPU로 전달  
: CPU가 가지고 있는 이전의 값들을 지우고 CPU 레지스터인 Program Counter(PC)를 초기화  
: ROM BIOS의 부트 프로그램 주소를 가리킴  
ROM BIOS  
- 순서  
: System Bus로 특정 시그널 전송  
: RTC(Real-Time Clock)테스트  
: 비디오 구성요소(비디오 메모리)테스트 : 이후 부팅과정에서 정의된 출력 확인 가능  
: RAM, 키보드, 드라이브 테스트  
: CMOS(RTC/NVRAM) 데이터와 비교  
: Plug and Play를 실행하여 운영체제를 위한 기본적인 구성을 RAM에 로드  
: 부팅의 첫번째 섹터인 MBR이 위치한 내용을 로드  
부트로드(MBR) 실행  
- 순서  
: MBR을 알려주는 시그니처 값을 할당  
: 부팅 가능한 파티션을 탐색
: NTLDR의 위치 정보를 로드  
- 특징  
: C드라이브에 운영체제를 설치한 경우 MBR이 삭제되더라도 무관  
NTLDR  
NTLDR은 NT계열의 시동로더로 FAT, NTFS 파일시스템에서 동작하는 로더이다. 이 로더를 통해 운영체제에 중요한 설정값을 로드한다.  
- 의미와 특징  
: NT Loader의 준말. 윈도우 NT계열 운영체제를 위한 시동 로더  
: FAT 또는 NT파일 시스템 NTFS에서 동작  
- 순서  
: 시동 드라이브의 파일 시스템에 접근  
: 최대 절전모드로 종료시 hiberfill.sys에서 확인하여 메모리로 로드  
: 발견하지 않은 경우 boot.ini를 읽어내어 시동메뉴를 사용자에게 출력  
: NT 기반의 운영체제 선택시 NTDETECT.COM을 실행하여 사용자 컴퓨터의 하드웨어 정보 획득  
: NT 기반의 운영체제가 아닌경우 boot.ini안에 나열된 연결 파일을 불러 제어권을 제공  
NTDETECT.COM단계는 하드웨어 설정파일에따라 구성되며 이후 ntoskrnl.exe 프로세스를 실행시켜 커널,메모리,시스템 프로세스 등 관리한다.  
NTDETECT.COM  
- 특징  
: 하드웨어 감지는 하드웨어의 ACPI 지원 여부에 따라 조금 다르게 동작  
: 어느 하드웨어 프로파일을 사용할지 결정하는 역할 수행  
- 순서  
: 하드웨어와 관련 구성 파일을 찾아 실행  
: ntoskrnl.exe 로드  
ntoskrnl.exe  
- 의미와 특징  
: NT Operating system kernel 준말로 커널 이미지로 알려져있음  
: 하드웨어 가상화, 프로세스, 메모리, 시스템 서비스관리 등의 역할을 수행  
: 캐시 매니저, 익스큐티브, 커널, 보안참조모니터, 메모리관리, 스케줄이 구성  

## 윈도우운영체제 부팅순서  
ntoskrnl.exe  
- 순서  
: 커널로드  
> HKEY_LOCAL_MACHINE/System/CurrentControlSet/Service에 시스템 설정 로드  
: 커널 초기화 - 드라이버에 대한 현재 제어세트를 검사하고 작업시작  
: 서비스 로드 : Service MAnager(smss.exe)와 Win32 서브시스템 로드  
: 로그인서비스 초기화 - winlogon.exe 시작을 통해 로그인창 비활성화 / 로그인 시도 후 로컬보안인증서버로 전송 / 보안계정관리자(SAM, Security Accounts Manager)에 정보비교 / userinit.exe 프로세스 실행  
- 쉘실행  
: 레지스트리에 구성된 쉘을 실행(기본값 : explorer.exe)  
: userinit.exe 프로세스에서 아래의 레지스트리 내용을 받아 실행  