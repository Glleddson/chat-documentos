import panel as pn
from typing import List, Dict
import os
from pathlib import Path

HOME_DIR = os.getcwd() if __name__.startswith('bokeh') else Path(os.getcwd()).parent

from chatrelatorios import ChatRelatoriosAuditoria

qa = ChatRelatoriosAuditoria(home_dir=HOME_DIR, persist_directory='bd\\chroma',
                              deployment_name='Teste', deployment_name_embedding='teste-embedding')

pn.extension('gridstack', 'texteditor','jsoneditor', template="bootstrap", sizing_mode='stretch_width', notifications=True)
pn.state.notifications.position = 'top-left'
pn.state.template.param.update(header_background="#F08080")

msg_inicial = 'Olá! Bem-vindo ao AuditPesquisa, o seu assistente virtual para pesquisa e' + \
              ' consulta de relatórios de auditoria da Controladoria Geral da União (CGU).' + \
              ' Estou aqui para ajudá-lo a encontrar informações transparentes e relevantes'+ \
              ' contidas nos relatórios de auditoria. Você pode digitar palavras-chave, temas,'+ \
              ' números de relatórios ou até mesmo fazer perguntas diretas. Eu estou aqui para' + \
              ' tornar a busca por informações e insights uma experiência simples e eficiente.' + \
              ' Vamos começar explorando os relatórios juntos!'

chat_box = pn.widgets.ChatBox(
    value=[
        {'AuditPesquisa': msg_inicial}
    ],    
    primary_name = 'Você'
)

def chat(user_messages: List[Dict[str, str]]) -> None:
    user_message = user_messages[-1]
    input = user_message.get("Você")
    if input is None:
        return
    resposta = qa(input)

    resposta = pn.Column(resposta['answer'], '<hr/>', '**Documentos Consultados:**<br>' + \
              ''.join([f'<a href="{docs.metadata["source"]}"> {i+1} - {docs.metadata["titulo"]}</a><br/>' for i, docs in enumerate(resposta['source_documents'])]))

    chat_box.append({"AuditPesquisa": resposta})

pn.bind(chat, user_messages=chat_box, watch=True)

pn.Row(chat_box).servable("Pesquisa em relatórios da CGU")
