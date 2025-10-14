from django.db import models
from django.utils import timezone
import datetime 
# Create your models here.


class categoria (models.Model):
    categoria_text = models.CharField(max_length=150)
    def __str__(self):
        return self.categoria_text

class produto (models.Model):
    categoria = models.ForeignKey('categoria', on_delete=models.PROTECT)
    produto_text = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=3, decimal_places=2)
    pub_date = models.DateField('data de emissão do produto', default=timezone.now)
    def __str__(self):
        return self.produto_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)