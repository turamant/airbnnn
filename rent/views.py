from django.db import connection, reset_queries
from django.db.models import Avg, Count
from django.shortcuts import render

# Create your views here.
from rent.models import Room, Reservation, Review


def index(request):
    #rooms = Room.objects.all()
    rooms = Room.objects.raw('SELECT * FROM room')
    context = {'rooms': rooms}
    return render(request, 'index.html', context)


def avg_reviews(request):
    """
    select room_id, AVG(rating) as avg_score from Reservations
    INNER JOIN Reviews ON Reviews.reservation_id = Reservations.id
    GROUP BY room_id HAVING avg_score;
    """
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'avg_reviews.html', context)


def avg_count(request):
    rooms = Room.objects.all()
    avg_p = Room.objects.all().aggregate(Avg('price'))
    context = {'rooms': rooms, 'avg': avg_p['price__avg']}
    return render(request, 'avg_count.html', context)


def reservation_count_avg_price(request):
    '''select room_id, avg(price) as avg_price, count(room_id) as count
    from Reservations group by room_id order by count desc, avg_price desc;'''
    reservations = Reservation.objects.values('room_id')\
        .annotate(count=Count('room_id'), avg_price=Avg('price')).filter(avg_price__lte=1000).order_by('-count', '-avg_price')

    context = {'reservations': reservations }
    print("++++++++++++++++", reservations)
    return render(request, 'group_by.html', context)


def reservation_count_avg_price_old(request):
    rooms = Room.objects.all()
    reservation = Reservation.objects.aggregate(count=Count('room_id'), avg_price=Avg('price'))
    print("...........", reservation)
    context = {'rooms': rooms, 'count': reservation['count'], 'avg_price': reservation['avg_price']}
    return render(request, 'group_by.html', context)