import os
from lightrag import LightRAG
from lightrag.llm import OpenAI
from lightrag.embeddings import OpenAIEmbedder
from PyPDF2 import PdfReader
from pathlib import Path


def initialize_rag(working_dir="db"):
    """
    Inicializa o LightRAG SEM GRAPH.
    Agora compatível com a versão nova (1.4.9.9).
    """

    llm = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    embedder = OpenAIEmbedder(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="text-embedding-3-large"
    )

    return LightRAG(
        working_dir=working_dir,
        llm=llm,
        embedding=embedder
    )


def load_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t + "\n"
    return text


def insert_text_and_check_graph(rag, text, working_dir="db"):
    """
    Insere o texto no LightRAG e checa se algum grafo foi criado.
    (Não deve criar nada se graph estiver desativado internamente)
    """
    rag.insert(text)

    graph_dir = Path(working_dir) / "graph"

    return {
        "graph_exists": graph_dir.exists(),
        "graph_files": [str(f) for f in graph_dir.glob("**/*")] if graph_dir.exists() else []
    }


def query_rag(rag, query):
    return rag.query(query)
