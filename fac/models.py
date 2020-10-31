from django.db import models

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from sisfya.models import ClaseModelo, ClaseModelo2
from inv.models import Producto,Marca,UnidadMedida

class Cliente(ClaseModelo):
    NAT='Primario_Prepimario'
    JUR='Básico'
    TIPO_CLIENTE = [
        (NAT,'Primaria_Prepimaria'),
        (JUR,'Básico')
    ]
    nombre_centro = models.CharField(
        max_length=100
    )
    numero_centro = models.CharField(
        max_length=100
    )
    contacto = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    nivel=models.CharField(
        max_length=20,
        choices=TIPO_CLIENTE,
        default=NAT
    )

    def __str__(self):
        return '{} {}'.format(self.numero_centro,self.nombre_centro)

    def save(self):
        self.nombre_centro = self.nombre_centro.upper()
        self.numero_centro = self.numero_centro.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural = "Centros"

class Menu(ClaseModelo):
    
    nombre_menu = models.CharField(
        max_length=100
    )

    def __str__(self):
        return '{}'.format(self.nombre_menu)

    def save(self):
        self.nombre_menu = self.nombre_menu.upper()
        super(Menu, self).save()

    class Meta:
        verbose_name_plural = "Menus"

    
class FacturaEnc(ClaseModelo2):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.id)

    def save(self):
        self.total = self.sub_total - self.descuento
        super(FacturaEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Facturas"
        verbose_name="Encabezado Factura"
        permissions = [
            ('sup_caja_facturaenc','Permisos de Supervisor de Caja Encabezado')
        ]
    

class FacturaDet(ClaseModelo2):
    factura = models.ForeignKey(FacturaEnc,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad_menu = models.FloatField(default=0)
    total_alumnos= models.FloatField(default=0)
    cantidad=models.BigIntegerField(default=0)
    precio=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.cantidad = int(int(float(self.cantidad_menu)) * int(self.total_alumnos))/40
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio))
        self.total = self.sub_total - float(self.descuento)
        super(FacturaDet, self).save()
    
    class Meta:
        verbose_name_plural = "Detalles Facturas"
        verbose_name="Detalle Factura"
        permissions = [
            ('sup_caja_facturadet','Permisos de Supervisor de Caja Detalle')
        ]


@receiver(post_save, sender=FacturaDet)
def detalle_fac_guardar(sender,instance,**kwargs):
    factura_id = instance.factura.id
    producto_id = instance.producto.id

    enc = FacturaEnc.objects.get(pk=factura_id)
    if enc:
        sub_total = FacturaDet.objects \
            .filter(factura=factura_id) \
            .aggregate(sub_total=Sum('sub_total')) \
            .get('sub_total',0.00)
        
        descuento = FacturaDet.objects \
            .filter(factura=factura_id) \
            .aggregate(descuento=Sum('descuento')) \
            .get('descuento',0.00)
        
        enc.sub_total = sub_total
        enc.descuento = descuento
        enc.save()

    prod=Producto.objects.filter(pk=producto_id).first()
    prod.save()
