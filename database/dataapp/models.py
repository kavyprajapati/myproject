from django.db import models
import mongoengine as me


# Create your models here.

class UserMaster(me.Document):
       usrName = me.StringField(max_length=100)
       useEmail = me.StringField(max_length=100)
       usrPassword = me.IntField(max_length=20)


class categoryMaster(me.Document):
       catName = me.StringField(max_length=200)
       catSlug = me.StringField(max_length=200)
       catSeqno = me.IntField()
       catStates = me.BooleanField(default=True)