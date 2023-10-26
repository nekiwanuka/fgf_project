from api.models import UserEmailAddress
from api.models import EmailAddress
from api.models import OrganizationEmailAddress
import datetime
from django.utils.timezone import utc


def delete_unverified_user_emailAddress():
    print('\nJob: deleting unverified user emailAddress')
    now = datetime.datetime.utcnow().replace(tzinfo=utc)

    user_email_instances = UserEmailAddress.objects.filter(is_verified=False)

    for user_email_instance in user_email_instances:
        if ((now - user_email_instance.created_at).total_seconds())/60 > 1440:

            organization_emailaddress_instances = OrganizationEmailAddress.objects.filter(
                email=user_email_instance.email)

            if not organization_emailaddress_instances.exists():
                emailaddress_instance = EmailAddress.objects.get(
                    email=user_email_instance.email)
                emailaddress_instance.delete()
                emailaddress_instance.save()
        else:
            continue
