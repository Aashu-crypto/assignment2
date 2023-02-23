
from django.urls import path,include
from main import views

urlpatterns = [
    
    path('', views.index,name = 'home'),
    
    path('login/', views.loginPage,name = 'login'),
    path('register/', views.register,name = 'register'),
    path('logout/', views.logoutUser,name = 'logout'),
    path('products/', views.products,name = 'products'),
    path('page2/', views.page2,name = 'page2'),
    path('page3/', views.page3,name = 'page3'),
    path('page4/', views.page4,name = 'page4'),
    path('page5/', views.page4,name = 'page5'),
    
]
