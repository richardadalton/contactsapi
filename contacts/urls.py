from django.conf.urls import url, include
from contacts import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Contact API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'contacts', views.ContactViewSet, base_name='contacts')
router.register(r'users', views.UserViewSet, base_name='users')

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', schema_view),
]