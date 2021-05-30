from .merchandise_admin import *
from .owner_admin import *
from .category_admin import *
from .item_admin import *
from .billing_admin import *
from .user_admin import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)