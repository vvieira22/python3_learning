from ast import Raise
from ctypes.wintypes import INT

class Cpf:
    def __init__(self, documento: str):
        try:
            int(documento)
        except:
            raise ValueError("CPF COM CARACTERES INCORRETOS")
            
        if self.validar_tamanho_cpf(documento):
            self._cpf = documento
        else:
            raise ValueError("CPF NO TAMANHO INCORRETO")
       
        try:
            self._cpf = self.formatar_cpf(documento)
            self.validar_cpf(self._cpf)
        except ValueError as e: 
            raise e
            
    def validar_cpf(self, documento : str) -> bool:
        
        fatia_1 = documento[0:3]
        fatia_2 = documento[4:7]
        fatia_3 = documento[8:11]
        fatia_4 = documento[12:]

        cpf_so_digitos = fatia_1 + fatia_2 + fatia_3 + fatia_4
        cpf_so_digitos = list(cpf_so_digitos)

        if ( len(set(cpf_so_digitos)) != 1):
            ##Primeiro Digito
            multiplicadores = [10,9,8,7,6,5,4,3,2]
            fatia_1_a_3 = fatia_1 + fatia_2 + fatia_3 + fatia_4
            resultado_dig1 = 0

            for digito, multiplicador in zip(fatia_1_a_3, multiplicadores):
                resultado_dig1 += int(digito) * multiplicador
            
            resultado_dig1 = resultado_dig1 * 10
            resultado_dig1 = resultado_dig1 % 11

            resultado_dig1 = resultado_dig1 if resultado_dig1 != 10 else 0
            resultado_dig1 = resultado_dig1 == int(fatia_4[0]) 
            
            if(resultado_dig1):
                ##Segundo Dígito
                multiplicadores.insert(0, 11)
                
                resultado_dig2 = 0

                for digito, multiplicador in zip(fatia_1_a_3 + str(resultado_dig1), multiplicadores):
                    resultado_dig2 += int(digito) * multiplicador

                resultado_dig2 = resultado_dig2 * 10
                resultado_dig2 = resultado_dig2 % 11

                resultado_dig2 = resultado_dig2 if resultado_dig2 != 10 else 0

                resultado_dig2 = resultado_dig2 == int(fatia_4[1])
                
                if(resultado_dig2):
                    return True
                else:
                    raise ValueError("CPF INCORRETO")
            raise ValueError("CPF INCORRETO")
        else:
            raise ValueError("CPF COM NUMEROS IGUAIS")
            # raise ValueError("CPF COM NUMEROS IGUAIS")
        
    def validar_tamanho_cpf(sef, documento):
        if(len(str(documento)) == 11):
            return True
        else:
            return False

    def formatar_cpf(self, documento : str):
        try:
            fatia_1 = documento[0:3]
            fatia_2 = documento[3:6]
            fatia_3 = documento[6:9]
            fatia_4 = documento[9:]

            cpf_formatado = "{}.{}.{}-{}".format(
                fatia_1,
                fatia_2,
                fatia_3,
                fatia_4
            )
            return cpf_formatado
        except:
            raise ValueError("ERRO NA FORMATAÇÃO DO CPF")

    def __str__(self):
        return str(self.validar_cpf(self._cpf))

cpf = Cpf("12256122760")
