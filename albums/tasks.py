from celery import shared_task
from musicplatform.celery import app
from time import sleep
from django.core.mail import send_mail
from django.conf import settings
@app.task
def fetch_data():
    print("fetch")
    # fetch data from spotify every 14 days
    return



@shared_task
def send_album_creation_succeded_mail(user , album):
    subject = 'Album Created Successfully'
    message = f'hello {user["username"] } your album {album["name"]} has been created successfuly'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user["email"],]
    print (recipient_list)
    send_mail( subject, message, email_from, recipient_list )
    return 