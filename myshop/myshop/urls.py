from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('shop.urls', namespace='shop')),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # change password urls
    path('accounts/password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('accounts/password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',	auth_views.PasswordResetView.as_view(),	name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),	name='password_reset_done'),
    path('reset/<uidb64>/<token>/',	auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',	auth_views.PasswordResetCompleteView.as_view(),	name='password_reset_complete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
