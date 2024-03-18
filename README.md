# 공통

1. filepath 설정하기 #실행
   file_path = "C:/Users/TAK/Downloads/CSVData/CSVData/Language/" >> 원하는 파일이 있는 상위폴더로 지정 시 모든 하위 파일에 대해 작업을 수행합니다.

2. csv 파일 설정
   다른 이름 저장 > csv(etf-8)으로 속성 지정하여 저장.

3. from googletrans import Translator 오류
   pip를 통해 googletrans install.

4. 권한 오류
   작업 예정인 파일이 오픈되어있지는 않은지 확인.

5. googletrans 오류 시 버전 변경하여 재설치.

# firstPy

csv파일의 1행 데이터를 번역하여 새로운 행으로 추가하는 예제.

# secondPy

csv파일의 1열 데이터를 번역하여 새로운 열로 추가하는 예제.
reader 객체는 데이터를 추가할 때 기본적으로 1행씩 추가하기 때문에, 데이터 삽입 전
기존의 데이터를 모두 삭제한 후에 추가하였음.
