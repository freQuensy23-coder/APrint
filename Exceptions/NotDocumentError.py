
class NotDocumentError(Exception):
    """Вызывается, когда переданная страница не является главной страницей документа (с надписью извещание итп"""
    def __init__(self):
        self.txt = "This page is not main document's page"
