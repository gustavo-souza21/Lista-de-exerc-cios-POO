from typing import Protocol


class Imprimivel(Protocol):
    def imprimir(self) -> None:
        ...


class Boleto:
    def __init__(self, codigo, valor):
        self.codigo = codigo
        self.valor = valor

    def imprimir(self) -> None:
        print(f"Imprimindo boleto {self.codigo} no valor de R$ {self.valor:.2f}")


class Etiqueta:
    def __init__(self, destinatario, endereco):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self) -> None:
        print(f"Imprimindo etiqueta para {self.destinatario} — {self.endereco}")


class RelatorioSimples:
    def __init__(self, titulo):
        self.titulo = titulo

    def imprimir(self) -> None:
        print(f"Imprimindo relatório: {self.titulo}")


def processar_impressao(item: Imprimivel) -> None:
    item.imprimir()
