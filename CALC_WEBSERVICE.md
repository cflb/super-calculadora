# Isolamento de estrutura - Ambiente Virtual - Virutal Enviroment - env - venv

Pseudo container onde tudo fica dentro.
Tudo pode ser:
   - bibliotecas auxiliares
   - códigos de terceiros
   - ferrametnas de test

## Virtual Enviroment

É composto de um ***diretório*** que vai centralizar toda a estrutura
necessária para sua apliacação funcionar.

minha_env/
   bin/ # binários (ou executáveis, Ex. python)
   lib/ # librarys (bibliotecas compartilhadas do seu amviente virtual)

## Criando ambiente virtual para python 
### Com o meodulo venv

> python3 -m venv nome_do_ambiente

## Para sair do ambiente

> deactivate 

## Removendo ambiente:

```
No Linux:
```
> rm -rf nome_do_ambiente/

```
No windows
```
> del nome_do_ambiente

# AVamos migrar nossa interface da calculadora para Web

Vamos implementar uma calculara que funciona via webservice,
ela ira funcionar da seguinte forma:

- http://localhost/soma/2/3
  Resultado esperado: 5

- http://localhost/div/5/2
  Resultado esperado: 2.5

# Requisitos para criar um webservice

## Preciso de um framework web: 

***Flask*** Microframework escrito em python para python. ;)

## Instalando o flask

> python3 -m pip install flask

## Para instalar e rodar a aplicacao  execute

> python3 -m pip install -r requirements.txt

