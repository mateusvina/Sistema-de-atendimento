# main.py

from Pessoa import Pessoa

class FilaHospital:
    def __init__(self):
        self.fila = []  # Fila de pacientes
        self.max_pacientes = 11  # Limite de pacientes na fila

    def cadastrar_paciente(self, nome, idade):
        if len(self.fila) < self.max_pacientes:
            paciente = Pessoa(nome, idade)
            self.fila.append(paciente)
            print(f"Paciente {nome} cadastrado com sucesso.")
        else:
            print("Fila cheia! Não é possível cadastrar mais pacientes.")

    def listar_fila(self):
        if not self.fila:
            print("A fila está vazia.")
        else:
            print("Fila de Pacientes:")
            for i, paciente in enumerate(self.fila):
                print(f"{i + 1}. {paciente}")

    def atender_paciente(self):
        if self.fila:
            paciente = self.fila.pop(0)
            print(f"Paciente {paciente.nome} atendido.")
        else:
            print("A fila está vazia. Não há pacientes para atender.")

    def remover_paciente(self, nome):
        for paciente in self.fila:
            if paciente.nome.lower() == nome.lower():
                self.fila.remove(paciente)
                print(f"Paciente {nome} removido da fila.")
                return
        print(f"Paciente {nome} não encontrado na fila.")

    def buscar_paciente(self, nome):
        for paciente in self.fila:
            if paciente.nome.lower() == nome.lower():
                print(f"Paciente encontrado: {paciente}.")
                return
        print(f"Paciente {nome} não encontrado na fila.")

    def quantidade_pacientes(self):
        return len(self.fila)

def main():
    sistema_fila = FilaHospital()
    
    while True:
        print("\nOpções:")
        print("1. Cadastrar Paciente")
        print("2. Listar Fila")
        print("3. Atender Paciente")
        print("4. Remover Paciente")
        print("5. Buscar Paciente")
        print("6. Quantidade de Pacientes na Fila")
        print("q. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Digite o nome do paciente: ")
            idade = int(input("Digite a idade do paciente: "))
            sistema_fila.cadastrar_paciente(nome, idade)
        elif escolha == '2':
            sistema_fila.listar_fila()
        elif escolha == '3':
            sistema_fila.atender_paciente()
        elif escolha == '4':
            nome = input("Digite o nome do paciente a ser removido: ")
            sistema_fila.remover_paciente(nome)
        elif escolha == '5':
            nome = input("Digite o nome do paciente a ser buscado: ")
            sistema_fila.buscar_paciente(nome)
        elif escolha == '6':
            quantidade = sistema_fila.quantidade_pacientes()
            print(f"Quantidade de pacientes na fila: {quantidade}")
        elif escolha.lower() == 'q':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
