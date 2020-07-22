from app1 import views
from django.conf.urls import url

#TEMPLATE TAGGING

app_name = "app1"

urlpatterns = [
    url(r'^other',views.other,name="other"),
    url(r'^relative',views.relative,name="relative"),
]