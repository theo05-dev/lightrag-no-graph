from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
from .ingest import (
    initialize_rag,
    load_pdf_text,
    insert_text_and_check_graph,
    query_rag
)

app = FastAPI()

# Inicializa o LightRAG SEM GRAPH
rag = initialize_rag("db")

@app.post("/insert_pdf")
async def insert_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Somente arquivos PDF são aceitos.")

    content = await file.read()
    temp_file = "temp_upload.pdf"

    with open(temp_file, "wb") as f:
        f.write(content)

    text = load_pdf_text(temp_file)
    result = insert_text_and_check_graph(rag, text, "db")

    Path(temp_file).unlink()

    return JSONResponse({"ok": True, "graph_check": result})

@app.get("/query")
def query(q: str):
    answer = query_rag(rag, q)
    return {"answer": answer}

@app.get("/health")
def health():
    graph_dir = Path("db/graph")
    return {
        "ok": True,
        "graph_exists": graph_dir.exists(),
        "graph_files": [str(f) for f in graph_dir.glob("**/*")] if graph_dir.exists() else []
        }
