from .models import Categories

def categories_processor(request):
    categories = Categories.objects.filter(product__is_active=True).distinct()
    return {'categories': categories}
