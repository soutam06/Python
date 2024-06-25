from PyPDF2 import PdfReader, PdfWriter

def PDFrotate(origFileName, newFileName, rotation):
    # creating a pdf Reader object 
    reader = PdfReader(origFileName)

    # creating a pdf writer object for new pdf 
    writer = PdfWriter()

    # rotating each page 
    for page in range(len(reader.pages)):
        # creating rotated page object 
        pageObj = reader.pages[page]
        # if rotation > 0:
        pageObj = pageObj.rotate(rotation)
        # else:
        #     pageObj = pageObj.rotate(-rotation)

        # adding rotated page object to pdf writer 
        writer.add_page(pageObj)

    # new pdf file object 
    with open(newFileName, 'wb') as newFile:
        # writing rotated pages to new file 
        writer.write(newFile)

# original pdf file name 
origFileName = 'delegatepass (1).pdf'

# new pdf file name 
newFileName = 'rotated_example.pdf'

# rotation angle 
rotation = 270

# calling the PDFrotate function 
PDFrotate(origFileName, newFileName, rotation)
