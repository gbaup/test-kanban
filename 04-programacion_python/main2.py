import csv

from models import funcionario, recibo_sueldo, detalle_recibo


def cargar_datos_desde_csv(filename):
    with (open(filename, mode='r') as file):
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            empleado = funcionario.Funcionario.create({
                'cedula': row['cedula'],
                'nombre': row['nombre'],
                'cargo': row['cargo'],
                'sueldo': float(row['sueldo']),
                'fecha_ingreso': row['fecha_ingreso']
            })

            detalle = detalle_recibo.DetalleRecibo.create({
                'tipo_concepto': row['tipo_concepto'],
                'cantidad': int(row['cantidad']),
                'monto': float(row['monto'])
            })

            recibo = recibo_sueldo.ReciboSueldo.create({
                'anio': int(row['anio']),
                'mes': int(row['mes']),
                'tipo_recibo': row['tipo_recibo'],
                'cedula_funcionario': funcionario.Funcionario.cedula,
                'nombre_empleador': row['nombre_empleador'],
                'detalle_recibo_id': [detalle]
            })


def eliminar_recibos_por_cedula(cedula):
    recibos = recibo_sueldo.search([('cedula_funcionario', '=', cedula)])
    for recibo in recibos:
        recibo.delete()
    print(f"Recibos de sueldo del funcionario con cédula {cedula} han sido eliminados.")


def modificar_funcionario_por_cedula(cedula, nuevo_nombre, nuevo_cargo):
    empleado = funcionario.search([('cedula', '=', cedula)])
    if empleado:
        empleado.update({
            'nombre': nuevo_nombre,
            'cargo': nuevo_cargo
        })
        print(f"Funcionario con cédula {cedula} ha sido actualizado con nombre: {nuevo_nombre} y cargo: {nuevo_cargo}.")
    else:
        print(f"No se encontró funcionario con cédula {cedula}.")


if __name__ == "__main__":
    cargar_datos_desde_csv('app/databse2.csv')

    eliminar_recibos_por_cedula('12345678')

    modificar_funcionario_por_cedula('87654321', 'Ana García', 'Gerente de Proyectos')
