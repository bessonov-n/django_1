# change_fonts.py
from fpdf import FPDF


import datetime

RFIO=''
IFIO=''
group=''
prof1=''

date = datetime.datetime.today().strftime("%d.%m.%Y")

def profils2(RFIO,IFIO,group,prof1):
    pdf: FPDF = FPDF()
    pdf.set_display_mode(zoom='fullwidth')
    pdf.add_page()
    pdf.image("pic.png",190,280, 7,7)
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    pdf.set_font_size(12)
    pdf.cell(97,15)
    pdf.multi_cell(100,6,
    'Руководителю образовательной программы 27.03.04_05  Интеллектуальные системы обработки информации и управления Онуфриеву В.А. от студента группы',0,'L',False)
    pdf.cell(97, 40)
    pdf.multi_cell(100, 7, group, 0, 'L', False)
    pdf.set_font_size(12)
    pdf.cell(96,20)
    pdf.multi_cell(100,4,RFIO)
    pdf.set_font_size(20)
    pdf.set_xy(85,55)
    pdf.cell(50, 30, 'Заявление')
    pdf.set_font_size(15)
    pdf.set_xy(15,80)
    pdf.multi_cell(0, 7, ' Прошу разрешить включить в модуль мобильности на 7-й семестр следующую дисцплину:')


    pdf.rect(x=33, y=100, w=90, h=17)
    pdf.rect(x=123, y=100, w=32, h=17)
    pdf.rect(x=155, y=100, w=32, h=17)

    pdf.rect(x=33, y=117, w=90, h=20)
    pdf.rect(x=123, y=117, w=32, h=20)
    pdf.rect(x=155, y=117, w=32, h=20)


    pdf.rect(x=33, y=137, w=90, h=10)
    pdf.rect(x=123, y=137, w=32, h=10)
    pdf.rect(x=155, y=137, w=32, h=10)

    pdf.set_xy(60,105)
    pdf.multi_cell(0,7,'Дисциплина')

    pdf.set_xy(124, 103)
    pdf.set_font_size(12)
    pdf.multi_cell(32, 5, 'Трудоёмкость,          з.е.')

    pdf.set_xy(162, 100)
    pdf.set_font_size(12)
    pdf.multi_cell(33, 5, 'Период изучения  (семестр)')

    pdf.set_xy(35, 140)
    pdf.multi_cell(33, 5, 'Итого')

    pdf.set_xy(136, 140)
    pdf.set_font_size(15)
    pdf.multi_cell(33, 5, '4')



    pdf.set_xy(15, 140)
    pdf.cell(1, 30, 'Студент')
    pdf.set_xy(87, 140)
    pdf.cell(1, 30, '________________/')
    pdf.set_xy(15, 150)
    pdf.cell(1, 30, 'Дата')
    pdf.set_xy(130, 140)
    pdf.cell(1, 30, IFIO)
    pdf.set_xy(130, 150)
    pdf.cell(1, 30, date)

    pdf.set_xy(15, 175)
    pdf.multi_cell(180,7,' До меня доведена информация о том, что в случае отсутствия или несвоевременного предоставления документа, подтверждающего оценку результатов обучения, у меня возникает академическая задолженность.')

    pdf.set_xy(15, 200)
    pdf.cell(1, 30, 'Студент')
    pdf.set_xy(87, 200)
    pdf.cell(1, 30, '________________/')
    pdf.set_xy(15, 210)
    pdf.cell(1, 30, 'Дата')
    pdf.set_xy(130, 200)
    pdf.cell(1, 30, IFIO)
    pdf.set_xy(130, 210)
    pdf.cell(1, 30, date)

    if prof1 == 'MANAG':
        pdf.set_font_size(12)
        pdf.set_xy(35,120)
        pdf.multi_cell(87, 5, 'Менеджмент')
        pdf.set_font_size(15)
        pdf.set_xy(136,127)
        pdf.multi_cell(0,0,'4')
        pdf.set_xy(168, 127)
        pdf.multi_cell(0, 0, '7')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/MANAG')
        pdf.output('online4d05.pdf')

    if prof1 == 'MATHPH':
        pdf.set_font_size(12)
        pdf.set_xy(35, 120)
        pdf.multi_cell(87, 5, 'Математическая физика')
        pdf.set_font_size(15)
        pdf.set_xy(136, 127)
        pdf.multi_cell(0, 0, '4')
        pdf.set_xy(168, 127)
        pdf.multi_cell(0, 0, '7')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/MATHPH')
        pdf.output('online4d05.pdf')


    if prof1 == 'ECOMAN1':
        pdf.set_font_size(12)
        pdf.set_xy(35,120)
        pdf.multi_cell(87, 5, 'Экономика предприятия. Часть 1')
        pdf.set_font_size(15)
        pdf.set_xy(136, 127)
        pdf.multi_cell(0, 0, '4')
        pdf.set_xy(168, 127)
        pdf.multi_cell(0, 0, '7')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/ECOMAN1')
        pdf.output('online4d05.pdf')


    if prof1 == 'TMASH':
        pdf.set_font_size(12)
        pdf.set_xy(35,120)
        pdf.multi_cell(87, 5, 'Основы технологии машиностроения')
        pdf.set_font_size(15)
        pdf.set_xy(136, 127)
        pdf.multi_cell(0, 0, '4')
        pdf.set_xy(168, 127)
        pdf.multi_cell(0, 0, '7')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/TMASH')
        pdf.output('online4d05.pdf')

    else:
        pdf.set_font_size(12)
        pdf.set_xy(35,120)
        pdf.multi_cell(87, 5, 'Маркетинг')
        pdf.set_font_size(15)
        pdf.set_xy(136, 127)
        pdf.multi_cell(0, 0, '4')
        pdf.set_xy(168, 127)
        pdf.multi_cell(0, 0, '7')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/MARKET')
        pdf.output('online4d05.pdf')









