from functools import wraps
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import resolve_url


def user_passes_test(
 test_func, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Dekorator sprawdza, czy User posiada już przydzieloną kwaterę. Jeśli nie,
    wymusza przejście testu na przydział kwatery.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            path = request.build_absolute_uri()
            resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
            # If the login url is the same scheme and net location then just
            # use the path as the "next" url.
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if ((not login_scheme or login_scheme == current_scheme) and
                    (not login_netloc or login_netloc == current_netloc)):
                path = request.get_full_path()
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(
                path, resolved_login_url, redirect_field_name)
        return _wrapped_view
    return decorator



# Dekorator Rady Studentów - ustal w funkcji power_level jeśli ma być bardziej restrykcyjny.
def council_only(
 function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None,
 power_level=1
 ):
    """
    Decorator for views that checks that the user belongs to the council
    , redirecting  to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.role_council > power_level,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


# Szybki fix dla zduplikowanych widoków. Do usunięcia w przyszłości.
def user_is_owner(
 function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None,
 owner_id=None
 ):
    """
    Dekorator sprawdza, czy user jest właścicielem danego eventu.
    """
    actual_decorator = user_passes_test(
        lambda u: u.mnemo_login == owner_id,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
