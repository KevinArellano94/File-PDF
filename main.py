from fpdf import FPDF
# https://www.askpython.com/python-modules/fpdf-module-convert-to-pdf

def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 10)
    pdf.cell(200, 10, txt = "Kevin Arellano", ln = 1, align = 'C')
    pdf.cell(200, 10, txt = "This is how to create a pdf file with Python!", ln = 2, align = 'C') 
    pdf.output("data.pdf")
    print(f'Completed')

if __name__ == "__main__":
    main()