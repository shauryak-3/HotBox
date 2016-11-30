from __future__ import unicode_literals

from django.db import models

from datetime import datetime, timedelta



from math import sqrt

from django.core.urlresolvers import reverse


# Create your models here.

	
	
class User (models.Model) :
	handle =  models.CharField(max_length = 30) ### User handle, other users will see this
	passwd = models.CharField(max_length = 30) ### User password, later will be sent through Django-Bcrypt
#	img =  models.ImageField(upload_to = 'localhost:8000\\UserIMG') ### Image of the user
	first_name = models.CharField(max_length = 30) ###First Name - This is ID Thingy
	last_name = models.CharField(max_length = 30) ###Last Name - This is ID Thingy
	gender = models.CharField(max_length = 1) ### M for Male, F for Female, O for Other and U for Unspecified
	birth_date = models.DateField('Your Birth Date') ### Birth Date DD-MM-YYYY
	ph_no = models.CharField(max_length = 14) ### As international codes can have 0 - 4 chars and phones have a max of 10 chars
	email = models.EmailField(max_length = 254, unique = True) ### email id, has to be unique, will do Queryset Check down bellow
	bio = models.TextField(max_length = 3000)
	#subs_user = models.ManyToManyField("self")
	"""
	def clean_handle(self):
		try:
			handle = User.objects.get(handle__iexact=self.cleaned_data['handle'])
		except User.DoesNotExist:
			return self.cleaned_data['handle']
		raise forms.ValidationError(_("The handle already exists. Please try another one."))

	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_("The two password fields did not match."))

		return self.cleaned_data
#	subs_forum = models.ManyToManyField(Forums)
#	subs_subforum = models.ManyToManyField(Subforums)
#	subs_thread = models.ManyToManyField(Threads)"""

	def __unicode__(self):              # __unicode__ on Python 2
		return self.handle

class User_qualifications (models.Model) :
	handle = models.ForeignKey(User, on_delete=models.CASCADE) ### User handle linking to Qual Table
	qual = models.CharField(max_length = 50) ### Title of Qualification
	desc = models.TextField(max_length = 300) ### Short description of qualification

	def __unicode__(self):              # __unicode__ on Python 2
		return self.qual

class User_achievements (models.Model) : 
	handle = models.ForeignKey(User, on_delete=models.CASCADE)
	achv = models.CharField(max_length = 50) ### Title of Achievement
	desc = models.TextField(max_length = 300) ### Short description of achievement

	def __unicode__(self):              # __unicode__ on Python 2
		return self.achv

class Forums (models.Model) :
	title = models.CharField(max_length = 50) ### Title length limited at 50 chars
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('Publish Date')
	upvotes = models.IntegerField(default = 0)
	downvotes = models.IntegerField(default = 0)
	rating_rel = models.BigIntegerField(default = 0)
	rating_pop = models.BigIntegerField(default = 0)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.title

class Subforums (models.Model) : 
	title = models.CharField(max_length = 50) ### Title length limited at 50 chars
	forum = models.ForeignKey(Forums, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
#	mods = models.ManyToManyField(User)
	pub_date =  models.DateTimeField('Publish Date')
	upvotes =  models.IntegerField(default = 0)
	downvotes =  models.IntegerField(default = 0)
	rating_rel = models.BigIntegerField(default = 0)
	rating_pop = models.BigIntegerField(default = 0)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.title

class Threads (models.Model) :
	title = models.CharField(max_length = 50) ### Title length limited at 50 chars
	subforum = models.ForeignKey(Subforums, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	op = models.TextField(max_length = 3000) ### The Original Post by the author is coupled with the Thread, limited to 3000 chars
	pub_date = models.DateTimeField('Publish Date')
	upvotes =  models.IntegerField(default = 0)
	downvotes =  models.IntegerField(default = 0)
	rating_rel = models.BigIntegerField(default = 0)
	rating_pop = models.BigIntegerField(default = 0)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.title

class Posts (models.Model) :
	thread = models.ForeignKey(Threads, on_delete=models.CASCADE)
	text = models.TextField(max_length = 3000) ### Text field is limited to 3000 chars
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('Publish Date')
	upvotes =  models.IntegerField(default = 0)
	downvotes = models.IntegerField(default = 0)
	rating_rel = models.BigIntegerField(default = 0)
	rating_pop = models.BigIntegerField(default = 0)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.text


class forum_mods (models.Model) : 
	handle = models.ForeignKey(User, on_delete = models.CASCADE)
	forum = models.ForeignKey(Forums, on_delete = models.CASCADE)

class subforum_mods (models.Model) : 
	handle = models.ForeignKey(User, on_delete = models.CASCADE)
	subforum = models.ForeignKey(Subforums, on_delete = models.CASCADE)

class tags (models.Model) :
	text = models.CharField(max_length = 30, primary_key = True)

class tag_to_subforum (models.Model) :
	tag = models.ForeignKey(tags, on_delete=models.CASCADE)
	subforum = models.ForeignKey(Subforums, on_delete=models.CASCADE)

class tag_to_forum (models.Model) :
	tag = models.ForeignKey(tags, on_delete=models.CASCADE)
	thread = models.ForeignKey(Forums, on_delete=models.CASCADE)


#class post_thread_rel (models.Model) :

#class thread_subforum_rel (models.Model) :

#class 

class subs_users (models.Model) :
	handle =  models.ForeignKey(User, related_name='%(class)s_subber')
	subs_handle =  models.ForeignKey(User, related_name='%(class)s_subbed')

class subs_thread (models.Model) :
	handle = models.ForeignKey(User, on_delete=models.CASCADE)
	subs_title = models.ForeignKey(Threads, on_delete=models.CASCADE)
	
class subs_subforum (models.Model) :
	handle = models.ForeignKey(User, on_delete=models.CASCADE)
	subs_title = models.ForeignKey(Subforums, on_delete=models.CASCADE)

class subs_forum (models.Model) :
	handle = models.ForeignKey(User, on_delete=models.CASCADE)
	subs_title = models.ForeignKey(Forums, on_delete=models.CASCADE)

epoch = datetime(1970, 1, 1)

def epoch_seconds(date):
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)

def _confidence(ups, downs):
    n = ups + downs

    if n == 0:
        return 0

    z = 1.281551565545
    p = float(ups) / n

    left = p + 1/(2*n)*z*z
    right = z*sqrt(p*(1-p)/n + z*z/(4*n*n))
    under = 1+1/n*z*z

    return (left - right) / under

def confidence(ups, downs):
    if ups + downs == 0:
        return 0
    else:
        return _confidence(ups,downs)

