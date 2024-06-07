#questão 05
from modelos.livro import Livro

#questão 06
#emprestar livro
livro_biblioteca=Livro('"Orgulho e Preconceito"', 'Jane Austen', '1813' )
print(f'Antes de emprestar (biblioteca: Livro disponível? {livro_biblioteca.disponivel})')
livro_biblioteca.emprestar_livro()
print(f'Antes de emprestar (biblioteca: Livro disponível? {livro_biblioteca.disponivel})')

#questão 07