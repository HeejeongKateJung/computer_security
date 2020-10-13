## Computer Security _ Assignment1

### 암호화 종류별로 대표적인 암호화 기법들을 종류별로 구현하였습니다.
- 언어: python3.8.0
- 라이브러리: pycrypto, hashlib

![image](https://user-images.githubusercontent.com/45758481/95831772-6eba4280-0d74-11eb-81e1-1f4550ab093a.png)

- 프로그램은 순서대로 Hash type 암호화(sha256), 대칭키 암호화(AES), 비대칭키 암호화(RSA)를 수행합니다.
- Hash type 의 경우에만 decoding 된 본래 문자열을 반환하지 않고, 나머지 경우에는 encrypted 문자열을 byte 형식으로, decrypted 문자열을 string 형식으로 출력합니다.
