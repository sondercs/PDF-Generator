from fpdf import FPDF

project_description = input('Enter the project description: ')
estimated_hours = input('Enter the total estimated hours: ')
hours_worked = input('Enter the total hours worked: ')
deadline = input('Enter the estimated deadline: ')

total_value = int(estimated_hours) * int(hours_worked)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, project_description) # Precisa de correção
pdf.text(115, 160, estimated_hours) # Precisa de correção
pdf.text(115, 175, hours_worked) # Precisa de correção
pdf.text(115, 190, deadline) # Precisa de correção
pdf.text(115, 205, str(total_value)) # Precisa de correção

pdf.output("Budget.pdf")
print("Budget generated successfully!")
