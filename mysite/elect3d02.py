# change_fonts.py
from fpdf import FPDF


import datetime

RFIO=''
IFIO=''
group=''
prof1=''
prof2=''
prof3=''

date = datetime.datetime.today().strftime("%d.%m.%Y")

def profils2(RFIO,IFIO,group,prof1,prof2,prof3):
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
    pdf.multi_cell(0, 7, ' Прошу утвердить в качестве дисциплин :')


    pdf.rect(x=33, y=80, w=90, h=17)
    pdf.rect(x=123, y=80, w=32, h=17)
    pdf.rect(x=155, y=80, w=32, h=17)

    pdf.rect(x=33, y=97, w=154, h=10)

    pdf.rect(x=33, y=107, w=90, h=14)
    pdf.rect(x=123, y=107, w=32, h=14)
    pdf.rect(x=155, y=107, w=32, h=14)

    pdf.rect(x=33, y=121, w=154, h=10)

    pdf.rect(x=33, y=131, w=90, h=14)
    pdf.rect(x=123, y=131, w=32, h=14)
    pdf.rect(x=155, y=131, w=32, h=14)

    pdf.rect(x=33, y=145, w=154, h=10)

    pdf.rect(x=33, y=155, w=90, h=14)
    pdf.rect(x=123, y=155, w=32, h=14)
    pdf.rect(x=155, y=155, w=32, h=14)

    pdf.set_xy(60, 98)
    pdf.multi_cell(120, 7, 'Дисциплина модуля мобильности(7 семестр)')

    pdf.set_xy(60, 122)
    pdf.multi_cell(120, 7, 'Дисциплины(модули) по выбору(7-8 семестр)')

    pdf.set_xy(60, 146)
    pdf.multi_cell(120, 7, 'Дисциплины(модули) по выбору(8 семестр)')

    pdf.set_xy(60,85)
    pdf.multi_cell(0,7,'Дисциплина')

    pdf.set_xy(124, 83)
    pdf.set_font_size(12)
    pdf.multi_cell(32, 5, 'Трудоёмкость,          з.е.')

    pdf.set_xy(162, 81)
    pdf.set_font_size(12)
    pdf.multi_cell(33, 5, 'Период изучения,  (семестр)')






    pdf.set_xy(15, 170)
    pdf.cell(1, 30, 'Студент')
    pdf.set_xy(87, 170)
    pdf.cell(1, 30, '________________/')
    pdf.set_xy(15, 180)
    pdf.cell(1, 30, 'Дата')
    pdf.set_xy(130, 170)
    pdf.cell(1, 30, IFIO)
    pdf.set_xy(130, 180)
    pdf.cell(1, 30, date)

    pdf.set_xy(15, 205)
    pdf.multi_cell(180,7,' До меня доведена информация о том, что в случае отсутствия или несвоевременного предоставления документа, подтверждающего оценку результатов обучения, у меня возникает академическая задолженность.')

    pdf.set_xy(15, 230)
    pdf.cell(1, 30, 'Студент')
    pdf.set_xy(87, 230)
    pdf.cell(1, 30, '________________/')
    pdf.set_xy(15, 240)
    pdf.cell(1, 30, 'Дата')
    pdf.set_xy(130, 230)
    pdf.cell(1, 30, IFIO)
    pdf.set_xy(130, 240)
    pdf.cell(1, 30, date)

    if prof1 == 'OF':
        pdf.set_font_size(15)
        pdf.set_xy(35,111)
        pdf.multi_cell(87, 8, 'Образовательный форсайт')
        pdf.set_font_size(15)
        pdf.set_xy(136,114)
        pdf.multi_cell(0,0,'3')
        pdf.set_xy(168, 114)
        pdf.multi_cell(0, 0, '6')
    if prof1 == 'KA':
        pdf.set_font_size(15)
        pdf.set_xy(35, 111)
        pdf.multi_cell(87, 8, 'Карьерная адаптивность')
        pdf.set_font_size(15)
        pdf.set_xy(136, 114)
        pdf.multi_cell(0, 0, '3')
        pdf.set_xy(168, 114)
        pdf.multi_cell(0, 0, '5')
    if prof2 == 'TSA':
        pdf.set_font_size(15)
        pdf.set_xy(35, 132)
        pdf.multi_cell(85, 6, 'Технические средства автоматизации')
        pdf.set_font_size(15)
        pdf.set_xy(136, 138)
        pdf.multi_cell(0, 0, '2')
        pdf.set_xy(168, 138)
        pdf.multi_cell(0, 0, '2')
        pdf.set_xy(35, 130)
    if prof2 == 'EEA':
        pdf.set_font_size(13)
        pdf.set_xy(35, 133)
        pdf.multi_cell(85, 6, 'Электрические и электронные аппараты')
        pdf.set_xy(136, 138)
        pdf.multi_cell(0, 0, '2')
        pdf.set_xy(168, 138)
        pdf.multi_cell(0, 0, '2')
    if prof3 == 'CMI':
        pdf.set_font_size(15)
        pdf.set_xy(35,158)
        pdf.multi_cell(87, 5, 'Человеко-машинные интерфейсы')
        pdf.set_font_size(15)
        pdf.set_xy(136, 162)
        pdf.multi_cell(0, 0, '4')
        pdf.set_xy(168, 162)
        pdf.multi_cell(0, 0, '4')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
        pdf.output('elect_3_02.pdf')
    if prof3 == 'SKY':
        pdf.set_font_size(13)
        pdf.set_xy(35,158)
        pdf.multi_cell(87, 5, 'Системы компьютерного управления')
        pdf.set_font_size(15)
        pdf.set_xy(136, 162)
        pdf.multi_cell(0, 0, '4')
        pdf.set_xy(168, 162)
        pdf.multi_cell(0, 0, '4')
        pdf.output('elect3d02.pdf')








