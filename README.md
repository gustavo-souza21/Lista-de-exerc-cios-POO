# Lista de Exercícios II — Parte 1
### POO em Python | ICET-UFAM | Prof. Alternei Brito

Implementação das 5 questões da Lista II (Parte 1) de Programação Orientada a Objetos, cobrindo **classes abstratas (ABC)**, **herança**, **polimorfismo** e **Protocol**.

---

## Estrutura do repositório

```
lista2/
├── questao1/          # Sistema de Mídias Educacionais
│   ├── midia.py
│   ├── plataforma.py
│   └── main.py
├── questao2/          # Sistema de Funcionários
│   ├── funcionario.py
│   ├── empresa.py
│   └── main.py
├── questao3/          # Sistema de Notificações com ABC
│   ├── notificador.py
│   ├── central.py
│   └── main.py
├── questao4/          # Sistema de Impressão com Protocol
│   ├── impressao.py
│   └── main.py
└── questao5/          # Armazenamento com ABC e Protocol
    ├── Parte_A.py
    ├── Parte_B.py
    ├── Parte_C.py
    └── main.py
```

---

## Pré-requisitos

- Python **3.10** ou superior
- Sem dependências externas (apenas biblioteca padrão)

---

## Como executar

Clone o repositório e entre na pasta de cada questão:

```bash
git clone https://github.com/<seu-usuario>/<nome-do-repo>.git
cd lista2
```

Execute o `main.py` de cada questão individualmente:

```bash
# Questão 1
cd questao1 && python main.py

# Questão 2
cd ../questao2 && python main.py

# Questão 3
cd ../questao3 && python main.py

# Questão 4
cd ../questao4 && python main.py

# Questão 5
cd ../questao5 && python main.py
```

> Cada `main.py` é independente e deve ser executado a partir do próprio diretório da questão.

---

## Resumo das questões

### Questão 1 — Sistema de Mídias Educacionais
Classe abstrata `Midia` com método concreto `mostrar_info()` e método abstrato `reproduzir()`. Subclasses `Video`, `Podcast` e `TextoNarrado` implementam `reproduzir()` cada uma à sua forma. A classe `Plataforma` armazena mídias e chama `reproduzir()` polimorficamente em `reproduzir_todas()`.

**Conceitos:** ABC, `@abstractmethod`, herança, polimorfismo.

---

### Questão 2 — Sistema de Funcionários
Classe abstrata `Funcionario` com método abstrato `calcular_pagamento()`. Cada subclasse (`FuncionarioAssalariado`, `FuncionarioHorista`, `FuncionarioComissionado`) tem sua própria fórmula de cálculo. `Empresa.mostrar_folha_pagamento()` percorre a lista e exibe os valores polimorficamente.

**Conceitos:** ABC, sobrescrita de método, polimorfismo, herança.

---

### Questão 3 — Sistema de Notificações com ABC
Classe abstrata `Notificador` com método abstrato `notificar(mensagem)`. Subclasses `NotificadorEmail`, `NotificadorSMS` e `NotificadorApp` implementam o envio cada uma ao seu canal. `CentralNotificacoes.enviar_para_todos()` dispara a notificação polimorficamente para todos os canais cadastrados.

**Conceitos:** ABC, contrato formal por herança, polimorfismo.

---

### Questão 4 — Sistema de Impressão com Protocol
`Imprimivel` é definido como `Protocol` (contrato estrutural, sem herança obrigatória). Classes `Boleto`, `Etiqueta` e `RelatorioSimples` implementam `imprimir()` sem precisar herdar de `Imprimivel`. A função `processar_impressao(item)` aceita qualquer objeto que satisfaça o protocolo.

**Conceitos:** `typing.Protocol`, duck typing estrutural, polimorfismo sem herança.

---

### Questão 5 — Armazenamento com ABC e Protocol (comparação)
Combina as duas abordagens no mesmo domínio:
- **Parte A (ABC):** `Armazenador` define contrato por herança; `ArmazenadorArquivo` e `ArmazenadorBanco` herdam e implementam `salvar()`.
- **Parte B (Protocol):** `Salvavel` define contrato estrutural; `ArmazenadorNuvem` implementa `salvar()` sem herdar de nada.
- **Parte C:** `executar_salvamento_formal()` exige subclasse de `Armazenador`; `executar_salvamento_flexivel()` aceita qualquer objeto compatível com `Salvavel`.

**Conceitos:** comparação ABC vs Protocol, rigidez vs flexibilidade de contratos.

---

## Conceitos abordados

| Conceito | Onde aparece |
|---|---|
| Classe abstrata (`ABC`) | Q1, Q2, Q3, Q5 |
| `@abstractmethod` | Q1, Q2, Q3, Q5 |
| Herança | Q1, Q2, Q3, Q5 |
| Sobrescrita de método | Q1, Q2, Q3, Q4, Q5 |
| Polimorfismo | Q1, Q2, Q3, Q4, Q5 |
| `typing.Protocol` | Q4, Q5 |
| Duck typing estrutural | Q4, Q5 |
