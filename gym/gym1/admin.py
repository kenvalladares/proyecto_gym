from django.contrib import admin
from gym1.models import *
from gym1.forms import *
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export import resources, fields



# Register your models here.
@admin.register(GeneroPersona)
class GeneroPersonaAdmin(admin.ModelAdmin):
    form = GeneroPersonaForm
    list_display = ("idGenero","nombreGenero")
    ordering = ("idGenero","nombreGenero")
    search_fields = ("idGenero","nombreGenero")

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    form = CategoriaForm
    list_display = ("idCategoria","nombreCategoria","descripcionCategoria")
    ordering = ("idCategoria","nombreCategoria","descripcionCategoria")
    search_fields = ("idCategoria","nombreCategoria","descripcionCategoria")


@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    form = ProveedoresForm
    list_display = ("NombreProveedor","Direccion","Contacto","rtnProveedor")
    search_fields = ('NombreProveedor','rtnProveedor')

@admin.register(Impuestos)
class ImpuestosAdmin(admin.ModelAdmin):
    form = ImpuestosForm
    list_display = ("idImpuesto","nombre","fechaInicial","fechaFinal","valor",)
    ordering = ("idImpuesto","nombre","fechaInicial","fechaFinal","valor",)
    search_fields = ("idImpuesto","nombre","fechaInicial","fechaFinal","valor",)

@admin.register(Productos) 
class ProductosAdmin(admin.ModelAdmin):
    form = ProductoForm
    list_display = ("idProducto","nombreProducto","precio","idImpuesto","descuento","idCategoria","idProveedor","stockMinimo","stockMaximo")
    ordering = ('nombreProducto',)
    search_fields = ('nombreProducto',"precio")

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ("idProducto","stockActual")
    search_fields = ("idProducto","stockActual")
    form = InventarioForm

#COMPRAS
class ComprasResources(resources.ModelResource):
    idCompra = fields.Field(column_name="ID de Compra",attribute="idCompra")
    idProveedor = fields.Field(column_name="Proveedor",attribute="idProveedor",widget=ForeignKeyWidget(Proveedores,field='NombreProveedor'))
    detalle = fields.Field(column_name="Detalle",attribute="detalle")
    idInventario = fields.Field(column_name="Libro",attribute='idInventario',widget=ForeignKeyWidget(Inventario, 'idLibro'))
    cantidad = fields.Field(column_name="Cantidad",attribute="cantidad")
    precio = fields.Field(column_name="Precio",attribute="precio")
    fechaPedido = fields.Field(column_name="Fecha de Pedido",attribute="fechaPedido")
    fechaEntrega = fields.Field(column_name="Fecha de Entrega",attribute="fechaEntrega")
    fechaEnvio = fields.Field(column_name="Fecha de Envio",attribute="fechaEnvio")
    class Meta:
        model=Compras
        fields=('idCompra','idProveedor','detalle','idInventario','cantidad','precio','fechaPedido','fechaEntrega',
        'fechaEnvio')
        export_order=('idCompra','idProveedor','detalle','idInventario','cantidad','precio','fechaPedido','fechaEntrega',
        'fechaEnvio')

@admin.register(Compras)
class ComprasAdmin(admin.ModelAdmin):
    list_display = ("idCompra","idProveedor","detalle","idInventario","cantidad","precio","fechaPedido","fechaEntrega","fechaEnvio")
    search_fields = ("idCompra","idProveedor","detalle","idInventario","cantidad","precio","fechaPedido","fechaEntrega","fechaEnvio")
    form = ComprasForm
    resource_class = ComprasResources

@admin.register(TipoDeduccion)
class TipoDeduccionAdmin(admin.ModelAdmin):
    form = TipoDeduccionForm
    list_display = ("idTipoDeduccion","nombreTipoDeduccion","descripcionTipoDeduccion")
    ordering = ("idTipoDeduccion","nombreTipoDeduccion","descripcionTipoDeduccion")
    search_fields = ("idTipoDeduccion","nombreTipoDeduccion","descripcionTipoDeduccion")

#DOCUMENTOS

class TipoDocumentoResources(resources.ModelResource):
    idDocumento = fields.Field(column_name="iD Documento",attribute="idDocumento")
    nombreDocumento = fields.Field(column_name="Nombre",attribute="nombreDocumento")
    class Meta:
        model=TipoDocumento
        fields=("idDocumento","nombreDocumento")
        export_order=("idDocumento","nombreDocumento")

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    form = TipoDocumentoForm
    list_display = ("idDocumento","nombreDocumento")
    ordering = ("idDocumento","nombreDocumento")
    search_fields = ("idDocumento","nombreDocumento")

#CARGO

class CargoResources(resources.ModelResource):
    idCargo = fields.Field(column_name="iD Cargo",attribute="idCargo")
    nombreCargo = fields.Field(column_name="Nombre",attribute="nombreCargo")
    descripcionCargo = fields.Field(column_name="Descripcion",attribute="descripcionCargo")

    class Meta:
        model=Cargo
        fields=("idCargo","nombreCargo","descripcionCargo")
        export_order=("idCargo","nombreCargo","descripcionCargo")

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    form = CargoForm
    list_display = ("idCargo","nombreCargo","descripcionCargo")
    ordering = ("idCargo","nombreCargo","descripcionCargo")
    search_fields = ("idCargo","nombreCargo","descripcionCargo")

#EMPLEADOS

class EmpleadoResources(resources.ModelResource):
    idEmpleado = fields.Field(column_name="ID de Empleado",attribute="idEmpleado")
    nombreEmpleado = fields.Field(column_name="Nombre",attribute="nombreEmpleado")
    apellidoEmpleado = fields.Field(column_name="Apellido",attribute="apellidoEmpleado")
    direccion = fields.Field(column_name="Direccion",attribute="direccion")
    contacto = fields.Field(column_name="Contacto",attribute="contacto")
    fechaNacimiento = fields.Field(column_name="Fecha de Nacimiento",attribute="fechaNacimiento")
    fechaIngreso = fields.Field(column_name="Fecha de Ingreso",attribute="fechaIngreso")
    idCargo = fields.Field(column_name="Cargo",attribute="idCargo",widget=ForeignKeyWidget(Cargo,'nombrecargo'))
    idGenero = fields.Field(column_name="Genero",attribute="idGenero",widget=ForeignKeyWidget(GeneroPersona,'nombreSucursal'))
    idDocumento = fields.Field(column_name="Tipo de Documento",attribute="idDocumento",widget=ForeignKeyWidget(TipoDocumento,'nombreDocumento'))
    documento = fields.Field(column_name="Documento",attribute="documento")
    class Meta:
        model=Empleado
        fields=("idEmpleado","nombreEmpleado","direccion","contacto","fechaNacimiento","fechaIngreso","idCargo",
        "idGenero","idDocumento","documento")
        export_order=("idEmpleado","nombreEmpleado","direccion","contacto","fechaNacimiento","fechaIngreso","idCargo",
        "idGenero","idDocumento","documento")

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    form = EmpleadoForm
    resource_class = EmpleadoResources
    list_display = ("idEmpleado","nombreEmpleado","direccion","contacto","fechaNacimiento","fechaIngreso","idCargo",
        "idGenero","idDocumento","documento")
    ordering = ("idEmpleado","nombreEmpleado")
    search_fields = ("idEmpleado","nombreEmpleado","direccion","contacto","fechaNacimiento","fechaIngreso","idCargo",
        "idGenero","idDocumento","documento")

#CLIENTES

class ClienteResources(resources.ModelResource):
    idCliente = fields.Field(column_name="ID de Cliente",attribute="idCliente")
    nombreCliente = fields.Field(column_name="Nombre",attribute="nombreCliente")
    fechaNacimiento = fields.Field(column_name="Fecha de Nacimiento",attribute="fechaNacimiento")
    direccion = fields.Field(column_name="Direccion",attribute="direccion")
    contacto = fields.Field(column_name="Contacto",attribute="contacto")
    idDocumento = fields.Field(column_name="Tipo de Documento",attribute="idDocumento",widget=ForeignKeyWidget(TipoDocumento,'nombreDocumento'))
    documento = fields.Field(column_name="Documento",attribute="documento")
    idGeneor = fields.Field(column_name="Genero",attribute="idGenero",widget=ForeignKeyWidget(GeneroPersona,'genero'))

    class Meta:
        model=Cliente
        fields=("idCliente","nombreCliente","direccion","idCiudad","contacto","idRol","idClub","idEstudiante",
        "idDocumento","documento")
        export_order=("idCliente","nombreCliente","direccion","idCiudad","contacto","idRol","idClub","idEstudiante",
        "idDocumento","documento")

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    form = ClienteForm
    list_display = ("idCliente","nombreCliente","fechaNacimiento","direccion","contacto","idGenero",
    "idDocumento","documento")
    ordering = ("idCliente","nombreCliente")
    search_fields = ("idCliente","nombreCliente","fechaNacimiento","direccion","contacto","idGenero",
    "idDocumento","documento")
    resource_class = ClienteResources

#INFORMACIONFISICA

class InformacionFisicaResources(resources.ModelResource):
    idInformacionFisica = fields.Field(column_name="ID de Informacion Fisica",attribute="idInformacionFisica")
    idCliente = fields.Field(column_name="Nombre",attribute="idCliente")
    peso = fields.Field(column_name="Peso",attribute="peso")
    altura = fields.Field(column_name="Altura",attribute="altura")
    cintura = fields.Field(column_name="Cintura",attribute="cintura")
    pecho = fields.Field(column_name="Pecho",attribute="pecho")
    brazo = fields.Field(column_name="Brazo",attribute="brazo")
    fecha = fields.Field(column_name="Fecha",attribute="fecha")

    class Meta:
        model=InformacionFisica
        fields=("idInformacionFisica","idCliente","peso","altura","cintura","pecho","brazo","fecha")
        export_order=("idInformacionFisica","idCliente","peso","altura","cintura","pecho","brazo","fecha")

@admin.register(InformacionFisica)
class InformacionFisicaAdmin(admin.ModelAdmin):
    form = InformacionFisicaForm
    list_display = ("idInformacionFisica","idCliente","peso","altura","cintura","pecho","brazo","fecha")
    ordering = ("idInformacionFisica","idCliente")
    search_fields = ("idInformacionFisica","idCliente","peso","altura","cintura","pecho","brazo","fecha")
    resource_class = InformacionFisicaResources

#TIPOMEMBRESIA

class TipoMembresiaResources(resources.ModelResource):
    idTipoMembresia = fields.Field(column_name="ID de Tipo Membresia",attribute="idTipoMembresia")
    nombreTipoMembresia = fields.Field(column_name="Nombre",attribute="nombreTipoMembresia")
    detalleTipoMembresia = fields.Field(column_name="Detalle",attribute="detalleTipoMembresia")
    precio = fields.Field(column_name="Precio",attribute="precio")
    

    class Meta:
        model=TipoMembresia
        fields=("idTipoMembresia","nombreTipoMembresia","detalleTipoMembresia","precio")
        export_order=("idTipoMembresia","nombreTipoMembresia","detalleTipoMembresia","precio")

@admin.register(TipoMembresia)
class TipoMembresiaAdmin(admin.ModelAdmin):
    form = TipoMembresiaForm
    list_display = ("idTipoMembresia","nombreTipoMembresia","detalleTipoMembresia","precio")
    ordering = ("idTipoMembresia","nombreTipoMembresia")
    search_fields = ("idTipoMembresia","nombreTipoMembresia","detalleTipoMembresia","precio")
    resource_class = TipoMembresiaResources

#MEMBRESIA

class MembresiaResources(resources.ModelResource):
    idMembresia = fields.Field(column_name="ID de Tipo Membresia",attribute="idMembresia")
    fechaInicial = fields.Field(column_name="Fecha Inicial",attribute="fechaInicial")
    fechaFinal = fields.Field(column_name="Fecha Final",attribute="fechaFinal")
    idCliente = fields.Field(column_name="Cliente",attribute="idCliente")
    idTipoMembresia = fields.Field(column_name="Tipo de Membresia",attribute="idTipoMembresia")

    class Meta:
        model=Membresia
        fields=("idMembresia","fechaInicial","fechaFinal","idCliente","idTipoMembresia")
        export_order=("idMembresia","fechaInicial","fechaFinal","idCliente","idTipoMembresia")

@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    form = MembresiaForm
    list_display = ("idMembresia","fechaInicial","fechaFinal","idCliente","idTipoMembresia")
    ordering = ("idMembresia","idCliente")
    search_fields = ("idMembresia","fechaInicial","fechaFinal","idCliente","idTipoMembresia")
    resource_class = MembresiaResources

#TIPORECETANUTRICIONAL

class TipoRecetaNutricionalResources(resources.ModelResource):
    idTipoRecetaNutricional = fields.Field(column_name="ID de Tipo Receta Nutricional",attribute="idTipoRecetaNutricional")
    nombreTipoRecetaNutricional = fields.Field(column_name="Nombre",attribute="nombreTipoRecetaNutricional")
    detalleTipoRecetaNutricional = fields.Field(column_name="Detalle",attribute="detalleTipoRecetaNutricional")
    

    class Meta:
        model=TipoRecetaNutricional
        fields=("idTipoRecetaNutricional","nombreTipoRecetaNutricional","detalleTipoRecetaNutricional")
        export_order=("idTipoRecetaNutricional","nombreTipoRecetaNutricional","detalleTipoRecetaNutricional")

@admin.register(TipoRecetaNutricional)
class TipoRecetaNutricionalAdmin(admin.ModelAdmin):
    form = TipoRecetaNutricionalForm
    list_display = ("idTipoRecetaNutricional","nombreTipoRecetaNutricional","detalleTipoRecetaNutricional")
    ordering = ("idTipoRecetaNutricional","nombreTipoRecetaNutricional")
    search_fields = ("idTipoRecetaNutricional","nombreTipoRecetaNutricional","detalleTipoRecetaNutricional")
    resource_class = TipoRecetaNutricionalResources

#RECETANUTRICIONAL

class RecetaNutricionalResources(resources.ModelResource):
    idReceta = fields.Field(column_name="ID de Receta Nutricional",attribute="idReceta")
    ingredientes = fields.Field(column_name="Ingredientes",attribute="ingredientes")
    fecha = fields.Field(column_name="Fecha",attribute="fecha")
    idtipoRecetaNutricional = fields.Field(column_name="Tipo Receta",attribute="idtipoRecetaNutricional")


    class Meta:
        model=RecetaNutricional
        fields=("idReceta","ingredientes","fecha","idtipoRecetaNutricional")
        export_order=("idReceta","ingredientes","fecha","idtipoRecetaNutricional")

@admin.register(RecetaNutricional)
class RecetaNutricionalAdmin(admin.ModelAdmin):
    form = RecetaNutricionalForm
    list_display = ("idReceta","ingredientes","fecha","idtipoRecetaNutricional")
    ordering = ("idReceta","ingredientes")
    search_fields = ("idReceta","ingredientes","fecha","idtipoRecetaNutricional")
    resource_class = RecetaNutricionalResources

#PLANNUTRICIONAL

class PlanNutricionalResources(resources.ModelResource):
    idPlanNutricional = fields.Field(column_name="ID de Plan Nutricional",attribute="idPlanNutricional")
    idCliente = fields.Field(column_name="Cliente",attribute="idCliente")
    idReceta = fields.Field(column_name="Receta",attribute="idReceta")
    fechaInicial = fields.Field(column_name="Fecha Inicial",attribute="fechaInicial")
    fechaFinal = fields.Field(column_name="Fecha Final",attribute="fechaFinal")
    
    class Meta:
        model=PlanNutricional
        fields=("idPlanNutricional","idCliente","idReceta","fechaInicial","fechaFinal")
        export_order=("idPlanNutricional","idCliente","idReceta","fechaInicial","fechaFinal")

@admin.register(PlanNutricional)
class PlanNutricionalAdmin(admin.ModelAdmin):
    form = PlanNutricionalForm
    list_display = ("idPlanNutricional","idCliente","idReceta","fechaInicial","fechaFinal")
    ordering = ("idPlanNutricional","idCliente")
    search_fields = ("idPlanNutricional","idCliente","idReceta","fechaInicial","fechaFinal")
    resource_class = PlanNutricionalResources

#TIPOMAQUINA

class TipoMaquinaResources(resources.ModelResource):
    idTipoMaquina = fields.Field(column_name="ID de Tipo Maquina",attribute="idTipoMaquina")
    nombreTipoMaquina = fields.Field(column_name="Nombre",attribute="nombreTipoMaquina")
    detalleTipoMaquina = fields.Field(column_name="Detalle",attribute="detalleTipoMaquina")
    

    class Meta:
        model=TipoMaquina
        fields=("idTipoMaquina","nombreTipoMaquina","detalleTipoMaquina")
        export_order=("idTipoMaquina","nombreTipoMaquina","detalleTipoMaquina")

@admin.register(TipoMaquina)
class TipoMaquinaAdmin(admin.ModelAdmin):
    form = TipoMaquinaForm
    list_display = ("idTipoMaquina","nombreTipoMaquina","detalleTipoMaquina")
    ordering = ("idTipoMaquina","nombreTipoMaquina")
    search_fields = ("idTipoMaquina","nombreTipoMaquina","detalleTipoMaquina")
    resource_class = TipoMaquinaResources

#EJERCICIOSRUTINA

class EjerciciosRutinaResources(resources.ModelResource):
    idEjerciciosRutina = fields.Field(column_name="ID de Rutina de Ejercicios",attribute="idEjerciciosRutina")
    nombreEjercicio = fields.Field(column_name="Nombre",attribute="nombreEjercicio")
    series = fields.Field(column_name="Series",attribute="series")
    repeticiones = fields.Field(column_name="Repeticiones",attribute="repeticiones")
    descanso = fields.Field(column_name="Descanso",attribute="descanso")
    idTipoMaquina = fields.Field(column_name="Tipo de Maquina",attribute="idTipoMaquina")

    

    class Meta:
        model=EjerciciosRutina
        fields=("idEjerciciosRutina","nombreEjercicio","series","repeticiones","descanso","idTipoMaquina")
        export_order=("idEjerciciosRutina","nombreEjercicio","series","repeticiones","descanso","idTipoMaquina")

@admin.register(EjerciciosRutina)
class EjerciciosRutinaAdmin(admin.ModelAdmin):
    form = EjerciciosRutinaForm
    list_display = ("idEjerciciosRutina","nombreEjercicio","series","repeticiones","descanso","idTipoMaquina")
    ordering = ("idEjerciciosRutina","nombreEjercicio")
    search_fields = ("idEjerciciosRutina","nombreEjercicio","series","repeticiones","descanso","idTipoMaquina")
    resource_class = EjerciciosRutinaResources

#RUTINA

class RutinaResources(resources.ModelResource):
    idRutina = fields.Field(column_name="ID de Rutina",attribute="idRutina")
    fechaInicial = fields.Field(column_name="Fecha Inicial",attribute="fechaInicial")
    fechaFinal = fields.Field(column_name="Fecha Final",attribute="fechaFinal")
    idCliente = fields.Field(column_name="Cliente",attribute="idCliente")
    idEjerciciosRutina= fields.Field(column_name="Ejercicios ",attribute="idEjerciciosRutina")

    

    class Meta:
        model=Rutina
        fields=("idRutina","fechaInicial","fechaFinal","idCliente","idEjerciciosRutina")
        export_order=("idRutina","fechaInicial","fechaFinal","idCliente","idEjerciciosRutina")

@admin.register(Rutina)
class RutinaAdmin(admin.ModelAdmin):
    form = RutinaForm
    list_display = ("idRutina","fechaInicial","fechaFinal","idCliente","idEjerciciosRutina")
    ordering = ("idRutina","idCliente")
    search_fields = ("idRutina","fechaInicial","fechaFinal","idCliente","idEjerciciosRutina")
    resource_class = RutinaResources

#SALON

class SalonResources(resources.ModelResource):
    idSalon = fields.Field(column_name="ID de Salon",attribute="idSalon")
    nombreSalon = fields.Field(column_name="Nombre",attribute="nombreSalon")
    descripcionSalon = fields.Field(column_name="Descripcion",attribute="descripcionSalon")

    

    class Meta:
        model=Salon
        fields=("idSalon","nombreSalon","descripcionSalon")
        export_order=("idSalon","nombreSalon","descripcionSalon")

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    form = SalonForm
    list_display = ("idSalon","nombreSalon","descripcionSalon")
    ordering = ("idSalon","nombreSalon")
    search_fields = ("idSalon","nombreSalon","descripcionSalon")
    resource_class = SalonResources

#CLASES

class ClasesResources(resources.ModelResource):
    idClases = fields.Field(column_name="ID de Clases",attribute="idClases")
    nombreClases = fields.Field(column_name="Nombre",attribute="nombreClases")
    detalleClases = fields.Field(column_name="Detalles",attribute="detalleClases")
    idSalon = fields.Field(column_name="Salon",attribute="idSalon")    

    class Meta:
        model=Clases
        fields=("idClases","nombreClases","detalleClases","idSalon")
        export_order=("idClases","nombreClases","detalleClases","idSalon")

@admin.register(Clases)
class ClasesAdmin(admin.ModelAdmin):
    form = ClasesForm
    list_display = ("idClases","nombreClases","detalleClases","idSalon")
    ordering = ("idClases","nombreClases")
    search_fields = ("idClases","nombreClases","detalleClases","idSalon")
    resource_class = ClasesResources

#CLASESCLIENTES
class ClasesClienteResources(resources.ModelResource):
    idClasesCliente = fields.Field(column_name="ID de Clases de Clientes",attribute="idClasesCliente")
    fechaInicial = fields.Field(column_name="Fecha Inicial",attribute="fechaInicial")
    fechaFinal = fields.Field(column_name="Fecha Final",attribute="fechaFinal")
    idCliente = fields.Field(column_name="Cliente",attribute="idCliente")
    idClases= fields.Field(column_name="Clases ",attribute="idClases")

    

    class Meta:
        model=ClasesCliente
        fields=("idClasesCliente","fechaInicial","fechaFinal","idCliente","idClases")
        export_order=("idClasesCliente","fechaInicial","fechaFinal","idCliente","idClases")

@admin.register(ClasesCliente)
class ClasesClienteAdmin(admin.ModelAdmin):
    form = ClasesClienteForm
    list_display = ("idClasesCliente","fechaInicial","fechaFinal","idCliente","idClases")
    ordering = ("idClasesCliente","idCliente")
    search_fields = ("idClasesCliente","fechaInicial","fechaFinal","idCliente","idClases")
    resource_class = ClasesClienteResources

#PLANILLA
class PlanillaResources(resources.ModelResource):
    idPlanilla = fields.Field(column_name="ID de Planilla",attribute="idPlanilla")
    nombrePlanilla = fields.Field(column_name="ID de Clases de Clientes",attribute="nombrePlanilla")
    fechaInicial = fields.Field(column_name="Fecha Inicial",attribute="fechaInicial")
    fechaFinal = fields.Field(column_name="Fecha Final",attribute="fechaFinal")
    fechaPago = fields.Field(column_name="Fecha Pago",attribute="fechaPago")
    detallePlanilla= fields.Field(column_name="Detalles",attribute="detallePlanilla")

    class Meta:
        model=Planilla
        fields=("idPlanilla","nombrePlanilla","fechaInicial","fechaFinal","fechaPago","detallePlanilla")
        export_order=("idPlanilla","nombrePlanilla","fechaInicial","fechaFinal","fechaPago","detallePlanilla")

@admin.register(Planilla)
class PlanillaAdmin(admin.ModelAdmin):
    form = PlanillaForm
    list_display = ("idPlanilla","nombrePlanilla","fechaInicial","fechaFinal","fechaPago","detallePlanilla")
    ordering = ("idPlanilla","nombrePlanilla")
    search_fields = ("idPlanilla","nombrePlanilla","fechaInicial","fechaFinal","fechaPago","detallePlanilla")
    resource_class = PlanillaResources

#TIPOBONO

class TipoBonoResources(resources.ModelResource):
    idTipoBono = fields.Field(column_name="ID de Tipo Bono",attribute="idTipoBono")
    nombreTipoBono = fields.Field(column_name="Nombre",attribute="nombreTipoBono")
    descripcionTipoBono = fields.Field(column_name="Descripcion",attribute="descripcionTipoBono")

    class Meta:
        model=TipoBono
        fields=("idTipoBono","nombreTipoBono","descripcionTipoBono")
        export_order=("idTipoBono","nombreTipoBono","descripcionTipoBono")

@admin.register(TipoBono)
class TipoBonoAdmin(admin.ModelAdmin):
    form = TipoBonoForm
    list_display = ("idTipoBono","nombreTipoBono","descripcionTipoBono")
    ordering = ("idTipoBono","nombreTipoBono")
    search_fields = ("idTipoBono","nombreTipoBono","descripcionTipoBono")
    resource_class = TipoBonoResources

#BONO
class BonoResources(resources.ModelResource):
    idBono = fields.Field(column_name="ID de Bono",attribute="idBono")
    monto = fields.Field(column_name="Monto",attribute="monto")
    fecha = fields.Field(column_name="Fecha ",attribute="fecha")
    idEmpleado = fields.Field(column_name="Empleado",attribute="idEmpleado")
    idPlanilla = fields.Field(column_name="Planilla",attribute="idPlanilla")
    idTipoBono= fields.Field(column_name="Tipo de Bono",attribute="idTipoBono")

    class Meta:
        model=Bono
        fields=("idBono","monto","fecha","idEmpleado","idPlanilla","idTipoBono")
        export_order=("idBono","monto","fecha","idEmpleado","idPlanilla","idTipoBono")

@admin.register(Bono)
class BonoAdmin(admin.ModelAdmin):
    form = BonoForm
    list_display = ("idBono","monto","fecha","idEmpleado","idPlanilla","idTipoBono")
    ordering = ("idBono","idEmpleado")
    search_fields = ("idBono","monto","fecha","idEmpleado","idPlanilla","idTipoBono")
    resource_class = BonoResources

#CARGOEMPLEADO
class CargoEmpleadoResources(resources.ModelResource):
    idCargoEmpleado = fields.Field(column_name="ID de Cargo Empleado",attribute="idCargoEmpleado")
    fechaInicial = fields.Field(column_name="Fecha Inicial",attribute="fechaInicial")
    fechaFinal = fields.Field(column_name="Fecha Final",attribute="fechaFinal")
    idCargo = fields.Field(column_name="Cargo",attribute="idCargo")
    idEmpleado= fields.Field(column_name="Empleado",attribute="idEmpleado")  

    class Meta:
        model=Planilla
        fields=("idCargoEmpleado","fechaInicial","fechaFinal","idCargo","idEmpleado")
        export_order=("idCargoEmpleado","fechaInicial","fechaFinal","idCargo","idEmpleado")

@admin.register(CargoEmpleado)
class CargoEmpleadoAdmin(admin.ModelAdmin):
    form = CargoEmpleadoForm
    list_display = ("idCargoEmpleado","fechaInicial","fechaFinal","idCargo","idEmpleado")
    ordering = ("idCargoEmpleado","idEmpleado")
    search_fields = ("idCargoEmpleado","fechaInicial","fechaFinal","idCargo","idEmpleado")
    resource_class = CargoEmpleadoResources