import PIL


def get_file_name(filename):
    """Returns filename without extension"""
    dot_array = filename.split(".")
    res = ""
    for el in dot_array[:-1]:
        res += el
    return res


class Printer:
    def __init__(self, image_file, file_name):
        self.image_file = image_file
        self.file_name = file_name

    def save(self):
        self.image_file.save(get_file_name(self.file_name) + "_withQR.pdf")

    def print_doc(self):
        """Print document"""
        # TODO: Complete this task
