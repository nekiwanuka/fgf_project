from apscheduler.schedulers.background import BackgroundScheduler

from business_logic.utilities.cron_jobs import unverfiedEmailAdress_cronjob
from business_logic.utilities.cron_jobs import unverifiedUserEmail_cronjob
from business_logic.utilities.cron_jobs import unverifiedOrgEmail_cronjob
# from business_logic.utilities.cron_jobs import courierpayment_cronjob
from business_logic.utilities.cron_jobs import delivery_cronjobs
from business_logic.utilities.cron_jobs import deliverystatus_cronjob
from business_logic.utilities.cron_jobs import expiredResetCode_cronjob
from business_logic.utilities.cron_jobs import transaction_cronjobs
from business_logic.utilities.cron_jobs import unverified_accounts_cronjobs

def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(unverfiedEmailAdress_cronjob.delete_unverified_emailAddress() , "interval", minutes=1)
    scheduler.add_job(unverifiedUserEmail_cronjob.delete_unverified_user_emailAddress , "interval", minutes=1)
    scheduler.add_job(unverifiedOrgEmail_cronjob.delete_unverified_org_emailAddress , "interval", minutes=1)
    scheduler.add_job(delivery_cronjobs.confirm_delivery , "interval", minutes=1)
    scheduler.add_job(deliverystatus_cronjob.delivery_status_update , "interval", minutes=1)
    scheduler.add_job(expiredResetCode_cronjob.delete_expired_reset_code , "interval", minutes=1)
    scheduler.add_job(transaction_cronjobs.change_transaction_status , "interval", minutes=1)
    scheduler.add_job(transaction_cronjobs.delete_uninitiated_transactions , "interval", minutes=1)
    scheduler.add_job(unverified_accounts_cronjobs.delete_unverified_accounts , "interval", minutes=1)    
    scheduler.start()
