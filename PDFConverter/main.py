from pdf2docx import Converter

pdfFile = "belge.pdf"
docxFile = "convertBelge.docx"

cv = Converter(pdf_file=pdfFile)
cv.convert(docx_filename=docxFile)
cv.close()