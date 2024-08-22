from django.urls import path

from . import views

app_name = "accounts"  # アプリケーションの名前空間を設定

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
]
