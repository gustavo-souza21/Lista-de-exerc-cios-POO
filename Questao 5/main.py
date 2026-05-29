from Parte_A import ArmazenadorArquivo, ArmazenadorBanco
from Parte_B import ArmazenadorNuvem
from Parte_C import executar_salvamento_formal, executar_salvamento_flexivel


def main():
    arquivo = ArmazenadorArquivo()
    banco = ArmazenadorBanco()
    nuvem = ArmazenadorNuvem()

    print("=== Salvamento formal (ABC) ===")
    executar_salvamento_formal(arquivo, "dados do usuário")
    executar_salvamento_formal(banco, "dados do usuário")

    print("\n=== Salvamento flexível (Protocol) ===")
    executar_salvamento_flexivel(arquivo, "backup diário")
    executar_salvamento_flexivel(banco, "backup diário")
    executar_salvamento_flexivel(nuvem, "backup diário")


if __name__ == "__main__":
    main()
