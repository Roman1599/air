import pdfplumber
import json

def extract_pdf_data(pdf_path):
    extracted_data = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split("\n"):
                    if ":" in line:
                        key, value = line.split(":", 1)
                        extracted_data[key.strip()] = value.strip()
    return extracted_data

# Запуск обработки (пример)
if __name__ == "__main__":
    pdf_path = "test_task.pdf"  # Укажи путь к PDF
    data = extract_pdf_data(pdf_path)
    print(json.dumps(data, indent=4, ensure_ascii=False))
