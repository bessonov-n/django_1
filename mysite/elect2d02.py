# change_fonts.py
from fpdf import FPDF


import datetime

RFIO=''
IFIO=''
group=''
prof1=''
prof2=''
prof3=''
prof4=''
prof5=''

date = datetime.datetime.today().strftime("%d.%m.%Y")

def profils2(RFIO,IFIO,group,prof1,prof2,prof3,prof4,prof5):
    pdf: FPDF = FPDF()
    pdf.set_display_mode(zoom='fullwidth')
    pdf.add_page()
    pdf.image("pic.png",190,280, 7,7)
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    pdf.set_font_size(12)
    pdf.cell(97,15)
    pdf.multi_cell(100,6,
    'Руководителю образовательной программы 27.03.04_02 Системы и технические средства автоматизации и управления Онуфриеву В.А. от студента группы',0,'L',False)
    pdf.cell(97, 40)
    pdf.multi_cell(100, 7, group, 0, 'L', False)
    pdf.set_font_size(12)
    pdf.cell(96,20)
    pdf.multi_cell(100,4,RFIO)
    pdf.set_font_size(20)
    pdf.set_xy(85,40)
    pdf.cell(50, 30, 'Заявление')
    pdf.set_font_size(15)
    pdf.set_xy(15,60)
    pdf.multi_cell(0, 7, ' Прошу утвердить в качестве дисциплин элективных и факультативного модуля:')


    pdf.rect(x=33, y=80, w=90, h=17)
    pdf.rect(x=123, y=80, w=32, h=17)
    pdf.rect(x=155, y=80, w=32, h=17)

    pdf.rect(x=33, y=97, w=154, h=8)

    pdf.rect(x=33, y=105, w=90, h=12)
    pdf.rect(x=123, y=105, w=32, h=12)
    pdf.rect(x=155, y=105, w=32, h=12)

    pdf.rect(x=33, y=117, w=154, h=8)

    pdf.rect(x=33, y=125, w=90, h=10)
    pdf.rect(x=123, y=125, w=32, h=10)
    pdf.rect(x=155, y=125, w=32, h=10)

    pdf.rect(x=33, y=135, w=154, h=10)

    pdf.rect(x=33, y=145, w=90, h=10)
    pdf.rect(x=123, y=145, w=32, h=10)
    pdf.rect(x=155, y=145, w=32, h=10)

    pdf.rect(x=33, y=155, w=154, h=10)

    pdf.rect(x=33, y=165, w=90, h=10)
    pdf.rect(x=123, y=165, w=32, h=10)
    pdf.rect(x=155, y=165, w=32, h=10)

    pdf.rect(x=33, y=175, w=154, h=10)

    pdf.rect(x=33, y=185, w=90, h=10)
    pdf.rect(x=123, y=185, w=32, h=10)
    pdf.rect(x=155, y=185, w=32, h=10)


    pdf.set_xy(67, 98)
    pdf.multi_cell(120, 7, 'Дисциплины модуля мобильности')

    pdf.set_xy(69, 118)
    pdf.multi_cell(120, 7, 'Дисциплины(модули) по выбору')

    pdf.set_xy(67, 137)
    pdf.multi_cell(120, 7, 'Дисциплины модуля мобильности')

    pdf.set_xy(82, 156)
    pdf.multi_cell(120, 7, 'Факультатив ФТД.В.02')

    pdf.set_xy(69, 176)
    pdf.multi_cell(120, 7, 'Дисциплины(модули) по выбору')


    pdf.set_xy(60,85)
    pdf.multi_cell(0,7,'Дисциплина')

    pdf.set_xy(124, 83)
    pdf.set_font_size(12)
    pdf.multi_cell(32, 5, 'Трудоёмкость,          з.е.')

    pdf.set_xy(162, 81)
    pdf.set_font_size(12)
    pdf.multi_cell(33, 5, 'Период изучения,  (семестр)')









    pdf.set_xy(15, 190)
    pdf.cell(1, 30, 'Студент')
    pdf.set_xy(87, 190)
    pdf.cell(1, 30, '________________/')
    pdf.set_xy(15, 200)
    pdf.cell(1, 30, 'Дата')
    pdf.set_xy(130, 190)
    pdf.cell(1, 30, IFIO)
    pdf.set_xy(130, 200)
    pdf.cell(1, 30, date)

    pdf.set_xy(15, 223)
    pdf.multi_cell(180,7,' До меня доведена информация о том, что в случае отсутствия или несвоевременного предоставления документа, подтверждающего оценку результатов обучения, у меня возникает академическая задолженность.')

    pdf.set_xy(15, 235)
    pdf.cell(1, 30, 'Студент')
    pdf.set_xy(87, 235)
    pdf.cell(1, 30, '________________/')
    pdf.set_xy(15, 245)
    pdf.cell(1, 30, 'Дата')
    pdf.set_xy(130, 235)
    pdf.cell(1, 30, IFIO)
    pdf.set_xy(130, 245)
    pdf.cell(1, 30, date)

    if prof1 == 'OF':
        pdf.set_font_size(15)
        pdf.set_xy(35,109)
        pdf.multi_cell(87, 8, 'Образовательный форсайт')
        pdf.set_font_size(15)
        pdf.set_xy(136,112)
        pdf.multi_cell(0,0,'3')
        pdf.set_xy(168, 112)
        pdf.multi_cell(0, 0, '5')
    if prof1 == 'KA':
        pdf.set_font_size(15)
        pdf.set_xy(35, 109)
        pdf.multi_cell(87, 8, 'Карьерная адаптивность')
        pdf.set_font_size(15)
        pdf.set_xy(136, 112)
        pdf.multi_cell(0, 0, '3')
        pdf.set_xy(168, 112)
        pdf.multi_cell(0, 0, '5')
    if prof2 == 'DM':
        pdf.set_font_size(15)
        pdf.set_xy(35, 128)
        pdf.multi_cell(85, 6, 'Дискретная математика')
        pdf.set_font_size(15)
        pdf.set_xy(136, 130)
        pdf.multi_cell(0, 0, '4')
        pdf.set_xy(168, 130)
        pdf.multi_cell(0, 0, '5')
        pdf.set_xy(35, 130)
    if prof2 == 'LS':
        pdf.set_font_size(15)
        pdf.set_xy(35, 128)
        pdf.multi_cell(85, 6, 'Логические системы')
        pdf.set_xy(136, 130)
        pdf.multi_cell(0, 0, '4')
        pdf.set_xy(168, 130)
        pdf.multi_cell(0, 0, '5')
    if prof3 == 'OF':
        pdf.set_font_size(15)
        pdf.set_xy(35,149)
        pdf.multi_cell(87, 5, 'Образовательный форсайт')
        pdf.set_font_size(15)
        pdf.set_xy(136, 150)
        pdf.multi_cell(0, 0, '3')
        pdf.set_xy(168, 150)
        pdf.multi_cell(0, 0, '6')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
    if prof3 == 'KA':
        pdf.set_font_size(15)
        pdf.set_xy(35,149)
        pdf.multi_cell(87, 5, 'Карьерная адаптивность')
        pdf.set_font_size(15)
        pdf.set_xy(136, 150)
        pdf.multi_cell(0, 0, '3')
        pdf.set_xy(168, 150)
        pdf.multi_cell(0, 0, '6')
    if prof4 == 'SL':
        pdf.set_font_size(12)
        pdf.set_xy(35,165)
        pdf.multi_cell(87, 5, 'Профессионально-ориентированный курс второго иностранного языка')
        pdf.set_font_size(15)
        pdf.set_xy(136, 170)
        pdf.multi_cell(0, 0, '2')
        pdf.set_xy(168, 170)
        pdf.multi_cell(0, 0, '6')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
    if prof4 == 'NO':
        pdf.set_font_size(15)
        pdf.set_xy(35,168)
        pdf.multi_cell(87, 5, 'Нет')
        pdf.set_font_size(15)
        pdf.set_xy(136, 170)
        pdf.multi_cell(0, 0, '2')
        pdf.set_xy(168, 170)
        pdf.multi_cell(0, 0, '6')
    if prof5 == 'SE':
        pdf.set_font_size(15)
        pdf.set_xy(35,188)
        pdf.multi_cell(87, 5, 'Силовая электроника')
        pdf.set_font_size(15)
        pdf.set_xy(136, 190)
        pdf.multi_cell(0, 0, '5')
        pdf.set_xy(168, 190)
        pdf.multi_cell(0, 0, '6')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)

    if prof5 == 'EE':
        pdf.set_font_size(15)
        pdf.set_xy(35,188)
        pdf.multi_cell(87, 5, 'Энергетическая электроника')
        pdf.set_font_size(15)
        pdf.set_xy(136, 190)
        pdf.multi_cell(0, 0, '5')
        pdf.set_xy(168, 190)
        pdf.multi_cell(0, 0, '6')
    pdf.output('elect2d02.pdf')









