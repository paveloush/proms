from django.contrib.auth.models import User
import django_filters

from promise.models import Promise


class PromiseFilter(django_filters.FilterSet):
    class Meta:
        model = Promise
        # fields = ['status', 'region', 'tag', ]
        fields = {
            'status': ['exact', ],
            'region': ['exact', ],
            'tag': ['exact', ],

            'finish_date': ['gt', 'lt'],
        }
