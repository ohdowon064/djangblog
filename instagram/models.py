from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    tag_set = models.ManyToManyField("Tag", blank=True)
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"({self.id}) {self.message}"

    class Meta:
        ordering = ["-id"]


class Comment(models.Model):
    post = models.ForeignKey("instagram.Post", on_delete=models.CASCADE, limit_choices_to={"is_public": True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # 태그를 여러 곳에서 활용하기 때문에 사용하는 곳에서 tag_set을 저장하는 것이 적합하다.

    def __str__(self):
        return self.name