from django.utils.deprecation import MiddlewareMixin
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from rest_framework.views import APIView

# Create your views here.
from core.models import User
from .authentication import JWTAuthentication
from .serializers import UserSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Password does not match!')

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed('User  Not Found!')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Incorrect password!')

        token = JWTAuthentication.generate_jwt(user.id)

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message': 'success'
        }

        return response


class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response()
        response.delete_cookie(key='jwt')
        # del request.data['jwt']
        response.data = {
            'message': 'success'
        }
        return response
