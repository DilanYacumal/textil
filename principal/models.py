# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    idarea = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'


class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    nombre_bodega = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'bodega'

class CabezaMovimiento(models.Model):
    idcabeza_movimiento = models.AutoField(primary_key=True)
    numero_factura = models.CharField(max_length=50)
    fecha_factura = models.DateField()
    tipomovimientof_idtipomovimientof = models.ForeignKey('Tipomovimientof', models.DO_NOTHING, db_column='tipomovimientof_idtipomovimientof')
    persona_id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_id_persona')

    class Meta:
        managed = False
        db_table = 'cabeza_movimiento'


class Cargo(models.Model):
    idcargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=50)
    descripcion_cargo = models.CharField(max_length=100, blank=True, null=True)
    area_idarea = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_idarea')

    class Meta:
        managed = False
        db_table = 'cargo'

class Categorias(models.Model):
    idcategorias = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categorias'

class Confeccion(models.Model):
    idconfeccion = models.AutoField(primary_key=True)
    telefono_secundario = models.CharField(max_length=13, blank=True, null=True)
    direccion = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=50)
    tipo_producto = models.CharField(max_length=50)
    talla = models.CharField(max_length=10)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.CharField(db_column='Imagen', max_length=45, blank=True, null=True)  # Field name made lowercase.
    persona_id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_id_persona')
    tela_idtela = models.ForeignKey('Tela', models.DO_NOTHING, db_column='tela_idtela')

    class Meta:
        managed = False
        db_table = 'confeccion'


class CuerpoMovimiento(models.Model):
    idcuerpo_movimiento = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    cabeza_movimiento_idcabeza_movimiento = models.ForeignKey(CabezaMovimiento, models.DO_NOTHING, db_column='cabeza_movimiento_idcabeza_movimiento')
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id producto')  # Field renamed to remove unsuitable characters.
    confeccion_idconfeccion = models.ForeignKey(Confeccion, models.DO_NOTHING, db_column='confeccion_idconfeccion')

    class Meta:
        managed = False
        db_table = 'cuerpo_movimiento'


class Kardex(models.Model):
    idkardex = models.AutoField(primary_key=True)
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id producto')  # Field renamed to remove unsuitable characters.
    bodega_id_bodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='bodega_id_bodega')
    stock_actual = models.IntegerField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=0)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'kardex'

class MovimientoBodega(models.Model):
    idmovimiento_bodega = models.AutoField(primary_key=True)
    kardex_idkardex = models.ForeignKey(Kardex, models.DO_NOTHING, db_column='kardex_idkardex')
    tipo_movimiento_bodega_idtipo_movimiento_bodega = models.ForeignKey('TipoMovimientoBodega', models.DO_NOTHING, db_column='tipo_movimiento_bodega_idtipo_movimiento_bodega')
    bodega_id_bodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='bodega_id_bodega')

    class Meta:
        managed = False
        db_table = 'movimiento_bodega'

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    correo_electronico = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13)
    edad = models.CharField(max_length=4)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    tipo_persona_idtipo_persona = models.ForeignKey('TipoPersona', models.DO_NOTHING, db_column='tipo_persona_idtipo_persona')
    area_idarea = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_idarea')
    tipo_documento_idtipo_documento = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='tipo_documento_idtipo_documento')

    class Meta:
        managed = False
        db_table = 'persona'

class Producto(models.Model):
    id_producto = models.AutoField(db_column='id producto', primary_key=True)  # Field renamed to remove unsuitable characters.
    nombre_producto = models.CharField(max_length=50)
    codigo = models.CharField(max_length=30)
    talla = models.CharField(max_length=4)
    color = models.CharField(max_length=20)
    imagen_producto = models.CharField(max_length=20, blank=True, null=True)
    tipo_producto_idtipo_producto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='tipo_producto_idtipo_producto')
    stock_minimo = models.IntegerField()
    stock_maximo = models.IntegerField()
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'producto'


class Tela(models.Model):
    idtela = models.AutoField(primary_key=True)
    nombre_tela = models.CharField(max_length=50)
    valor_tela_idvalor_tela = models.ForeignKey('ValorTela', models.DO_NOTHING, db_column='valor_tela_idvalor_tela')

    class Meta:
        managed = False
        db_table = 'tela'


class Temporada(models.Model):
    idtemporada = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'temporada'


class TipoDocumento(models.Model):
    idtipo_documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoMovimientoBodega(models.Model):
    idtipo_movimiento_bodega = models.AutoField(primary_key=True)
    nombre_movimientob = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_movimiento_bodega'


class TipoPersona(models.Model):
    idtipo_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_persona'

class TipoProducto(models.Model):
    idtipo_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    temporada_idtemporada = models.ForeignKey(Temporada, models.DO_NOTHING, db_column='temporada_idtemporada')
    categorias_idcategorias = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='categorias_idcategorias')
    class Meta:
        managed = False
        db_table = 'tipo_producto'

class Tipomovimientof(models.Model):
    idtipomovimientof = models.AutoField(primary_key=True)
    nombre_movimientof = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipomovimientof'


class ValorTela(models.Model):
    idvalor_tela = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'valor_tela'
