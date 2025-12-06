import pdfplumber

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

                
                

        
        

    



        
            