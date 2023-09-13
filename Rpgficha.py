fichas = []

class FichaRPG:
    def __init__(self, nome, vida, mana, classe, nivel):
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.classe = classe
        self.nivel = nivel
    
    def __str__(self):
        return f"Nome: {self.nome}\nVida: {self.vida}\nMana: {self.mana}\nClasse: {self.classe}\nNível: {self.nivel}\n"

def criar_ficha():
    nome = input("Digite o nome do personagem: ")
    vida = input("Digite a quantidade de vida: ")
    mana = input("Digite a quantidade de mana: ")
    classe = input("Digite a classe: ")
    nivel = input("Digite o nível: ")
    if vida.isdigit() and mana.isdigit() and nivel.isdigit():
        ficha = FichaRPG(nome, int(vida), int(mana), classe, int(nivel))
        fichas.append(ficha)
        print("Ficha criada com sucesso!\n")
    else:
        print("Erro: a quantidade de vida, mana e nível devem ser valores numéricos.\n")
    
def excluir_ficha():
    nome = input("Digite o nome do personagem a ser excluído: ")
    for ficha in fichas:
        if ficha.nome.lower() == nome.lower():
            fichas.remove(ficha)
            print("Ficha excluída com sucesso!\n")
            return
    print("Erro: personagem não encontrado.\n")
    
def listar_fichas():
    if not fichas:
        print("Nenhuma ficha encontrada.\n")
    else:
        for ficha in fichas:
            print(ficha)

def pesquisar_ficha():
    nome = input("Digite o nome do personagem a pesquisar: ")
    for ficha in fichas:
        if ficha.nome.lower() == nome.lower():
            print(ficha)
            return
    print("Erro: personagem não encontrado.\n")

def modo_combate():
    nome = input("Digite o nome do personagem em combate: ")
    ficha = None
    for f in fichas:
        if f.nome.lower() == nome.lower():
            ficha = f
            break
    if ficha is None:
        print("Erro: personagem não encontrado.\n")
        return
    
    combate_ativo = True
    while combate_ativo:
        comando = input("Digite o comando de combate: ")
        if comando.lower() == "!fim_combate":
            combate_ativo = False
            print("Combate encerrado.\n")
        elif comando.startswith("!-"):
            partes = comando[1:].split()
            if len(partes) == 2:
                atributo = partes[0].lower()
                valor = int(partes[1])
                if atributo == "vida":
                    ficha.vida -= valor
                    print("Nova quantidade de vida:", ficha.vida)
                elif atributo == "mana":
                    ficha.mana -= valor
                    print("Nova quantidade de mana:", ficha.mana)
                else:
                    print("Comando inválido.")
            else:
                print("Comando inválido.")
        else:
            print("Comando inválido.")

# Exemplo de uso
while True:
    print("Escolha uma opção:")
    print("1 - Criar ficha")
    print("2 - Excluir ficha")
    print("3 - Listar fichas")
    print("4 - Pesquisar ficha")
    print("5 - Modo de combate")
    print("0 - Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        criar_ficha()
    elif opcao == "2":
        excluir_ficha()
    elif opcao == "3":
        listar_fichas()
    elif opcao == "4":
        pesquisar_ficha()
    elif opcao == "5":
        modo_combate()
    elif opcao == "0":
        break
    else:
        print("Opção inválida.\n")
      