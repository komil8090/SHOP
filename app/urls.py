# from django.urls import path,include
# from .views import index


# app_name = 'app'

# urlpatterns = [
#     path('', index, name='index'),
#     path('products/', include('app.product_urls'))
# ]



from django.urls import path, include
from .views import index, detail


app_name = 'app'  # ← this must match 'app' in 'app:index'

urlpatterns = [
    path('', index, name='index'),
    path('detail<int:product_id>/', detail, name='detail'),
]
