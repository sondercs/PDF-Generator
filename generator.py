from fpdf import FPDF

project_name = input('Enter the project name: ')
estimated_hours = input('Enter the total estimated hours: ')
hours_value = input('Enter the total price of the hour worked: ')

total_value = int(estimated_hours) * int(hours_value)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.image("template.png", x=0, y=0, w=210, h=290)

pdf.text(147, 126, project_name) # Nome do projeto
pdf.text(169, 138, estimated_hours) # Estimativas de horas
pdf.text(169, 150, hours_value) # valor da hora
pdf.text(157, 173, "R$" + str(total_value)) # Valor total

pdf.output("Budget.pdf")
print("Budget generated successfully!")
