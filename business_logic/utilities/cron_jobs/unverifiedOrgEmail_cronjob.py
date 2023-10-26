from api.models import UserEmailAddress
from api.models import EmailAddress
from api.models import OrganizationEmailAddress
import datetime
from django.utils.timezone import utc


def delete_unverified_org_emailAddress():
    print('\nJob: delete_unverified_org_emailAddress')
    now = datetime.datetime.utcnow().replace(tzinfo=utc)

    org_email_instances = OrganizationEmailAddress.objects.filter(
        is_verified=False)

    for org_email_instance in org_email_instances:
        if ((now - org_email_instance.created_at).total_seconds())/60 > 1440:
            user_emailaddress_instances = UserEmailAddress.objects.filter(
                email=org_email_instance.email)

            if not user_emailaddress_instances.exists():
                emailaddress_instance = EmailAddress.objects.get(
                    email=org_email_instance.email)
                org_email = org_email_instance.email
                emailaddress_instance.delete()
                emailaddress_instance.save()
        else:
            continue
