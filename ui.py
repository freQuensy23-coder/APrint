from Classes_and_Func.PagesFunc import *


def main(file_path):
    _, pages_texts = get_pages_texts_docs(file_path)
    
    images = get_pdf_images(file_path)

    pages_data = get_pages_data(pages_texts)



if __name__ == '__main__':
    main("test.pdf")