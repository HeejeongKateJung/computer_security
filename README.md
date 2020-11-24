Assignment1: Implementation of Encryption Algorithm
=====

### 대표적인 암호화 기법들을 종류별로 구현하였습니다.
- 언어: python3.8.0
- 라이브러리: pycrypto, hashlib

![image](https://user-images.githubusercontent.com/45758481/95831772-6eba4280-0d74-11eb-81e1-1f4550ab093a.png)

- 프로그램은 순서대로 Hash type 암호화(sha256), 대칭키 암호화(AES), 비대칭키 암호화(RSA)를 수행합니다.
- Hash type 의 경우에만 decoding 된 본래 문자열을 반환하지 않고, 나머지 경우에는 암호화 된 문자열을 byte 형식으로, 복호화 된 문자열을 string 형식으로 출력합니다.




Assignment2: Implementation of Ransomware Detection Algorithm
=====
-----

### 1.	참고이론
  #### A. N-gram 기법
  n-gram 언어 모델은 ‘일부’ 단어들이 얼마나 자주 등장하느냐에 따라 문서들을 분류하는 기법입니다. 이때  몇 개의 단어들이 연속으로 등장할지 결정하는 변수가 n 이며, 이 프로젝트에서는 4-gram 기법을 사용하였습니다.
  #### B.	TF-IDF 기법
TF-IDF (Term Frequency-Inverse Document Frequency) 는 단어의 빈도와 역 문서 빈도를 사용하여 코퍼스 내의 각 단어들의 중요성을 가중치로 줄 수 있는 기준을 정의합니다. 이 프로젝트에서는 TF 만 사용하였습니다.
 


-----
### 2. 개발 환경 및 사용 라이브러리
* 개발 언아: Python3.8.0
* 라이브러리: Pandas, Numpy, os


-----
### 3. 실행 결과
![image](https://user-images.githubusercontent.com/45758481/100049864-9e706600-2e5b-11eb-8be5-2af13b4c4b49.png)

-	악성코드 샘플 파일로부터 40개의 악성코드 특징 서열을 추출합니다.
-	악성코드 특징 서열을 포함하고 있는 파일은 악성코드로 분류됩니다.
-	악성코드 샘플 파일 중 약 79%의 파일이 악성코드 파일로 분류되었습니다.
-	정상 샘플 파일 중 약 52%의 파일이 악성코드 파일로 분류되었습니다.



-----
### 4. 실행 방법

##### 악성코드 API 샘플 파일과 일반 샘플 API 파일이 포함 된 경로를 입력합니다.
##### ‘0’ 폴더에는 187 개의 일반 샘플 파일, ‘1’ 폴더에는 176개의 악성코드 샘플 파일이 포함되어 있습니다. 
##### Term_frequency_0.csv: column은 정상 샘플 파일들로부터 추출한 4gram api sequence, row는 각 샘플 파일별로 4gram api sequence 의 등장 빈도 카운트가 row 로 구성되어 있습니다.
##### Term_frequency_1.csv: 악성코드 샘플 파일로부터 추출한 csv 파일 입니다.
##### ***4gram api sequence: 예를 들어, file1이 [A, B, C, D, E, F, G, H] 로 구성되어 있다면, 4gram api sequence 는 [ABCD, BCDE, CDEF, DEFG, EFGH] 입니다. 





