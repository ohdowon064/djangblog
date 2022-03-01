from django.urls import path, re_path

from instagram import views

urlpatterns = [
    path('', views.post_list),
    # http://pythonstudy.xyz/python/article/401-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-Regex
    re_path(r"archives/(?P<year>\d{4})/", views.archive_year)
]