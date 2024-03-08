from PyPDF2 import PdfFileReader, PdfFileWriter
pdf_file_path = 'file.pdf'
pdf = PdfFileReader(pdf_file_path)

page = [1]
pdfwriter = PdfFileWriter()

for page_num in page:
    pdfwriter.addPage(pdf.getPage(page_num))


with open ('output.pdf','wb') as out:
    pdfwriter.write(out)
print ('PDF file has been split')
