from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

class City(models.Model):
    name = models.CharField(_('city'), max_length=200)
    user = models.OneToOneField(User, related_name='city',\
            verbose_name=_('user'))
    is_actived = models.BooleanField(_('is actived'), default=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta(object):
        verbose_name = _('city')
        verbose_name_plural = _('city')
