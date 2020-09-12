from impostos import calcula_ICMS, calcula_ISS

class Calculador_de_impostos(object):

    def realize_calculo(self, orcamento, imposto):
        if (imposto == 'ISS'):
            imposto_calculado = calcula_ISS(orcamento)
        
        if (imposto== 'ICMS'):
            imposto_calculado = calcula_ICMS(orcamento)

        print(imposto_calculado)

if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()

    orcamento = Orcamento(500)

    calculador.realize_calculo(orcamento, 'ISS')
    calculador.realize_calculo(orcamento, 'ICMS')