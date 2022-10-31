from django.urls import path
from . import views

app_name='cms'


urlpatterns = [
    #----------------First------------
	path('first_edit/',views.first_edit,name='first_edit'),
 
    #----------------Three------------
    path('list/threes/',views.list_three,name='three_list'),
    path('three/', views.three_view,name='three_asli'),
    path('detail/three/<int:id>',views.detail_three_asli,name='three_detail'),
    path('delete/three/<int:id>',views.three_asli,name='three_delete'),
    
    #----------------Team------------
    path('list/teams/',views.list_team,name='team_list'),
    path('team/', views.team_view,name='team_asli'),
    path('detail/team/<int:id>',views.detail_team_asli,name='team_detail'),
    path('delete/team/<int:id>',views.team_asli,name='team_delete'),
    
    #----------------Company------------
    path('list/companys/',views.list_company,name='company_list'),
    path('companys/',views.company_view,name='company_asli'),
    path('detail/company/<int:id>',views.detail_company_asli,name='company_detail'),
    path('delete/company/<int:id>',views.company_asli,name='company_delete'),
    
    #----------------OurShop------------
    path('list/ourshops/',views.list_ourshop,name='ourshop_list'),
    path('ourshop/', views.ourshop_view,name='ourshop_asli'),
    path('detail/ourshop/<int:id>',views.detail_ourshop_asli,name='ourshop_detail'),
    path('delete/ourshop/<int:id>',views.ourshop_asli,name='ourshop_delete'),
    
    #----------------ContactUs------------
    path('list/contactuss/',views.list_contactus,name='contactus_list'),
    path('detail/contactus/<int:id>',views.detail_contactus_asli,name='contactus_detail'),
    path('delete/contactus/<int:id>',views.contactus_asli,name='contactus_delete'),
    
    #----------------ContactUsDetail------------
    path('contactusdetail_edit/',views.contactusdetail_edit,name='contactusdetail_edit'),

    #----------------KhabarName------------
    path('list/khabarnames/',views.list_khabarname,name='khabarname_list'),
    path('khabarname/', views.khabarname_view,name='khabarname_asli'),
    path('detail/khabarname/<int:id>',views.detail_khabarname_asli,name='khabarname_detail'),
    path('delete/khabarname/<int:id>',views.khabarname_asli,name='khabarname_delete'),
    
    #--------------USER---------------------
    path('list/user/',views.UserView,name='UserView'),
    path('CreateUser/',views.CreateUser,name='CreateUser'),
    path('detail/user/<id>/',views.detail_user,name='detail_user'),
    path('delete/user/<id>/',views.DeleteUser,name='DeleteUser'),
    
    #-----------------footer list----------
    path('list/footers/',views.list_footer,name='footer_list'),
    
    #-----------------footer asli----------
    path('footerasli/', views.footer_asli_view,name='footer_asli'),
    path('detail/footerasli/<int:id>',views.detail_footer_asli,name='footer_asli_detail'),
    path('delete/footerasli/<int:id>',views.delete_footer_asli,name='footer_asli_delete'),
    
    #-----------------footer zir----------
    path('footerzir/', views.footer_zir_view,name='footer_zir'),
    path('detail/footerzir/<int:id>/', views.detail_footer_zir,name='footer_zir_detail'),
    path('delete/footerzir/<int:id>',views.delete_footer_zir,name='footer_zir_delete'),
    
    #-----------------navbar----------
    path('navlist/',views.list_nav,name='nav_list'),
    path('navone/',views.nav_one_view,name='navone'),
    path('detail/navone/<int:id>',views.detail_nav_one,name='detail_nav_one'),
    path('delete/navone/<int:id>',views.delete_nav_one,name='delete_nav_one'),
    path('navtwo/',views.nav_two_view,name='navtwo'),
    path('detail/navtwo/<int:id>',views.detail_nav_two,name='detail_nav_two'),
    path('delete/navtwo/<int:id>',views.delete_nav_two,name='delete_nav_two'),
    path('navthree/',views.nav_three_view,name='navthree'),
    path('detail/navthree/<int:id>',views.detail_nav_three,name='detail_nav_three'),
    path('delete/navthree/<int:id>',views.delete_nav_three,name='delete_nav_three'),
    
    #----------------SITESETTING--------
    path('detail_site_setting/',views.detail_site_setting,name='detail_site_setting'),
    
    #-----------------SLIDERS----------
    path('slider_list/',views.slider_listview,name='slider_listview'),
    path('slider_add/',views.slider_add_view,name='slider_add_view'),
    path('detail_Slider/<id>/',views.detail_Slider,name='detail_Slider'),
    path('delete_slider/<id>/',views.Delete_Slider,name='Delete_Slider'),
    
    #---------------Tabligh----------------
    path('tabligh_list/',views.Tabligh_listview,name='tabligh_list'),
    path('tabligh/',views.tabligh_view,name='tabligh'),
    path('tabligh_detail/<id>/',views.detail_Tabligh,name='detail_Tabligh'),
    path('delete_tabligh/<id>/',views.Delete_tabligh,name='Delete_tabligh'),
    
    #-----------------TAGNEWPAGE----------------------
    path('tag_list/',views.TagNewPages_listview,name='TagNewPages_listview'),
    path('detail_tagnewpages/<id>/',views.detail_tagnewpages,name='detail_tagnewpages'),
    path('Delete_NewTagPage/<id>/',views.Delete_NewTagPage,name='Delete_NewTagPage'),
    path('New_Tag_Page_Add/',views.New_Tag_Page_Add,name='New_Tag_Page_Add'),
    
    #---------------TAGFOOTER-------------
    path('TagFooter_listview/',views.TagFooter_listview,name='TagFooter_listview'),
    path('tag_footer_add/',views.tag_footer_add,name='tag_footer_add'),
    path('detail_tag_footer/<id>/',views.detail_tag_footer,name='detail_tag_footer'),
    path('delete_tag_footer/<id>/',views.delete_tag_footer,name='delete_tag_footer'),
    
    #----------------Tag_navbar------------
    path('Tag_navbar/',views.Tag_navbar_view,name='Tag_navbar'),
    path('Tag_navbar_list/',views.Tag_navbar_listview,name='listview_navbar'),
    path('Tag_navbar_detail/<id>/',views.detail_tag_navbar,name='tag_detail'),
    path('delete/<id>/',views.Delete,name='Delete'),
    
    #----------------ZirSlider--------
    path('zirslider_edit/',views.zirslider_edit,name='zirslider_edit'),
    
    #----------------category------------
    path('list/categorys/',views.list_category,name='category_list'),
    path('categorys/',views.category_view,name='category_asli'),
    path('detail/category/<int:id>',views.detail_category_asli,name='category_detail'),
    path('delete/category/<int:id>',views.category_asli,name='category_delete'),
    
    #----------------zircategory------------
    path('list/zircategorys/',views.list_zircategory,name='zircategory_list'),
    path('zircategorys/',views.zircategory_view,name='zircategory_asli'),
    path('detail/zircategory/<int:id>',views.detail_zircategory,name='zircategory_detail'),
    path('delete/zircategory/<int:id>',views.delete_zircategory,name='zircategory_delete'),

    #---------------tags-------------
    path('tags_listview/',views.tags_listview,name='tags_listview'),
    path('tags_add/',views.tags_add,name='tags_add'),
    path('detail_tags/<id>/',views.detail_tags,name='detail_tags'),
    path('delete_tags/<id>/',views.delete_tags,name='delete_tags'),
    
    #--------------- products -------------
    path('list/product/',views.product_list,name='product_list'),
    path('product/',views.product_view,name='product_view'),
    path('detail/product/<id>/',views.product_detail,name='product_detail'),
    path('delete_product/<id>/',views.delete_product,name='delete_product'),
    path('product_zircat_ajax',views.product_zircat_ajax,name='product_zircat_ajax'),
    path('product_add_size',views.product_add_size,name='product_add_size'),
    path('product_add_color',views.product_add_color,name='product_add_color'),
    path('product_add_image',views.product_add_image,name='product_add_image'),
    path('product_changealt_ajax',views.product_changealt_ajax,name='product_changealt_ajax'),
    path('search_name/',views.search_name,name='search_name'),
    
    
    #--------------- comment -------------
    
    path('comment_listview/',views.comment_listview,name='comment_listview'),
    path('detail_comment/<id>/',views.detail_comment,name='detail_comment'),
    path('delete_comment/<id>/',views.delete_comment,name='delete_comment'),    

]