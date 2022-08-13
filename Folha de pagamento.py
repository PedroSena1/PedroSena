for repetir in range(1,6):
    input(f'Digite {repetir} o nome do funcionário')
    hora_trabalhada =  float(input(f'Digite o valor das horas trabalhadas'))
    hora_total = float(input(f' Digite a hota total trabalhadas'))

    salario_bruto = hora_trabalhada * hora_total

    if salario_bruto <= 900:
        desconto_ir = 0.0
    
    elif salario_bruto <= 1500:
        desconto_ir = 5
    elif salario_bruto <= 2500:
         desconto_ir = 10
    else:
        desconto_ir = 2500
    
    ir   =   salario_bruto * (desconto_ir/100)
    inss =   salario_bruto * (10/100)
    fgts =   salario_bruto * (11/100)
    total_desconto = ir + inss
    salario_liquido = salario_bruto - total_desconto


    print (
    f"\nsalário_bruto     : R${salario_bruto:.2f}",
    f"\n(-) IR (5%)       : R${ir:.2f}",
    f"\n(-) INSS ( 10%)   : R${inss:.2f}",
    f"\nFGTS (11%)        : R${fgts:.2f}",
    f"\nTotal de descontos: R${total_desconto:.2f}",
    f"\nSalário Liquido   : R${salario_liquido:.2f}",
    )
    





