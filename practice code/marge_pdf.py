from pypdf import PdfWriter #PdfMerger is deprecated and will be removed in pypdf 5.0.0. Use PdfWriter instead 

def pdf_marger(pdfs,output):
    pdfmarger=PdfWriter()
    for pdf in pdfs:
        pdfmarger.append(pdf)
    # with open(output,'wb') as f:
    pdfmarger.write(output)
pdfs=['bonafide.pdf','commonFileDownloader.pdf']
output='marged_pdf2.pdf'
pdf_marger(pdfs,output)
