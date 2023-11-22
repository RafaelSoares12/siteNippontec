from django.urls import path

from main.views import IndexTemplateView

app_name='main'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
]