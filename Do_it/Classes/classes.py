import re

class CalcIpv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

    # Validando os valores (usamos getters e setters)
    @property  # getters
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError("Ip inválido")
        self._ip = valor

    @property
    def mascara(self):
        return self._mascara

    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return

        if not self._valida_ip(valor):
            raise ValueError("Mascara inválida")
        self._mascara = valor

    @property
    def prefixo(self):
        return self._prefixo

    @prefixo.setter
    def prefixo(self, valor):
        if not valor:
            return

        if not isinstance(valor, int):
            raise TypeError("Prefixo needs be int")

        if valor > 32:
            raise TypeError("Prefixo precisa ter 32 bits")
        self._prefixo = valor

    # Validando o ip
    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r"^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$"
        )
        if regexp.search(ip):
            return True
        print(regexp.search(ip))


    @staticmethod
    def _ip_to_binario(self, ip):


calc_ipv4 = CalcIpv4(ip="192.168.0.1", prefixo=24)