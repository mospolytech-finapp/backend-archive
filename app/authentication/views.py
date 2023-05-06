from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import FinappUserSerializer


class RegistrationView(generics.CreateAPIView):
    serializer_class = FinappUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        if 'email' in data:
            data['email'] = data['email'].lower()
        serializer = FinappUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
