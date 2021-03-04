from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from data.forms import UserLoginForm, UserRegisterForm
from data.models import DataBeforeProcess, DataAfterProcess
from data.serializers import DataBeforeProcessSerializer


# ===================== Django Rest Framework ===================== #
class DataBeforeProcessViewSet(viewsets.ModelViewSet):
    queryset = DataBeforeProcess.objects.get_queryset().order_by('id')
    serializer_class = DataBeforeProcessSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ===================== ОТОБРАЖЕНИЕ НА САЙТЕ ===================== #
class HomeView(ListView):
    template_name = 'data/home_list.html'
    context_object_name = 'data'
    model = DataAfterProcess

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['FirstName'] = self.request.user.first_name
            context['Cows'] = User.objects.filter(is_staff=False, is_superuser=False)
        return context


class DetailCowView(ListView):
    template_name = 'data/detail_cow_list.html'
    context_object_name = 'data'
    model = DataAfterProcess

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['cow_name'] = self.kwargs['cow_name']
            context['FirstName'] = self.request.user.first_name
            context['CowDetail'] = DataAfterProcess.objects.filter(user__username=self.kwargs['cow_name']).order_by(
                '-id')
            labels = []
            DataHeartBeat = []
            DataCondition = []
            query = DataAfterProcess.objects.filter(user__username=self.kwargs['cow_name']).order_by('-id')[:100]
            for item in query:
                DataHeartBeat.append(int(item.HeartBeat))
                DataCondition.append(int(item.CowCondition))
                labels.append(int(item.pk))
            context['label'] = labels
            context['DataHeartBeat'] = DataHeartBeat
            context['DataCondition'] = DataCondition
        return context


# ===================== РЕГИСТРАЦИЯ, АВТОРИЗАЦИЯ, РАЗЛОГИНИВАНИЕ ===================== #
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'data/login.html', {"form": form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'data/register.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('MyLogin')
