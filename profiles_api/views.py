from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (POST, GET, PUT, PATCH, DELETE',
            'Is similar to a traditional Django View'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})