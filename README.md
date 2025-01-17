# Invoice Extractor
It uses the OCR tool [Tesseract](https://github.com/tesseract-ocr/tesseract) to recognize text from the PDF file. This Python script processes a PDF invoice and extracts specific details: 
- **Supplier Name**
- **Invoice Date**
- **Total Amount**

## Usage
1. Clone this repository or download the script.
2. Install Tesseract OCR. Instructions are available on the [official GitHub page](https://github.com/tesseract-ocr/tesseract).
3. App poppler binary from the project directory to your system environment variable
    ```envfile
    C:\file-path\invoice_extractor\poppler-24.08.0\bin
    ```
4. Modify the path in line 5 of the script to the installation path of Tesseract OCR.
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HomePC\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    ```
5. Install the necessary Python libraries using pip:
     ```bash
     pip install -r requirements.txt
     ```
6. Modify line 52 of the script to your sample PDF invoice
    ```python
    pdf_path = 'sample.pdf'
    ```
7. Run the script with the following command:
   ```bash
   python main.py
   ```
8. The script outputs the extracted details in the terminal.


## Note:
Kindly note that this script depends on the formatting of the invoice.
