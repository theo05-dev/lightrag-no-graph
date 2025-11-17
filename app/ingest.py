from lightrag import LightRAG
from PyPDF2 import PdfReader
from pathlib import Path

def initialize_rag(working_dir="db"):
    """
    Inicializa o LightRAG 100% SEM GRAPH.
    """
    return LightRAG(
        working_dir,
        graph_enabled=False,
        enable_graph_index=False,
        graph_mode="none",
        enable_llm_for_edges=False,
        enable_edge_llm=False,
        do_reflection=False,
        do_initial_summary=False,
        do_summary=False,
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
    """
    rag.insert(text)
    graph_dir = Path(working_dir) / "graph"

    return {
        "graph_exists": graph_dir.exists(),
        "graph_files": [str(f) for f in graph_dir.glob("**/
def query_rag(rag, query):
    return rag.query(query)
