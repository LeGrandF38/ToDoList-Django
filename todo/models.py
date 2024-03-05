from django.db import models
#from django.utils.translation import ugettext_lazy as _

class Task (models.Model):
    content = models.CharField((u'task'),max_length= 225) 
    is_resolved=models.BooleanField((u'Resolved?'))


def __unicode__(self):
    return u'Task %s' % (self.id, self.id, self.content)                           

