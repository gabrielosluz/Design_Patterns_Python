from impostos import ICMS, ISS, ICPP, IKCV

class Calculador_de_impostos(object):

    def realize_calculo(self, orcamento, imposto):
        
        imposto_calculado = imposto.calcula(orcamento)
        
        print(imposto_calculado)

if __name__ == '__main__':
    from orcamento import Orcamento, Item

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('ITEM-1', 50))
    orcamento.adiciona_item(Item('ITEM-2', 200))
    orcamento.adiciona_item(Item('ITEM-3', 250))

    print("ISS e ICMS")
    calculador.realize_calculo(orcamento, ISS())
    calculador.realize_calculo(orcamento, ICMS())

    print("ISS com ICMS")
    calculador.realize_calculo(orcamento, ISS(ICMS()))

    print("ICPP e IKCV")
    calculador.realize_calculo(orcamento, ICPP())
    calculador.realize_calculo(orcamento, IKCV())

    print("ICPP com IKCV")
    calculador.realize_calculo(orcamento, ICPP(IKCV()))