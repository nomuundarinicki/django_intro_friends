# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from datetime import datetime
from django.db import models, IntegrityError


# Create your models here.
class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {'status': True, 'errors': [], 'user': None}
        if not postData['fname'] or len(postData['fname']) < 3:
            results['errors'].append("First Name must be at least 3 characters")
            results['status'] = False
        if not postData['lname'] or len(postData['lname']) < 3:
            results['errors'].append("Last Name must be at least 3 characters")
            results['status'] = False
        if not postData['username'] or len(postData['username']) < 3:
            results['errors'].append("Username must be at least 3 characters")
            results['status'] = False
        if not postData['dob']:
            results['errors'].append("Birthday is required")
            results['status'] = False
        if not postData['password'] or len(postData['password']) < 8:
            results['errors'].append("Password must be at least 8 characters")
            results['status'] = False
        if postData['cpassword'] != postData['password']:
            results['errors'].append("Passwords do not match")
            results['status'] = False
        if not postData['email'] or len(postData['email']) < 5:
            results['errors'].append("Email must be at least 5 characters")
            results['status'] = False

        if results['status']:
            try:
                print 'trying'
                user = User.objects.create(
                    fname=postData['fname'],
                    lname=postData['lname'],
                    username=postData['username'],
                    dob=postData['dob'],
                    email=postData['email'],
                    password=(bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())))
                user.save()
                print user
                results['user'] = user
            except IntegrityError as e:
                print 'tried'
                results['errors'].append(e.message)

        return results


    def loginVal(self, postData):
        results = {'status': True, 'user': None, 'errors': []}

        try:
            print 'this is not above user GET'
            user = User.objects.get(username=postData['username'])

            print user

            if user.password == bcrypt.hashpw(postData['password'].encode(), user.password.encode()):
                print ' anython!!!'

        except:
            results['status'] = False
            results['errors'].append("Incorrect Username or Password")

        if results['status']:
            results['user'] = user
        return results


class User(models.Model):
        fname = models.CharField(max_length=100)
        lname = models.CharField(max_length=100)
        username = models.CharField(max_length=255, unique=True)
        email = models.CharField(max_length=100, unique=True)
        password = models.CharField(max_length=100)
        dob = models.DateField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.username
        objects = UserManager()
