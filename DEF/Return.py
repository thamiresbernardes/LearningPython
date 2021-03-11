def liquidificador(ingrediente1, ingrediente2, ingrediente3):
    mistura = ingrediente1 + ingrediente2 + ingrediente3
    bolo = mistura + '=assada'
    return bolo


o_retorno_é_um_bolo = liquidificador('Trigo', 'Açucar', 'Fermento')
print(o_retorno_é_um_bolo)  # TrigoAçucarFermento=assada