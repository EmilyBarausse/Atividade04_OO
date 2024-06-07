#questão 01
class Livro:
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo=titulo
        self.autor=autor
        self.ano_publicacao=ano_publicacao
        self.disponivel=True
        
#questão 02
    def __str__(self):
        return f'O livro {self.titulo} foi escrito por {self.autor} e publicado em {self.ano_publicacao}.'
    
# livro1=Livro('"Orgulho e Preconceito"', 'Jane Austen', '1813' )
# livro2=Livro('"A menina que roubava livros"', 'Markus Zusak', '2005' )

# print(livro1)
# print('')
# print(livro2)

#questão 03
    # def emprestar_livro(self):
    #     self.disponivel= not self.disponivel
    #     if not self.disponivel:
    #         print(f'O livro {self.titulo} encontra-se INDISPONÍVEL')
    #     else:
    #         print(f'O livro {self.titulo} encontra-se DISPONÍVEL')
    
# livro1=Livro('"Orgulho e Preconceito"', 'Jane Austen', '1813' )
# livro1.emprestar_livro()
# print(livro1)

#questão 03 - Corrigida
    def emprestar_livro(self):
        self.disponivel= False
        
# livro3=Livro('"O código da Vinci"','Dan Brown',2013)
# print(f'Antes de emprestar: Livro dispinível? {livro3.disponivel}')
# livro3.emprestar_livro()
# print(f'Depois de emprestar: Livro dispinível? {livro3.disponivel}')
# livro3.emprestar_livro()


#questão 04
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis=[livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        for livro in livros_disponiveis:
            print(f'Livros disponíveis em {ano}: {livro}')
            
livro1=Livro('"Orgulho e Preconceito"', 'Jane Austen', '1813' )
livro2=Livro('"A menina que roubava livros"', 'Markus Zusak', '2005' )
livro3=Livro('"O código da Vinci"','Dan Brown',2013)

Livro.livros=[livro1,livro2,livro3]
         




    