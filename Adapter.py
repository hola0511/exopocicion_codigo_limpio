# Clase que espera temperaturas en Celsius
class CelsiusThermometer:
    def get_temperature(self):
        # Supongamos que retorna siempre una temperatura fija para el ejemplo
        return 50  # 50 grados Celsius

# Dispositivo externo que trabaja con Fahrenheit
class FahrenheitThermometer:
    def get_temperature_fahrenheit(self):
        return 30  # 30 grados Fahrenheit

# Adaptador que convierte Fahrenheit a Celsius
class FahrenheitToCelsiusAdapter:
    def __init__(self, fahrenheit_thermometer):
        self.fahrenheit_thermometer = fahrenheit_thermometer

    def get_temperature(self):
        # Convierte la temperatura de Fahrenheit a Celsius
        temp_fahrenheit = self.fahrenheit_thermometer.get_temperature_fahrenheit()
        return (temp_fahrenheit - 32) * 5.0 / 9.0  # Conversión a Celsius

# Uso del adaptador
fahrenheit_thermometer = FahrenheitThermometer()
adapter = FahrenheitToCelsiusAdapter(fahrenheit_thermometer)

# El adaptador convierte la temperatura para que sea compatible con el sistema que usa Celsius
print("Temperatura en Celsius:", adapter.get_temperature())
