from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from ..models import Message_Model
from ..util import get_current_recipient

@login_required
def create_message(request):

	# list of all users
	contacts_list = User.objects.all()


	# get current recipient from Cookie
	cur_recipient=get_current_recipient(request)
	if cur_recipient is not None:

		whom = User.objects.filter(username=cur_recipient)

		# message history with current recipient
		message_history = Message_Model.objects.filter(author=cur_recipient)[::-1]
	else:
		whom=None
		message_history=None


	if request.method == 'POST':
		if request.POST.get('send_button') is not None:

			data = {}

			data['author'] = request.user
			data['whom'] = whom

			data['text'] = request.POST.get('text', '').strip()

			new_message=Message_Model(**data)
			new_message.save()

			return render(request, 'message.html', {'contacts_list': contacts_list, 'message_history': message_history})



		else:
			return (request, 'message.html', {'contacts_list': contacts_list, 'message_history': message_history})


	else:
		return (request, 'message.html', {'contacts_list': contacts_list, 'message_history': message_history})
		