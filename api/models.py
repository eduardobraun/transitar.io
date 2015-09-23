from django.contrib.gis.db import models

class Node(models.Model):
    name = models.CharField(max_length=50)
    pos = models.PointField()
    osm_id = models.PositiveIntegerField(default=0)
    objects = models.GeoManager()
    def __unicode__(self):
        return self.name

class Stop(Node):
    pass

