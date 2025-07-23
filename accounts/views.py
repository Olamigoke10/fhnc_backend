from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse
from .serializers import LoginSerializer
from django.utils.translation import gettext_lazy as _

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    @extend_schema(
        tags=["Accounts"],
        request=LoginSerializer,
        responses={
            200: OpenApiResponse(
                description="Successful login with access and refresh tokens",
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value={
                            "refresh": "eyJ0eXAiOiJKV1QiLCJh...refresh_token...",
                            "access": "eyJ0eXAiOiJKV1QiLCJh...access_token..."
                        },
                        status_codes=["200"]
                    )
                ]
            ),
            400: OpenApiResponse(
                description="Invalid credentials or missing fields",
                examples=[
                    OpenApiExample(
                        name="Invalid Credentials",
                        value={"non_field_errors": [_("Invalid credentials.")]},
                        status_codes=["400"]
                    )
                ]
            )
        },
        summary="User Login",
        description="Authenticates a user using email and password and returns JWT tokens.",
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
