from __future__ import unicode_literals

from django.db import models

import forums

import subforums

# Create your models here.


#USER DETAILS
class UserDets(models.Model):     
    handle = models.CharField(max_length = 30) # Handle is Username with maxlength set at 30 chars
    birth_date = models.DateField('Your birth date') # Birth Date DD - MM - YYYY
    ph_no = models.CharField(max_length = 14)# As international codes can have 0 - 4 chars and phones have a max of 10 chars
    first_name =  models.CharField(max_length = 30) #Max length of first name
    last_name =  models.CharField(max_length = 30) #Max length of first name
    email = models.EmailField(max_length = 254, unique = True) # email id, has to be unique, will do Queryset Check down bellow
    bio = models.TextField(max_length = 3000)

    #def save(self, *args, **kwargs):
    ## ... other things not important here
    #self.email = self.email.lower().strip() # Hopefully reduces junk to ""
    #if self.email != "": # If it's not blank
    #    if not email_re.match(self.email) # If it's not an email address
    #        raise ValidationError(u'%s is not an email address, dummy!' % self.email)
    #if self.email == "":
    #    self.email = None
    #super(Contact, self).save(*args, **kwargs)

    #picture = models.ImageField

    #def __str__(self):
    #    return self.question_text
    #def was_published_recently(self):
    #   return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


#USER SUBSCRIPTIONS AND LIKES
class UserSubs(models.Model):
	handle = models.ForeignKey(UserDets, on_delete = models.CASCADE)
	sub_User = models.ManyToManyField(UserDets, through = 'subUsers', through_fields = ('subscriber','subscribed_to'))
	sub_Thread = models.ManyToManyField(UserDets, through = 'subThreads', through_fields = ('subscriber','subscribed_to'))
	sub_Subforum = models.ManyToManyField(UserDets, through = 'subSubforums', through_fields = ('subscriber','subscribed_to'))
	sub_Forum = models.ManyToManyField(UserDets, through = 'subForums', through_fields = ('subscriber','subscribed_to'))

## Here the sub prefix means something user has subscribed to ##

##Threads Subscribed##
class subThreads(models.Model):
	subscriber = models.ForeignKey(UserDets, on_delete = models.CASCADE)
	subscribed_to = models.ForeignKey(Thread_list, on_delete = models.CASCADE)

##Other Users Subscribed##
class subUsers(models.Model):
	subscriber = models.ForeignKey(UserDets, on_delete = models.CASCADE)
	subscribed_to = models.ForeignKey(UserDets, on_delete = models.CASCADE)

##Forums Subscribed##
class subForums(models.Model):
	subscriber = models.ForeignKey(UserDets, on_delete = models.CASCADE)
	subscribed_to = models.ForeignKey(Forum_list, on_delete = models.CASCADE)

##Subforums Subscribed##
class subSubforums(models.Model):
	subscriber = models.ForeignKey(UserDets, on_delete = models.CASCADE)
	subscribed_to = models.ForeignKey(Subforum_list, on_delete = models.CASCADE)
