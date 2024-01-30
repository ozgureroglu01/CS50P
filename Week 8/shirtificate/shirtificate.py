from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 45)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate",  align="C")
        self.ln(20)



def main():
    name = input("Name: ").strip().title()
    genarate(name)


def genarate(name):
    pdf = PDF()
    pdf.add_page()
    pdf.set_margin(0)
    pdf.image("shirtificate.png")
    width = len(name) * 13
    x = (pdf.w - width) / 2
    y = pdf.h / 2
    pdf.set_xy(x, y)
    pdf.set_font("helvetica", "B", 30)
    pdf.set_text_color(255, 255, 255)
    pdf.multi_cell(width, 10, f"{name} took CS50", align='C')
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
