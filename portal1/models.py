from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    coupon = models.IntegerField(default=0)
    email = models.EmailField()
    mobile = models.IntegerField(max_length=10, default=0)
    Event = models.ForeignKey('Events')

class Events(models.Model):
	EVENT_CHOICES = (
		('NIL','None(Rs.0)'),
		('SH','Space Hackathon(Rs.100)'),
		('CS','Cansat Seminar(Rs.150)'),
		('SW','Space Workshops(Rs.200)'),
		)	
	costdic={'NIL':0,'SH':100,'CS':150, 'SW':200}
   	eventName=models.CharField(max_length=200, choices=EVENT_CHOICES, default='NIL')

   	#cost=costdic[eventName]
