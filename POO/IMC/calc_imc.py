def imc_calc(height=int, weight=int):
    imc= weight / (height*height)
    print('Your IMC is {}'.format(imc))

persona1 = imc_calc(163, 62)