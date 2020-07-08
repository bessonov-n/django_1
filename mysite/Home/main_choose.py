# change_fonts.py
from fpdf import FPDF


import datetime


IFIO=''
group=''
ball=''
RFIO=''
prof=''
date = datetime.datetime.today().strftime("%d.%m.%Y")

def profils2(RFIO,group,ball,IFIO,prof):
	pdf = FPDF()
	pdf.set_display_mode(zoom='fullwidth')
	pdf.add_page()
	pdf.image("pic.png",190,280, 7,7)
	pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
	pdf.set_font('DejaVu', '', 14)
	pdf.set_font_size(12)
	pdf.cell(97,15)
	pdf.multi_cell(100,7,'Директору Института Компьютерных Наук и технологий Дробинцеву П.Д. от студента',0,'L',False)
	pdf.set_font_size(12)
	pdf.cell(97,15)
	pdf.multi_cell(100,7,RFIO,0,'L',False)
	pdf.cell(97,15)
	pdf.multi_cell(100,7,group,0,'L',False)
	pdf.cell(97,15)
	pdf.multi_cell(100,7,'27.03.04 Управление в технических системах',0,'L',False)
	pdf.set_font_size(20)
	pdf.set_xy(85,45)
	pdf.cell(50, 30, 'Заявление')
	pdf.set_font_size(15)
	pdf.set_xy(15,55)
	pdf.cell(0, 30, ' Прошу допустить меня к участию в конкурсе по распределению студентов ')
	pdf.set_xy(10,65)
	pdf.cell(1, 30, 'по профилям направления 27.03.04 Управление в технических системах с ')
	pdf.set_xy(10,75)
	pdf.cell(1, 30, 'академическим рейтингом (количеством баллов)')
	pdf.set_font_size(14)
	pdf.set_xy(136,75)
	pdf.cell(1, 30, ball)
	pdf.set_xy(10,90)
	pdf.cell(1, 30, 'Приоритет конкурсных профилей определен мною:')
	pdf.set_xy(10,100)
	pdf.cell(1, 30, '1.')
	pdf.set_xy(10,110)
	pdf.cell(1, 30, '2.')
	pdf.set_xy(10, 140)
	pdf.cell(1, 30, 'Студент')
	pdf.set_xy(70, 140)
	pdf.cell(1, 30, '________________/')
	pdf.set_xy(10, 160)
	pdf.cell(1, 30, 'Дата')
	pdf.set_xy(120, 140)
	pdf.cell(1, 30, IFIO)
	pdf.set_xy(130, 160)
	pdf.cell(1, 30, date)
	if prof=='p02':
		pdf.set_xy(15, 100)
		pdf.cell(1, 30, '  27.03.04_02 Системы и технические средства автоматизации и управления')
		pdf.set_xy(15, 110)
		pdf.cell(1, 30, '  27.03.04_05 Интеллектуальные системы обработки информации и управления')
		pdf.output("main_choose.pdf")
	else:
		pdf.set_xy(15, 100)
		pdf.cell(1, 30, '  27.03.04_05 Интеллектуальные системы обработки информации и управления')
		pdf.set_xy(15, 110)
		pdf.cell(1, 30, '  27.03.04_02 Системы и технические средства автоматизации и управления')
		pdf.output("main_choose.pdf")


