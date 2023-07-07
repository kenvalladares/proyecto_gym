from django.db import models
from django.core.validators import RegexValidator
from django.forms import ValidationError
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save, post_delete, pre_delete
from datetime import timedelta, datetime



identidad =RegexValidator(r'^[[0,1]{1}[0-9]{3}[0-9]{9}]*$',"No puede ingresar letras en este campo, este campo debe comenzar con 0 o 1, este campo debe tener 13 digitos") 

letters = RegexValidator(r'^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$',"No puede ingresar números a este campo.")
repeatedLetters = RegexValidator(r'^(?!.*(\w)\1{2,}).+$', "No se pueden ingresar letras repetidas más de 2 veces")
Numeros = RegexValidator(r'^[0-9 ]*$',"No puede ingresar letras a este campo.")
rtnn =RegexValidator(r'^[[01,10]{1}[0-9]{3}[0-9]{10}]*$',"No puede ingresar letras en este campo, este campo debe comenzar con 0 o 1, este campo debe tener 14 digitos") 
numbers = RegexValidator(r'^[[2,3,7,8,9]{1}[0-9]{3}[0-9]{4}]*$',"No puede ingresar letras en este campo, este campo debe comenzar con 2,3,8,9, este campo debe tener 8 digitos") 

class GeneroPersona(models.Model):
    idGenero = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombreGenero = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Genero')

    def __str__(self):
        return self.nombreGenero

    def clean(self):
        nombreGenero = self.nombreGenero
       
        if '  ' in nombreGenero:
            raise ValidationError('No se permiten doble espacios en el nombre de Genero')
        return nombreGenero
    
class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombreCategoria = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Categoria')
    descripcionCategoria = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Descripcion')

    def __str__(self):
        return self.nombreCategoria

    def clean(self):
        nombreCategoria = self.nombreCategoria
       
        if '  ' in nombreCategoria:
            raise ValidationError('No se permiten doble espacios en el nombre de Categoria')
        return nombreCategoria

class Proveedores(models.Model):
    idProveedor = models.AutoField(primary_key=True,null=False,verbose_name='ID')
    NombreProveedor = models.CharField(max_length=200,unique=True,verbose_name='Nombre',validators=[repeatedLetters])
    Direccion = models.CharField(max_length=200,verbose_name='Dirección',validators=[repeatedLetters])
    Contacto = models.CharField(max_length=8,validators=[numbers,Numeros],verbose_name='Número telefónico')
    rtnProveedor = models.CharField(help_text=("formato xxxx-xxxx-xxxxx") ,max_length=50,validators=[Numeros,rtnn],verbose_name='RTN')

    def __str__(self):
        return self.NombreProveedor

    def clean(self):
        nombreProveedor = self.NombreProveedor
        direccionProveedor = self.Direccion
        if '  ' in nombreProveedor:
            raise ValidationError('No se permiten doble espacios en el nombre de Proveedor')
        elif '  ' in direccionProveedor:
            raise ValidationError('No se permiten doble espacios en la dirección de Proveedor')
        return nombreProveedor,direccionProveedor

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

class Impuestos(models.Model):
    idImpuesto = models.AutoField(primary_key=True,null=False,verbose_name='ID de Impuesto')
    nombre = models.CharField(max_length=50,unique = True,verbose_name='Nombre')
    fechaInicial = models.DateField(blank=False,verbose_name='Fecha Inicial')
    fechaFinal = models.DateField(blank=True,null=True,verbose_name='Fecha Final')
    valor = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Valor',unique=True)

    def __str__(self):
        return str(self.valor)

    def clean(self):
        nombre = self.nombre
        if '  ' in nombre:
            raise ValidationError('No se permiten doble espacios en el nombre de Impuesto')
        if self.fechaInicial:
            if self.fechaFinal:
                if self.fechaInicial >= self.fechaFinal:
                    raise ValidationError(('La fecha final debe ser posterior a la fecha inicial'))
        return nombre
    
    class Meta: 
        verbose_name = "Impuesto"
        verbose_name_plural = "Impuestos"

class Productos(models.Model):
    idProducto = models.AutoField(primary_key=True,null=False,verbose_name='ID')
    nombreProducto = models.CharField(max_length=100,unique = True,verbose_name='Nombre de Producto',validators=[repeatedLetters])
    descripcion = models.CharField(max_length=2000,verbose_name='Descripción',validators=[repeatedLetters])
    precio = models.DecimalField(max_digits=10,decimal_places=2,blank=False,verbose_name='Precio')
    idImpuesto = models.ForeignKey(Impuestos,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Impuesto')
    descuento = models.DecimalField(max_digits=10,null=True,decimal_places=2,verbose_name='Descuento')
    idCategoria = models.ForeignKey(Categoria,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Categoria')
    idProveedor = models.ForeignKey(Proveedores,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Proveedor')
    stockMinimo = models.IntegerField(verbose_name='Stock Mínimo')
    stockMaximo = models.IntegerField(verbose_name='Stock Máximo')
    imagenProducto = models.ImageField(null=True,blank=True,verbose_name='Imagen de Producto')
        
    def __str__(self):
        return self.nombreProducto

    def clean(self):
        nombreProducto = self.nombreProducto
        descripcion = self.descripcion
        if '  ' in nombreProducto:
            raise ValidationError('No se permiten doble espacios en el nombre del Producto')
        elif '  ' in descripcion:
            raise ValidationError('No se permiten doble espacios en la descripción del Producto')
        return nombreProducto,descripcion

    def impuestoProducto(self):
        return self.precio * self.idImpuesto.valor

    def descuentoProducto(self):
        return self.precio * self.descuento

    
    @property
    def imageURL(self):
        try:
            url = self.imagenProducto.url
        except: 
            url = ''
        return url

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Inventario(models.Model):
    idInventario = models.AutoField(primary_key=True,null=False,verbose_name='ID')  
    idProducto = models.ForeignKey(Productos,null=False,blank=False,unique=True,on_delete=models.CASCADE,verbose_name='Producto')
    stockActual = models.IntegerField(verbose_name='Stock Actual')
    
    def __str__(self):
        return str(self.idProducto.nombreProducto)

    class Meta:
        verbose_name = "al Inventario"
        verbose_name_plural = "Inventario"
    
class Compras(models.Model):
    idCompra = models.AutoField(primary_key=True,null=False,verbose_name='ID')  
    idProveedor = models.ForeignKey(Proveedores,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Proveedor')
    detalle = models.CharField(max_length=2000,null=True,blank=True,verbose_name='Detalle de Compra',validators=[repeatedLetters])
    idInventario = models.ForeignKey(Inventario,null=True,blank=False,on_delete=models.CASCADE,verbose_name='Inventario')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio = models.DecimalField(max_digits=10,decimal_places=2,blank=False,verbose_name='Precio')
    fechaPedido = models.DateField(blank=False,verbose_name='Fecha de Pedido')
    fechaEntrega = models.DateField(blank=False,verbose_name='Fecha de Entrega')
    fechaEnvio = models.DateField(blank=False,verbose_name='Fecha de Envío')

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
    def __str__(self):
        return "ID: "+str(self.idCompra)

    def clean(self):
        detalle = self.detalle
        if self.fechaPedido and self.fechaEnvio and self.fechaEntrega:
            if self.fechaPedido > self.fechaEntrega:
                raise ValidationError(('La fecha de entrega debe ser posterior a la fecha de pedido'))
            elif self.fechaPedido > self.fechaEnvio:
                raise ValidationError(('La fecha de envio debe ser posterior a la fecha de pedido'))
            elif self.fechaEntrega < self.fechaEnvio:
                raise ValidationError(('La fecha de entrega debe ser posterior a la fecha de envio'))
        if detalle:
            if '  ' in detalle:
                raise ValidationError('No se permiten doble espacios en el detalle de Compras')
            return detalle
        
    
@receiver(post_save, sender = Compras)
def add_productos_inventario(sender,created, instance, **kwargs):
    
    if created:
        inv = instance.idInventario.idInventario
        items = Compras.objects.filter(idInventario = inv)
        stock = 0 
        for i in items:
            stock = abs(i.idInventario.stockActual + i.cantidad)

        instance.idInventario.stockActual = stock
    instance.idInventario.save()
    
class TipoDeduccion(models.Model):
    idTipoDeduccion = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombreTipoDeduccion = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Tipo de Deduccion')
    descripcionTipoDeduccion = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Descripcion')

    def __str__(self):
        return self.nombreTipoDeduccion

    def clean(self):
        nombreTipoDeduccion = self.nombreTipoDeduccion
       
        if '  ' in nombreTipoDeduccion:
            raise ValidationError('No se permiten doble espacios en el nombre de Tipo de Deduccion')
        return nombreTipoDeduccion
    
    class Meta:
        verbose_name = "Tipo Deduccion"
        verbose_name_plural = "Tipo Deduccion"

class TipoDocumento(models.Model):
    idDocumento = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombreDocumento = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Documento')

    def __str__(self):
        return self.nombreDocumento

    def clean(self):
        nombreDocumento = self.nombreDocumento
       
        if '  ' in nombreDocumento:
            raise ValidationError('No se permiten doble espacios en el nombre de Documento')
        return nombreDocumento

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

class Cargo(models.Model):
    idCargo = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombreCargo = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Cargo')
    descripcionCargo = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Descripcion')

    def __str__(self):
        return self.nombreCargo

    def clean(self):
        nombreCargo = self.nombreCargo
       
        if '  ' in nombreCargo:
            raise ValidationError('No se permiten doble espacios en el nombre de Cargo')
        return nombreCargo

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True,null=False,verbose_name='ID de Empleado')
    nombreEmpleado = models.CharField(max_length=50,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Nombre')
    apellidoEmpleado = models.CharField(max_length=50,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Apellido')
    direccion = models.CharField(max_length=200,verbose_name='Dirección',validators=[repeatedLetters])
    contacto = models.CharField(max_length=50,null=True,validators=[numbers], blank=True,verbose_name='Contacto')
    fechaNacimiento = models.DateField(blank=False,verbose_name='Fecha de Nacimiento')
    fechaIngreso = models.DateField(blank=False,verbose_name='Fecha de Ingreso')
    idCargo = models.ForeignKey(Cargo,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Cargo') 
    idDocumento = models.ForeignKey(TipoDocumento,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Documento') 
    documento = models.CharField(max_length=50,null=False, blank=True,verbose_name='Documento')
    idGenero = models.ForeignKey(GeneroPersona,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Genero') 


    
    def clean(self):
        nombreEmpleado = self.nombreEmpleado
        apellidoEmpleado = self.apellidoEmpleado
        direccion = self.direccion
        
        if self.fechaNacimiento:
            if self.fechaNacimiento > (datetime.now().date() - timedelta(days=6574,)):
                raise ValidationError(('La fecha de Nacimiento debe ser mayor a 18 años')) 
            if self.fechaNacimiento < (datetime.now().date() - timedelta(days=31025,)):
                raise ValidationError(('El empleado no puede ser mayor a 85 años'))
        if self.fechaIngreso:
            if self.fechaIngreso > (datetime.now().date() + timedelta(days=6574)):
                raise ValidationError(('La fecha de ingreso no puede ser mayor a hoy'))
            elif self.fechaIngreso > (datetime.now().date()):
                raise ValidationError(('la fecha de ingreso no puede estar adelantada a la fecha de hoy'))
            if self.fechaIngreso < self.fechaNacimiento:
                raise ValidationError(('La fecha de Ingreso no puede ser menor a la fecha de Nacimiento'))
            
        if '  ' in nombreEmpleado:
            raise ValidationError('No se permiten doble espacios en el nombre de Empleado')
        if '  ' in apellidoEmpleado:
            raise ValidationError('No se permiten doble espacios en el nombre de Empleado')
        if '  ' in direccion:
            raise ValidationError('No se permiten doble espacios en la dirección del Empleado')
            
       
    def __str__(self):
        return self.nombreEmpleado

    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True,null=False,verbose_name='ID de Cliente')
    nombreCliente = models.CharField(max_length=50,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Nombre')
    fechaNacimiento = models.DateField(blank=False,verbose_name='Fecha de Nacimiento')
    direccion = models.CharField(max_length=200,verbose_name='Dirección',validators=[repeatedLetters])
    contacto = models.CharField(max_length=50,null=True,validators=[numbers], blank=True,verbose_name='Contacto')
    idDocumento = models.ForeignKey(TipoDocumento,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Documento')     
    documento = models.CharField(max_length=50,null=False,unique=True,validators=[identidad], blank=True,verbose_name='Documento')
    idGenero = models.ForeignKey(GeneroPersona,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Genero') 

    def __str__(self):
        return self.nombreCliente

   

    def clean(self):
        nombreCliente = self.nombreCliente
        direccionCliente = self.direccion
        if self.fechaNacimiento:
            if self.fechaNacimiento > (datetime.now().date() - timedelta(days=6574,)):
                raise ValidationError(('La fecha de Nacimiento debe ser mayor a 18 años')) 
            if self.fechaNacimiento < (datetime.now().date() - timedelta(days=31025,)):
                raise ValidationError(('El empleado no puede ser mayor a 85 años'))
        if '  ' in nombreCliente:
            raise ValidationError('No se permiten doble espacios en el nombre de Cliente')
        elif '  ' in direccionCliente:
            raise ValidationError('No se permiten doble espacios en la dirección del Cliente')
        return nombreCliente,direccionCliente

        

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class InformacionFisica(models.Model):
    idInformacionFisica = models.AutoField(primary_key=True,null=False,verbose_name='ID de Informacion Fisica')
    idCliente = models.ForeignKey(Cliente,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Cliente') 
    peso = models.DecimalField(max_digits=10,decimal_places=2,blank=False,verbose_name='Peso')
    altura = models.DecimalField(max_digits=10,decimal_places=2,blank=False,verbose_name='Altura')
    cintura = models.DecimalField(max_digits=10,decimal_places=2,blank=False,verbose_name='Cintura')
    pecho = models.DecimalField(max_digits=10,decimal_places=2,blank=False,verbose_name='Pecho')
    brazo = models.DecimalField(max_digits=10,decimal_places=2,blank=False,verbose_name='Brazo')
    fecha = models.DateField(blank=False,verbose_name='Fecha')


    def __str__(self):
        return self.idCliente.nombreCliente
    def clean(self):
        if self.peso<50:
            raise ValidationError('El peso no puede ser menor a 50 kg')
        

    class Meta:
        verbose_name = "Informacion Fisica"
        verbose_name_plural = "Informacion Fisicas"

class TipoMembresia(models.Model):
    idTipoMembresia = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombreTipoMembresia = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Membresia')
    detalleTipoMembresia = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Detalle')
    precio = models.DecimalField(max_digits=10,decimal_places=2,blank=False,verbose_name='Precio')


    def __str__(self):
        return self.nombreTipoMembresia

    def clean(self):
        nombreTipoMembresia = self.nombreTipoMembresia
       
        if '  ' in nombreTipoMembresia:
            raise ValidationError('No se permiten doble espacios en el nombre de Tipo Membresia')
        return nombreTipoMembresia

    class Meta:
        verbose_name = "Tipo Membresia"
        verbose_name_plural = "Tipo Membresias"

class Membresia(models.Model):
    idMembresia = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    fechaInicial = models.DateField(blank=False,verbose_name='Fecha Inicial')
    fechaFinal = models.DateField(blank=False,verbose_name='Fecha Final')
    idCliente = models.ForeignKey(Cliente,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Cliente') 
    idTipoMembresia = models.ForeignKey(TipoMembresia,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Tipo Membresia') 

    def __str__(self):
        return str(self.idMembresia)

    def clean(self):
        if self.fechaFinal < (self.fechaInicial + timedelta(days=30,)):
            raise ValidationError(('La fecha Final debe ser 1 mes posterior a la fecha Inicial  '))
        if self.fechaInicial < (datetime.now().date()):
            raise ValidationError(('La fecha Inicial debe ser mayor a hoy'))


    class Meta:
        verbose_name = "Membresia"
        verbose_name_plural = "Membresias"

class TipoRecetaNutricional(models.Model):
    idTipoRecetaNutricional = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombreTipoRecetaNutricional = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Nombre')
    detalleTipoRecetaNutricional = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Detalle')


    def __str__(self):
        return self.nombreTipoRecetaNutricional

    def clean(self):
        nombreTipoRecetaNutricional = self.nombreTipoRecetaNutricional
       
        if '  ' in nombreTipoRecetaNutricional:
            raise ValidationError('No se permiten doble espacios en el nombre de Tipo Receta Nutricional')
        return nombreTipoRecetaNutricional

    class Meta:
        verbose_name = "Tipo Receta Nutricional"
        verbose_name_plural = "Tipo Receta Nutricional"

class RecetaNutricional(models.Model):
    idReceta = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    ingredientes = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Ingredientes')
    fecha = models.DateField(blank=False,verbose_name='Fecha')
    idtipoRecetaNutricional = models.ForeignKey(TipoRecetaNutricional,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Tipo Receta') 

    def __str__(self):
        return "ID:"+str(self.idReceta)

    def clean(self):
        if self.fecha < (datetime.now().date()):
            raise ValidationError(('La fecha debe ser mayor a hoy'))


    class Meta:
        verbose_name = "Receta Nutricional"
        verbose_name_plural = "Receta Nutricional"

class PlanNutricional(models.Model):
    idPlanNutricional = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    idCliente = models.ForeignKey(Cliente,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Cliente') 
    idReceta = models.ForeignKey(RecetaNutricional,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Receta') 
    fechaInicial = models.DateField(blank=False,verbose_name='Fecha Inicial')
    fechaFinal = models.DateField(blank=True,verbose_name='Fecha Final')

    def __str__(self):
        return "ID:"+str(self.idPlanNutricional)

    def clean(self):
        if self.fechaInicial < (datetime.now().date()):
            raise ValidationError(('La fecha Inicial debe ser mayor a hoy'))
        if self.fechaInicial >= self.fechaFinal:
                raise ValidationError(('La fecha final debe ser posterior a la fecha inicial'))


    class Meta:
        verbose_name = "Plan Nutricional"
        verbose_name_plural = "Plan Nutricional"

class TipoMaquina(models.Model):
    idTipoMaquina = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombreTipoMaquina = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Nombre')
    detalleTipoMaquina = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Detalle')


    def __str__(self):
        return self.nombreTipoMaquina

    def clean(self):
        nombreTipoMaquina = self.nombreTipoMaquina
       
        if '  ' in nombreTipoMaquina:
            raise ValidationError('No se permiten doble espacios en el nombre de Tipo Maquina')
        return nombreTipoMaquina

    class Meta:
        verbose_name = "Tipo Maquina"
        verbose_name_plural = "Tipo Maquina"

class EjerciciosRutina(models.Model):
    idEjerciciosRutina = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombreEjercicio = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Nombre')
    series = models.DecimalField(max_digits=10,decimal_places=2,blank=False,verbose_name='Series')
    repeticiones = models.DecimalField(max_digits=10,decimal_places=2,blank=False,verbose_name='Repeticiones')
    descanso = models.DecimalField(max_digits=10,decimal_places=2,blank=False,verbose_name='Descanso')
    idTipoMaquina = models.ForeignKey(TipoMaquina,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Tipo Maquina') 



    def __str__(self):
        return self.nombreEjercicio

    def clean(self):
        nombreEjercicio = self.nombreEjercicio
       
        if '  ' in nombreEjercicio:
            raise ValidationError('No se permiten doble espacios en el nombre de Ejercicios')
        return nombreEjercicio

    class Meta:
        verbose_name = "Ejercicios Rutina"
        verbose_name_plural = "Ejercicios Rutinas"

class Rutina(models.Model):
    idRutina = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    fechaInicial = models.DateField(blank=False,verbose_name='Fecha Inicial')
    fechaFinal = models.DateField(blank=False,null=True,verbose_name='Fecha Final')
    idCliente = models.ForeignKey(Cliente,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Cliente') 
    idEjerciciosRutina = models.ForeignKey(EjerciciosRutina,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Rutina') 

    def __str__(self):
        return self.idRutina

    def clean(self):
        if self.fechaInicial < (datetime.now().date()):
            raise ValidationError(('La fecha Inicial debe ser mayor a hoy'))
        if self.fechaInicial >= self.fechaFinal:
                raise ValidationError(('La fecha final debe ser posterior a la fecha inicial'))
    class Meta:
        verbose_name = "Rutina"
        verbose_name_plural = "Rutinas"

class Salon(models.Model):
    idSalon = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombreSalon = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Salon')
    descripcionSalon = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Descripcion')

    def __str__(self):
        return self.nombreSalon

    def clean(self):
        nombreSalon = self.nombreSalon
       
        if '  ' in nombreSalon:
            raise ValidationError('No se permiten doble espacios en el nombre del Salon')
        return nombreSalon
    
    class Meta:
        verbose_name = "Salon"
        verbose_name_plural = "Salon"

class Clases(models.Model):
    idClases = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombreClases = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Clases')
    detalleClases = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Detalle')
    idSalon = models.ForeignKey(Salon,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Salon') 

    def __str__(self):
        return self.nombreClases

    def clean(self):
        nombreClases = self.nombreClases
       
        if '  ' in nombreClases:
            raise ValidationError('No se permiten doble espacios en el nombre de la Clases')
        return nombreClases


    class Meta:
        verbose_name = "Clases"
        verbose_name_plural = "Clases"

class ClasesCliente(models.Model):
    idClasesCliente = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    fechaInicial = models.DateField(blank=False,verbose_name='Fecha Inicial')
    fechaFinal = models.DateField(blank=False,null=True,verbose_name='Fecha Final')
    idCliente = models.ForeignKey(Cliente,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Cliente') 
    idClases = models.ForeignKey(Clases,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Clases') 

    def __str__(self):
        return self.idClasesCliente

    def clean(self):
        if self.fechaInicial < (datetime.now().date()):
            raise ValidationError(('La fecha Inicial debe ser mayor a hoy'))
        if self.fechaInicial >= self.fechaFinal:
                raise ValidationError(('La fecha final debe ser posterior a la fecha inicial'))
    class Meta:
        verbose_name = "Clases Clientes"
        verbose_name_plural = "Clases Clientes"

class Planilla(models.Model):
    idPlanilla = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombrePlanilla = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Nombre')
    fechaInicial = models.DateField(blank=False,verbose_name='Fecha Inicial')
    fechaFinal = models.DateField(blank=False,null=True,verbose_name='Fecha Final')
    fechaPago = models.DateField(blank=False,null=True,verbose_name='Fecha Final')
    detallePlanilla = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Detalle')

    def __str__(self):
        return self.idPlanilla

    def clean(self):
        if self.fechaInicial < (datetime.now().date()):
            raise ValidationError(('La fecha Inicial debe ser mayor a hoy'))
        if self.fechaInicial >= self.fechaFinal:
                raise ValidationError(('La fecha final debe ser posterior a la fecha inicial'))
        if self.fechaPago < (datetime.now().date()):
            raise ValidationError(('La fecha Pago debe ser mayor a hoy'))

    class Meta:
        verbose_name = "Planilla"
        verbose_name_plural = "Planillas"

class TipoBono(models.Model):
    idTipoBono = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    nombreTipoBono = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Tipo Bono')
    descripcionTipoBono = models.CharField(max_length=50,unique = True,null=False,validators=[letters,repeatedLetters], blank=True,verbose_name='Descripcion')

    def __str__(self):
        return self.nombreTipoBono

    def clean(self):
        nombreTipoBono = self.nombreTipoBono
       
        if '  ' in nombreTipoBono:
            raise ValidationError('No se permiten doble espacios en el nombre del Tipo de Bono')
        return nombreTipoBono
    
    class Meta:
        verbose_name = "Tipo Bono"
        verbose_name_plural = "Tipo Bonos"

class Bono(models.Model):
    idBono = models.AutoField(primary_key=True,null=False,verbose_name='ID') 
    monto = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Monto',unique=True)
    fecha = models.DateField(blank=False,verbose_name='Fecha')
    idEmpleado = models.ForeignKey(Empleado,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Empleado') 
    idPlanilla = models.ForeignKey(Planilla,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Planilla') 
    idTipoBono = models.ForeignKey(TipoBono,null=False,blank=False,on_delete=models.CASCADE,verbose_name='TipoBono') 

    def __str__(self):
        return self.idBono

    def clean(self):
         if self.fecha < (datetime.now().date()):
            raise ValidationError(('La fecha debe ser mayor a hoy'))

    class Meta:
        verbose_name = "Bono"
        verbose_name_plural = "Bonos"

class CargoEmpleado(models.Model):
    idCargoEmpleado = models.AutoField(primary_key=True,null=False,verbose_name='ID de Cargo Empleado')
    fechaInicial = models.DateField(blank=False,verbose_name='Fecha Inicial')
    fechaFinal = models.DateField(blank=False,null=True,verbose_name='Fecha Final')
    idEmpleado = models.ForeignKey(Empleado,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Empleado') 
    idCargo = models.ForeignKey(Cargo,null=False,blank=False,on_delete=models.CASCADE,verbose_name='Cargo') 

    def __str__(self):
        return str(self.idCargoEmpleado)

    def clean(self):
        if self.fechaInicial >= self.fechaFinal:
            raise ValidationError(('La fecha final debe ser posterior a la fecha inicial'))
        if self.fechaInicial < (datetime.now().date()):
            raise ValidationError(('La fecha debe ser mayor a hoy'))

    class Meta: 
        verbose_name = "Cargo Empleado"
        verbose_name_plural = "Cargo Empleado"

