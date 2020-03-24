from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
import jdatetime



def validate_file_extenstion(value):  # 7
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # 8
    valid_extenstion = ['.jpg', 'png.']  # 9
    if not ext.lower() in valid_extenstion:  # 10
        raise ValidationError('unsoport')  # 11


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 1
    avator = models.FileField(upload_to='images/user_avator/%Y/%m/%d', validators=[validate_file_extenstion])  # 2
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.user.username




class Article(models.Model):
    title = models.CharField(max_length=128)
    cover = models.FileField(upload_to='images/article/%Y/%m/%d', validators=[validate_file_extenstion])
    content = RichTextField()  # 4
    created_at = models.DateTimeField(default=jdatetime.datetime.now)  # 5
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  # 6
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)




class Category(models.Model):
    title = models.CharField(max_length=128)
    cover = models.FileField(upload_to='images/catalog/%Y/%m/%d', validators=[validate_file_extenstion])

    def __str__(self):
        return self.title
