# Um Chatbot Impulsionado por LangChain e GPT-3.5 para Análise de Relatórios da CGU

Este repositório é a implementação de um chatbot impusionado por LangChain e GPT-3.5, maiores descrições estão no artigo https://medium.com/@glleddson/um-chatbot-impulsionado-por-langchain-e-gpt-3-5-para-análise-de-relatórios-da-cgu-178c3553dade

## Executando a aplicação localmente

1. Instale as dependências pelo arquivo requirements.txt.
2. Para iniciar o frontend no navegador digite na linha de comando o seguinte código "python -m panel serve 'interface_pesquisa.py' --autoreload --show".

## Descrição dos arquivos
1. chatrelatorio.py: implementação das classes principais que realiza a conversa com o usuário e cria o banco de dados vetorizado.
2. criabd.ipynb: Jupyter Notebook que cria o banco de dados vetorizado no diretorio "bd" com base no JSON do diretorio "relatorios".
3. interface_pesquisa.py: implementação do frontend do chatbot.

## Conexão com a OpenAI 

É necessário criar um arquivo .env na raiz com a definição das seguintes variáveis de ambiente:

OPENAI_API_KEY = "your-api-key" 

Estas são necessárias apenas com o serviço do Azure:
OPENAI_API_TYPE = "azure"
OPENAI_API_BASE = "https://your-api-base.openai.azure.com/"
OPENAI_API_VERSION = "2023-05-15"