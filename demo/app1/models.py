from django.db import models


# Create your models here.

class Employee(models.Model):

    def nameFile(instance, filename):
        return '/'.join(['file docs', str(instance.char_field), filename])


    char_field = models.CharField(max_length=100, null=True)
    text_field = models.TextField(null=True)
    integer_field = models.IntegerField(max_length=50, null=True)
    float_field = models.FloatField(max_length=40, null=True)
    ip_address = models.GenericIPAddressField( protocol='both', unpack_ipv4=False,null=True)
    date_field = models.DateField(auto_now=True, null=True)
    datetime_field = models.DateTimeField(auto_now=True, null=True)
    decimal_field = models.DecimalField(max_digits=19, decimal_places=10, null=True)
    email_field = models.EmailField(max_length=254, null=True)
    file_field = models.FileField(upload_to='nameFile', blank=True, null=True)

    def __str__(self):
        return f"{self.char_field}--{self.text_field}--{self.integer_field}--{self.float_field}--{self.ip_address}--{self.date_field}--{self.datetime_field}--{self.decimal_field}--{self.email_field}--{self.file_field}"
