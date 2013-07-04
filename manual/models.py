from django.db import models

class PublishedPagesManager(models.Manager):
    def get_query_set(self):
        return super(PublishedPagesManager, self).get_query_set().filter(published=True)

class ManualPage(models.Model):
    parent = models.ForeignKey('ManualPage', null=True, blank=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    content = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    added = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    all_objects = models.Manager()
    objects = PublishedPagesManager()

    def __unicode__(self):
        return self.title