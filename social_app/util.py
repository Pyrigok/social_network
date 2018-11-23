def get_current_recipient(request):
	pk=request.COOKIES.get('current_recipient')

	if pk:
		from .models import Message_Model
		try:
			whom=Message_Model.objects.get(pk=int(pk))

		except Message_Model.DoesNotExist:
			return None
		else:
			return whom
	else:
		return None