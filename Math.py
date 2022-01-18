# Los métodos estáticos no se llaman  a través de la instancia de una clase
# El método estático debe llamarse siempre a través de la clase
# Una clase que tenga método estático sólo debe tener métodos estáticos

# Sirve para agrupar funciones

class Math:
    @staticmethod
    def suma(num1, num2):
        return num1 + num2
    
    @staticmethod
    def resta(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplica(num1, num2):
        return num1 * num2
    
    @staticmethod
    def divide(num1, num2):
        return num1 / num2