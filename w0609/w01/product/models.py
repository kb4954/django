from django.db import models

# class Product(models.Model):
#     code = models.AutoField()
#     name = models.CharField(max_length=32, verbose_name = '상품명')
#     upcategory = models.CharField(max_length=50)
#     lowcategory = models.CharField(max_length=50)
#     origin = models.CharField(max_length=100, verbose_name='원산지')
#     weight = models.DecimalField(max_digits=5,decimal_places=2)
#     # DecimalField: 숫자표현 , max_digits: 숫자에 허용되는 최대 자리수 , decimal_places: 숫자와 함께 저장할 소수 자릿수
#     consumer_price = models.PositiveIntegerField(verbose_name='소비자가격')
#     discount_price = models.PositiveIntegerField(verbose_name='할인가')
#     stock = models.PositiveIntegerField(verbose_name='재고')
    