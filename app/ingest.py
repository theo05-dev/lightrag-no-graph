import os
from lightrag import LightRAG
from lightrag.llm import OpenAI
from lightrag.embeddings import OpenAIEmbedder
from PyPDF2 import PdfReader

def initialize_rag(working_dir="db"):
    llm = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    embedder = OpenAIEmbedder(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="text-embedding-3-large"
    )

    # LightRAG atual NÃO aceita graph_enabled nem enable_summary
    return LightRAG(
        working_dir=working_dir,
        llm=llm,
        embedder=embedder
    )

def load_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"
    return text

def insert_text_and_check_graph(rag, text, working_dir="db"):
    from pathlib import Path

    rag.insert(text)
    graph_dir = Path(working_dir) / "graph"

    return {
        "graph_exists": graph_dir.exists(),
        "graph_files": [str(f) for f in graph_dir.glob("**/*")] if graph_dir.exists() else []
    }

def query_rag(rag, query):
    return rag.query(query)
