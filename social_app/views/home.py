from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from ..models import Message_Model
from ..util import get_current_recipient

@login_required
def create_message(request):

	# list of all users without secured user
	contacts_list = User.objects.all().exclude(username=request.user)


	# get current recipient from Cookie
	cur_recipient=get_current_recipient(request)

	#if cur_recipient is not None:

	selected_contact = User.objects.filter(username=cur_recipient)

	# message history with current recipient
	message_history = Message_Model.objects.filter(whom=request.user, author=cur_recipient)
	print('history - ', message_history)
	message_count = Message_Model.objects.filter(whom=request.user, status='not read').count()

	# show authors of unreaded messages
	authors = []
	for entry in Message_Model.objects.filter(status='not read'):
		authors.append(entry.author)
	authors=set(authors)

	# count messages by authors
	author_message={}
	for entry in authors:
		author_message[entry] = Message_Model.objects.filter(status='not read', author=entry).count()


	if request.method == 'POST':
		if request.POST.get('send_button') is not None:

			data = {}

			data['author'] = request.user
			data['whom'] = cur_recipient

			content = request.POST.get('content', '').strip()
			data['content']=content

			new_message=Message_Model(**data)
			new_message.save()

			return render(request, 'message.html', {'author_message': author_message, 'authors': authors, 'message_count': message_count, 'cur_recipient': cur_recipient, 'contacts_list': contacts_list, 'message_history': message_history, 'selected_contact': selected_contact})

		else:
			return render(request, 'message.html', {'author_message': author_message, 'authors': authors, 'message_count': message_count, 'cur_recipient': cur_recipient, 'contacts_list': contacts_list, 'message_history': message_history, 'selected_contact': selected_contact})


	else:
		return render(request, 'message.html', {'author_message': author_message, 'authors': authors, 'message_count': message_count, 'cur_recipient': cur_recipient, 'contacts_list': contacts_list, 'message_history': message_history, 'selected_contact': selected_contact})

	# else:
	# 	current_whom=''
	# 	message_history=None
	# 	return render(request, 'message.html', {'contacts_list': contacts_list, 'message_history': message_history, 'current_whom': current_whom})

