from django.db import models
from account_module.models import User
from product_module.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name="نهایی شده / نشده")
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return f'{self.user}'

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for cart_detail in self.orderdetail_set.all():
                total_amount += cart_detail.final_price.price * cart_detail.count
        else:
            for cart_detail in self.orderdetail_set.all():
                total_amount += cart_detail.product.price * cart_detail.count
        return total_amount


    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = "سبد های خرید"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True,verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def __str__(self):
        return f'{self.order}'

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = "لیست جزییات سبد های خرید"