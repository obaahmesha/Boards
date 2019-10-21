from django.shortcuts import render
from django.http import HttpResponse

#importing our model class from models
from .models import Board




# Create your views here.
def home(request):
    boards = Board.objects.all()
    # boards_name = list()

    # for board in boards:
    #     boards_name.append(board.name) #appending board.name to the list

    # response_html = '<br>'.join(boards_name)

    # return HttpResponse(response_html)
    return render(request, 'home.html', {'boards':boards})