from goods.models import Product
from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

def q_search(query):
    
    # Пошук по id
    if isinstance(query, str):
        if query.isdigit() and len(query) <= 5: 
            return Product.objects.filter(id=int(query)) 
        
        # Пошук по словах (від postgre)
        vector = SearchVector('name', 'description')
        query = SearchQuery(query)
        return Product.objects.annotate(rank=SearchRank(vector, query)).order_by('-rankє')
        
        # keywords = [word for word in query.split() if len(word) > 2]
        # q_objects = Q()
        
        # for token in keywords:
        #     q_objects |= Q(name__icontains=token)
        #     q_objects |= Q(description__icontains=token)
        
        # return Product.objects.filter(q_objects)
    
    else:
        return Product.objects.all()