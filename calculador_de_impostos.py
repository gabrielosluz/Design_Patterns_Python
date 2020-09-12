from impostos import ICMS, ISS

class Calculador_de_impostos(object):

    def realize_calculo(self, orcamento, imposto):
        
        imposto_calculado = imposto.calcula(orcamento)
        
        print(imposto_calculado)

if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()

    orcamento = Orcamento(500)

    calculador.realize_calculo(orcamento, ISS())
    calculador.realize_calculo(orcamento, ICMS())