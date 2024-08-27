from app import models, columns


class DetalleRecibo(models.Model):
    _table = 'detalle_recibo'
    _description = 'Detalle de Recibo'

    _columns = {
        'tipo_concepto': columns.VarChar('Tipo de Concepto'),
        'cantidad': columns.Integer('Cantidad'),
        'monto': columns.Integer('Monto')
    }
