from django.db import models
from django.utils import timezone
import datetime
import os
import uuid

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    req_token = models.CharField(max_length=200)
    log = models.CharField(max_length=5) 

    def profile(self):
        return Profile.objects.filter(user = self.id)
    
class Profile(models.Model):
    user = models.ForeignKey(User)
    dis_name = models.CharField(max_length=50)
    profile_pic = models.CharField(max_length=200)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    mail_address = models.CharField(max_length=30)
    
class Post(models.Model):
    user = models.ForeignKey(User)
    user_pic = models.CharField(max_length=200)
    user_dis_name = models.CharField(max_length=50)
    share_type = models.CharField(max_length=50)
    date = models.DateTimeField('date published')
    title = models.CharField(max_length=50)
    content_text = models.CharField(max_length=500)
    content_image = models.CharField(max_length=200)
    content_link = models.CharField(max_length=500)
    agrees = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    def comment(self):
        return Comment.objects.filter(post = self.id)
    
    def agreed(self):
        return Agree.objects.filter(post = self.id)
    
class Agree(models.Model):
    post = models.ForeignKey(Post)
    user_name = models.CharField(max_length=50) 

class Comment(models.Model):
    post = models.ForeignKey(Post)
    user_pic_url = models.CharField(max_length=200)
    user_name = models.CharField(max_length=50)
    comment_date = models.DateTimeField('date published')
    comment = models.CharField(max_length=500)

# Groups - A private Collaboration for teams (Page Spec)
class Group(models.Model):
    group_name = models.CharField(max_length=50)
    group_detail = models.CharField(max_length=300)
    group_created = models.DateTimeField('date published')
    group_pic = models.CharField(max_length=200)
    group_users = models.IntegerField(default=0)
    
class GroupUser(models.Model):
    group = models.ForeignKey(Post)
    group_joined_user_id = models.IntegerField(default=0)
    group_joined_date = models.DateTimeField('date published')


def gen_post_file_name(instance, filename):
    path = 'appstarter/static/colla/images/post_img/'
    f, ext = os.path.splitext(filename)
    return path+'%s%s' % (uuid.uuid4().hex, ext)

def gen_profile_file_name(instance, filename):
    path = 'appstarter/static/colla/images/profile_img/'
    f, ext = os.path.splitext(filename)
    return path+'%s%s' % (uuid.uuid4().hex, ext)

class PostImage(models.Model):
    post_image = models.ImageField(upload_to = gen_post_file_name)

class ProfileImage(models.Model):
    profile_image = models.ImageField(upload_to = gen_profile_file_name)
