#Fabritzio Lopez
#Ejercicio no.1
from abc import ABC, abstractmethod
class ExperimentoFisico(ABC):
    @abstractmethod
    def realizar_experimento(self):
        pass
class CaidaLibre(ExperimentoFisico):
    def __init__(self, altura, gravedad):
        self.altura = altura
        self.gravedad = gravedad

    def raiz_cuadrada(self, valor):
        x = valor
        for _ in range(10):
            x = 0.5 * (x + valor / x)
        return x

    def realizar_experimento(self):
        try:
            if self.altura < 0:
                raise ValueError("La altura no puede ser negativa.")
            if self.gravedad == 0:
                raise ZeroDivisionError("La gravedad no puede ser cero.")
            tiempo = self.raiz_cuadrada((2 * self.altura) / self.gravedad)
            return tiempo
        except ValueError as a:
            print("Error de valor:", a)
        except ZeroDivisionError as b:
            print("Error de división:", b)
        except Exception as c:
            print("Error desconocido:", c)

caida = CaidaLibre(altura=20, gravedad=9.8)
tiempo = caida.realizar_experimento()
if tiempo:
    print("Tiempo de caída:", tiempo)
#Ejercicio no.2 
class OperacionCientifica:
    def calcular(self):
        raise NotImplementedError("Este método debe ser implementado en las subclases")

class RaizCuadrada(OperacionCientifica):
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return self.numero ** 0.5  
class Potencia(OperacionCientifica):
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def calcular(self):
        return self.base ** self.exponente  

class Logaritmo(OperacionCientifica):
    def __init__(self, numero, base=10):
        self.numero = numero
        self.base = base

    def calcular(self):
        if self.numero <= 0:
            raise ValueError("No se puede calcular el logaritmo de un número no positivo.")
        return self._logaritmo(self.numero) / self._logaritmo(self.base)
    def _logaritmo(self, numero):
        if numero <= 0:
            raise ValueError("El logaritmo no está definido para números no positivos.")
        log = 0
        while numero > 1:
            numero /= self.base
            log += 1
        return log
class Factorial(OperacionCientifica):
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero < 0:
            raise ValueError("No se puede calcular el factorial de un número negativo.")
        if not self.numero.is_integer():
            raise ValueError("El factorial solo está definido para números enteros.")
        return self._factorial(int(self.numero))

    def _factorial(self, numero):
        if numero == 0 or numero == 1:
            return 1
        result = 1
        for i in range(2, numero + 1):
            result *= i
        return result
try:
    raiz = RaizCuadrada(-9)
    print(f"Raíz cuadrada: {raiz.calcular()}")
except ValueError as e:
    print(e)
try:
    potencia = Potencia(2, 3)
    print(f"Potencia: {potencia.calcular()}")
except Exception as e:
    print(e)
try:
    logaritmo = Logaritmo(100)
    print(f"Logaritmo: {logaritmo.calcular()}")
except ValueError as e:
    print(e)
try:
    factorial = Factorial(5.5)
    print(f"Factorial: {factorial.calcular()}")
except ValueError as e:
    print(e)



