from app import models, columns


class Funcionario(models.Model):
    _table = 'funcionarios'
    _description = 'Funcionario'

    _columns = {
        'cedula': columns.VarChar('Cédula'),
        'nombre': columns.VarChar('Nombre'),
        'cargo': columns.VarChar('Cargo'),
        'sueldo': columns.Integer('Sueldo'),
        'fecha_ingreso': columns.VarChar('Fecha de Ingreso')
    }
