from datetime import datetime


def year_processor(request):
    current_year = datetime.now().year
    return { 'current_year': current_year }
