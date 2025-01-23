import requests
import base64

class ManipulaRepositorio:

    def __init__(self, username):
        self.username = username
        self.api_base_github = 'https://api.github.com'
        self.acess_token = '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'
        self.headers = headers = {'Authorization' : 'Bearer ' + self.acess_token,
           'X-GitHub-Api-Version': '2022-11-28'}
        
    def cria_repo(self, nome_repo):
        data = {
            'name' : nome_repo,
            'description' : 'Dados dos repositórios de algumas empresas ',
            'private' : True
        }

        response = requests.post(f'{self.api_base_github}/user/repos', json=data, headers=self.headers) 

        print(f'O status_code da criação do repositório: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):

        with open(caminho_arquivo, 'rb') as file:
            file_content = file.read()

        encoded_content = base64.b64encode(file_content)

        url = f'{self.api_base_github}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}'

        data = {
            'message': 'Adicionando um novo arquivo',
            'content': encoded_content.decode('utf-8')
        }

        response = requests.put(url,json=data, headers=self.headers)

        print(f'O status_code do upload do arquivo: {response.status_code}')

novo_repo = ManipulaRepositorio('RenanLagrt')

nome_repo = 'Linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo)

novo_repo.add_arquivo(nome_repo, 'dados_repos.py', 'dados_repos.py')
novo_repo.add_arquivo(nome_repo, 'manipula_repos.py', 'manipula_repos.py')
novo_repo.add_arquivo(nome_repo, 'linguagens_amazon.csv', 'Dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'Dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'Dados/linguagens_spotify.csv')




                
        