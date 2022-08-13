#IBGE: QUANTIDADE DE HOMENS E MULHERES
#O IBGE irá iniciar a pesquisa para definir a porcentagem da população por sexo no Brasil em 2019 e precisa da sua ajuda. 
# Sua tarefa é, dada uma lista de pessoas que moram em uma cidade, definir a quantidade de Homens e Mulheres.  
#Entrada: Na primeira linha da entrada temos um inteiro ‘N’, representando o número de pessoas que moram na cidade. 
# Nas próximas ‘N’ linhas haverá uma sequência de ‘N’ inteiros ‘S’ (S ∈ {1, 2}), um inteiro por linha, 
# representando o sexo de cada pessoa, ou seja, se ‘S’ for 1 quer dizer que é um homem, se ‘S’ for 2 quer dizer que é uma mulher.
#Saída: A saída consiste em duas linhas contendo dois números inteiros: a primeira linha
#  representando a quantidade de homens e a segunda linha representando a quantidade de mulheres.  

#------------------------------------------------------------------------------------------

H=0
M =0
Pessoas = int(input('Digite a quantidade de pessoas:    '))

for repetir in range(0,10):
    Genero = float(input('Digite [1]Homem e [2]Mulher:      ' ))

    
    if  Genero ==1:
        H+=1
    elif Genero ==2:
        M+=1
    


print(

    f'\n A quantidade de pessoas na cidade {Pessoas}',
    f'\n A quantidade:       homens {H}' 
    f'\n A quantidade de Mulheres :{M}',
)
        






    


        
        
        

 
    

  


    




