# Crie um algoritmo em Python, que dado dois números informados pelo usuário e
# sua operação (das 4 operações básicas da matemática), realize os cálculos
# adequados dentro de funções.

#--------------------------------------------------------------------

n1 = float(input('Digite numero1:       '))
n2 = float(input('Digite numero2:       '))
op = input('Digite a op: +, - , *, /:       ')

def calc(n1, n2 , op):

   
    if op == '+':
        return n1+n2
   

    elif op == '-':
        return n1-n2
    

    elif op == '*':
        return n1*n2

    elif op == '/':
        return n1/n2
   
    return n1+n2, n1-n2,n1*n2, n1/n2

print(calc(n1,n2,op))



