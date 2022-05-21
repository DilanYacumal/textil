from django.contrib import admin

# Register your models here.

from.models import Area
from.models import Bodega
from.models import CabezaMovimiento
from.models import Cargo
from.models import Categorias
from.models import Confeccion
from.models import CuerpoMovimiento
from.models import Kardex
from.models import MovimientoBodega
from.models import Persona
from.models import Producto
from.models import Tela
from.models import Temporada
from.models import TipoDocumento
from.models import TipoMovimientoBodega
from.models import TipoPersona
from.models import TipoProducto
from.models import Tipomovimientof
from.models import ValorTela


admin.site.register(Area)
admin.site.register(Bodega)
admin.site.register(CabezaMovimiento)
admin.site.register(Cargo)
admin.site.register(Categorias)
admin.site.register(Confeccion)
admin.site.register(CuerpoMovimiento)
admin.site.register(Kardex)
admin.site.register(MovimientoBodega)
admin.site.register(Persona)
admin.site.register(Producto)
admin.site.register(Tela)
admin.site.register(Temporada)
admin.site.register(TipoDocumento)
admin.site.register(TipoMovimientoBodega)
admin.site.register(TipoPersona)
admin.site.register(TipoProducto)
admin.site.register(Tipomovimientof)
admin.site.register(ValorTela)