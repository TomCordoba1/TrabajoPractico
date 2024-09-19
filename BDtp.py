import pandas as pd
from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Crear listas para almacenar los datos
data = {
    'id_hotel': [],
    'nombre_hotel': [],
    'ciudad_hotel': [],
    'direccion_hotel': [],
    'calle_hotel': [],
    'numero_hotel': [],
    'celular_hotel': [],
    'id_empleado': [],
    'nombre_empleado': [],
    'celular_empleado': [],
    'direccion_empleado': [],
    'calle_empleado': [],
    'numero_empleado': [],
    'ciudad_empleado': [],
    'id_cliente': [],
    'nombre_cliente': [],
    'apellido_cliente': [],
    'direccion_cliente': [],
    'calle_cliente': [],
    'numero_cliente': [],
    'celular_cliente': [],
    'id_pago': [],
    'fecha_pago': [],
    'anio_pago': [],
    'mes_pago': [],
    'dia_pago': [],
    'hora_pago': [],
    'minuto_pago': [],
    'id_reserva': [],
    'fecha_reserva': [],
    'anio_reserva': [],
    'mes_reserva': [],
    'dia_reserva': [],
    'id_habitacion': [],
    'tamano_habitacion': [],
    'id_servicio': [],
    'tipo_servicio': [],
    'id_ubicacion': [],
    'tipo_ubicacion': [],
    'id_promocion': [],
    'tipo_promocion': [],
    'id_opinion': [],
    'tipo_opinion': [],
    'puntaje': [],
}

# Generar 10 registros
for i in range(10):
    data['id_hotel'].append(i + 1)
    data['nombre_hotel'].append(fake.company())
    data['ciudad_hotel'].append(fake.city())
    data['direccion_hotel'].append(fake.address().replace('\n', ', '))
    data['calle_hotel'].append(fake.street_name())
    data['numero_hotel'].append(fake.building_number())
    data['celular_hotel'].append(fake.phone_number())
    
    data['id_empleado'].append(i + 1)
    data['nombre_empleado'].append(fake.name())
    data['celular_empleado'].append(fake.phone_number())
    data['direccion_empleado'].append(fake.address().replace('\n', ', '))
    data['calle_empleado'].append(fake.street_name())
    data['numero_empleado'].append(fake.building_number())
    data['ciudad_empleado'].append(fake.city())
    
    data['id_cliente'].append(i + 1)
    data['nombre_cliente'].append(fake.first_name())
    data['apellido_cliente'].append(fake.last_name())
    data['direccion_cliente'].append(fake.address().replace('\n', ', '))
    data['calle_cliente'].append(fake.street_name())
    data['numero_cliente'].append(fake.building_number())
    data['celular_cliente'].append(fake.phone_number())
    
    data['id_pago'].append(i + 1)
    data['fecha_pago'].append(fake.date())
    data['anio_pago'].append(fake.year())
    data['mes_pago'].append(fake.month())
    data['dia_pago'].append(fake.day_of_month())
    data['hora_pago'].append(random.randint(0, 23))
    data['minuto_pago'].append(random.randint(0, 59))
    
    data['id_reserva'].append(i + 1)
    data['fecha_reserva'].append(fake.date())
    data['anio_reserva'].append(fake.year())
    data['mes_reserva'].append(fake.month())
    data['dia_reserva'].append(fake.day_of_month())
    
    data['id_habitacion'].append(i + 1)
    data['tamano_habitacion'].append(random.choice(['Pequeña', 'Mediana', 'Grande']))
    
    data['id_servicio'].append(i + 1)
    data['tipo_servicio'].append(random.choice(['Spa', 'Restaurante', 'Tour']))
    
    data['id_ubicacion'].append(i + 1)
    data['tipo_ubicacion'].append(random.choice(['Centro', 'Periferia', 'Playa']))
    
    data['id_promocion'].append(i + 1)
    data['tipo_promocion'].append(random.choice(['Descuento', 'Paquete', 'Fidelidad']))
    
    data['id_opinion'].append(i + 1)
    data['tipo_opinion'].append(random.choice(['Positiva', 'Negativa']))
    data['puntaje'].append(random.randint(1, 5))

# Crear un DataFrame y guardarlo en un archivo Excel
df = pd.DataFrame(data)
df.to_excel('datos_hotel.xlsx', index=False)

print("Archivo Excel 'datos_hotel.xlsx' creado con éxito.")
