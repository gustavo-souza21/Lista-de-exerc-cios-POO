from imprimivel import Boleto, Etiqueta, RelatorioSimples, processar_impressao


def main():
    boleto = Boleto("34191.09008 00000.209058 01001.903002 4 92690000010000", 100.00)
    etiqueta = Etiqueta("João Silva", "Rua das Flores, 123 - Manaus/AM")
    relatorio = RelatorioSimples("Relatório Mensal de Vendas")

    processar_impressao(boleto)
    processar_impressao(etiqueta)
    processar_impressao(relatorio)


if __name__ == "__main__":
    main()
