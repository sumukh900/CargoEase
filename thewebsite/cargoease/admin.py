from django.contrib import admin
from .models import User
from .models import Carrier
from .models import Route
from .models import Container
from .models import Carrier_details




admin.site.register(User)
admin.site.register(Carrier)
admin.site.register(Route)
admin.site.register(Container)
admin.site.register(Carrier_details)