from django.contrib import admin
from django.urls import path,include

from USER_AUTH import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),

	path('',views.home,name='home'),
	path('signup',views.signup,name='signup'),
	path('secret',views.secret_page,name="secret"),
	path('profile',views.profile,name="profile"),


]
