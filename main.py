import requests
import zipfile
from bs4 import BeautifulSoup
def main():
    resposta=requests.get(url='https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
    soup = BeautifulSoup(resposta.text, 'html.parser')
    elemento_link=soup.select('#cfec435d-6921-461f-b85a-b425bc3cb4a5 > div > ol > li:nth-child(1) > a:nth-child(1)')
    resposta_pdf=requests.get(url=elemento_link[0].attrs['href'])
    file_name = 'anexo1.pdf'
    with open(file_name, 'wb') as file:
        for chunk in resposta_pdf.iter_content(chunk_size=8192):
            file.write(chunk)



    
    elemento_link2=soup.select('#cfec435d-6921-461f-b85a-b425bc3cb4a5 > div > ol > li:nth-child(2) > a')
    resposta_pdf=requests.get(url=elemento_link2[0].attrs['href'])
    file_name2 = 'anexo2.pdf'
    with open(file_name2, 'wb') as file:
        for chunk in resposta_pdf.iter_content(chunk_size=8192):
            file.write(chunk)
    
    with zipfile.ZipFile('arquivos.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_name)
        zipf.write(file_name2)
    
    #debug=0
    
if __name__ == '__main__':
    main()      