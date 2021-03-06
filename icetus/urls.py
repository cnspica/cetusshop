"""imycart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns("",
	url(r'^$', 'shopcart.index.view_index',name='view_index'),
	url(r'^refresh-captcha$', 'shopcart.index.refresh_captcha',name='refresh_captcha'),	
	url(r'^user/register$', 'shopcart.myuser.register',name='myuser_register'),
	url(r'^user/login/$', 'shopcart.myuser.login',name='myuser_login'),
	url(r'^user/logout/$', 'shopcart.myuser.logout',name='myuser_logout'),
	url(r'^user/forget-password$', 'shopcart.myuser.forget_password',name='myuser_forget_password'),
	url(r'^user/reset-password$', 'shopcart.myuser.reset_password',name='myuser_reset_password'),
	url(r'^user/info/$', 'shopcart.myuser.info',name='myuser_info'),
	url(r'^user/address/opration/(.+)/(.+)/$', 'shopcart.myuser.address',name='myuser_address'),
	url(r'^user/address/opration/(.+)/$', 'shopcart.myuser.address',name='myuser_address'),
	url(r'^user/address/detail/(.+)/$', 'shopcart.myuser.address_detail',name='myuser_address_detail'),
	url(r'^user/address/show/$', 'shopcart.myuser.address_list',name='myuser_address_list'),
	url(r'^validate/user/(.+)/$', 'shopcart.validate.ajax_validate_user',name='validate_ajax_validate_user'),
	url(r'^cart/add$', 'shopcart.cart.add_to_cart',name='cart_add_to_cart'),
	url(r'^cart/modify$', 'shopcart.cart.ajax_modify_cart',name='cart_ajax_modify_cart'),
	url(r'^cart/show/$', 'shopcart.cart.view_cart',name='cart_view_cart'),
	url(r'^cart/check-out$', 'shopcart.cart.check_out',name='cart_check_out'),
	url(r'^cart/re-calculate-price/$', 'shopcart.cart.re_calculate_price',name='re_calculate_price'),
	url(r'^cart/place-order$', 'shopcart.order.place_order',name='order_place_order'),
	url(r'^cart/payment/(\d+)/$', 'shopcart.order.payment',name='order_payment'),
	url(r'^order/show/$', 'shopcart.order.show_order',name='order_show_order'),
	url(r'^order/show/(\d+)/$', 'shopcart.order.order_detail',name='order_order_detail'),
	url(r'^order/cancel$', 'shopcart.order.ajax_cancel_order',name='order_ajax_cancel_order'),
	url(r'^order-remark/list/(\d+)/$', 'shopcart.order.list_order_remark',name='order_list_order_remark'),
	url(r'^attribute/group/info/(\d+)/$', 'shopcart.attribute.get_group_info',name='attribute_get_group_info'),
	
	url(r'^wishlist/$', 'shopcart.wishlist.view_wishlist',name='wishlist_view_wishlist'),
	url(r'^wishlist/add$', 'shopcart.wishlist.add_to_wishlist',name='wishlist_add_to_wishlist'),
	url(r'^wishlist/remove$', 'shopcart.wishlist.remove_from_wishlist',name='wishlist_remove_from_wishlist'),
	url(r'^category-list/(\d+)/$', 'shopcart.category.category_list',name='category_list'),
	
	url(r'^product/(\d+)/$', 'shopcart.product.detail',name='product_detail'),
	url(r'^category/(\d+)/$', 'shopcart.product.category',name='product_category'),
	url(r'^product/$', 'shopcart.product.view_list',name='product_view_list'),
	url(r'^product/get-product-extra/$', 'shopcart.product.ajax_get_product_info',name='product_ajax_get_product_info'),
	url(r'^product/get-product-description/(\d+)/$', 'shopcart.product.ajax_get_product_description',name='product_ajax_get_product_description'),
	url(r'^article/(\d+)/$', 'shopcart.article.detail',name='article_detail'),
	url(r'^blog/$', 'shopcart.article.view_blog_list',name='article_view_blog_list'),
	url(r'^captcha/', include('captcha.urls')),
	url(r'^ajax_val_captcha/$', 'shopcart.validate.ajax_validate_captcha',name='ajax_validate_captcha'),
	url(r'^paypal/', include('paypal.standard.ipn.urls')),
	url(r'^comments/', include('django_comments.urls')),
	url(r'^admin/file-upload/(.+)/(.+)/$', 'shopcart.myadmin.file.file_upload',name='admin_file_upload'),
	url(r'^file-delete/(.+)/(.+)/(.+)/$', 'shopcart.myadmin.file.file_delete',name='admin_file_delete'),
	url(r'^email-list/add/$', 'shopcart.emaillist.add_to_email_list',name='emaillist_add_to_email_list'),
	url(r'^query/product/$', 'shopcart.product.query_product_show',name='product_query_product_show'),

	url(r'^contact/show/$', 'shopcart.views.contact_page',name='views_contact_page'),
	url(r'^inquiry/add/$', 'shopcart.inquiry.add',name='inquiry.add'),
	url('^admin/ckediter/(.+)/(.+)/$', 'shopcart.myadmin.file.ckediter',name='admin_ckediter'),
	url('^admin/product/make-static/$', 'shopcart.myadmin.product.product_make_static',name='admin_product_make_static'),
	
	url('^admin/product/(.+)/(\d+)/$', 'shopcart.myadmin.product.product_opration',name='admin_product_opration'),
	url('^admin/article/make-static/$', 'shopcart.myadmin.article.article_make_static',name='admin_article_make_static'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^i18n/', include('django.conf.urls.i18n')),
	
	#以下是正式的admin url
	url('^myadmin/$', 'shopcart.myadmin.index.login',name='admin_index_login'),
	
	url('^admin/index/$', 'shopcart.myadmin.index.view',name='admin_index_view'),
	url('^admin/index-content/$', 'shopcart.myadmin.index.content_view',name='admin_index_content_view'),
	
	
	url('^admin/menu/$', 'shopcart.myadmin.index.menu_view',name='admin_index_menu_view'),
	#url('^admin/order/$', 'shopcart.myadmin.order.view',name='admin_order_view'),
	
	url('^admin/order-list/$', 'shopcart.myadmin.order.list_view',name='admin_order_list_view'),
	url('^admin/order-detail/(\d+)/$', 'shopcart.myadmin.order.detail',name='admin_order_detail'),
	url('^admin/order-remark-add/$', 'shopcart.myadmin.order.remark_add',name='admin_order_remark_add'),
	url('^admin/order-oper/$', 'shopcart.myadmin.order.oper',name='admin_order_oper'),
	url('^admin/order-shippment-manage/$', 'shopcart.myadmin.order.ship_out',name='admin_order_ship_out'),
	url('^admin/order-shippment-manage/delete/(\d+)/$', 'shopcart.myadmin.order.shipment_delete',name='admin_order_shipment_delete'),
	url('^admin/order-status/(.+)/(\d+)/$', 'shopcart.myadmin.order.modify_status',name='admin_modify_status'),
	
	url('^admin/article-list/$', 'shopcart.myadmin.article.list_view',name='admin_article_list_view'),
	url('^admin/article-delete/$', 'shopcart.myadmin.article.delete',name='admin_article_delete'),
	url('^admin/article-detail/(\d+)/$', 'shopcart.myadmin.article.detail',name='admin_article_detail'),
	url('^admin/article-edit/$', 'shopcart.myadmin.article.article_basic_edit',name='admin_article_basic_edit'),
	url('^admin/article-detail-manage/$', 'shopcart.myadmin.article.article_detail_info_manage',name='admin_article_detail_info_manage'),
	url('^admin/article-picture-manage/$', 'shopcart.myadmin.article.article_picture_manage',name='admin_article_picture_manage'),
	
	url('^admin/category-list/$', 'shopcart.myadmin.category.list_view',name='admin_category_list_view'),
	url('^admin/category-edit/$', 'shopcart.myadmin.category.edit',name='admin_category_edit'),
	url('^admin/category-detele/(\d+)/$', 'shopcart.myadmin.category.delete',name='admin_category_delete'),
	url('^admin/ajax_add_category/$', 'shopcart.myadmin.category.ajax_add_category',name='admin_category_ajax_add_category'),
	
	
	url('^admin/system-config/(.+)/$', 'shopcart.myadmin.system_config.view',name='admin_system_config_view'),
	url('^admin/pay-config/(.+)/$', 'shopcart.myadmin.system_config.pay_config',name='admin_system_config_pay_config'),
	
	url('^admin/site-config-manage/$', 'shopcart.myadmin.system_config.site_config_manage',name='admin_site_config_manage'),
	url('^admin/display-config-manage/$', 'shopcart.myadmin.system_config.display_config_manage',name='admin_display_config_manage'),
	url('^admin/email-config-manage/$', 'shopcart.myadmin.system_config.email_config_manage',name='admin_email_config_manage'),
	
	url('^admin/delivery-type-list/$', 'shopcart.myadmin.delivery.type_list_view',name='admin_delivery_type_list_view'),
	url('^admin/delivery-type-edit/$', 'shopcart.myadmin.delivery.type_edit',name='admin_delivery_type_edit'),
	url('^admin/delivery-type-delete/(\d+)/$', 'shopcart.myadmin.delivery.type_delete',name='admin_type_delete'),
	url('^admin/express-list/$', 'shopcart.myadmin.delivery.express_list_view',name='admin_express_list_view'),
	url('^admin/express-edit/$', 'shopcart.myadmin.delivery.express_edit',name='admin_express_edit'),
	url('^admin/express-delete/(\d+)/$', 'shopcart.myadmin.delivery.express_delete',name='admin_express_delete'),
	
	
	url('^admin/no-permission/$', 'shopcart.myadmin.index.no_permission',name='admin_no_permission'),
	url('^admin/product-oper/$', 'shopcart.myadmin.product.oper',name='admin_product_oper'),
	url('^admin/product/$', 'shopcart.myadmin.product.product_list',name='admin_product_list'),
	url('^admin/product-edit/$', 'shopcart.myadmin.product.product_basic_edit',name='admin_product_basic_edit'),
	url('^admin/product-detail-manage/$', 'shopcart.myadmin.product.product_detail_info_manage',name='admin_product_detail_info_manage'),
	url('^admin/product-picture-manage/$', 'shopcart.myadmin.product.product_picture_manage',name='admin_product_picture_manage'),
	url('^admin/product-sku-manage/(\d+)/$', 'shopcart.myadmin.product.product_sku_manage',name='admin_product_sku_manage'),
	url('^admin/product-sku-delete/(\d+)/$', 'shopcart.myadmin.product.product_sku_delete',name='admin_product_sku_delete'),
	url('^admin/product-sku-attribute-manage/$', 'shopcart.myadmin.product.product_sku_attribute_manage',name='admin_product_sku_attribute_manage'),
	
	
	#下面是初始化方法
	url(r'^initdb/$', 'shopcart.views.init_database',name='init_database'),
	
	#优惠码
	url(r'^promotion/$', 'shopcart.promotion.calculate',name='promotion_calculate'),
	#URL解析器
	url(r'(.*\.html)$','shopcart.views.url_dispatch',name='url_dispatch'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
