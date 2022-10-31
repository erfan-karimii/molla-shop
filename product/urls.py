from django.urls import path
from . import views

app_name='product'


urlpatterns = [
	path('listview/',views.listView,name='listview'),
	path('compare_listview/<id>/<cat>',views.compare_listview,name='compare_listview'),
	path('detailview/<id>/',views.detailview,name='detailview'),
	path('compare/',views.compare,name='compare'),
	path('compare/<int:id>',views.compare_1,name='compare_1'),
	path('compare_2/<int:id>',views.compare_2,name='compare_2'),
	path('comment/',views.comment_view,name='comment'),
	path('size_name_ajax/',views.size_name_ajax,name='size_name_ajax'),
 
 
 
 
]