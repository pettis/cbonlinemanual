from django.db import models

class ManualPage(models.Model):
    parent = models.ForeignKey('ManualPage', null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    added = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title