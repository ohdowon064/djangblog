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
### static & media 파일
1. static 파일
   - 개발 리소스로서의 정적 파일(js, css, image 등)
   - 앱/프로젝트 단위로 저장/서빙
2. media 파일
   - FileField/ImageField를 통해 저장한 모든 파일
   - DB필드에는 저장경로를 저장, 파일은 파일스토리지에 저장
     -> 실제로는 문자열을 저장하는 필드
   - 프로젝트 단위로 저장/서빙
3. django.conf.settings를 사용해야한다.
   - django.conf.global_settings와 내 프로젝트 settings가 합쳐진다.
4. 파일이 많으면 노드가 많아서 파일을 찾는데 시간이 걸린다.
   - 하위 폴더가 많은 것은 상관없으므로 하위 폴더를 많이 두는 식으로 개발하는 것이 낫다.
   - upload_to 옵션을 사용할 수 있다.
   - 해당 옵션은 파일을 저장할 때 적용된다.
5. 동일파일일 경우 자동 더미문자로 덮어쓰기를 방지한다.
6. 새로운 파일을 업로드하면 기존 파일을 자동으로 삭제안함
   1) FileField에서 삭제하도록 설정
   2) 참조하지 않는 파일을 삭제하도록 배치프로그램 설정
7. file upload handler 
   - 관련 설정 settings.FILE_UPLOAD_MAX_MEMORY_SIZE
### QuerySet
1. queryset은 lazy하다.
   - 데이터가 필요한 시점에 query한다.
     - 쿼리셋을 만드는 동에는 db접근하지 않는다.
   - 슬라이싱을 하면 쿼리에 limit이 적용된다.
     - Post.objects.all().order_by("id")[:2] -> limit 2가 쿼리에 들어간다.
2. queryset은 lazy하므로 chaining이 가능하다.
3. 데이터가 필요한 시점은 언제인가?
   1. queryset
   2. print(queryset)
   3. list(queryset)
   4. for instance in queryset: print(instance)
### view
   1. request 인자
      - request.GET
      - request.POST
      - request.FILES