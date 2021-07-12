import requests
from requests import status_codes


class Repos():

    def __init__(self, usuario):
        self._usuario = usuario

    def requestRepos(self):
        response = requests.get(
            f"https://api.github.com/users/{self._usuario}/repos"
        )
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
    
    def printRepos(self):
        dados = self.requestRepos()
        if type (dados) is not int:
            for i in range (len(dados)):
                print(dados[i]['name'])
        else:
            print(dados)


Repos('bugelseif').printRepos()
