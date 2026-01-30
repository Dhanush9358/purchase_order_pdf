from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from app.schemas import PurchaseOrderRequest
from app.services.pdf_service import generate_po_pdf

app = FastAPI(title="Purchase Order PDF Generator")

# Serve static assets (logo, signature)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home():
    return FileResponse("frontend/index.html")


@app.post("/api/generate-po")
def generate_po(data: PurchaseOrderRequest):
    pdf_bytes = generate_po_pdf(data)
    return StreamingResponse(
        pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=purchase_order.pdf"},
    )
