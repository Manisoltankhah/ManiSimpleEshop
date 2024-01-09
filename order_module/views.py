import time

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from order_module.models import Order, OrderDetail
from product_module.models import Product
from django.shortcuts import redirect
import requests
import json

MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "نهایی کردن خرید شما از سایت ما"  # Required
email = ''  # Optional
mobile = ''  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8080/order/verify-payment/'


def add_product_to_shopping_cart(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    if count < 1:
        return JsonResponse({
            "status": "invalid Number",
            'text': 'مقدار وارد شده معتبر نیست',
            'confirm_button_text': 'باشه',
            'icon': 'warning'
        })
    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            # todo: get current user open cart
            current_cart, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_cart_detail = current_cart.orderdetail_set.filter(product_id=product_id).first()
            if current_cart_detail is not None:
                current_cart_detail.count += count
                current_cart_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_cart.id, product_id=product_id, count=count)
                new_detail.save()

            # todo: add product to cart
            return JsonResponse({
                'status': 'successful',
                'text': 'محصول با موفقیت به سبد خرید شما اضافه شد',
                'confirm_button_text': 'متوجه شدم',
                'icon': 'success'
            })
        else:
            return JsonResponse({
                'status': 'Product Not Found',
                'text': 'محصول یافت نشد',
                'confirm_button_text': 'متوجه شدم',
                'icon': 'error'
            })
    else:
        return JsonResponse({
            'status': 'user is not authenticated',
            'text': 'قبل از سفارش در سایت ثبت نام کنید یا وارد شوید',
            'confirm_button_text': 'ورود به سایت',
            'icon': 'error'
        })


@login_required
def request_payment(request: HttpRequest):
    current_cart, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_cart.calculate_total_price()
    if total_price == 0:
        return redirect(reverse('user-cart'))

    req_data = {
        "merchant_id": MERCHANT,
        "amount": total_price * 10,
        "callback_url": CallbackURL,
        "description": description,
        # "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json", "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


@login_required
def verify_payment(request: HttpRequest):
    current_cart, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_cart.calculate_total_price()
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json", "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": total_price * 10,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                current_cart.is_paid = True
                current_cart.payment_date = time.time()
                current_cart.save()
                ref_str = str(req.json()['data']['ref_id'])
                return render(request, 'order_module/payment_result.html', {
                    'success': f'تراکنش شما با کد پیگیری {ref_str} با موفقیت انجام شد'
                })
            elif t_status == 101:
                return render(request, 'order_module/payment_result.html', {
                    'info': 'این تراکنش قبلا انجام و ثبت شده است'
                })
            else:
                return render(request, 'order_module/payment_result.html', {
                    'error': str(req.json()['data']['message'])
                })
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            # return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
            return render(request, 'order_module/payment_result.html', {
                'error': f"Error code: {e_code}, Error Message: {e_message}"
            })
    else:
        return render(request, 'order_module/payment_result.html', {
            'error': 'پرداخت با خطا مواجه شده یا کاربر از پرداخت انصراف داده'
        })





















