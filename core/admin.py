from django.contrib import admin # type: ignore
from .models import Pessoa

admin.site.register(Pessoa)
