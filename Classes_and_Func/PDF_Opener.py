import fitz


def open_PDF(path):
    return fitz.open(path)


def get_pdf_pages_text(fitz_PDF):
    """Get all pages text (from fitz document)"""
    result = []
    for page in fitz_PDF:
        result.append(page.getText("text"))
    return result
