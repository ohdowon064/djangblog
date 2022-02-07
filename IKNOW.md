1. startproject 후 migrate해야 필수 테이블들이 생성된다.
2. model 필드 자주 쓰는 공통 옵션
   - blank: 장고 단에서 validation 시 empty 허용 여부 (default False)
   - null(DB 옵션): DB 단에서 null 허용 여부 (default False)
   - db_index(DB 옵션): 인덱스 필드 여부 (default False)
   - default: 디폴트 값 지정, 또는 값을 리턴할 함수 지정
   - unique(DB 옵션): 현재 테이블에서 유일성 여부 (default False)
   - choices: select 박스 소스로 사용
   - validators: validators를 수행할 함수를 다수 지정
     - 모델 필드에 따라 고유한 validators들이 등록, ex) 이메일만 받기
   - verbose_name: 필드 레이블, 미지정시 필드명이 사용된다.
   - help_text: 필드 입력 도움말
3. models.ImageField는 pillow 설치가 필요