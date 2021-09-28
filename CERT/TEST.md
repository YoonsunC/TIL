## SQL Injection  
SQL : 데이터베이스의 Data를 관리하기 위한 특수한 목적의 프로그래밍 언어  
SQL Injection  
- 웹 어플리케이션이 Database에 접근하는 과정에 일반적이지 않은 query를 공격자가 악의적으로 임의의 query 구문을 실행하는 기법  
- code 인젝션 기법 중 입력 값을 조작하여 데이터베이스에 접근, 공격할 수 있는 기법  
- 악의적인 SQL을 실행시키면서 데이터베이스를 조작할 수 있는 code 인젝션  

종류  
1) 논리적 에러를 이용하는 SQL Injection  
 : 논리적 에러를 발생시킬 수 있는 패턴을 이용한 인증 우회 기법  
 : ex) SELECT * FROM user WHERE user_id='$id' AND user_pw = '$pw'  
 : 다음과 같은 형태의 query로 Login을 처리한다고 할 때 보호기법이 없다면 논리적 에러를 이용하여 SQL Injection 시도 가능  
 : admin이라는 유저가 있다고 가정할 때, user_id=admin, user_pw=1'or'1'='1을 삽입  
 : SELECT * FROM user WHERE user_id='admin' and user_pw = '1' or '1' = '1' 이라는 구문을 완성해 TRUE로 만들어 table을 가져오는 방법  

2) Union SQL Injection  
 ref) Union : 두 개 이상의 쿼리를 요청해 결과를 얻는 SQL 연산자  
      -> union의 query 결과와 기존 query의 결과의 row 수가 같아야 함  
 : 두 개 이상의 쿼리를 사용한다는 점을 이용해 공격자가 원래의 요청에 한 개의 추가 쿼리를 삽입하여 정보를 획득하는 기법  
 : ex) SELECT * FROM user WHERE user_id='$id' AND user_pw = '$pw'  
 : admin이라는 유저가 있다고 생각하고 union을 사용한 sql injecton 시도 가능  
 : user_id=admin' union select * from user--를 삽입  
   -> SELECT * FROM user WHERE user_id='admin' union select * from user와 같은 쿼리가 완성  
   -> SQL의 주석기능을 이용해 뒷부분을 지워주는 것  

3) Blind SQL Injection  
 : 임의의 SQL 쿼리를 이용해 정보를 얻어내는 것은 일반적인 SQL Injection과 비슷하나 쿼리 결과에 따른 서버의 반응을 통해 공격하는 기법  
   -> 참, 거짓에 따라 서버의 반응이 달라야 사용 가능  
   -> SUBSTR함수나 ASCII함수, Limit을 이용하는 방법  

4) Stored Procedure SQL Injection  
 ref) Stored Procedure : DBMS에서 지원하는 저장 프로시져, 운영상 편의를 위해 만들어 놓은 SQL 집합형태, 입력된 파라미터는 문자열로 처리, SQL 구문보다 성능 좋음  
  : 취약한 프로시저를 이용해 쉘을 실행하거나 쿼리 결과를 얻어낼 수 있음  