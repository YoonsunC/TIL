## NAT(Network Address Translation)  
: 사설 네트워크에 속한 여러개의 호스트가 하나의 공인 IP 주소로 인터넷에 접속할 때 많이 활용되는 기술로 IP 주소등을 재기록하여 네트워크 장비를 통해 트래픽을 주고 받는 기술  

컴퓨터 네트워킹에서 쓰이는 용어로 IP패킷의 TCP/UDP 포트 숫자와 소스 및 목적지의 IP 주소 등을 재기록하여 네트워크 장비를 통해 트래픽을 주고 받는 기술  
사설 네트워크에 속한 여러개의 호스트가 하나의 공인 IP주소로 인터넷에 접속할 때 많이 활용  

NAT의 분류  
- Cone NAT  
> 내부의 IP와 포트에 대해 도착지에 관계없이 동일한 외부의 IP와 포트로 매핑
> Full Cone  
>> 요청시 원격주소/포트와 응답시 원격주소/포트가 모두 다르더라도 NAT Client로 연결
> Restricted Cone  
>> 요청시 원격주소와 응답시 주소가 같은 경우에만 NAT Client로 연결  
> Port Restricted Cone  
>> 요청시 원격주소와 응답시 원격주소/포트가 다르면 연결하지 않음  
- Symmetric NAT  
> 요청시 원격주소와 응답시 원격주소/포트가 다르면 연결하지 않음  
> 단, 서버의 주소/포트가 다르면 Client의 주소 포트 되는 포트를 새로 할당하여 사용  

NAT 통신과정의 예  
www.naver.com URL의 IP주소가 무엇인지 질의 - URL의 IP주소를 묻는 DNS Request 패킷 생성(목적지는 DNS서버로 질의 목적 패킷 생성) - 게이트웨이인 공유기로 Request 패킷 전달 - 패킷을 전달받은 공유기는 자신의 외부 IP를 Source IP로 변경하여 패킷을 재생성 - 전달받은 Request 패킷에 대해 DNS 서버가 가지고 있는 NAver의 IP 주소의 데이터가 담겨 있는 Response패킷을 생성하여 전달 - Response 패킷을 전달받은 공유기는 내부IP로 패킷을 재생성하여 요청한 PC에 전달 - Naver의 주소로 웹페이지를 요청하는 Request패킷을 생성하여 DNS 질의와 동일하게 전달 - 전달받은 Request패킷을 받아 외부 IP주소로 Response패킷을 생성하여 전달 - 이후 이전과 동일하게 내부 IP하는 P로 전달

