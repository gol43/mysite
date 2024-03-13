from django.shortcuts import render, get_object_or_404
from users.models import User
#from .utils import paginate

#RECORD:int = 10

# Create your views here.
def index(request):
    title = 'КомфортСтрой'
    context = {
        'title': title
    }
    return render(request, 'products/index.html', context)


def profile(request, username):
    title = "Профиль"
    user = get_object_or_404(User, username=username)
    #cards = ShoppingCard.objects.filter(user=username)
    #count_products = cards.count()
    #cards_objects = paginate(request, cards, RECORD)

    context =  {
        'title': title,
        'user': user,
        #'count_products': count_products,
        #'cards_objects': cards_objects
    }
    return render(request, 'products/profile.html', context)
