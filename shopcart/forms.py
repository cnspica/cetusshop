# -*- coding:utf-8 -*-
from django import forms
from shopcart.models import MyUser,Address,Product,Inquiry,OrderShippment,Email,Article,Express,ExpressType,Category
from captcha.fields import CaptchaField
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError 	
		

#只验证captcha字段的form
class captcha_form(forms.Form):
	#暂时什么都不校验
	#captcha = CaptchaField()
	pass

class register_form(forms.ModelForm):
	#captcha = CaptchaField(),新版暂时不要验证码
	class Meta:
		model = MyUser
		fields = ('email','password','first_name','last_name')

class user_info_form(forms.ModelForm):
	#captcha = CaptchaField(),新版暂时不要验证码
	password = forms.CharField(required=False)
	class Meta:
		model = MyUser
		fields = ('password','first_name','last_name') 
		
class address_form(forms.ModelForm):
	tel = forms.CharField(required=False)
	mobile = forms.CharField(required=False)
	sign_building = forms.CharField(required=False)
	useage = forms.CharField(required=False)
	class Meta:
		model = Address
		fields = ('useage','is_default','first_name','last_name','country','province','city','district','address_line_1','address_line_2','zipcode','tel','mobile','sign_building') 

class product_add_form(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('item_number','name')
		
class product_basic_info_form(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('item_number','name','is_publish','price','market_price','quantity','min_order_quantity')
		
class article_basic_info_form(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('title','category')	
		
class article_detail_info_form(forms.ModelForm):
	content = forms.CharField(required=False)
	keywords = forms.CharField(required=False)
	page_title = forms.CharField(required=False)
	short_desc = forms.CharField(required=False)
	static_file_name = forms.CharField(required=False)
	detail_template = forms.CharField(required=False)
	breadcrumbs = forms.CharField(required=False)
	class Meta:
		model = Product
		fields = ('content','keywords','page_title','short_desc','static_file_name','breadcrumbs','detail_template')		
		
class product_detail_info_form(forms.ModelForm):
	keywords = forms.CharField(required=False)
	page_title = forms.CharField(required=False)
	static_file_name = forms.CharField(required=False)
	detail_template = forms.CharField(required=False)
	short_desc = forms.CharField(required=False)
	description = forms.CharField(required=False)
	class Meta:
		model = Product
		fields = ('keywords','page_title','static_file_name','detail_template','short_desc','description')

class order_shippment_form(forms.ModelForm):		
	shipper_name = forms.CharField(required=False)
	ship_no = forms.CharField(required=False)
	shipping_cost = forms.CharField(required=False)
	shipping_time = forms.CharField(required=False)
	remark = forms.CharField(required=False)
	country = forms.CharField(required=False)
	province = forms.CharField(required=False)
	city = forms.CharField(required=False)
	district = forms.CharField(required=False)
	address_line_1 = forms.CharField(required=False)
	address_line_2 = forms.CharField(required=False)
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	zipcode = forms.CharField(required=False)
	tel = forms.CharField(required=False)
	class Meta:
		model = OrderShippment
		fields = ('shipper_name','ship_no','shipping_cost','shipping_time','remark','country','province','city','district','address_line_1','address_line_2','first_name','last_name','zipcode','tel')
	
class email_form(forms.ModelForm):		
	useage_name = forms.CharField(required=False)
	is_send = forms.CharField(required=False)
	email_address = forms.CharField(required=False)
	title = forms.CharField(required=False)
	smtp_host = forms.CharField(required=False)
	username = forms.CharField(required=False)
	password = forms.CharField(required=False)
	template = forms.CharField(required=False)
	template_file = forms.CharField(required=False)
	class Meta:
		model = Email
		fields = ('useage_name','is_send','email_address','title','smtp_host','username','password','template','template_file')

class category_simple_form(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('name','code')
		
class category_form(forms.ModelForm):
	name = forms.CharField(required=False)
	code = forms.CharField(required=False)
	page_title = forms.CharField(required=False)
	keywords = forms.CharField(required=False)
	short_desc = forms.CharField(required=False)
	sort_order = forms.CharField(required=False)
	detail_template = forms.CharField(required=False)
	category_template = forms.CharField(required=False)
	static_file_name = forms.CharField(required=False)
	class Meta:
		model = Category
		fields = ('name','code','page_title','keywords','short_desc','sort_order','detail_template','category_template','static_file_name')

class express_form(forms.ModelForm):
	class Meta:
		model = Express
		fields = ('name','is_in_use','price_fixed')	

class express_type_form(forms.ModelForm):
	class Meta:
		model = ExpressType
		fields = ('name','is_in_use','price_fixed')			
	
class inquiry_form(forms.ModelForm):
	company = forms.CharField(required=False)
	class Meta:
		model = Inquiry
		fields = ('name','company','email','message')