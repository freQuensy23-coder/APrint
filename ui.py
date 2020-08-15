from Classes_and_Func.PagesFunc import *
pages_texts, images, pages_data = 0, 0, 0


def getting_data_from_pdf(file_path):
    global pages_data, pages_texts, images
    _, pages_texts = get_pages_texts_docs(file_path)

    images = get_pdf_images(file_path)

    pages_data = get_pages_data(pages_texts)



def main(file_path):
    getting_data_from_pdf(file_path)
    global pages_data, pages_texts, images
    



if __name__ == '__main__':
    main("test.pdf")