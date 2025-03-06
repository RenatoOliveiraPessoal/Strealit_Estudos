import os
import requests
import xml.etree.ElementTree as ET
import pandas as pd

# URL do OneDrive compartilhado
onedrive_url = "https://dmparanacombr-my.sharepoint.com/:f:/g/personal/renato_oliveira_dmparana_com_br/ElvYJlvDqQJAoiqTCVq_ebABFKlOla8u2QvZhGj8qCgwrA?e=fVjISK"

# Função para baixar o conteúdo de um arquivo
def download_file(url):
    response = requests.get(url)
    response.raise_for_status()  # Verifica se houve erro na requisição
    return response.content

# Função para extrair os dados do XML
def extract_data_from_xml(xml_content):
    namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
    root = ET.fromstring(xml_content)
    
    chave = root.find(".//nfe:protNFe/nfe:infProt/nfe:chNFe", namespaces).text
    nNF = root.find(".//nfe:NFe/nfe:infNFe/nfe:ide/nfe:nNF", namespaces).text
    cnpj_emissor = root.find(".//nfe:NFe/nfe:infNFe/nfe:emit/nfe:CNPJ", namespaces).text
    nome_emissor = root.find(".//nfe:NFe/nfe:infNFe/nfe:emit/nfe:xNome", namespaces).text
    
    data = []
    for det in root.findall(".//nfe:NFe/nfe:infNFe/nfe:det", namespaces):
        cProd = det.find(".//nfe:prod/nfe:cProd", namespaces).text
        ean = det.find(".//nfe:prod/nfe:cEAN", namespaces).text
        xProd = det.find(".//nfe:prod/nfe:xProd", namespaces).text
        qCom = det.find(".//nfe:prod/nfe:qCom", namespaces).text
        vUnCom = det.find(".//nfe:prod/nfe:vUnCom", namespaces).text
        vProd = det.find(".//nfe:prod/nfe:vProd", namespaces).text
        
        data.append([chave, nNF, cnpj_emissor, nome_emissor, cProd, ean, xProd, qCom, vUnCom, vProd])
    return data

# Lista para armazenar os dados
all_data = []

# Baixar e processar os arquivos XML
# Aqui você precisaria obter a lista de arquivos XML disponíveis no link compartilhado.
# Como o link é anônimo, você precisaria inspecionar o conteúdo da página ou usar uma API para listar os arquivos.
# Este exemplo assume que você já conhece os nomes dos arquivos XML.

# Exemplo de nomes de arquivos (substitua pelos nomes reais dos arquivos no seu OneDrive)
file_names = ["arquivo1.xml", "arquivo2.xml"]

for file_name in file_names:
    file_url = f"{onedrive_url}/{file_name}"  # Monta a URL completa do arquivo
    try:
        file_content = download_file(file_url)
        all_data.extend(extract_data_from_xml(file_content))
    except Exception as e:
        print(f"Erro ao processar o arquivo {file_name}: {e}")

# Criar um DataFrame com os dados
df = pd.DataFrame(all_data, columns=['Chave', 'Numero da Nota', 'CNPJ do Emissor', 'Nome do Emissor', 'Cod do Produto', 'EAN', 'Nome do Produto', 'Quantidade', 'Valor Unitário', 'Valor Total'])

# Exibir a tabela
print(df)

# Salvar a tabela em um arquivo CSV
df.to_csv('notas_fiscais.csv', index=False)