# Diagrama de Classes - Simulador Lanhouse - Trabalho da disciplina de Lógica de Programação

Este diagrama de classes descreve a estrutura e os relacionamentos entre os principais componentes do sistema **Simulador Lanhouse**, desenvolvido em Python.

## Descrição das Classes

### 1. **PC**

Representa um computador no sistema.

- **Atributos**:
  - `id: String` - Identificador único do computador.
  - `ligado: Boolean` - Estado de ligação (ligado/desligado).
  - `componentes: [Comp]` - Lista de componentes associados ao computador.

- **Métodos**:
  - `quebrarRand(): Boolean` - Método para simular falha no computador.
  - `vidautil(): void` - Método para calcular a vida útil do computador.

### 2. **Computador**

Representa a classe de computador no contexto do sistema de manutenção de equipamentos.

- **Atributos**:
  - `id: String` - Identificador único do computador.
  - `custo: Float` - Custo de manutenção do computador.
  - `tempo_de_vida: int` - Tempo de vida útil do computador em anos.
  - `quebrarRand(): Boolean` - Método para gerar falhas randômicas no computador.
  - `vidautil(): void` - Método para calcular a vida útil.

### 3. **Manutenção**

Representa as informações de manutenção realizadas no computador.

- **Atributos**:
  - `id: String` - Identificador único da manutenção.
  - `custo: Float` - Custo da manutenção.
  - `tipo: String` - Tipo de manutenção (preventiva, corretiva, etc).
  - `finalizada: Boolean` - Status de finalização da manutenção.
  - `componentes: [Comp]` - Lista de componentes substituídos na manutenção.

### 4. **Program**

Representa o software que está sendo executado no computador, incluindo a simulação do tempo de uso.

- **Atributos**:
  - `dias: int` - Número de dias de uso do programa.
  - `minutos: int` - Número de minutos de uso.
  - `horas: int` - Número de horas de uso.
  - `maquinas: [PC]` - Lista de computadores associados ao programa.

- **Métodos**:
  - `render(): Void` - Método para renderizar os dados do programa.
