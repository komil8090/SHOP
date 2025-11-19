# from django.urls import path,include
# from .views import index


# app_name = 'app'

# urlpatterns = [
#     path('', index, name='index'),
#     path('products/', include('app.product_urls'))
# ]



# from django.urls import path, include
# from .views import index, detail


# app_name = 'app'  # ← this must match 'app' in 'app:index'

# urlpatterns = [
#     path('', index, name='index'),
#     path('category/<int:category_id>/', index, name='category'),
#     path('detail/<int:product_id>/', detail, name='detail'),
    
# ]



from django.urls import path,include
from .views import create_order, index, detail, create_product, delete_product, update_product, comment_list



app_name = 'app'

urlpatterns = [
    path('',index,name='index'),
    path('category/<int:category_id>',index,name='products_of_category'),
    path('product/<int:pk>/', detail, name='detail'),
    path('create/',create_product,name='create'),
    path('delete/<int:pk>',delete_product,name='delete'),
    path("edit/<int:product_id>/",update_product, name="update"),
    path('detail/<int:pk>/orders/',create_order,name='create_order'),
    path('product/<int:pk>/', detail, name='detail'),
]


