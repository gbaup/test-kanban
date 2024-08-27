from app import models, columns
from . import funcionario, detalle_recibo


class ReciboSueldo(models.Model):
    _table = 'recibos_sueldo'
    _description = 'Recibo de Sueldo'

    _columns = {
        'anio': columns.Integer('Año'),
        'mes': columns.Integer('Mes'),
        'tipo_recibo': columns.VarChar('Tipo de Recibo'),
        'cedula_funcionario': columns.Relation('Cédula Funcionario', funcionario.Funcionario),
        'nombre_empleador': columns.VarChar('Nombre del Empleador'),
        'detalle_recibo_id': columns.Relation('Detalle Recibo', detalle_recibo.DetalleRecibo)
    }
