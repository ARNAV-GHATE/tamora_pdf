import camelot
import PyPDF2
import json
import pandas as pd
import csv
import tabula


# Path to the password-protected PDF file
# pdf_path = "D:/PROJECTS/HarshitFreelance/scrapper/contract-notes-broker-wise/contract-notes-broker-wise/icici-securities/411038_8509008928376_20220221_36605_NSE - Amey Athale - amey1906.pdf"
# Password for the PDF file
# password = "amey1906"

pdf_path = "D:/PROJECTS/HarshitFreelance/scrapper/contract-notes-broker-wise/contract-notes-broker-wise/zerodha/2022-09-01-contract-notes_LF7798 Shruti Apte PW - AFKPA8051J.pdf"
password = "AFKPA8051J"


# Open the PDF file in read binary mode
with open(pdf_path, "rb") as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)

    # Check if the PDF is encrypted
    if reader.is_encrypted:
        # Decrypt the PDF using the provided password
        if reader.decrypt(password):
            # Successfully decrypted the PDF
            # Access the PDF content
            num_pages = len(reader.pages)
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                # Do further processing with the extracted text
                print(f"Page {page_num + 1}:")
                file_path = "D:/PROJECTS/HarshitFreelance/scrapper/file.txt"
                with open(file_path, "a") as file:
                    # Write the text to the file
                    file.write("\n")
                    file.write("Page number: " + str(page_num + 1) + "\n")
                    file.write(text)
                
                # Extract tables from the page using camelot
                tables = camelot.read_pdf(pdf_path, pages=str(page_num+1), password=password)
                tables.export("D:/PROJECTS/HarshitFreelance/scrapper/tables.csv", f="csv", compress=True) # json, excel, html
                tables[0]
                print(tables[0])
                tables[0].parsing_report
                tables[0].to_csv("D:/PROJECTS/HarshitFreelance/project_v2/tables.csv")
                tables[0].df
                print(tables[0].df)
                print("tables",tables)

