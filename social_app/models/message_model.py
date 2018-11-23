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

	content = models.CharField(
		max_length = 500,
		blank = False,
		verbose_name = u'Text of Message')

	status = models.CharField(
		max_length=10,
		blank=False,
		default='not read',
		verbose_name=u'Status of message')

	created_on = models.DateField(
		auto_now_add = True,
		verbose_name=u'Date of message created')

	def __str__(self):
		return '%s %s %s %s %s' %(self.author, self.whom, self.content, self.status, self.created_on)
