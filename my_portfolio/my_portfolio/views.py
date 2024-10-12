from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.http import JsonResponse


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to Sam Scarisbrick Portfolio API!"
    })


# view for csrf token
# @ensure_csrf_cookie
# def get_csrf_token(request):
#     return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})
