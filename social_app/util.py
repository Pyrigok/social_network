def get_current_recipient(request):
	pk=request.COOKIES.get('current_recipient')

	if pk:
		from django.contrib.auth.models import User

		try:
			whom=User.objects.get(pk=int(pk))

		except Message_Model.DoesNotExist:
			return None
		else:
			return whom
	else:
		return None