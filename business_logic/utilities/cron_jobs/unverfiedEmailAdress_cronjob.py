from api.models import UserEmailAddress
from api.models import EmailAddress
from api.models import OrganizationEmailAddress
import datetime
from django.utils.timezone import utc


def delete_unverified_emailAddress():

    now = datetime.datetime.utcnow().replace(tzinfo=utc)

    queryset_org_email = UserEmailAddress.objects.all().filter(is_verified=0)
    
    queryset_user_email = OrganizationEmailAddress.objects.all().filter(is_verified=0)
    
    queryset_email = EmailAddress.objects.all()

    for query in queryset_email:
        if(queryset_org_email.email==None and queryset_user_email.email==None):
            query.delete()
            query.save
        else:
            pass

    print('deleted')