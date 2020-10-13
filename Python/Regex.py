# Python ReGex Ou Expressao regular
"""Um RegEx,ou expressao regular,e uma sequencia de caracteres que forma um padrão de pesquisa.
RegEx pode ser usado para verificar se uma string contem o padrão de pesquisa especificado."""

# Module ReGex
"""Python tem um pacote embutido chamado re,que pode ser usado para trabalhar com expressoes regulares.
Importe a re modelacao:"""

import re

re.compile(".*")

# Metacaracteres
"""Metacaracteres sao caracteres com um significado especial:"""

"""CARATER	 DESCRICAO	                            EXEMPLO
	[]	    Um conjunto de personagens	            "[a-m]"
	\	   Sinaliza uma sequência especial
		   (também pode ser usado para
		   escapar de caracteres especiais)         "\d"
	.	    Qualquer caractere
			(exceto caractere de nova linha)	    "he..o"
	^	    Comeco com	                            "^hello"
	$	    termina Com	                            "world$"
	*	    Zero ou mais ocorrências	            "aix*"
	+	    Um ou mais ocorrências	                "aix+"
	{}	    Exatamente o número especificado
	        de ocorrências	                        "al{2}"
	|	    ou ... ou	                            "falls|stays"
	()	    Capturar e agrupar                       ....
"""
# Exemplo por []
import re
txt = "Sem dor,Sem Ganho"

"""Encontre todos os caracteres minúsculos em ordem alfabética entre "a" e "m":"""
x = re.findall("[a-m]", txt)
print(x)

# Exemplo por \
import re
txt = "Isso vai ser 59 dólares"

"""Encontre todos os caracteres de dígitos:"""
x = re.findall("\d", txt)
print(x)

# Exemplo por .
import re
txt = "hello world"

"""Procure uma sequência que comece com "wo",seguido por dois (quaisquer) caracteres e um "d":"""
x = re.findall("wo..d", txt)
print(x)

# Exemplo por ^
import re
txt = "hello world"

"""Verifique se a string começa com 'hello':"""
x = re.findall("^hello", txt)
if x:
  print("Sim, a string começa com 'hello'")
else:
  print("Nenhuma correspondência")
















# ReGex em Python
"""Depois de importar a remodelação, você pode começar a usar expressões regulares:
Depois de importar a remodelação, você pode começar a usar expressões regulares:"""

# Exemplo: Procure a string para ver se ela começa com "The" e termina com "Spain":

import re

txt = "Sem dor,Sem Ganho"
x = re.search("^Sem.*Ganho$", txt)

if x:
	print("SIM!tem uma correspondência!")
else:
	print("Nenhuma correspondência")
