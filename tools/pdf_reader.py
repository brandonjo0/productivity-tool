import fitz

def read_pdf(path):
    """
    Reads and extracts text from all pages of a PDF file.

    @param path: The file path of the PDF to read.
    @return: A string containing all extracted text from the PDF.
    """
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text