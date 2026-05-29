from Parte_A import Armazenador
from Parte_B import Salvavel


def executar_salvamento_formal(armazenador, dado):
    if isinstance(armazenador, Armazenador):
        armazenador.salvar(dado)
    else:
        raise TypeError("O objeto não herda da classe abstrata Armazenador")


def executar_salvamento_flexivel(objeto, dado):
    if isinstance(objeto, Salvavel):
        objeto.salvar(dado)
    else:
        raise TypeError("O objeto não implementa a interface Salvavel")
