import fitz


class Converter:
    """Конвертирует fitz document page в текст страницы"""
    def __int__(self, page):
        self.page_text = page.getText("text")