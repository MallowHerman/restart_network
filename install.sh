#!/bin/sh

# \n

echo "Iniciando as instalações necessárias...\n\n###########################\n\n"
echo "Iniciando a clonagem do repositório...\n\n"

git clone https://github.com/MallowHerman/restart_network.git

echo "Entrando na pasta restart_network...\n\n"
cd restart_network
cp .env.sample .env
 
echo "Criando um ambiente virtual para a instalação das dependências do código...\n\n"

python3 -m venv venv
source venv/bin/activate

echo "Instalando as dependências dentro do requirements.txt...n\n"
pip install --upgrade pip && pip install -r requirements.txt
