from datetime import datetime
from goods.models import Category
from app.settings import SITE_NAME


def base_processors(request):
    categories = Category.objects.all().order_by('slug')
    current_year = datetime.now().year
    
    return { 'current_year': current_year, 
             'all_categories': categories,
             'site_name': SITE_NAME,}

