from classes.cp import ContaPoupanca
from classes.cc import ContaCorrente


cp = ContaPoupanca(0148, 17980, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

print('##########################')
cc = ContaCorrente(agencia=0148, conta=17980, saldo=0, limite=1650)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
