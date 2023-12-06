# Importação da class Calculadora e comodo
from calculadora import Calculadora
from comodo import Comodo
# Forma na qual o python chama a class
calc = Calculadora()
comodo = Comodo(
    input(" Qual a largura do cômodo ? "),
    input(" Qual a profundidade do cômodo ?  ")
)
print("O valor da área da parede é: ", calc.calcular_area_paredes(comodo))
print("Area do teto: ", calc.calcular_area_teto(comodo))
print("A litragem da tinta é ", calc.calcular_litragem_tinta())

