from .serializers import ContactSerializer
from rest_framework import viewsets
from .models import Contact

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer