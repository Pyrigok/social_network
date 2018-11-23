# -*- coding: utf-8 -*-

from django.db import models


class Message_Model(models.Model):
	class Meta(object):
		verbose_name=u'Messages'
		verbose_name_plural=u'Messages'

	author = models.CharField(
		max_length = 100,
		blank = False,
		verbose_name = u'Author of Message')

	whom = models.CharField(
		max_length = 100,
		blank = False,
		verbose_name = u'Recipient of Message')

	text = models.CharField(
		max_length = 500,
		blank = True,
		verbose_name = u'Text of Message')

	created_on = models.DateField(
		auto_now_add = True,
		verbose_name=u'Date of message created')

	def __init__(self):
		return '%s %s %s %s' %(self.author, self.whom, self.text, self.created_on)
