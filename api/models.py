from django.contrib.gis.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Node(models.Model):
    DELETED = "D"
    ACTIVE  = "A"
    REVIEW  = "R"
    STATE_CHOICES = ((DELETED,"Deleted"),(ACTIVE,"Active"),
                     (REVIEW,"Review"))
    name = models.CharField(max_length=50)
    pos = models.PointField()
    osm_id = models.BigIntegerField(default=0)
    osm_data = models.TextField(default=u"")
    state = models.CharField(max_length=1, choices=STATE_CHOICES,
                             default=ACTIVE)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

class Stop(Node):
    pass

