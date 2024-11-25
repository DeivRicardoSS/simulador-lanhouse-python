# Como vai funcionar:

## Pc
### Atributos
- id : String
- componentes : [Componente]
- ligado : Bool
### Métodos
- ligar_desligar : ligar ou desligar computador com base em um randomizador

## Componente
### Atributos
- id : String
- tempo-de-vida : Number
- quebrado : Bool

### Métodos
#### decaimento
- cpu => decaimento de 0.5
- memória => decaimento de 0.4
- processador => decaimento de 0.8
- placa-mae => decaimento de 0.2
- fonte => decaimento de 0.6

#### quebrar : quebrar a peça aleatoriamente


Nota: para as manutenções eu penseiem fazer um sistema pra solicitar uma manutenção, o que daria um delay que simularia o tempo de chegada do cara da manutenção.