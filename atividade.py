class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def aumentar_salario(self, aumento):
        if aumento > 0:
            self.__salario += aumento

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, bonus):
        super().__init__(nome, cargo, salario)

        self.bonus = bonus

    def get_salario(self):
        return super().get_salario() + self.bonus

if __name__ == "__main__":
    funcionario = Funcionario("Theuzindo7", "Desenvolvedor", 5000)
    gerente = Gerente("Maria", "Gerente de Projetos", 8000, 2000)

    print(f"Salário do Funcionário {funcionario.nome}: {funcionario.get_salario()}")
    print(f"Salário do Gerente {gerente.nome}: {gerente.get_salario()}")

    funcionario.aumentar_salario(500)
    gerente.aumentar_salario(1000)

    print(f"Salário do Funcionário {funcionario.nome} após aumento: {funcionario.get_salario()}")
    print(f"Salário do Gerente {gerente.nome} após aumento: {gerente.get_salario()}")