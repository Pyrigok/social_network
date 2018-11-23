function initRecipientSelector() {
	$('.user_div').click(function(event) {

		var recipient = $(this).find('input').val();

		if (recipient) {

			/*create cookie named 'current_recipient'*/
			$.cookie('current_recipient', recipient, {'path': '/', 'expires': 365});
		} else {
			$.removeCookie('current_recipient', {'path': '/'});
		}
		location.reload(true);
		return true;
	});
}

$(document).ready(function() {
	initRecipientSelector();
});