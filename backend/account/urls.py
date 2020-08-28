from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]

# djoser.urls
# /users/                                       ## creating users  method POST
# /users/me/                                    ## looking at current user method GET PUT PATCH DELETE
# /users/confirm/                               ## method POST
# /users/resend_activation/                     ## method POST
# /users/set_password/                          ## method POST
# /users/reset_password/                        ## method POST
# /users/reset_password_confirm/                
# /users/set_username/                          ## aka set_email method POST
# /users/reset_username/                        ## aka reset_email method POST # not configured 
# /users/reset_username_confirm/                ## not configured
# /token/login/ (Token Based Authentication)
# /token/logout/ (Token Based Authentication)

