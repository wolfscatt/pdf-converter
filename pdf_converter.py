from pdf2docx import Converter

pdf_file = r'Pdf Dosyası Yolu'
docx_file = r'Dönüştürülecek olan docx formatı yolu'

cv = Converter(pdf_file)
cv.convert(docx_file,start=0,end=None)
cv.close()
















