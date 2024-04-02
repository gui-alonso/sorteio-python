import random

def carregar_arquivo(nome_arquivo):
    """
    Carrega os dados de um arquivo de texto.

    Args:
        nome_arquivo (str): O nome do arquivo a ser carregado.

    Returns:
        list: Uma lista contendo os itens carregados do arquivo.
    """
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        itens = [linha.strip() for linha in linhas]
    return itens

def sortear(grupos, temas):
    """
    Realiza o sorteio, atribuindo temas aleatórios a cada grupo.

    Args:
        grupos (list): Uma lista contendo os nomes dos grupos.
        temas (list): Uma lista contendo os temas disponíveis.

    Returns:
        dict: Um dicionário contendo o sorteio final, onde as chaves são os nomes dos grupos e os valores são os temas sorteados.
    """
    sorteio = {}
    grupos_embaralhados = grupos.copy()
    random.shuffle(grupos_embaralhados)
    
    for grupo in grupos_embaralhados:
        tema = random.choice(temas)
        sorteio[grupo] = tema
        temas.remove(tema)
    
    return sorteio

def main():
    """
    Função principal do programa.
    Carrega os grupos e temas dos arquivos de texto, verifica se há grupos suficientes para os temas, realiza o sorteio e exibe os resultados.
    """
    grupos = carregar_arquivo('grupos.txt')
    temas = carregar_arquivo('temas.txt')

    if len(grupos) > len(temas):
        print("Erro: Número de grupos é maior que o número de temas.")
        return
    
    sorteio_final = sortear(grupos, temas)

    print("Sorteio:")
    for grupo, tema in sorteio_final.items():
        print(f"{grupo}: {tema}")

if __name__ == "__main__":
    main()