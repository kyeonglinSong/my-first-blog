from django.db import models


class Post(models.Model):  # 포스트
    category = models.ForeignKey('blog.category', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.Charfield(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(defualt=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


class Comment(models.Model):  # 댓글
    post = models.ForeignKey('blog.post', related_name='comments', on_delete=models.CASCADE)
    author = models.models.ForeignKey('blog.user', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


class Good(models.Model):  # 좋아요
    post = models.ForeignKey(Post, related_name='good', on_delete=models.CASCADE())
    count = models.IntegerField(default=0)  #좋아요 눌린 횟


class Category(models.Model):  # 카테고리
    name = models.TextField(max_length=20)


class User(models.Model):  # 유저
    name = models.TextField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    joined_date = models.DateTimeField()
