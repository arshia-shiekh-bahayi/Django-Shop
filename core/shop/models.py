from django.db import models

class ProductStatusType(models.IntegerChoices):
    publish = 1 , ("نمایش")
    draft = 2 , ("عدم نمایش")
    



class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    
    create_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class ProductModel(models.Model):
    user = models.ForeignKey("accounts.User",on_delete=models.PROTECT)
    category = models.ManyToManyField(ProductCategoryModel)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    image = models.ImageField(default='/default/product-image.png', upload_to='product/img/')
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=ProductStatusType.choices,default=ProductStatusType.draft)
    price= models.DecimalField(default=0,max_digits=None,decimal_places=0)
    discount_percent = models.IntegerField(default=0)
    
    create_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
class ProductImageModel(models.Model):
    product = models.ForeignKey("accounts.User",on_delete=models.CASCADE)
    file = models.ImageField(upload_to='product/extra-img/') 
    
    create_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)   
    