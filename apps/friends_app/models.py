from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User


# Create your models here.

class FriendManager(models.Manager):
    def addFriend(self, postData):
        results = {'status': True, 'errors': []}
        if len(postData['title']) < 1 and len(postData['content']) < 1:
            results['errors'].append('All fields must be filled out')
            results['status'] = False

        user = User.objects.get(id=postData['user_id'])
        if results['status']:

            try:
                friend = Friend.objects.create(
                    title=postData['title'],
                    content=postData['content'],
                    user_id=user,
                )
                friend.save()
            except:
                results['errors'].append('Error: Friend not created')

        return results

    def addQuote(self, postData, user_id):
        results = {'status': True, 'errors': []}
        try:
            print 'mskjsdkjskdksjksdjksdjksjksdjskjdkjsdkj'

            user = User.objects.get(id=user_id)
            friend = Friend.objects.create(title=postData['title'],content=postData['content'],user_id=user)
            quote.save()
        except:
            results['errors'].append('Error: not addeddd')

        return results

class Friend(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    user_id = models.ForeignKey('loginreg.User', related_name='friends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = FriendManager()
