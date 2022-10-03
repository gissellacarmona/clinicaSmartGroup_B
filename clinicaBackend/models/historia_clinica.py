from django.db import models


class Historia_clinica(models.Model): 
    id = models.AutoField(primary_key=True)
    frec_cardiaca= models.CharField(max_length = 30)
    pres_arterial = models.CharField(max_length = 30)
    temperatura = models.CharField(max_length = 30)
    