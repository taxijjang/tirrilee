from django.db import models

class Posts(models.Model):
    product = models.CharField(max_length=30, name = "product")
    price = models.IntegerField(default=0, name = "price")

    CLASS_CHOICES = (
        ('SP','봄'),
        ('SU',"여름"),
        ('FA','가을'),
        ('WI','겨울'),
    )
    classification = models.CharField(max_length=2, choices= CLASS_CHOICES, name = "classification")
    product_image = models.ImageField(blank=True, upload_to='media/', default='media/base.jpg')
    writer = models.ForeignKey('users.Users',name='writer', on_delete=models.CASCADE)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name_plural = "상품"
