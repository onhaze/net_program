
#### 1. 문자열 슬라이싱과 함수 사용
**문제**: 문자열 `'Hello, IoT'`를 변수 `str`에 저장하고, 슬라이싱과 함수를 사용해 문자수 출력, 5번 반복, 처음 3문자, 마지막 3문자, 대문자 변환을 수행. 반복문 사용 불가.

**설명**:
- `len(str)`: 문자열 길이 9 출력.
- `str * 5`: 문자열 5번 반복.
- `str[:3]`: 처음 3문자 `'Hel'`.
- `str[-3:]`: 마지막 3문자 `'IoT'`.
- `str.upper()`: 대문자 변환 `'HELLO, IOT'`.
- 반복문 없이 슬라이싱과 문자열 메소드만 사용.

---

#### 2. 리스트 슬라이싱과 함수 사용
**문제**: 리스트 `['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']`를 변수 `lst`에 저장하고, 슬라이싱과 함수를 사용해 '!' 추가, 다섯 번째 요소 제거, 인덱스 4에 'a' 삽입, 문자열 변환, 오름차순 정렬 수행. 반복문 사용 불가.

**설명**:
- `append('!')`: 리스트 끝에 '!' 추가.
- `pop(4)`: 인덱스 4(다섯 번째, 'o') 제거.
- `insert(4, 'a')`: 인덱스 4에 'a' 삽입.
- `join()`: 리스트를 문자열 `'Hell,a IoT!'`로 변환.
- `sorted()`: 오름차순 정렬 `[' ', '!', ',', 'I', 'T', 'a', 'e', 'h', 'l', 'l']`.
- 반복문 없이 리스트 메소드와 함수 사용.

---

#### 3. URL 파싱 (딕셔너리 생성)
**문제**: 문자열 `'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'`를 사용해 `split` 함수로 쿼리 파라미터를 딕셔너리 `{'where':'nexearch', 'ie':'utf8', 'query':'iot'}`로 변환. URL 파싱 라이브러리 사용 불가.

**설명**:
- `split('?')`: URL을 쿼리 문자열로 분리.
- `split('&')`: 쿼리 파라미터를 개별 항목으로 분리.
- 각 파라미터를 `split('=')`로 키-값 쌍으로 나눠 딕셔너리에 저장.
- 결과 딕셔너리 출력.
- 반복문 사용(제약 없음), 라이브러리 사용 없이 `split`만 활용.

---

#### 4. 복소수 클래스 구현
**문제**: `MyComplex` 클래스를 정의해 두 복소수 `a=3-4i`, `b=-5+2i`를 저장하고, 곱셈 연산 `(a + bi) x (c + di) = ac – bd + (ad + bc)i`를 클래스 메소드로 구현해 결과 `-7+26i` 출력. 내장 복소수 클래스 사용 불가.

**설명**:
- 클래스 멤버 변수: `real_1`, `imaginary_1` (첫 번째 복소수), `real_2`, `imaginary_2` (두 번째 복소수).
- `multiply` 메소드: 복소수 곱셈 공식 적용.
- 실수부: `real_1 * real_2 - imaginary_1 * imaginary_2 = 3 * (-5) - (-4) * 2 = -15 + 8 = -7`.
- 허수부: `real_1 * imaginary_2 + imaginary_1 * real_2 = 3 * 2 + (-4) * (-5) = 6 + 20 = 26`.
- 결과: `-7+26i` 출력.

---

#### 5. TCP 메시지 송수신 프로그램
**문제**: 강의자료 “소켓 프로그래밍 (UDP)” 슬라이드 11, 12, 13의 “과제 8: UDP message 송수신 프로그램”을 TCP로 구현. 서버는 "quit" 수신 후 연결 종료 없이 다음 클라이언트 연결 대기. 서버와 클라이언트 코드 제출.

**설명**:
- **서버**: TCP 소켓(`SOCK_STREAM`)으로 포트 12345 바인딩, 클라이언트 연결 수락. `mailboxes` 딕셔너리로 메시지 저장. "send mboxId message"로 메시지 저장, "receive mboxId"로 메시지 반환. "quit" 시 클라이언트 연결 종료, 서버는 계속 실행.
- **클라이언트**: 서버에 TCP 연결 후 "send" 또는 "receive" 메시지 전송, 서버 응답 출력. "quit" 입력 시 연결 종료.
- 출력: 클라이언트는 "OK", "No messages", 메시지 등 출력. 서버는 연결/종료 로그.
- 두 TCP 연결(클라이언트별, `mailboxes` 공유) 유지.

---

#### 6. UDP 에코 서버/클라이언트 (손실 복구)
**문제**: 강의자료 “소켓 프로그래밍 (UDP)” 슬라이드 3, 4의 “UDP 에코 서버/클라이언트 프로그램”에 손실 복구 추가. 클라이언트→서버 메시지 40% 확률 손실, 60% 확률로 ‘ack’ 전송. 클라이언트는 ‘ack’ 미수신 시 1초 간격 최대 3회 재전송(총 4회).

**설명**:
- **클라이언트**: 메시지 입력 후 `reTx`와 함께 전송. ‘ack’ 미수신 시 1초 타임아웃 후 최대 3회 재전송. 성공 시 서버 에코 메시지 출력, 실패 시 종료.
- **서버**: 수신 메시지 출력, 40% 확률로 무응답, 60% 확률로 ‘ack’과 에코 메시지 전송.
- 출력: 클라이언트는 `-> msg` 입력, `<- reTx msg` 출력. 서버는 `<- reTx msg` 로그.
- 제공된 코드 수정: 클라이언트 재전송 5→3회, 타임아웃 2→1초. 서버 손실 50→40%, 불필요한 재전송 로직 제거.

---

#### 7. HTTP 릴레이 서버
**문제**: TCP 소켓으로 HTTP 릴레이 서버 구현. 브라우저에서 `http://localhost:9000` 요청 시, 릴레이 서버는 www.daum.net으로 요청 라인과 `Host: www.daum.net` 전송, 응답을 브라우저로 전달. `socket` 모듈만 사용, 두 TCP 연결 유지.

**설명**:
- 서버는 포트 9000에서 브라우저 요청 수신, 요청 라인(예: `GET / HTTP/1.1`)과 `Host` 헤더 추출.
- www.daum.net(포트 80)에 TCP 연결로 요청 전송, 응답 수신.
- 응답을 브라우저로 전달, 브라우저는 www.daum.net 웹페이지 표시.
- 출력: 서버는 연결 로그 출력. 브라우저는 Daum 홈페이지 렌더링.
- 두 TCP 연결: 브라우저↔서버, 서버↔외부 서버.

---

#### 8. UDP 에코 서버/클라이언트 (손실 복구 수정)
**문제**: 강의자료 “소켓 프로그래밍 (UDP)” 슬라이드 3, 4의 “UDP 에코 서버/클라이언트 프로그램”에 손실 복구 추가. 클라이언트→서버 메시지 40% 손실, 60% ‘ack’ 전송. 클라이언트는 ‘ack’ 미수신 시 1초 간격 최대 3회 재전송.

**설명**:
- **클라이언트**: 메시지 입력, `reTx` 포함 전송. ‘ack’ 미수신 시 1초 타임아웃 후 최대 3회 재전송. 성공 시 에코 출력, 실패 시 종료.
- **서버**: 메시지 수신 후 출력, 40% 확률 무응답, 60% 확률로 ‘ack’과 에코 전송.
- 출력: 클라이언트는 `-> msg`, `<- reTx msg`. 서버는 `<- reTx msg` 로그.
- 제공된 코드 수정: 클라이언트 재전송 5→3회, 타임아웃 2→1초. 서버 손실 50→40%, 불필요한 입력/재전송 제거.

--- 

**참고**:
- 각 문제는 제약 조건(반복문 사용 여부, 라이브러리 제한 등)을 준수.
- 출력 결과는 문제에 명시된 대로(예: `-7+26i`, 브라우저 웹페이지 표시) 또는 제공된 코드의 동작 기반.
- 추가 정보나 특정 출력 형식이 필요하면 요청 주시면 보완하겠습니다.