from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect,redirect

# multiple inheritence

class LoginRequiredMixin(object):
    """
    View mixin which verifies that the user has authenticated.

    NOTE:
        This should be the left-most mixin of a view.
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class LogoutRequiredMixin(object):

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect('detail',pk=self.request.user.id)
        return super(LogoutRequiredMixin, self).dispatch(*args, **kwargs)