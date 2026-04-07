
nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("Média do aluno:", media)

if media >= 7:
    print(nome + " está aprovado")
elif media >= 5:
    print(nome + " está em recuperação")
else:
    print(nome + " está reprovado")
    print("Fim do programa")