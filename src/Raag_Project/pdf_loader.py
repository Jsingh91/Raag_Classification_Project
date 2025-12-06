import pdfplumber
# Load PDF
def load_pdf_text(pdf_path):
    """
    Open a PDF, read all pages, and return one big string.
    """
    all_pages_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                all_pages_text.append(page_text)

    full_text = "\n\n".join(all_pages_text)
    return full_text


# PDF-Txt
def get_txt_file(pdf_text):
    """
    Write the text of pdf passed and save as a txt file.
    
    """
    txt_path = "../data/raw_text/Gurbani_with_index_Uni.txt"
    with open(txt_path,"w", encoding="utf-8") as text_file:
        text_file.write(pdf_text)
    return txt_path
    

        
        

    



        
            