from django.db import models

class UserModel(models.Model):
    users_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    uname = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.uname

class ProductDetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    stqty = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(UserModel, to_field='uname', on_delete=models.CASCADE, related_name='products')
    def __str__(self):
        return self.pname

class ProductAudit(models.Model):
    version = models.PositiveIntegerField()
    product = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    modifier = models.CharField(max_length=100)  # User who made the change
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of the change

    def __str__(self):
        return f"V{self.version} - {self.product.name}"
