from django.db import models
from django.contrib.auth import get_user_model

class Interest(models.Model):
   sender = models.ForeignKey(get_user_model(), related_name='sent_interests', on_delete=models.CASCADE)
   receiver = models.ForeignKey(get_user_model(), related_name='received_interests', on_delete=models.CASCADE)
   accepted = models.BooleanField(default=False)