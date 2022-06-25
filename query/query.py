# python3 manage.py shell
# https://docs.djangoproject.com/en/4.0/ref/models/querysets/#exclude

# cara parsing view per bagian
from queryset.models import Query
# first
first = Query.objects.first()
# get / filter
get = Query.objects.get(id=1)
# exclude / selain / ambil selain
exclude = Query.objects.exclude(id=1).exclude(char="first")
# aggregat
# from django.db.models import Count
# {'char__count': 7}
aggregat = Query.objects.aggregate(Count('char'))
# annotate
aggregat = Query.objects.annotate(Count('char'))
