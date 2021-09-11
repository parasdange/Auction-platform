

from django.urls import path

from . import views


app_name="bidder"

urlpatterns=[

path('viewproduct/<int:id>',views.viewproduct,name="view_product"),

path('buy_product/',views.buy_product),

path('userprofile/',views.userprofile),

# path('bid_product/<int:id>',views.bid_product,name="bid_product"),

path('bid_update/<int:id>',views.bid_update,name="bid_update"),

path('bid_approve/<int:id>',views.bid_approve,name="bid_approve"),

path('win_proceed/<int:id>',views.win_proceed,name="win_proceed"),

path('category_edit/<int:id>',views.category_edit,name='category_edit'),

path('category_delete/<int:id>',views.category_delete,name='category_delete'),

path('auction_list/',views.auction_list),

path('admin_delete_product/<int:id>',views.admin_delete_product,name="admin_delete_product"),

path('add_new_user/',views.add_new_user),

path('user_list/',views.user_list),

path('user_delete/<int:id>',views.user_delete,name="user_delete"),

path('admin_update_detail/',views.admin_update_detail),

path('log_out/',views.log_out),
]




