from authentication.models import User
import datetime
from django.utils.timezone import utc


def delete_unverified_accounts():
    print('\nJob: deleting unverified user accounts')
    now = datetime.datetime.utcnow().replace(tzinfo=utc)

    users = User.objects.all().filter(
            is_verified=False
        ).filter(
                is_staff=False
            ).filter(
                    is_admin=False
                )

    for user in users:
        if(((now - user.date_joined).total_seconds())/60 > 1440):
            user.delete()
