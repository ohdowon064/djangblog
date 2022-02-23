from django.urls import path

from instagram import views

urlpatterns = [
    path('', views.post_list),
    path("archives/<int:year>/", views.archive_year)
]