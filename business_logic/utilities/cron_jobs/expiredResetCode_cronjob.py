from authentication.models import PasswordResetInfo
import datetime
from django.utils.timezone import utc


def delete_expired_reset_code():
    print('\nJob: deleting expired reset codes')
    now = datetime.datetime.utcnow().replace(tzinfo=utc)

    queryset = PasswordResetInfo.objects.all()

    for query in queryset:
        if(((now - query.created_at).total_seconds())/60 > 1440):
            query.delete()
            query.save
