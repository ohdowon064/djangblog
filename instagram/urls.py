from django.urls import path, re_path, register_converter

from instagram import views

class YearConverter:
    regex = r"20\d{2}"

    # view 함수 호출 전 인자를 정리한다.
    def to_python(self, value):
        return int(value)

    # url reverse할 때 url 문자열로 리버싱
    def to_url(self, value):
        return "%04d" % value

register_converter(YearConverter, "year")


urlpatterns = [
    path('', views.post_list),
    # <컨버터이름:인자>
    path("archive/<year:year>", views.archive_year)
]