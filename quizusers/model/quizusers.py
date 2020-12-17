from django.db import models
from datetime import datetime

class Users(models.Model):
    user_name = models.CharField('User Name', max_length=200)
    user_email = models.EmailField('User Email',max_length=200)
    user_created_on = models.DateTimeField('User Created Time', default=datetime.now())