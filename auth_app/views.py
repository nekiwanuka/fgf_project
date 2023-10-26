"""
Views for FGF User Authentication Module
"""

from ._views import administrator_views as administrator_views
from ._views import contributor_views as contributor_views
from ._views import account_views as account_views

administrator_views
contributor_views
account_views


# Create your views here.

# Account Views
SendVerificationLinkView = account_views.SendVerificationLinkView
VerifyEmailView = account_views.VerifyEmailView
UserLoginView = account_views.UserLoginView
PasswordResetView = account_views.PasswordResetView
PasswordResetConfirmView = account_views.PasswordResetConfirmView

