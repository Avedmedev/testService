from django.urls import path
from myTest.views import *


urlpatterns = [
    path('', index, name='home'),
    path('myTest/index/', index, name='home'),
    
    path('myTest/to_test/', index, name='to_test'),
    path('myTest/watch_results/', index, name='watch_results'),
    
    path('myTest/regist/', RegisterUser.as_view(), name='regist'),
    path('myTest/log_in/', LoginUser.as_view(), name='log_in'),
    path('myTest/logout/', logout_user, name='logout'),
    # path('women/stars/', cache_page(60)(WomenStars.as_view()), name='stars'),
    #path('women/stars/', WomenStars.as_view(), name='stars'),
    #path('women/feed_back/', ContactFormView.as_view(), name='feed_back'),
    #path('women/add_post/', AddPage.as_view(), name='addpost'),
    #path('women/post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    # path('women/cat/<slug:cat_slug>', cache_page(60)(CatWomen.as_view()), name='cat'),
    #path('women/cat/<slug:cat_slug>', CatWomen.as_view(), name='cat'),

]
