import streamlit as st
from backend import cria_chain_conversa, folder_files
from langchain.memory import ConversationBufferMemory


def chat_app():
    st.header("🤖 Bem vindo ao ChatPDF", divider =True)
    if not "chain" in st.session_state:
        st.error("Por favor, faça o upload de pelo menos um arquivo PDF para iniciar o chat.")
        st.stop()

    chain = st.session_state["chain"]
    memory = chain.memory
    mensagens = memory.load_memory_variables({})["chat_history"]
  

   
    container = st.container()
    for mensagem in mensagens:
        chat = container.chat_message(mensagem.type)
        chat.markdown(mensagem.content)

    nova_mensagem = st.chat_input("Converse com seus documentos")
    if nova_mensagem:
        chat = container.chat_message("human")
        chat.markdown(nova_mensagem)
        chat = container.chat_message("ai")
        chat.markdown("Gerando sua resposta...")
        chain.invoke({"question": nova_mensagem})
        st.rerun()
        

def save_uploaded_files(uploaded_files, folder):
    """Salva os arquivos enviados pelo usuário na pasta especificada."""
    for file in folder.glob("*.pdf"):
        file.unlink()
    """Salvar novos arquivos enviados pelo usuário."""
    for file in uploaded_files:
        (folder / file.name).write_bytes(file.read())


def main():
    with st.sidebar:
        st.header("Upload de PDFs")
        uploaded_pdfs = st.file_uploader("Adicione arquivos PDF", type="pdf", accept_multiple_files=True)
        if uploaded_pdfs:
            save_uploaded_files(uploaded_pdfs, folder_files)
            st.success(f"{len(uploaded_pdfs)} arquivos PDF foram salvos com sucesso!")

        lable_botao = "Inicializar Chat"
        if "chain" in st.session_state:
            lable_botao = "Atualizar Chat"
        if st.button(lable_botao, use_container_width=True):
            if len(list(folder_files.glob("*.pdf"))) == 0:
                st.warning("Por favor, faça o upload de pelo menos um arquivo PDF para iniciar o chat.")
            else:
                st.success("inicializando o Chat...")
                cria_chain_conversa()
                st.rerun()

    chat_app()

if __name__ == "__main__":
    main()