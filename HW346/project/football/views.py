from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def player(request):
    if request.method == 'GET':
        player_info = {
            'id': 1,
            'first_name': 'John',
            'last_name': 'Doe',
            'gender': 'M',
            'age': 25,
            'club': 'Sample Club',
        }
        return JsonResponse(player_info)
    else:
        return HttpResponseBadRequest('Invalid request method')


@require_http_methods(["GET", "POST"])
def club(request):
    if request.method == 'GET':
        club_info = {
            'id': 1,
            'name': 'Sample Club',
            'foundation_date': '2020-01-01',
        }
        return JsonResponse(club_info)
    else:
        return HttpResponseBadRequest('Invalid request method')


@require_http_methods(["GET", "POST"])
def match(request):
    if request.method == 'GET':
        match_info = {
            'id': 1,
            'city': 'New York',
            'date': '2022-05-10',
            'players': ['John Doe', 'Jane Smith'],
        }
        return JsonResponse(match_info)
    else:
        return HttpResponseBadRequest('Invalid request method')
