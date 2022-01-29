from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.

class Categorias(models.TextChoices):
    TECH = 'TEC', 'Tecnologia'
    GR = 'GR', 'Geral'
    OT = 'OT', 'Outros'

class Posts(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=3,
        choices=Categorias.choices,
        default=Categorias.GR,
    )
    deleted = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)


#essa função define o titulo no admin
    def __str__(self):
        return self.title

    def full_name(self):
     return self.title + self.sub_title

    def get_caterory(self):
     return self.categories.get_categories_display()

    
    full_name.admin_order_field = 'title'





