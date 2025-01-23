import requests
import pandas as pd 
from math import ceil

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_github = 'https://api.github.com'
        self.acess_token = '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'
        self.headers = headers = {'Authorization' : 'Bearer ' + self.acess_token,
           'X-GitHub-Api-Version': '2022-11-28'}
        
    def lista_repositorios(self):
        repos_list = []

        response = requests.get(f'https://api.github.com/users/{self.owner}')
        num_pages = ceil(response.json()['public_repos']/30)
        
        for page_num in range(1, num_pages + 1):
            try:
                url_page = f'{self.api_base_github}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url_page,headers=self.headers)
                repos_list.append(response.json())
            
            except:
                repos_list.append(None)

        return repos_list
    
    def __nome_repos(self,repos_list):
        repos_name = []

        for page in repos_list:
            for repo in page:
                repos_name.append(repo['name'])

        return repos_name
    
    def __linguagem_repos(self,repos_list):
        repos_language = []

        for page in repos_list:
            for repo in page:
                repos_language.append(repo['language'])
        
        return repos_language
    
    def cria_df_linguagens(self):
        repositorios = self.lista_repositorios()
        nomes = self.__nome_repos(repositorios)
        linguagens = self.__linguagem_repos(repositorios)

        dados = pd.DataFrame()
        dados['Repository Name'] = nomes
        dados['Language'] = linguagens

        return dados
    
amazon_rep = DadosRepositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()

netflix_rep = DadosRepositorios('netflix')
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

spotify_rep = DadosRepositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()

# Salvando 

ling_mais_usadas_amzn.to_csv('Dados/linguagens_amzn.csv',index=False)
ling_mais_usadas_netflix.to_csv('Dados/linguagens_netflix.csv',index=False)
ling_mais_usadas_spotify.to_csv('Dados/linguagens_spotify.csv',index=False)
ling_mais_usadas_apple.to_csv('Dados/linguagens_apple.csv',index=False)


