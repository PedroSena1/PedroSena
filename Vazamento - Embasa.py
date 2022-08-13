#Você foi contratado pela prefeitura para criar um programa que calcule 
# a quantidade de água desperdiçada em vazamentos de água por toda a cidade.
#O programa deve receber a quantidade de vazamentos notificados a prefeitura no 
# dia e para cada um deles deve pedir a quantidade de água perdida por hora e a 
# quantidade de horas que o vazamento ficou aberto e ao final da execução exibir 
# o total de água desperdiçada 

#Exemplo:
#Entrada:
#Vazamentos: 2
#litros por hora: 10 horas: 2
#litros por horas: 4 horas: 1 

#Saída:

#24 litros
#Questão que quase me fez ficar careca!

#-----------------------------------------------------------------------------
dia = input('Digite o dia: Seg; Ter; Qua; Qui; Sex:         ')
litros = 0
total = 0
horas = 0
vaz = int(input('Quantidade de vazamentos: '))
for repetir in range(vaz):
    litros = int(input('Digite a quantidade de litros :         '))
    horas = int(input('Digite a quantidade de horas:        '))
    total += (litros*horas)
    

print(
    f'\n Dia do vazamento:            {dia}',
    f'\n A quantidade de vazamento:     {vaz}',
    f'\n A quantidade de litros:        {litros}',
    f'\n A quantidade de horas:         {horas}',
    f'\n O total vazados é :            {total}',
)