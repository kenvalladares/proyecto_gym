
from django import forms
from .models import *
from django.forms import ValidationError
import datetime

class GeneroPersonaForm(forms.ModelForm):
    nombreGenero = forms.CharField(min_length=3,max_length=50,label='Genero:')
    class Meta: 
        model = GeneroPersona
        fields = [
            'idGenero',
            'nombreGenero',
        ]
        labels = {
            'idGenero':"ID de Genero:",
            'nombreGenero':"Genero:",

        }
        widget = {
            'idGenero':forms.TextInput(attrs={'class':'form-control'}),
            'nombreGenero':forms.TextInput(attrs={'class':'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class CategoriaForm(forms.ModelForm):
    nombreCategoria = forms.CharField(min_length=3,max_length=50,label='Categoria:')
    descripcionCategoria = forms.CharField(min_length=3,max_length=50,label='Descripcion:')

    class Meta: 
        model = Categoria
        fields = [
            'idCategoria',
            'nombreCategoria',
            'descripcionCategoria',
        ]
        labels = {
            'idCategoria':"ID de Categoria:",
            'nombreCategoria':"Nombre:",
            'descripcionCategoria':"Descripcion:",


        }
        widget = {
            'idCategoria':forms.TextInput(attrs={'class':'form-control'}),
            'nombreCategoria':forms.TextInput(attrs={'class':'form-control'}),
            'descripcionCategoria':forms.TextInput(attrs={'class':'form-control'}),

        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class ProveedoresForm(forms.ModelForm):
    NombreProveedor = forms.CharField(min_length=5,max_length=50,label='Nombre:')
    Direccion = forms.CharField(min_length=8,max_length=50,label='Dirección:')
    Contacto = forms.CharField(min_length=8,max_length=50,label='Número telefónico:')
    rtnProveedor = forms.CharField(min_length=14,max_length=14,label='RTN:')

    class Meta:
        model = Proveedores
        fields = [
            'idProveedor',
            'NombreProveedor',
            'Direccion',
            'Contacto',
            'rtnProveedor'
        ]
        labels = {
            'idProveedor': "ID del Proveedor:",
        }
        widget = {
            'idProveedor':forms.TextInput(attrs={'class':'form-control'}),
            'NombreProveedor':forms.TextInput(attrs={'class':'form-control'}),
            'Direccion':forms.Textarea(attrs={'class':'form-control'}),
            'Contacto':forms.TextInput(attrs={'class':'form-control'}),
            'rtnProveedor':forms.TextInput(attrs={'class':'form-control'})
            
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class ImpuestosForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3,max_length=50,label='Nombre:')
    valor = forms.DecimalField(decimal_places=2,min_value=0,max_value=0.31,max_digits=50,label='Valor:')

    class Meta:
        model = Impuestos
        fields = [
            'idImpuesto',
            'nombre',
            'fechaInicial',
            'fechaFinal',
            'valor',
        ]
        labels = {
            'idImpuesto':"ID de Impuesto:",
            'nombre':"Nombre:",
            'fechaInicial':"Fecha Inicial:",
            'fechaFinal':"Fecha Final:",
            'valor':"Valor:",
        }
        widget = {
            'idImpuesto':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'fechaInicial':forms.TextInput(attrs={'class':'form-control'}),
            'fechaFinal':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
        } 
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )
class ProductoForm(forms.ModelForm):
    nombreProducto = forms.CharField(min_length=3,max_length=50, label="Nombre de Producto:")
    descripcion = forms.CharField(min_length=10,max_length=2000, label="Descripción:")
    precio = forms.DecimalField(min_value=1,max_digits=10,decimal_places=2,label="Precio:")
    stockMinimo = forms.IntegerField(label="Stock Mínimo:")
    stockMaximo = forms.IntegerField(label="Stock Máximo:")
    descuento = forms.DecimalField(max_digits=1, min_value=0, max_value=0.80)


    def clean_stockMaximo(self):
        stockMinimo = self.cleaned_data["stockMinimo"]
        stockMaximo = self.cleaned_data["stockMaximo"]
        if stockMinimo<=0:
            raise ValidationError ("El stock minimo debe ser mayor a 0")
        elif stockMaximo<stockMinimo:
            raise ValidationError ("El stock maximo debe ser mayor al stock minimo")
        return stockMaximo
    
    class Meta:
        model = Productos
        fields = [
            'idProducto',
            'nombreProducto',
            'descripcion',
            'precio',
            'idImpuesto',
            'idCategoria',
            'idProveedor',
            'stockMinimo',
            'stockMaximo',
            'imagenProducto',
            
        ]
        labels = {
            'idProducto': "ID de Producto:",
            'idImpuesto':"Impuesto:",
            'descuento':"Descuento",
            'idCategoria': "Categoria:",
            'idProveedor': "Proveedor:",
            'imagenProducto': "Imagen del Producto:"
        }
        widget = {
            'idProducto':forms.TextInput(attrs={'class':'form-control'}),
            'nombreProducto':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(),
            'precio':forms.TextInput(attrs={'class':'form-control'}),
            'idImpuesto':forms.Select(attrs={'class':'form-control'}),
            'descuento':forms.TextInput(attrs={'class':'form-control'}),
            'idCategoria':forms.Select(attrs={'class':'form-control'}),
            'idProveedor':forms.Select(attrs={'class':'form-control'}),
            'stockMinimo':forms.TextInput(attrs={'class':'form-control'}),
            'stockMaximo':forms.TextInput(attrs={'class':'form-control'}),
            'imagenProducto':forms.ImageField(),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

        def __init__(self, *args, **kwargs):
            super(ProductoForm, self).__init__(*args, **kwargs)
            self.fields['idCategoria'].choices = [(i.idCategoria) for i in Categoria.objects.all]

class InventarioForm(forms.ModelForm):
    stockActual = forms.IntegerField(min_value=0,label='Stock Actual:')
    class Meta:
        model = Inventario
        fields = [
            'idInventario',
            'idProducto',
            'stockActual'
        ]
        labels = {
            'idInventario': "ID del Inventario:",
            'idProducto': "Producto:"
        }
        widget = {
            'idInventario':forms.TextInput(attrs={'class':'form-control'}),
            'idProducto':forms.Select(attrs={'class':'form-control'}),
            'stockActual':forms.TextInput(attrs={'class':'form-control'}),
            
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class ComprasForm(forms.ModelForm):
    cantidad = forms.IntegerField(min_value=1,label='Cantidad:')
    precio = forms.DecimalField(min_value=1,max_digits=10,decimal_places=2,label='Precio:')
    detalle = forms.CharField(min_length=5,max_length=2000, label='Detalle de Compra:')
   
    class Meta:
        model = Compras
        fields = [
            'idCompra',
            'idProveedor',
            'detalle',
            'idInventario',
            'cantidad',
            'precio',
            'fechaPedido',
            'fechaEntrega',
            'fechaEnvio'
        ]
        labels = {
            'idCompra': "ID de la Compra:",
            'idProveedor': "ID del Proveedor:",
            'idInventario': "Inventario:",
            'detalle': "Detalle de Compra:",
            'cantidad': "Cantidad:",
            'precio': "Precio:",
            'fechaPedido': "Fecha del Pedido:",
            'fechaEntrega': "Fecha de la Entrega:",
            'fechaEnvio': "Fecha del Envío:"
        }
        widget = {
            'idCompra':forms.TextInput(attrs={'class':'form-control'}),
            'idProveedor':forms.SelectMultiple(attrs={'class':'form-control'}),
            'idInventario':forms.Select(attrs={'class':'form-control'}),
            'detalle':forms.Textarea(attrs={'class':"form-control"}),
            'cantidad':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),
            'fechaPedido':forms.TextInput(attrs={'class':'form-control'}),
            'fechaEntrega':forms.TextInput(attrs={'class':'form-control'}),
            'fechaEnvio':forms.TextInput(attrs={'class':'form-control'}),
            
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )
class TipoDeduccionForm(forms.ModelForm):
    nombreTipoDeduccion = forms.CharField(min_length=3,max_length=50,label='Tipo Deduccion:')
    descripcionTipoDeduccion = forms.CharField(min_length=3,max_length=50,label='Descripcion:')

    class Meta: 
        model = TipoDeduccion
        fields = [
            'idTipoDeduccion',
            'nombreTipoDeduccion',
            'descripcionTipoDeduccion',
        ]
        labels = {
            'idTipoDeduccion':"ID de Tipo Deduccion:",
            'nombreTipoDeduccion':"Nombre:",
            'descripcionTipoDeduccion':"Descripcion:",


        }
        widget = {
            'idTipoDeduccion':forms.TextInput(attrs={'class':'form-control'}),
            'nombreTipoDeduccion':forms.TextInput(attrs={'class':'form-control'}),
            'descripcionTipoDeduccion':forms.TextInput(attrs={'class':'form-control'}),

        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class TipoDocumentoForm(forms.ModelForm):
    nombreDocumento = forms.CharField(min_length=3,max_length=50,label='Documento:')

    class Meta:
        model = TipoDocumento
        fields = [
            'idDocumento',
            'nombreDocumento',         
        ]
        labels = {
            'idDocumento': "ID del Documento:",
            'nombreDocumento': "Nombre del Documento:",
           
        }
        widget = {
            'idDocumento':forms.TextInput(attrs={'class':'form-control'}),
            'nombreDocumento':forms.TextInput(attrs={'class':'form-control'}),           

        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class CargoForm(forms.ModelForm):
    nombreCargo = forms.CharField(min_length=3,max_length=50,label='Cargo:')
    descripcionCargo = forms.CharField(min_length=3,max_length=50,label='Descripcion:')

    class Meta: 
        model = Cargo
        fields = [
            'idCargo',
            'nombreCargo',
            'descripcionCargo',
        ]
        labels = {
            'idCargo':"ID de Cargo:",
            'nombreCargo':"Nombre:",
            'descripcionCargo':"Descripcion:",


        }
        widget = {
            'idCargo':forms.TextInput(attrs={'class':'form-control'}),
            'nombreCargo':forms.TextInput(attrs={'class':'form-control'}),
            'descripcionCargo':forms.TextInput(attrs={'class':'form-control'}),

        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class EmpleadoForm(forms.ModelForm):
    nombreEmpleado = forms.CharField(min_length=3,max_length=50,label='Nombre:')
    apellidoEmpleado = forms.CharField(min_length=3,max_length=50,label='Apellido:')
    direccion = forms.CharField(min_length=8,max_length=50,label='Dirección:')
    contacto = forms.CharField(min_length=8,max_length=50,label='Número telefónico:')
    documento = forms.CharField(min_length=13,max_length=50,label='Documento:')
    class Meta:
        model = Empleado
        fields = [
            'idEmpleado',
            'nombreEmpleado',
            'apellidoEmpleado',
            'direccion',
            'contacto',
            'fechaNacimiento',
            'fechaIngreso',
            'idCargo',
            'idGenero',
            'idDocumento',
            'documento',           
        ]
        labels = {
            'idEmpleado': "ID del Empleado:",
            'nombreEmpleado': "Nombre del Empleado:",
            'apellidoEmpleado': "Apellido del Empleado:",
            'direccion': "Direccion:",
            'contacto': "Contacto:",
            'fechaNacimiento': "Fecha de Nacimiento:",
            'fechaIngreso': "Fecha de Ingreso:",
            'idCargo': "Cargo:",
            'idGenero': "Genero:",
            'idDocumento': "Tipo de Documento:",
            'documento': "Documento:",
           
        }
        widget = {
            'idEmpleado':forms.TextInput(attrs={'class':'form-control'}),
            'nombreEmpleado':forms.TextInput(attrs={'class':'form-control'}),
            'apellidoEmpleado':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.Textarea(attrs={'rows':4,'cols':40}),
            'contacto':forms.TextInput(attrs={'class':'form-control'}),
            'fechaNacimiento':forms.TextInput(attrs={'class':'form-control'}),
            'fechaIngreso':forms.TextInput(attrs={'class':'form-control'}),
            'idCargo':forms.Select(attrs={'class':'form-control'}),
            'idGenero':forms.Select(attrs={'class':'form-control'}),
            'idDocumento':forms.Select(attrs={'class':'form-control'}),
            'documento':forms.TextInput(attrs={'class':'form-control'}),
           

        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class ClienteForm(forms.ModelForm):
    nombreCliente = forms.CharField(min_length=3,max_length=50,label='Nombre:')
    direccion = forms.CharField(min_length=8,max_length=50,label='Dirección:')
    contacto = forms.CharField(min_length=8,max_length=50,label='Número telefónico:')
    documento = forms.CharField(min_length=13,max_length=50,label='Documento:')
    class Meta:
        model = Cliente
        fields = [
            'idCliente',
            'nombreCliente',
            'fechaNacimiento',
            'direccion',
            'contacto',
            'idDocumento',
            'documento',
            'idGenero',
                     
        ]
        labels = {
            'idCliente': "ID del Cliente:",
            'nombreCliente': "Nombre del Cliente:",
            'fechaNacimiento': "Fecha de Nacimiento:",
            'direccion': "Direccion:",
            'contacto': "Contacto:",
            'idDocumento': "Tipo de Documento:",
            'documento': "Documento:",
            'idGenero': "Genero:",
           
        }
        widget = {
            'idCliente':forms.TextInput(attrs={'class':'form-control'}),
            'nombreCliente':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.Textarea(attrs={'rows':4,'cols':40}),
            'fechaNacimiento':forms.TextInput(attrs={'class':'form-control'}),
            'contacto':forms.TextInput(attrs={'class':'form-control'}),
            'idDocumento':forms.Select(attrs={'class':'form-control'}),
            'documento':forms.TextInput(attrs={'class':'form-control'}),
            'idGenero':forms.Select(attrs={'class':'form-control'}),
       

        }
        

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class InformacionFisicaForm(forms.ModelForm):
    nombreCliente = forms.CharField(min_length=3,max_length=50,label='Nombre:')
    direccion = forms.CharField(min_length=8,max_length=50,label='Dirección:')
    contacto = forms.CharField(min_length=8,max_length=50,label='Número telefónico:')
    documento = forms.CharField(min_length=13,max_length=50,label='Documento:')
    class Meta:
        model = Cliente
        fields = [
            'idCliente',
            'nombreCliente',
            'fechaNacimiento',
            'direccion',
            'contacto',
            'idDocumento',
            'documento',
            'idGenero',
                     
        ]
        labels = {
            'idCliente': "ID del Cliente:",
            'nombreCliente': "Nombre del Cliente:",
            'fechaNacimiento': "Fecha de Nacimiento:",
            'direccion': "Direccion:",
            'contacto': "Contacto:",
            'idDocumento': "Tipo de Documento:",
            'documento': "Documento:",
            'idGenero': "Genero:",
           
        }
        widget = {
            'idCliente':forms.TextInput(attrs={'class':'form-control'}),
            'nombreCliente':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.Textarea(attrs={'rows':4,'cols':40}),
            'fechaNacimiento':forms.TextInput(attrs={'class':'form-control'}),
            'contacto':forms.TextInput(attrs={'class':'form-control'}),
            'idDocumento':forms.Select(attrs={'class':'form-control'}),
            'documento':forms.TextInput(attrs={'class':'form-control'}),
            'idGenero':forms.Select(attrs={'class':'form-control'}),
       

        }
        

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class InformacionFisicaForm(forms.ModelForm):
    peso = forms.DecimalField(min_value=1,max_digits=10,decimal_places=2,label="Peso:")
    altura = forms.DecimalField(min_value=1,max_digits=10,decimal_places=2,label="Altura:")
    cintura = forms.DecimalField(min_value=1,max_digits=10,decimal_places=2,label="Cintura:")
    pecho = forms.DecimalField(min_value=1,max_digits=10,decimal_places=2,label="Pecho:")
    brazo = forms.DecimalField(min_value=1,max_digits=10,decimal_places=2,label="Brazo:")

    
    class Meta:
        model = InformacionFisica
        fields = [
            'idInformacionFisica',
            'idCliente',
            'peso',
            'altura',
            'cintura',
            'pecho',
            'brazo',
            'fecha',
            
        ]
        labels = {
            'idInformacionFisica': "ID de Informacion Fisica:",
            'idCliente':"Cliente:",
            'peso':"Peso",
            'altura': "Altura:",
            'cintura': "Cintura:",
            'pecho': "Pecho:",
            'brazo': "Brazo:",
            'fecha': "Fecha:",

        }
        widget = {
            'idInformacionFisica':forms.TextInput(attrs={'class':'form-control'}),
            'idCliente':forms.Select(attrs={'class':'form-control'}),
            'peso':forms.TextInput(attrs={'class':'form-control'}),
            'altura':forms.TextInput(attrs={'class':'form-control'}),
            'cintura':forms.TextInput(attrs={'class':'form-control'}),
            'pecho':forms.TextInput(attrs={'class':'form-control'}),
            'brazo':forms.TextInput(attrs={'class':'form-control'}),
            'fecha':forms.TextInput(attrs={'class':'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class TipoMembresiaForm(forms.ModelForm):
    nombreTipoMembresia = forms.CharField(min_length=3,max_length=50,label='Membresia:')
    detalleTipoMembresia = forms.CharField(min_length=3,max_length=50,label='Detalle:')
    precio = forms.DecimalField(min_value=1,max_digits=10,decimal_places=2,label="Precio:")

    class Meta: 
        model = TipoMembresia
        fields = [
            'idTipoMembresia',
            'nombreTipoMembresia',
            'detalleTipoMembresia',
            'precio',
        ]
        labels = {
            'idTipoMembresia':"ID de Tipo Membresia:",
            'nombreTipoMembresia':"Nombre Tipo membresia:",
            'detalleTipoMembresia':"Descripcion:",
            'precio':"Precio:",


        }
        widget = {
            'idTipoMembresia':forms.TextInput(attrs={'class':'form-control'}),
            'nombreTipoMembresia':forms.TextInput(attrs={'class':'form-control'}),
            'detalleTipoMembresia':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),



        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class MembresiaForm(forms.ModelForm):

    class Meta: 
        model = Membresia
        fields = [
            'idMembresia',
            'fechaInicial',
            'fechaFinal',
            'idCliente',
            'idTipoMembresia',
        ]
        labels = {
            'idMembresia':"ID de Membresia:",
            'fechaInicial':"Fecha Inicial:",
            'fechaFinal':"Fecha Final:",
            'idCliente':"Cliente:",
            'idTipoMembresia':"Tipo membresia::",
        }
        widget = {
            'idMembresia':forms.TextInput(attrs={'class':'form-control'}),
            'fechaInicial':forms.TextInput(attrs={'class':'form-control'}),
            'fechaFinal':forms.TextInput(attrs={'class':'form-control'}),
            'idCliente':forms.Select(attrs={'class':'form-control'}),
            'idTipoMembresia':forms.Select(attrs={'class':'form-control'}),



        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class TipoRecetaNutricionalForm(forms.ModelForm):
    nombreTipoRecetaNutricional = forms.CharField(min_length=3,max_length=50,label='Tipo Receta Nutricional:')
    detalleTipoRecetaNutricional = forms.CharField(min_length=3,max_length=50,label='Detalle:')

    class Meta: 
        model = TipoRecetaNutricional
        fields = [
            'idTipoRecetaNutricional',
            'nombreTipoRecetaNutricional',
            'detalleTipoRecetaNutricional',
        ]
        labels = {
            'idTipoRecetaNutricional':"ID de Tipo Receta Nutricional:",
            'nombreTipoRecetaNutricional':"Nombre::",
            'detalleTipoRecetaNutricional':"Detalle:",


        }
        widget = {
            'idTipoRecetaNutricional':forms.TextInput(attrs={'class':'form-control'}),
            'nombreTipoRecetaNutricional':forms.TextInput(attrs={'class':'form-control'}),
            'detalleTipoRecetaNutricional':forms.TextInput(attrs={'class':'form-control'}),


        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class RecetaNutricionalForm(forms.ModelForm):
    ingredientes = forms.CharField(min_length=3,max_length=50,label='Ingredientes:')
    class Meta: 
        model = RecetaNutricional
        fields = [
            'idReceta',
            'ingredientes',
            'fecha',
            'idtipoRecetaNutricional',
        ]
        labels = {
            'idReceta':"ID de Receta Nutricional:",
            'ingredientes':"Ingredientes:",
            'fecha':"Fecha:",
            'idtipoRecetaNutricional':"Tipo de Receta:",


        }
        widget = {
            'idReceta':forms.TextInput(attrs={'class':'form-control'}),
            'ingredientes':forms.Textarea(attrs={'class':'form-control'}),
            'fecha':forms.TextInput(attrs={'class':'form-control'}),
            'idtipoRecetaNutricional':forms.Select(attrs={'class':'form-control'}),



        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class PlanNutricionalForm(forms.ModelForm):
    class Meta: 
        model = PlanNutricional
        fields = [
            'idPlanNutricional',
            'idCliente',
            'idReceta',
            'fechaInicial',
            'fechaFinal',
        ]
        labels = {
            'idPlanNutricional':"ID de Plan Nutricional:",
            'idCliente':"Cliente:",
            'idReceta':"Receta:",
            'fechaInicial':"Fecha Inicial:",
            'fechaFinal':"Fecha Final:",


        }
        widget = {
            'idPlanNutricional':forms.TextInput(attrs={'class':'form-control'}),
            'idCliente':forms.Select(attrs={'class':'form-control'}),
            'idReceta':forms.Select(attrs={'class':'form-control'}),
            'fechaInicial':forms.TextInput(attrs={'class':'form-control'}),
            'fechaFinal':forms.TextInput(attrs={'class':'form-control'}),


        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class TipoMaquinaForm(forms.ModelForm):
    nombreTipoMaquina = forms.CharField(min_length=3,max_length=50,label='Tipo Maquina:')
    detalleTipoMaquina = forms.CharField(min_length=3,max_length=50,label='Detalle:')

    class Meta: 
        model = TipoMaquina
        fields = [
            'idTipoMaquina',
            'nombreTipoMaquina',
            'detalleTipoMaquina',
        ]
        labels = {
            'idTipoMaquina':"ID de Tipo Maquina:",
            'nombreTipoMaquina':"Nombre::",
            'detalleTipoMaquina':"Detalle:",


        }
        widget = {
            'idTipoMaquina':forms.TextInput(attrs={'class':'form-control'}),
            'nombreTipoMaquina':forms.TextInput(attrs={'class':'form-control'}),
            'detalleTipoMaquina':forms.TextInput(attrs={'class':'form-control'}),


        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class EjerciciosRutinaForm(forms.ModelForm):
    nombreEjercicio = forms.CharField(min_length=3,max_length=50,label='Tipo Maquina:')
    series = forms.DecimalField(min_value=1,max_digits=10,decimal_places=2,label="Series:")
    repeticiones = forms.DecimalField(min_value=1,max_digits=10,decimal_places=2,label="Repeticiones:")
    descanso = forms.DecimalField(min_value=1,max_digits=10,decimal_places=2,label="Descanso:")

    class Meta: 
        model = EjerciciosRutina
        fields = [
            'idEjerciciosRutina',
            'nombreEjercicio',
            'series',
            'repeticiones',
            'descanso',
            'idTipoMaquina',
        ]
        labels = {
            'idEjerciciosRutina':"ID de Rutina de Ejercicio:",
            'nombreEjercicio':"Nombre::",
            'series':"Series:",
            'repeticiones':"Repeticiones:",
            'descanso':"Descanso:",
            'idTipoMaquina':"Tipo de Maquina:",


        }
        widget = {
            'idEjerciciosRutina':forms.TextInput(attrs={'class':'form-control'}),
            'nombreEjercicio':forms.TextInput(attrs={'class':'form-control'}),
            'series':forms.TextInput(attrs={'class':'form-control'}),
            'repeticiones':forms.TextInput(attrs={'class':'form-control'}),
            'descanso':forms.TextInput(attrs={'class':'form-control'}),
            'idTipoMaquina':forms.Select(attrs={'class':'form-control'}),


        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class RutinaForm(forms.ModelForm):
    class Meta: 
        model = Rutina
        fields = [
            'idRutina',
            'fechaInicial',
            'fechaFinal',
            'idCliente',
            'idEjerciciosRutina',
        ]
        labels = {
            'idRutina':"ID de Rutina:",
            'fechaInicial':"Fecha Inicio::",
            'fechaFinal':"Fecha Final:",
            'idCliente':"Cliente:",
            'idEjerciciosRutina':"Rutina de Ejercicios:",

        }
        widget = {
            'idRutina':forms.TextInput(attrs={'class':'form-control'}),
            'fechaInicial':forms.TextInput(attrs={'class':'form-control'}),
            'fechaFinal':forms.TextInput(attrs={'class':'form-control'}),
            'idCliente':forms.Select(attrs={'class':'form-control'}),
            'idEjerciciosRutina':forms.Select(attrs={'class':'form-control'}),


        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class SalonForm(forms.ModelForm):
    nombreSalon = forms.CharField(min_length=3,max_length=50,label='Salon:')
    descripcionSalon = forms.CharField(min_length=3,max_length=50,label='Descripcion:')

    class Meta: 
        model = Salon
        fields = [
            'idSalon',
            'nombreSalon',
            'descripcionSalon',
        ]
        labels = {
            'idSalon':"ID de Salon:",
            'nombreSalon':"Nombre:",
            'descripcionSalon':"Descripcion:",


        }
        widget = {
            'idSalon':forms.TextInput(attrs={'class':'form-control'}),
            'nombreSalon':forms.TextInput(attrs={'class':'form-control'}),
            'descripcionSalon':forms.TextInput(attrs={'class':'form-control'}),

        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class ClasesForm(forms.ModelForm):
    nombreClases = forms.CharField(min_length=3,max_length=50,label='Clases:')
    detalleClases = forms.CharField(min_length=3,max_length=50,label='Detalles:')

    class Meta: 
        model = Clases
        fields = [
            'idClases',
            'nombreClases',
            'detalleClases',
            'idSalon',
        ]
        labels = {
            'idClases':"ID de Clases:",
            'nombreClases':"Nombre:",
            'detalleClases':"Detalles:",
            'idSalon':"Salon:",


        }
        widget = {
            'idClases':forms.TextInput(attrs={'class':'form-control'}),
            'nombreClases':forms.TextInput(attrs={'class':'form-control'}),
            'detalleClases':forms.TextInput(attrs={'class':'form-control'}),
            'idSalon':forms.TextInput(attrs={'class':'form-control'}),

        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class ClasesClienteForm(forms.ModelForm):
    class Meta: 
        model = ClasesCliente
        fields = [
            'idClasesCliente',
            'fechaInicial',
            'fechaFinal',
            'idCliente',
            'idClases',
        ]
        labels = {
            'idClasesCliente':"ID de Rutina:",
            'fechaInicial':"Fecha Inicio::",
            'fechaFinal':"Fecha Final:",
            'idCliente':"Cliente:",
            'idClases':"Clases:",

        }
        widget = {
            'idClasesCliente':forms.TextInput(attrs={'class':'form-control'}),
            'fechaInicial':forms.TextInput(attrs={'class':'form-control'}),
            'fechaFinal':forms.TextInput(attrs={'class':'form-control'}),
            'idCliente':forms.Select(attrs={'class':'form-control'}),
            'idClases':forms.Select(attrs={'class':'form-control'}),


        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )
class PlanillaForm(forms.ModelForm):
    nombrePlanilla = forms.CharField(min_length=3,max_length=50,label='Planilla:')
    detallePlanilla = forms.CharField(min_length=3,max_length=50,label='Detalles:')
    class Meta: 
        model = Planilla
        fields = [
            'idPlanilla',
            'nombrePlanilla',
            'fechaInicial',
            'fechaFinal',
            'fechaPago',
            'detallePlanilla',
        ]
        labels = {
            'idPlanilla':"ID de Planilla:",
            'nombrePlanilla':"Nomre:",
            'fechaInicial':"Fecha Inicio::",
            'fechaFinal':"Fecha Final:",
            'fechaPago':"Fecha Pago:",
            'detallePlanilla':"Detalles:",

        }
        widget = {
            'idPlanilla':forms.TextInput(attrs={'class':'form-control'}),
            'nombrePlanilla':forms.TextInput(attrs={'class':'form-control'}),
            'fechaInicial':forms.TextInput(attrs={'class':'form-control'}),
            'fechaFinal':forms.TextInput(attrs={'class':'form-control'}),
            'fechaPago':forms.TextInput(attrs={'class':'form-control'}),
            'detallePlanilla':forms.TextInput(attrs={'class':'form-control'}),


        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class TipoBonoForm(forms.ModelForm):
    nombreTipoBono = forms.CharField(min_length=3,max_length=50,label='Tipo Bono:')
    descripcionTipoBono = forms.CharField(min_length=3,max_length=50,label='Descripcion:')

    class Meta: 
        model = TipoBono
        fields = [
            'idTipoBono',
            'nombreTipoBono',
            'descripcionTipoBono',
        ]
        labels = {
            'idTipoBono':"ID de Tipo Bono:",
            'nombreTipoBono':"Nombre:",
            'descripcionTipoBono':"Descripcion:",


        }
        widget = {
            'idTipoBono':forms.TextInput(attrs={'class':'form-control'}),
            'nombreTipoBono':forms.TextInput(attrs={'class':'form-control'}),
            'descripcionTipoBono':forms.TextInput(attrs={'class':'form-control'}),

        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class BonoForm(forms.ModelForm):
    monto = forms.DecimalField(min_value=1,max_digits=10,decimal_places=2,label="Monto:")

    class Meta: 
        model = Bono
        fields = [
            'idBono',
            'monto',
            'fecha',
            'idEmpleado',
            'idPlanilla',
            'idTipoBono',
        ]
        labels = {
            'idBono':"ID de Bono:",
            'monto':"Nombre:",
            'fecha':"Fecha:",
            'idEmpleado':"Empleado:",
            'idPlanilla':"Planilla:",
            'idTipoBono':"Tipo de Bono:",

        }
        widget = {
            'idBono':forms.TextInput(attrs={'class':'form-control'}),
            'monto':forms.TextInput(attrs={'class':'form-control'}),
            'fecha':forms.TextInput(attrs={'class':'form-control'}),
            'idEmpleado':forms.Select(attrs={'class':'form-control'}),
            'idPlanilla':forms.Select(attrs={'class':'form-control'}),
            'idTipoBono':forms.Select(attrs={'class':'form-control'}),

        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )

class CargoEmpleadoForm(forms.ModelForm):
    class Meta: 
        model = CargoEmpleado
        fields = [
            'idCargoEmpleado',
            'fechaInicial',
            'fechaFinal',
            'idCargo',
            'idEmpleado',
        ]
        labels = {
            'idCargoEmpleado':"ID de Cargo de Empleado:",
            'fechaInicial':"Fecha Inicio:",
            'fechaFinal':"Fecha Final:",
            'idCargo':"Cargo:",
            'idEmpleado':"Empleado:",

        }
        widget = {
            'idCargoEmpleado':forms.TextInput(attrs={'class':'form-control'}),
            'fechaInicial':forms.TextInput(attrs={'class':'form-control'}),
            'fechaFinal':forms.TextInput(attrs={'class':'form-control'}),
            'idCargo':forms.Select(attrs={'class':'form-control'}),
            'idEmpleado':forms.Select(attrs={'class':'form-control'}),


        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {
                        'class':'form-control'
                    }
                )