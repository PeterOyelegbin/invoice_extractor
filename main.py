import pytesseract
from pdf2image import convert_from_path

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HomePC\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def extract_invoice_details(pdf_path):
    try:
        # Convert PDF pages to images
        pages = convert_from_path(pdf_path, dpi=300)
        
        # Process the first page (assuming the invoice details are on the first page)
        invoice_text = pytesseract.image_to_string(pages[0])
        
        # Split text into lines for processing
        lines = invoice_text.split('\n')
        
        # Initialize details
        supplier_name, invoice_date, total_amount = None, None, None
        
        # Extract details based on line content
        for line in lines:
            line = line.strip()
            
            if 'Supplier Name' in line or 'Company Name' in line:
                supplier_name = line.split(':')[-1].strip()
            elif 'Invoice Date' in line or 'Period' in line:
                invoice_date = line.replace('Invoice Date', '').strip()
            elif 'Total' in line or 'Gross Amount' in line:
                total_amount = line.replace('Total', '').replace('N', '').strip()
        
        # Fallback for Supplier Name if not explicitly found
        if not supplier_name:
            supplier_name = lines[0]

        # Return the extracted details
        data = {
            "Supplier Name": supplier_name,
            "Invoice Date": invoice_date,
            "Total Amount": total_amount
        }

        # Print invoice details
        print("Extracted Invoice Details:")
        for key, value in data.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Test the function
pdf_path = 'sample3.pdf'
extract_invoice_details(pdf_path)
