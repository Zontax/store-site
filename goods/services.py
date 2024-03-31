from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, SearchHeadline
from django.db.models import Q

from goods.models import Product


def q_search(query):
    
    if isinstance(query, str):
        # Пошук по id
        if query.isdigit() and len(query) <= 5: 
            return Product.objects.filter(id=int(query)) 
        
        vector = SearchVector('name', 'description', 'meta_keywords') # Пошук по словах (від postgre)
        query = SearchQuery(query)
         
        result = (
            Product.objects
                    .annotate(rank=SearchRank(vector, query))
                    .filter(rank__gt=0)
                    .order_by('-rank')
                    )
        result = result.annotate(
            headline=SearchHeadline(
                'name',
                query,
                start_sel='<span style="background-color: yellow;">',
                stop_sel='</span>',
        ))
        result = result.annotate(
            bodyline=SearchHeadline(
                'description',
                query,
                start_sel='<span style="background-color: yellow;">',
                stop_sel='</span>',
        ))
        return result
    else:
        return Product.objects.all()
