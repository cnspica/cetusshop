#coding=utf-8
from django.shortcuts import render,redirect,render_to_response
from shopcart.models import System_Config
from shopcart.utils import get_system_parameters
from django.core.context_processors import csrf
from shopcart.forms import inquiry_form
from django.http import HttpResponse,JsonResponse
from django.utils.translation import ugettext as _
from django.http import Http404
from shopcart import signals
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger('icetus.shopcart')

# Create your views here.
def add(request):
	ctx = {}
	ctx.update(csrf(request))
	ctx['system_para'] = get_system_parameters()
	ctx['page_name'] = 'Inquiry'

	result_dict = {}
	
	if request.method == 'POST':
		form = inquiry_form(request.POST) # 获取Post表单数据
		if form.is_valid():# 验证表单
			inquiry = form.save()
			#logger.debug('request.META:%s' % request.META)
			
			if 'HTTP_X_FORWARDED_FOR' in request.META:
				ip =  request.META['HTTP_X_FORWARDED_FOR']
				logger.debug('There is HTTP_X_FORWARDED_FOR in request.META,ip is:%s' % ip)
			else:  
				ip = request.META['REMOTE_ADDR']
				logger.debug('Get ip from REMOTE_ADDR is:%s' % ip)
			
			inquiry.ip_address = ip
			inquiry.save()
			
			result_dict['success'] = True
			result_dict['message'] = _('Your inquiry was submitted and will be responded to as soon as possible. Thank you for contacting us.')
			
			#触发用户注册成功的事件
			signals.inquiry_received.send(sender='Inquiry',inquiry=inquiry)
		else:
			result_dict['success'] = False
			result_dict['message'] = _('Opration faild.')

		return JsonResponse(result_dict)
