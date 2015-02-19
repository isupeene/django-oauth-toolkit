from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

from .settings import oauth2_settings
from django.conf import settings


class HttpResponseUriRedirect(HttpResponseRedirect):
    def __init__(self, redirect_to, *args, **kwargs):
        self.allowed_schemes = oauth2_settings.ALLOWED_REDIRECT_URI_SCHEMES
        super(HttpResponseUriRedirect, self).__init__(redirect_to, *args, **kwargs)


def redirect_or_403(redirect_uri=None):
	if hasattr(settings, "LOGIN_URL"):
		redirect_uri = redirect_uri or settings.LOGIN_URL

	if redirect_uri:
		return HttpResponseUriRedirect(redirect_uri)
	else:
		raise PermissionDenied

