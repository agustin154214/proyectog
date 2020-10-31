from django.db import models

from sisfya.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural= "Categorias"


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural= "Sub Categorias"
        unique_together = ('categoria','descripcion')

            #modelo marca#
class Marca(ClaseModelo):
    marcap = models.CharField(
        max_length=100,
        help_text='Descripción de la Marca',
        unique=True
    )

    def __str__(self):
        return '{}' .format(self.marcap)

    def save(self):
        self.marcap = self.marcap.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural= "Marcas"

        #modelo unidad de medida#

class UnidadMedida(ClaseModelo):
    unidadp = models.CharField(
        max_length=100,
        help_text='Descripción de la unidad de medida',
        unique=True
    )

    def __str__(self):
        return '{}' .format(self.unidadp)

    def save(self):
        self.unidadp = self.unidadp.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural= "Unidades de medidas"

        #modelo Productos

class Producto(ClaseModelo):
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{}' .format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural= "Productos"

    
    
    
# Create your models here.
