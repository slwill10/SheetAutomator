## Sheet Automator
Sheet Automator é uma aplicação simples que permite que os usuários insiram dados em um formulário gráfico utilizando Tkinter. Os dados inseridos são enviados para uma planilha do Google Sheets, permitindo fácil gerenciamento e consulta. O projeto foi desenvolvido em Python e usa a API do Google Sheets para integrar e automatizar a inserção de dados.

## Funcionalidades

Formulário de Entrada de Dados: Interface gráfica que permite inserir dados em campos como "Data", "Nome da Campanha" e "Status do Print".
Envio de Dados: Após o preenchimento, os dados são enviados e registrados automaticamente em uma planilha do Google Sheets.
Abertura da Planilha: O usuário pode acessar diretamente a planilha no navegador por meio de um botão.
Validação de Dados: Verifica se todos os campos foram preenchidos corretamente antes de enviar os dados.
Tecnologias Utilizadas
Tkinter: Para a construção da interface gráfica.
Google Sheets API: Para integração com planilhas do Google.
gspread: Biblioteca Python para interagir com o Google Sheets.
oauth2client: Biblioteca para autenticação com a API do Google Sheets.

## Pré-requisitos
Antes de executar este projeto, é necessário instalar as dependências e configurar o acesso à API do Google Sheets.

## Dependências
Este projeto requer as seguintes bibliotecas Python:

tkinter (geralmente já incluído com o Python)
gspread
oauth2client
Você pode instalar as dependências necessárias com o seguinte comando:

bash

Copiar código

## pip install -r requirements.txt
