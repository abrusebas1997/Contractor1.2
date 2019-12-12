from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class Code(models.Model):
    """ Represents a single CODES Code. """
    title = models.CharField(max_length=settings.CODES_PAGE_TITLE_MAX_LENGTH, unique=True,
                             help_text="Title of your Code.")
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               help_text="The user that posted this article.")
    slug = models.CharField(max_length=settings.CODES_PAGE_TITLE_MAX_LENGTH, blank=True, editable=False,
                            help_text="Unique URL path to access this Code. Generated by the system.")
    content = models.TextField(
        help_text="Write the content of your Code here.")
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this Code was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True,
                                    help_text="The date and time this Code was updated. Automatically generated when the model updates.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a Code (/my-new-CODES-Code). """
        path_components = {'slug': self.slug}
        return reverse('codes-details-Code', kwargs=path_components)
        # return reverse('codes:codes-update-Code', kwargs=path_components)
    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a Code is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Code, self).save(*args, **kwargs)
