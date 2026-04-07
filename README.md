# medias_notas_python
elaboramos um código com o objetivo de calcular a média das notas de um determinado aluno o código em si é simple, mas o intuito é fazer a analize de possibilidade atraves do .md
test001: aprovação com média alta
entrada: "João", 8, 9
retorno_esperado: Média do aluno: 8.5 / João está aprovado
resultado: o código funcionou corretamente

test002: aprovação no limite
entrada: "Maria", 7, 7
retorno_esperado: Média do aluno: 7.0 / Maria está aprovado
resultado: o código funcionou corretamente

test003: recuperação no limite superior
entrada: "Carlos", 6, 5
retorno_esperado: Média do aluno: 5.5 / Carlos está em recuperação
resultado: o código funcionou corretamente

test004: recuperação no limite inferior
entrada: "Ana", 5, 5
retorno_esperado: Média do aluno: 5.0 / Ana está em recuperação
resultado: o código funcionou corretamente

test005: reprovação abaixo de 5
entrada: "Lucas", 4, 3
retorno_esperado: Média do aluno: 3.5 / Lucas está reprovado / Fim do programa
resultado: o código funcionou corretamente

test006: reprovação no limite inferior
entrada: "Beatriz", 0, 4
retorno_esperado: Média do aluno: 2.0 / Beatriz está reprovado / Fim do programa
resultado: o código funcionou corretamente

test007: notas com valores decimais
entrada: "Pedro", 6.5, 7.5
retorno_esperado: Média do aluno: 7.0 / Pedro está aprovado
resultado: o código funcionou corretamente

test008: nome vazio
entrada: "", 7, 8
retorno_esperado: Média exibida corretamente / " está aprovado"
resultado: o código não valida nome vazio, mas executa normalmente

test009: notas negativas
entrada: "Rafaela", -5, 6
retorno_esperado: exibir erro ou impedir cálculo
resultado: o código não valida notas negativas e calcula normalmente

test010: nota maior que 10
entrada: "Bruno", 11, 9
retorno_esperado: exibir erro ou limitar valores
resultado: o código não valida limite máximo de notas

test011: entrada não numérica na nota
entrada: "Fernanda", "abc", 5
retorno_esperado: exibir erro de entrada sem travar
resultado: o código gera erro (ValueError) e trava

test012: média exatamente 5
entrada: "Gabriel", 5, 5
retorno_esperado: recuperação
resultado: o código classificou corretamente

test013: média exatamente 7
entrada: "Juliana", 7, 7
retorno_esperado: aprovado
resultado: o código classificou corretamente

test014: valores zero nas notas
entrada: "Marcos", 0, 0
retorno_esperado: Média 0.0 / reprovado / Fim do programa
resultado: o código funcionou corretamente

test015: fluxo completo válido
entrada: "Larissa", 6, 8
retorno_esperado: execução sem erros / média 7.0 / aprovado
resultado: o código funcionou corretamente
