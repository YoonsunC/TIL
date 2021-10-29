## ARP의 이해  
ARP(Address Resolution Protocol)  
: Local Network 상에서 IP 주소에 해당하는 호스트의 물리주소(Mac Address)를 찾는 프로토콜  
ARP 구조  
- Structure  
      H/W 타입          |   프로토콜 타입  
H/W 길이 | 프로토콜 길이 | OP CODESegment  
        출발지 MAC Address  
- Segment  
> 작동코드(OPER): 1 = APR Request, 2 = APR Reply, 3 = RARP request, 4 = RARP reply  
> 출발지 이더넷/IP 주소 : 송신측 MAC/IP 주소  
> 목적지 이더넷/IP 주소 : 수신측 MAC/IP 주소  

ARP 동작 원리  
- 통신 원리  
> 특정 IP에 해당하는 PC를 찾기 위하여 자신이 속해 있는 대역망에 찾고자 하는 IP가 어떤 MAC 주소를 가지고 있는지 요청  
> 요청 PC는 자신의 IP와 MAC주소를 포함하여 전체 대역으로 ARP request패킷을 송출  
> 찾는 IP 대상의 PC는 자신의 MAC 주소가 무엇인지 정보와 함께 요청한 PC로부터 ARP reply 패킷을 송출  
> 관련이 없는 패킷을 받은 PC는 해당 ARP reply 패킷을 버림  
> 찾고자 하는 IP에 대한 MAC주소를 얻었다면 자신의 PC 내부에서 IP와 MAC주소의 값을 ARP table에 매핑하여 캐시에 저장  
> ARP table은 특정 시간마다 갱신하며 주기적으로 ARP reply 패킷을 보내 지속적인 MAC주소 매핑을 진행  