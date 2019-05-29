
class Maquina:
    estado = 'VAZIO'
    celula = 'VAZIO'

    # Sempre retorna a direção em que o leitor de se mover
    def consultar_tabela_de_processamento(self, leitura):
        self.celula = leitura
        if (self.estado == 'INICIO'):
            if (self.celula == '*'):
                self.estado = 'ADIÇÃO'

                resultados = {
                    'direcao': 'ESQUERDA',
                    'valor_a_escrever': '*'
                }
                return resultados
            
            pass

        elif (self.estado == 'ADIÇÃO'):
            if (self.celula == '0'):
                self.estado = 'RETORNO'

                resultados = {
                    'direcao': 'DIREITA',
                    'valor_a_escrever': '1'
                }
                return resultados

            elif (self.celula == '1'):
                self.estado = 'TRANSPORTE'

                resultados = {
                    'direcao': 'ESQUERDA',
                    'valor_a_escrever': '0'
                }
                return resultados
                
            elif (self.celula == '*'):
                self.estado = 'PARAR'

                resultados = {
                    'direcao': 'DIREITA',
                    'valor_a_escrever': '*'
                }
                return resultados

            pass
            
        elif (self.estado == 'TRANSPORTE'):
            if (self.celula == '0'):
                self.estado = 'RETORNO'

                resultados = {
                    'direcao': 'DIREITA',
                    'valor_a_escrever': '1'
                }
                return resultados

            elif (self.celula == '1'):
                self.estado = 'TRANSPORTE'

                resultados = {
                    'direcao': 'ESQUERDA',
                    'valor_a_escrever': '0'
                }
                return resultados
                
            elif (self.celula == '*'):
                self.estado = 'TRANSBORDAMENTO'

                resultados = {
                    'direcao': 'ESQUERDA',
                    'valor_a_escrever': '1'
                }
                return resultados


        elif (self.estado == 'TRANSBORDAMENTO'):
            if (self.celula == '-'):
                self.estado = 'RETORNO'

                resultados = {
                    'direcao': 'DIREITA',
                    'valor_a_escrever': '*'
                }
                return resultados
            pass
        elif (self.estado == 'RETORNO'):
            if (self.celula == '0'):
                self.estado = 'RETORNO'

                resultados = {
                    'direcao': 'DIREITA',
                    'valor_a_escrever': '0'
                }
                return resultados
            if (self.celula == '1'):
                self.estado = 'RETORNO'

                resultados = {
                    'direcao': 'DIREITA',
                    'valor_a_escrever': '1'
                }
                return resultados
            if (self.celula == '*'):
                self.estado = 'PARAR'

                resultados = {
                    'direcao': 'NAO_SE_MOVA',
                    'valor_a_escrever': '*'
                }
                return resultados
            pass

