from typing import Protocol, runtime_checkable, Any


@runtime_checkable
class Salvavel(Protocol):
    def salvar(self, dado: Any) -> None:
        ...


class ArmazenadorNuvem:
    def salvar(self, dado: Any) -> None:
        print(f"[Nuvem] Salvando: '{dado}'")
