from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import login as auth_login
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, get_user_model
# Project imports
from catalog import models as catalogmodels
from apuser import models
from client.api import serializers
from utils.views import APIView


class SignInAPIView(APIView):
    serializer_class = serializers.SignInSerializer
    permission_classes = (permissions.AllowAny, )

    def success_action(self, request, serializer):
        auth_login(request, serializer.object)

    def success_data(self, serializer):
        response = {}
        response['redirect_to'] = reverse_lazy('client:profile')
        return response


class SignUpAPIView(CreateAPIView):
    serializer_class = serializers.SignUpSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        response = {}
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response['status'] = 'success'
            response['message'] = _('Для завершения регистрации перейдите по ссылке из письма отправленного на ваш e-mail. Если не найдете во входящих, проверьте "спам"')
            return Response(response, status=status.HTTP_201_CREATED, headers=headers)
        else:
            response['status'] = 'fail'
            response['errors'] = serializer.errors
            headers = self.get_success_headers(serializer.data)
            return Response(response,
                            status=status.HTTP_400_BAD_REQUEST,
                            headers=headers)


class Recovery(APIView):
    serializer_class = serializers.RecoverySerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def success_action(self, request, serializer):
        email = serializer.validated_data.get('email')
        user = models.AlterPriceUser.objects.get(email=email)
        catalogmodels.PasswordRecovery.objects.make(user=user)

    def success_data(self, serializer):
        response = {}
        # email = serializer.validated_data.get('email')
        response['message'] = _(
            'Выслано сообщение со ссылкой на восстановление')
        return response


class RecoveryPassword(APIView):
    serializer_class = serializers.RecoveryPasswordSerializer
    permission_classes = (permissions.AllowAny, )

    def success_action(self, request, serializer):
        password = serializer.validated_data.get('password')
        pr = catalogmodels.PasswordRecovery.objects.get_valid(
            token=serializer.validated_data.get('token'))
        pr.recover()
        user = pr.user
        user.set_password(password)
        user.save()

    def success_data(self, serializers):
        response = {}
        response['message'] = _('Ваш пароль успешно изменен')
        response['redirect_to'] = reverse('client:login')
        return response


class UpdateEmail(APIView):
    serializer_class = serializers.UpdateEmailSerializer
    permission_classes = (permissions.AllowAny, )

    def success_action(self, request, serializer):
        user = serializer.validated_data.get('user')
        user.email = serializer.validated_data.get('email')
        user.save()