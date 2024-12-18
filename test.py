from manager.models import Funcionario

f = Funcionario(
    nome='Gabriel Pereira da Silva',
    email='gabriel.script@gmail.com',
    cpf='000.000.000-00',
    remuneracao=2500.00
)

f.save()