from django.contrib.gis.db import models

class Node(models.Model):
    DELETED = "D"
    ACTIVE  = "A"
    REVIEW  = "R"
    STATE_CHOICES = ((DELETED,"Deleted"),(ACTIVE,"Active"),
                     (REVIEW,"Review"))
    name = models.CharField(max_length=50)
    pos = models.PointField()
    osm_id = models.PositiveIntegerField(default=0)
    osm_data = models.TextField(default=u"")
    state = models.CharField(max_length=1, choices=STATE_CHOICES,
                             default=ACTIVE)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

class Stop(Node):
    pass

