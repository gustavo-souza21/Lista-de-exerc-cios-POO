from abc import ABC, abstractmethod


class Armazenador(ABC):
    @abstractmethod
    def salvar(self, dado):
        pass


class ArmazenadorArquivo(Armazenador):
    def salvar(self, dado):
        print(f"[Arquivo] Salvando: '{dado}'")


class ArmazenadorBanco(Armazenador):
    def salvar(self, dado):
        print(f"[Banco de Dados] Salvando: '{dado}'")
