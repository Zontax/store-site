from django.http import HttpRequest

from datetime import datetime
from goods.models import Category
from main.models import BaseAdvertisement
from app.settings import SITE_TITLE


def base_processors(request: HttpRequest):
    categories = Category.objects.all().order_by('slug')
    advertisement = BaseAdvertisement.objects.filter(is_active=True).first()
    current_year = datetime.now().year
    
    return { 'site_main_title': SITE_TITLE,
             'advertisement': advertisement,  
             'current_year': current_year, 
             'all_categories': categories,
             }
