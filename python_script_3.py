from tabula import read_pdf
import pandas as pd
import json
import csv
import PyPDF2
import camelot
import os
import sys
import re
import shutil

df = read_pdf("D:/PROJECTS/HarshitFreelance/project_v2/2022-09-01-contract-notes_LF7798 Shruti Apte PW - AFKPA8051J.pdf", pages="all",password="AFKPA8051J" ,multiple_tables=True,output_format = "json" ,lattice=True, pandas_options={'header': None})
print(df)
print("df",df[0]['data'])

import json

# Specify the output file path
json_file = "output.json"

# Open the output file in write mode
with open(json_file, "w") as file:
 # Write the list of JSON objects to the file
 json.dump(df, file)



 tabula.convert_into("1710.05006.pdf", "output.csv", output_format="csv", pages="all")

