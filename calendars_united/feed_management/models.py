from django.db import models
from django.contrib.auth.models import User

class IngoingFeed(models.Model):
	owner = models.ForeignKey(User)
	url = models.CharField(max_length=255)
	def __str__(self):
		return "Ingoing feed #%d" % self.id

class OutgoingFeed(models.Model):
	owner = models.ForeignKey(User)
	secret_uuid = models.CharField(max_length=36)
	def __str__(self):
		return "Outgoing feed #%d" % self.id

class FeedMapping(models.Model):
	creator = models.ForeignKey(User, related_name="mappings")
	ingoing = models.ForeignKey(IngoingFeed, related_name="mappings")
	outgoint = models.ForeignKey(OutgoingFeed, related_name="mappings")
	def __str__(self):
		return "%s's mapping from %s to %s" % (self.creator, self.ingoing, self.outgoint)