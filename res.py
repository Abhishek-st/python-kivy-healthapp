from PyPDF2 import  PdfFileReader, PdfFileWriter

pdf1 = PdfFileWriter()

pdf2 = PdfFileReader('astr.pdf')

pdf1.addPage(pdf2.getPage(0))

with open('astr2.pdf','wb') as out:
	pdf1.write(out)

