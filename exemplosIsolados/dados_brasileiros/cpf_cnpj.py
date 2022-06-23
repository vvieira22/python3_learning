from ctypes.wintypes import INT

class Documento:
    @staticmethod
    def criar_doc(documento):
        if(len(documento) == 11):
            return Cpf(documento)

        elif(len(documento) == 14):
            return Cnpj(documento)
        
        else:
            raise ValueError("Quantidade de dígitos incorreta.")

class Cpf:
    def __init__(self, documento):
        if self.valida(documento):
            self._cpf = self.formata(documento)
        else:
            raise ValueError("CPF INVÁLIDO")

    def valida(self, documento):
        fatia_1 = documento[0:3]
        fatia_2 = documento[3:6]
        fatia_3 = documento[6:9]
        fatia_4 = documento[9:]

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
            
            if(resultado_dig1 == int(fatia_4[0])):
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
        return False

    def formata(self, documento):
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
        return self._cpf

class Cnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self._cnpj = self.formata(documento)
        else:
            raise ValueError("CNPJ INVÁLIDO")

    def valida(self, documento):
        fatia_1 = documento[0:2]
        fatia_2 = documento[2:5]
        fatia_3 = documento[5:8]
        fatia_4 = documento[8:12]
        fatia_5 = documento[12:]
        
        cnpj_so_digitos = fatia_1 + fatia_2 + fatia_3 + fatia_4 + fatia_5
        cnpj_so_digitos = list(cnpj_so_digitos)
        
        if( len(set(cnpj_so_digitos)) != 1):
            ##Primeiro Digito
            multiplicadores = [5,4,3,2,9,8,7,6,5,4,3,2]
            fatia_1_a_4 = fatia_1 + fatia_2 + fatia_3 + fatia_4
            resultado_dig1 = 0

            for digito, multiplicador in zip(fatia_1_a_4, multiplicadores):
                resultado_dig1 += int(digito) * multiplicador

            resultado_dig1 = resultado_dig1 % 11
            
            if(resultado_dig1 < 2):
                resultado_dig1 = 0
            else:
                resultado_dig1 = 11 - resultado_dig1

            if(resultado_dig1 == int(fatia_5[0])):
                ##Segundo Dígito
                multiplicadores.insert(0, 6)
                resultado_dig2 = 0

                for digito, multiplicador in zip(fatia_1_a_4 + str(resultado_dig1), multiplicadores):
                    resultado_dig2 += int(digito) * multiplicador

                resultado_dig2 = resultado_dig2 % 11

                if(resultado_dig2 < 2):
                    resultado_dig2 = 0
                else:
                    resultado_dig2 = 11 - resultado_dig2

            resultado_dig2 = resultado_dig2 == int(fatia_5[1])

            if(resultado_dig2):
                return True
        return False

    def formata(self, documento: str):
        fatia_1 = documento[0:2]
        fatia_2 = documento[2:5]
        fatia_3 = documento[5:8]
        fatia_4 = documento[8:12]
        fatia_5 = documento[12:]

        cnpj_formatado = "{}.{}.{}/{}-{}".format(
            fatia_1,
            fatia_2,
            fatia_3,
            fatia_4,
            fatia_5
        )
        return cnpj_formatado


    def __str__(self):
        return self._cnpj


documento = Documento.criar_doc("65425721000199")
print(documento)