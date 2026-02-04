import csv

def ler_arquivo_csv(caminho):
    dados = []
    with open(caminho, newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append(linha)
    return dados

def gerar_relatorio(dados, arquivo_saida):
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as arquivo:
        campos = dados[0].keys()
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados)

def main():
    arquivo_entrada = 'dados.csv'
    arquivo_saida = 'relatorio.csv'

    dados = ler_arquivo_csv(arquivo_entrada)
    gerar_relatorio(dados, arquivo_saida)

    print('Relatório gerado com sucesso.')

if __name__ == '__main__':
    main()
