from datetime import datetime

from goods.models import Categories


def base_processors(request):
    categories = Categories.objects.all()
    current_year = datetime.now().year
    return { 'current_year': current_year, 'categories': categories  }

