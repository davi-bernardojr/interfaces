from profissional.Barbeiro import Barbeiro
from profissional.Freelancer import Freelancer
from Trabalhador import Trabalhador

trabalhador = Trabalhador("Julio")
barbeiro = Barbeiro("Barbeiro")
#testar com atributo em branco
#barbeiro = Barbeiro("")

freela = Freelancer("barman", "churrasco")
#testar com o segundo atributo em branco
#freela = Freelancer("barman", "")

trabalhador.servicoPrestado(barbeiro)
trabalhador.servicoExtra(barbeiro)
trabalhador.servicoPrestado(freela)
trabalhador.servicoExtra(freela)

