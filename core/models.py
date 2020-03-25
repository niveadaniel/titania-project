from django.db import models


class Tower(models.Model):
    number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        db_table = 'tower'
        verbose_name = 'Bloco'
        verbose_name_plural = 'Blocos'


class OwnerContractType(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'owner_contract_type'
        verbose_name = 'Tipo de Contrato'
        verbose_name_plural = 'Tipos de Contratos'


class OwnerSituation(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'owner_situation'
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'


class VehicleType(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'vehicle_type'
        verbose_name = 'Tipo de Veiculo'
        verbose_name_plural = 'Tipos de Veiculos'


class Owner(models.Model):
    name = models.CharField(null=True, blank=True, max_length=70)
    owner_code = models.CharField(null=True, blank=True, max_length=10)
    tower = models.ForeignKey(Tower,  on_delete=models.DO_NOTHING, null=True, blank=True)
    apartment = models.IntegerField(null=True, blank=True)
    residents = models.IntegerField(null=True, blank=True)
    contract_type = models.ForeignKey(OwnerContractType, on_delete=models.DO_NOTHING, null=True, blank=True)
    situation = models.ForeignKey(OwnerSituation, on_delete=models.DO_NOTHING, null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=15)
    cell_phone = models.CharField(null=True, blank=True, max_length=15)
    email = models.EmailField(null=True, blank=True)
    vehicle_type_1 = models.ForeignKey(VehicleType, on_delete=models.DO_NOTHING, related_name='vehicle_type_1', null=True, blank=True)
    vehicle_brand_1 = models.CharField(null=True, blank=True, max_length=30)
    vehicle_model_1 = models.CharField(null=True, blank=True, max_length=30)
    license_plate_1 = models.CharField(null=True, blank=True, max_length=8)
    vehicle_type_2 = models.ForeignKey(VehicleType, on_delete=models.DO_NOTHING, related_name='vehicle_type_2', null=True, blank=True)
    vehicle_brand_2 = models.CharField(null=True, blank=True, max_length=30)
    vehicle_model_2 = models.CharField(null=True, blank=True, max_length=30)
    license_plate_2 = models.CharField(null=True, blank=True, max_length=8)
    notes = models.TextField(null=True, blank=True, max_length=400)

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)

    class Meta:
        db_table = 'apartment_owner'
        verbose_name = 'Propretário'
        verbose_name_plural = 'Proprietários'


class Notification(models.Model):
    title = models.CharField(null=True, blank=True, max_length=40)
    description = models.CharField(null=True, blank=True, max_length=200)
    notification = models.TextField(null=True, blank=True, max_length=1000)
    created_date = models.DateTimeField(null=True, blank=True)
    author = models.CharField(null=True, blank=True, max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'notification'
        verbose_name = 'Aviso'
        verbose_name_plural = 'Avisos'