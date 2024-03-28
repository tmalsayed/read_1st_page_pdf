import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog

def select_pdf_files():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])  # Allows multiple selection
    return file_paths

def extract_first_page_and_save(pdf_paths):
    for pdf_path in pdf_paths:
        with open(pdf_path, 'rb') as infile:
            reader = PyPDF2.PdfReader(infile)
            writer = PyPDF2.PdfWriter()
            
            # Add only the first page
            writer.add_page(reader.pages[0])

            output_pdf_path = pdf_path.replace('.pdf', '_1st.pdf')
            with open(output_pdf_path, 'wb') as outfile:
                writer.write(outfile)

            print(f"Extracted first page saved as {output_pdf_path}")

# Select PDF files through file dialog
pdf_paths = select_pdf_files()
extract_first_page_and_save(pdf_paths)