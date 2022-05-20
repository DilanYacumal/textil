# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    idarea = models.IntegerField(primary_key=True)
    nombre_area = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'area'

    def __str__(self):
        return (self.idarea , self.nombre_area)


class Bodega(models.Model):
    id_bodega = models.IntegerField(primary_key=True)
    nombre_bodega = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=20)


    class Meta:
        managed = False
        db_table = 'bodega'

    def __str__(self):
        return (self.id_bodega , self.nombre_bodega)

class CabezaMovimiento(models.Model):
    idcabeza_movimiento = models.IntegerField(primary_key=True)
    numero_factura = models.CharField(max_length=45)
    fecha_documento = models.DateField()
    tipomovimientof_idtipomovimientof = models.ForeignKey('Tipomovimientof', models.DO_NOTHING, db_column='tipomovimientof_idtipomovimientof')
    persona_id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_id_persona')

    class Meta:
        managed = False
        db_table = 'cabeza_movimiento'


class Cargo(models.Model):
    idcargo = models.IntegerField(primary_key=True)
    nombre_cargo = models.CharField(max_length=45)
    descripcion_cargo = models.CharField(max_length=50)
    area_idarea = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_idarea')

    class Meta:
        managed = False
        db_table = 'cargo'


class Categorias(models.Model):
    idcategorias = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'categorias'


class CuerpoMovimiento(models.Model):
    idcuerpo_movimiento = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    cabeza_movimiento_idcabeza_movimiento = models.ForeignKey(CabezaMovimiento, models.DO_NOTHING, db_column='cabeza_movimiento_idcabeza_movimiento')
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id producto')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'cuerpo_movimiento'


class Kardex(models.Model):
    idkardex = models.IntegerField(primary_key=True)
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id producto')  # Field renamed to remove unsuitable characters.
    bodega_id_bodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='bodega_id_bodega')
    stock_actual = models.CharField(max_length=45)
    precio_venta = models.CharField(max_length=45)
    precio_compra = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'kardex'


class MovimientoBodega(models.Model):
    idmovimiento_bodega = models.IntegerField(primary_key=True)
    kardex_idkardex = models.ForeignKey(Kardex, models.DO_NOTHING, db_column='kardex_idkardex')
    tipo_movimiento_bodega_idtipo_movimiento_bodega = models.ForeignKey('TipoMovimientoBodega', models.DO_NOTHING, db_column='tipo_movimiento_bodega_idtipo_movimiento_bodega')
    bodega_id_bodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='bodega_id_bodega')

    class Meta:
        managed = False
        db_table = 'movimiento_bodega'


class Persona(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=45)
    primer_apellido = models.CharField(max_length=45)
    segundo_apellido = models.CharField(max_length=45)
    gmail = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=25)
    telefono = models.CharField(max_length=12)
    edad = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    tipo_persona_idtipo_persona = models.ForeignKey('TipoPersona', models.DO_NOTHING, db_column='tipo_persona_idtipo_persona')
    area_idarea = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_idarea')
    tipo_documento_idtipo_documento = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='tipo_documento_idtipo_documento')

    class Meta:
        managed = False
        db_table = 'persona'


class Producto(models.Model):
    id_producto = models.IntegerField(db_column='id producto', primary_key=True)  # Field renamed to remove unsuitable characters.
    nombre_producto = models.CharField(max_length=25)
    codigo = models.CharField(max_length=30)
    talla = models.CharField(max_length=4)
    color = models.CharField(max_length=20)
    imagen_producto = models.CharField(max_length=20)
    tipo_producto_idtipo_producto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='tipo_producto_idtipo_producto')
    stock_minimo = models.CharField(max_length=45)
    stock_maximo = models.CharField(max_length=45)
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'producto'


class Temporada(models.Model):
    idtemporada = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'temporada'


class TipoDocumento(models.Model):
    idtipo_documento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoMovimientoBodega(models.Model):
    idtipo_movimiento_bodega = models.IntegerField(primary_key=True)
    nombre_movimientob = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_movimiento_bodega'


class TipoPersona(models.Model):
    idtipo_persona = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_persona'


class TipoProducto(models.Model):
    idtipo_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=20)
    temporada_idtemporada = models.ForeignKey(Temporada, models.DO_NOTHING, db_column='temporada_idtemporada')
    categorias_idcategorias = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='categorias_idcategorias')

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class Tipomovimientof(models.Model):
    idtipomovimientof = models.IntegerField(primary_key=True)
    nombre_movimientof = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipomovimientof'
