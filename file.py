import requests
# used to get pdf files or urls
from bs4 import BeautifulSoup
# for tree traversal scraping 
import io 
from PyPDF2 import PdfFileReader

url = "https://www.ku.ac.ke/"
read = requests.get(url)
html_content = read.html_content
soup = BeautifulSoup(html_content, "html.parser")

list_of_pdf = set()
l = soup.find('p')
p = l.find_all('a')

for link in (p):
    pdf_link = (link.get('href') [:-5]) + ".pdf"
    print(pdf_link)
    list_of_pdf.add(pdf_link)

    def info(pdf_path):
        response = requests.get(pdf_path)

        with io.BytesIO(response.content) as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
        txt = f"""
        Information about {pdf_path}
        Creator: {information.creator}
        Author: {information.author}
        Subject: {information.subject}
        Title: {information.title}
        Number of pages: {number_of_pages}

        print(txt)
        return information

    for i in list_of_pdf:    
        info(i)