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
### django admin
1. django admin: 장고에서 제공하는 기본 앱
   - django.contrib.admin에 있다.
   - 서비스 초기에 관리도구로 좋다. -> 엔드유저 서비스에 집중가능
   ex) path('admin/', admin.site.urls) -> admin/ URL을 django admin앱에서 처리하겠다.
2. admin 주소로 변경하지 않으면 '/admin/'으로 설정된다.
   - django-admin-honeypot으로 가짜 어드민 사이트 설정가능
3. 생성한 앱을 admin.py에 등록해서 관리페이지에서 관제할 수 있다.
   1) admin.site.register(모델)
   2) class 모델Admin(admin.ModelAdmin), admin.site.register(모델, 모델Admin)
   3) @admin.register(모델) 장식자 사용
4. list_display: 모델 리스트에 출력할 형태 지정
5. list_display에서 함수를 지정한 경우에는 인자없는 함수만 가능
6. search_fields: admin내 검색 ui를 통해 db를 통한 where 쿼리 대상 필드 리스트
7. list_filter: 지정 필터링 옵션