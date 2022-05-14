from .models import Notification



def create_notification(request, to_user):
    notification = Notification.objects.create(to_user=to_user)