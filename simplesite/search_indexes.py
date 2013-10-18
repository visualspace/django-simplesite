""" django-haystack search index """
from haystack import indexes

from .models import Page


class PageIndex(indexes.ModelSearchIndex, indexes.Indexable):
    """ Search index for pages """

    class Meta:
        model = Page

    def index_queryset(self, using=None):
        """ Show only published pages. """

        return Page.objects.filter(publish=True)
