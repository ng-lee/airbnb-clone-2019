from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls.base import reverse_lazy
from . import models


class EmailLoginOnlyView(LoginRequiredMixin):
    def test_func(self):
        return self.request.user.login_method == models.User.LOGIN_EMAIL

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there!")
        return redirect(reverse("core:home"))


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there!")
        return redirect(reverse("core:home"))


class LoggedInOnlyView(LoginRequiredMixin):

    login_url = reverse_lazy("users:login")
