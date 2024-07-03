from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = CustomUser.obects.get(email=request.data['email'])
        if user.chek_password(request.data['password']):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response(status=status.HTTP_401_UNAUTHORIZED)
