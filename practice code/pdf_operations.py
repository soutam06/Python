# FOR READING THE PDF

# importing required classes 
from pypdf import PdfReader 

# creating a pdf reader object 
reader = PdfReader('delegatepass (1).pdf') 

# printing number of pages in pdf file 
print(len(reader.pages)) 

# creating a page object 
page = reader.pages[0] 

# extracting text from page 
print(page.extract_text(),end=" ") 


