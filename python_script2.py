import camelot
import PyPDF2
import json
import pandas as pd
import csv


# Path to the password-protected PDF file
# pdf_path = "D:/PROJECTS/HarshitFreelance/scrapper/contract-notes-broker-wise/contract-notes-broker-wise/icici-securities/411038_8509008928376_20220221_36605_NSE - Amey Athale - amey1906.pdf"
# Password for the PDF file
# password = "amey1906"

pdf_path = "D:/PROJECTS/HarshitFreelance/project_v2/2022-09-01-contract-notes_LF7798 Shruti Apte PW - AFKPA8051J.pdf"
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
                file_path = "D:/PROJECTS/HarshitFreelance/project_v2/file_script2.txt"
                with open(file_path, "a") as file:
                    # Write the text to the file
                    file.write("\n")
                    file.write("Page number: " + str(page_num + 1) + "\n")
                    file.write(text)
                
                # Extract tables from the page using camelot
                tables = camelot.read_pdf(pdf_path, pages=str(page_num+1), password=password)
                print("tables",tables)
                
                if tables:
                    # Print table information
                    for table_num, table in enumerate(tables):
                        print(f"Table {table_num + 1}:")
                        print(table.df)  
                        # Print the table DataFrame
                        # Convert the DataFrame to JSON

                        table_dict = table.df.to_dict(orient='split')
                        column_names = table_dict['columns']
                        data = table_dict['data']

                        # Create a list of dictionaries with column names as keys
                        json_data = [dict(zip(column_names, row)) for row in data]
                        print("json with columns",json_data)  # Print the JSON data



                        # json_data = table.df.to_json(orient='records', column=table.df.columns)
                        # print(json_data)  # Print the JSON data

                        json_file_path = f"D:/PROJECTS/HarshitFreelance/project_v2/Table_Zerodha/table_{page_num + 1}_{table_num + 1}.json"
                        with open(json_file_path, 'w') as json_file:
                            # Write the JSON data to the file
                            json.dump(json_data, json_file)

                        
                        # Save the table as CSV
                        csv_path = f"D:/PROJECTS/HarshitFreelance/project_v2/Table_Zerodha/table_{page_num + 1}_{table_num + 1}.csv"
                        table.to_csv(csv_path)
                        
                        print("Table saved as CSV successfully.")

                        def csvConvert(csv_path, json_path):
                            with open(csv_path, encoding='utf-8') as csvFile, open(json_path, 'w', encoding='utf-8') as jsonFile:
                                csvReader = csv.DictReader(csvFile)
                                jsonData = [{col.strip().replace('\n', ''): row[col] for col in row} for row in csvReader]
                                json.dump(jsonData, jsonFile, indent=4)

                        # csv_path = r'D:\PROJECTS\HarshitFreelance\scrapper\Tables_ICICI_Securities\table_{page_num + 1}_{table_num + 1}.csv'
                        # json_path = r'D:\PROJECTS\HarshitFreelance\scrapper\Tables_ICICI_Securities\new_table_{page_num + 1}_{table_num + 1}.csv'
                        csv_path = r'D:\PROJECTS\HarshitFreelance\project_v2\Table_Zerodha\table_{page_num + 1}_{table_num + 1}.csv'
                        json_path = r'D:\PROJECTS\HarshitFreelance\project_v2\Table_Zerodha\table_{page_num + 1}_{table_num + 1}.json'


                        csvConvert(csv_path, json_path)
                        print("CSV to JSON conversion completed successfully.")
    #             else:
