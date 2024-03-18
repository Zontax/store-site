from datetime import datetime

from goods.models import Category


def base_processors(request):
    categories = Category.objects.all().order_by('slug')
    current_year = datetime.now().year
    return { 'current_year': current_year, 'all_categories': categories  }

