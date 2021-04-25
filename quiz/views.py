from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def index(request):
    print('user is', request.user)
    print('Auth type:', request.auth)
    if request.method == 'GET':
        return Response(data={'message': 'Hello from Bolaji'}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        return Response(data=request.data, status=status.HTTP_200_OK)
    else:
        return Response(data='Request Method is Not right')


class Message(APIView):

    def get(self, request):
        return Response(data="This is the classed based view hit by get request", status=status.HTTP_200_OK)

    def post(self, request):
        print('Hit by Post Request')
        print(request.data)
        return Response(data="This is the class based view hit by the post method", status=status.HTTP_200_OK)
