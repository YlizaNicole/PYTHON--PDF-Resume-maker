# PDF Resume Creator
# 	- Create a python program that will create your personal resume in PDF format
# 	- All personal details are stored in a JSON file
# 	- Your program should read the JSON file and write the details in the PDF
# 	- The output file should be: LASTNAME_FIRSTNAME.pdf

from ast import In
import json
import os
from statistics import LinearRegression
from textwrap import fill
from turtle import fillcolor
from fpdf import FPDF
from PIL import Image

#json loc
cdirectory = os.getcwd()
print(cdirectory)
jsonfile = "%s/%s" % (cdirectory, "info.json")
jsondata = {}

#store in json
with open(jsonfile) as data_file:
    jsondata = json.load(data_file)

#Info
name = jsondata ["name"]
ad1= jsondata ["present ad"]
ad2 = jsondata ["permanent ad"]

#Contact
Email = jsondata ["email"]
Telenum = jsondata ["Telephone no."]
Pnumber = jsondata ["Phone no."]

#objective
Object1= jsondata ["objective1"]
Object2= jsondata ["objective2"]
Object3= jsondata ["objective3"]


#skills
sk1=jsondata["skills1"]
sk2=jsondata["skills2"]
sk3=jsondata["skills3"]

#character ref
ch1= jsondata["character 1"]
ch2= jsondata["character 2"]
ch3= jsondata["character 3"]

#educational background
College = jsondata ["college"]
Shs = jsondata ["senior high school"]
Jhs = jsondata ["junior high school"]


#create pdf file
pdf = FPDF ("P","cm","A4")
pdf.add_page ()
pdf.image('bg2.jpg', x = -5.6, y = -2, w = 0, h = 0, type = '', link = '')


#header
pdf.set_font("Times", "B", 32)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(247, 229, 205)
pdf.cell(0, 2, name, ln=.05, align="L", border=0, fill=0)
pdf.set_font("Times", "", 12)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(247, 229, 205)
pdf.cell(0,0.5, "Telephone Number: " + Telenum, align="L", ln=1, fill=0)
pdf.set_font("Times", "", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0,0.5, "Phone number: " + Pnumber, align="L", ln=1, fill=0)
pdf.cell(0,0.5, "Email: " + Email, align="L", ln=1, fill=0)
pdf.cell(0,0.5, "Present Address: " + ad1, align="L", ln=1, fill=0)
pdf.cell(0,0.5, "Permanent Address: " + ad2, align="L", ln=1, fill=0)
pdf.image('ID.png', 15, 1.25, 4.5)

pdf.ln(0.55)


pdf.set_font("Times", "B", 15)
pdf.set_text_color(255,255,255)
pdf.set_fill_color(40, 36, 29)
pdf.cell(0,1, "OBJECTIVE", align="C", ln=1, fill=1)
pdf.set_font("Times", "", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0,0.75, Object1, align="J", ln=1, fill=0)
pdf.cell(0,0.75, Object2, align="J", ln=1, fill=0)
pdf.cell(0,0.75, Object3, align="J", ln=1, fill=0)
pdf.ln(0.55)

pdf.set_font("Times", "B", 15)
pdf.set_text_color(255,255,255)
pdf.set_fill_color(40, 36, 29)
pdf.cell(0,1, "EDUCATIONAL BACKGROUND", align="C", ln=1, border=1, fill=1)
pdf.set_font("Times", "B", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0,0.75, "Year: 2021-2025" , ln=1, fill=0)
pdf.set_font("Times", "", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0,0.75, "University: " + College, align="L", ln=1, fill=0)
pdf.set_font("Times", "B", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0,0.75, "Year: 2019-2021" , ln=1, fill=0)
pdf.set_font("Times", "", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0,0.75, "Senior Highschool: " + Shs, align="L", ln=1, fill=0)
pdf.set_font("Times", "B", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0,0.75, "Year: 2015-2019" , ln=1, fill=0)
pdf.set_font("Times", "", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0,0.75, "Junior Highschool: " + Jhs, align="L", ln=1, fill=0)

pdf.set_font("Times", "B", 15)
pdf.set_text_color(255,255,255)
pdf.set_fill_color(40, 36, 29)
pdf.cell(0,1, "SKILLS", align="C", ln=1, fill=1)
pdf.set_font("Times", "", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0,0.75, sk1, align="J", ln=1, fill=0)
pdf.cell(0,0.75, sk2, align="J", ln=1, fill=0)
pdf.cell(0,0.75, sk3, align="J", ln=1, fill=0)
pdf.ln(0.55)
pdf.set_font("Times", "B", 15)
pdf.set_text_color(255,255,255)
pdf.set_fill_color(40, 36, 29)
pdf.cell(0,1, "CHARACTER REFERENCE", align="C", ln=1, fill=1)
pdf.set_font("Times", "", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0,0.75, ch1, align="J", ln=1, fill=0)
pdf.cell(0,0.75, ch2, align="J", ln=1, fill=0)
pdf.cell(0,0.75, ch3, align="J", ln=1, fill=0)
pdf.ln(0.55)

pdf.set_font("Times", "B", 12)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(247, 229, 205)
pdf.cell(0,1,"* * * INFORMATION WILL BE AVAILABLE IF REQUESTED * * *",  align="C", ln=1, fill=0)
pdf.cell(0,1,"* * * * * *",  align="C", ln=1, fill=0)
pdf.cell(0,1,"* * * ALL STATED INFORMATION IS DELARED TRUE AND ACCURATE * * *",  align="C", ln=1, fill=0)

pdf.output ("SALAZAR_YLIZA.pdf")



