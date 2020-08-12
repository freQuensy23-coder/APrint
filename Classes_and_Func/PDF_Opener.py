import fitz


def open_PDF(path):
    return fitz.open(path)


def get_pdf_pages(fitz_PDF):
    """Get all pages and text (from fitz PDF document)"""
    result = []
    pdf_pages = []
    for page in fitz_PDF:
        result.append(page.getText("text"))
        pdf_pages.append(page)
    return {"pdf_text":result, "pdf_pages":pdf_pages}
