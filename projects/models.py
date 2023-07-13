from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

class Technology(models.Model):
    name = models.CharField(_("Technology title"), max_length=100)

    class Meta:
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologies")

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(_("Project title"), max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="projects",
        null=True,
        on_delete=models.SET_NULL,
    )
    technologies = models.ManyToManyField(Technology, related_name="projects_list", blank=True)
    body = models.TextField(_("Description"))
    
    def __str__(self):
        return f"{self.title} by {self.author.username}"
