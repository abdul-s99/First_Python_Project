import math
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PdfCompilerClasses import PageSetup

if __name__ == '__main__':

    imagePaths = ["THP_1_SQUARE_CUTOUT.PNG", "THP_2_SQUARE_CUTOUT.PNG", "THP_3_SQUARE_CUTOUT.PNG"]
    imageSizes = [(300, 180)]
    imagePositions = [(30, 40), (30, 240), (30, 460)]

    page = PageSetup("TestPDF.pdf",
                     r"C:\Users\Abdul.Sharif\PycharmProjects\First_Python_Project\TORO\Training With "
                     r"Sai\ThontD_FL03_20231566_THP.csv")

    total_items = len(imagePaths)
    total_pages = math.ceil(total_items / 3)
    page_filenames = []

    for page_number in range(total_pages):
        c = canvas.Canvas(f"Page_{page_number + 1}.pdf", pagesize=letter)
        page.generate_page(c, imagePaths, imageSizes, imagePositions)
        page_filenames.append(f"Page_{page_number + 1}.pdf")

    output_pdf = "TestPDF.pdf"
    print(f"PDF created: {output_pdf}")
    print(f"Total pages created: {total_pages}")
