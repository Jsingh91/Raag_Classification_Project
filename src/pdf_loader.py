import pdfplumber

def load_pdf_text(pdf_path):
    """
    This will open the pdf file and iterate over all pages, extracts text for each page, joins it into a single string, and returns that string.

    Parameters:
    pdf_path: This is the string path to a pdf file.
    Returns:
     Single string containing the concatenated text from all pages.
    
    
    """
        all_pages_text = []
        with pdfplumber.open(pdf_path) as pdf:
            for idx,page_text in enumerate(pdf.pages,start=1):
                text = page_text.extract_text()

                if text:
                    all_pages_text.append(text)
                
               
            
         full_text = "\n\n".join(all_pages_text) 
         return full_text   
                
                

        
        

    



        
            