from django.urls import path
from. import views
urlpatterns = [
    
    #path('', views.home, name="home"),
    # path('signup/', views.signup, name="signup"),
    # path('login/', views.login_view, name="login"),  # Correct function name
    # path('logout/', views.logout_view, name="logout"),  # Use custom logout view
    # path('cart/', views.cart, name="cart"),
    # path('items/', views.items, name="items"),
    # path('profile/', views.profile, name="profile"),
    #path('account/', views.account, name="account"),
    path('home',views.home),
    path('account', views.account),
    path('order',views.order),
    path('cart', views.cart),
    path('decor', views.decor),
    path('elec', views.elec),
    path('beauty', views.beauty),
    path('jwel', views.jwel),
    path('sports', views.sports),
    path('cloth', views.cloth),
    path('signup', views.signup),
    path('sign', views.sign),
    path('login', views.login),
    path('log', views.log),
    path('show', views.show),
    path('del/<int:id>',views.dele),
    path('edit/<int:id>',views.edit),
    path('edcode/<int:id>',views.edcode),
    
]
