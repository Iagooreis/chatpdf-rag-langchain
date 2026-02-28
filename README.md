📄 ChatPDF com RAG (LangChain + Streamlit)

<img width="1911" height="902" alt="image" src="https://github.com/user-attachments/assets/414b93b3-5ad4-4756-a3fe-591846814f97" />

--------------------------------------------------------------------------

Aplicação web que permite fazer perguntas sobre documentos PDF utilizando:

🔎 RAG (Retrieval Augmented Generation)

🤖 LangChain

🧠 OpenAI (GPT-3.5)

📚 FAISS (Vector Store)

🖥 Streamlit (Interface Web)

-------------------------------------------------
🚀 Como funciona

O usuário faz upload de um ou mais PDFs.

Os documentos são:

- Carregados com PyPDFLoader

- Divididos em chunks com RecursiveCharacterTextSplitter

- Vetorizados com OpenAIEmbeddings

- Armazenados no FAISS

Um ConversationalRetrievalChain permite:

- Recuperar trechos relevantes

- Manter histórico da conversa

Responder com base no conteúdo do PDF

-------------------------------------------------

🔧 Tecnologias Utilizadas

Python 3.12

Streamlit

LangChain 0.1.17

FAISS

OpenAI API

python-dotenv

-------------------------------------------------
⚙️ Instalação
1️⃣ Clone o repositório:

- git clone https://github.com/seuusuario/chatpdf.git
- cd chatpdf

2️⃣ Crie o ambiente virtual:
- py -3.12 -m venv .venv
- .\.venv\Scripts\Activate.ps1
  
3️⃣ Instale as dependências:
- pip install -r requirements.txt
  
🔑 Configuração da API Key:

- Crie um arquivo .env na raiz do projeto
- OPENAI_API_KEY=sua_chave_aqui

⚠️ Nunca envie sua API key para o GitHub.

▶️ Executar o projeto:
- streamlit run app.py
  
Depois acesse:
- http://localhost:8501
  
-------------------------------------------------
💬 Como usar

Faça upload de um ou mais PDFs

Clique em Inicializar Chat

Comece a fazer perguntas sobre os documentos

-------------------------------------------------
🧠 Funcionalidades

Upload múltiplo de PDFs

Indexação automática

Memória conversacional

Busca vetorial com FAISS

Respostas contextualizadas

-------------------------------------------------
👨‍💻 Autor

- Desenvolvido por Iago Reis 🚀
- Projeto de estudo em RAG + LangChain
