# change_fonts.py
from fpdf import FPDF


import datetime

RFIO=''
IFIO=''
group=''
prof1=''
prof2=''

date = datetime.datetime.today().strftime("%d.%m.%Y")

def profils2(RFIO,IFIO,group,prof1,prof2):
    pdf: FPDF = FPDF()
    pdf.set_display_mode(zoom='fullwidth')
    pdf.add_page()
    pdf.image("pic.png",190,280, 7,7)
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    pdf.set_font_size(12)
    pdf.cell(97,15)
    pdf.multi_cell(100,6,
    'Руководителю образовательной программы 27.03.04_05 Интеллектуальные системы обработки информации и управления Онуфриеву В.А. от студента группы',0,'L',False)
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
    pdf.multi_cell(0, 7, ' Прошу разрешить включить в модуль мобильности на 5-й и 6-й семестры следующие дисцплины:')


    pdf.rect(x=33, y=100, w=90, h=17)
    pdf.rect(x=123, y=100, w=32, h=17)
    pdf.rect(x=155, y=100, w=32, h=17)

    pdf.rect(x=33, y=117, w=90, h=20)
    pdf.rect(x=123, y=117, w=32, h=20)
    pdf.rect(x=155, y=117, w=32, h=20)

    pdf.rect(x=33, y=137, w=90, h=20)
    pdf.rect(x=123, y=137, w=32, h=20)
    pdf.rect(x=155, y=137, w=32, h=20)

    pdf.rect(x=33, y=157, w=90, h=10)
    pdf.rect(x=123, y=157, w=32, h=10)
    pdf.rect(x=155, y=157, w=32, h=10)

    pdf.set_xy(60,105)
    pdf.multi_cell(0,7,'Дисциплина')

    pdf.set_xy(124, 103)
    pdf.set_font_size(12)
    pdf.multi_cell(32, 5, 'Трудоёмкость,          з.е.')

    pdf.set_xy(162, 100)
    pdf.set_font_size(12)
    pdf.multi_cell(33, 5, 'Период изучения  (семестр)')

    pdf.set_xy(35, 160)
    pdf.multi_cell(33, 5, 'Итого')

    pdf.set_xy(136, 160)
    pdf.set_font_size(15)
    pdf.multi_cell(33, 5, '6')



    pdf.set_xy(15, 160)
    pdf.cell(1, 30, 'Студент')
    pdf.set_xy(87, 160)
    pdf.cell(1, 30, '________________/')
    pdf.set_xy(15, 170)
    pdf.cell(1, 30, 'Дата')
    pdf.set_xy(130, 160)
    pdf.cell(1, 30, IFIO)
    pdf.set_xy(130, 170)
    pdf.cell(1, 30, date)

    pdf.set_xy(15, 195)
    pdf.multi_cell(180,7,' До меня доведена информация о том, что в случае отсутствия или несвоевременного предоставления документа, подтверждающего оценку результатов обучения, у меня возникает академическая задолженность.')

    pdf.set_xy(15, 220)
    pdf.cell(1, 30, 'Студент')
    pdf.set_xy(87, 220)
    pdf.cell(1, 30, '________________/')
    pdf.set_xy(15, 230)
    pdf.cell(1, 30, 'Дата')
    pdf.set_xy(130, 220)
    pdf.cell(1, 30, IFIO)
    pdf.set_xy(130, 230)
    pdf.cell(1, 30, date)

    if prof1 == 'GTCOM':
        pdf.set_font_size(12)
        pdf.set_xy(35,120)
        pdf.multi_cell(87, 5, 'Общая теория связи. Вероятностные модели сигналов и систем.')
        pdf.set_font_size(15)
        pdf.set_xy(136,127)
        pdf.multi_cell(0,0,'3')
        pdf.set_xy(168, 127)
        pdf.multi_cell(0, 0, '5')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/GTCOM')



    if prof1 == 'CLEWO':
        pdf.set_font_size(12)
        pdf.set_xy(35,120)
        pdf.multi_cell(87, 5, 'Делопроизводство(Документационное обеспечение)')
        pdf.set_font_size(15)
        pdf.set_xy(136, 127)
        pdf.multi_cell(0, 0, '3')
        pdf.set_xy(168, 127)
        pdf.multi_cell(0, 0, '5')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/CLEWO')

    if prof1 == 'MATLOG':
        pdf.set_font_size(12)
        pdf.set_xy(35,120)
        pdf.multi_cell(87, 5, 'Математическая логика')
        pdf.set_font_size(15)
        pdf.set_xy(136, 127)
        pdf.multi_cell(0, 0, '3')
        pdf.set_xy(168, 127)
        pdf.multi_cell(0, 0, '5')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/MATLOG')

    if prof1 == 'BIGDATA':
        pdf.set_font_size(12)
        pdf.set_xy(35,120)
        pdf.multi_cell(87, 5, 'Наука о данных и аналитика больших объёмов данных')
        pdf.set_font_size(15)
        pdf.set_xy(136, 127)
        pdf.multi_cell(0, 0, '3')
        pdf.set_xy(168, 127)
        pdf.multi_cell(0, 0, '5')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/BIGDATA')

    if prof1 == 'FOMO':
        pdf.set_font_size(12)
        pdf.set_xy(35,120)
        pdf.multi_cell(87, 5, 'Формализация моделирования')
        pdf.set_font_size(15)
        pdf.set_xy(136, 127)
        pdf.multi_cell(0, 0, '3')
        pdf.set_xy(168, 127)
        pdf.multi_cell(0, 0, '5')
        pdf.set_xy(35, 130)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/FOMO')




    if prof2=='NUCPOW':
        pdf.set_font_size(12)
        pdf.set_xy(35,140)
        pdf.multi_cell(87, 5, 'Атомная энергетика. Введение')
        pdf.set_font_size(15)
        pdf.set_xy(136, 147)
        pdf.multi_cell(0, 0, '3')
        pdf.set_xy(168, 147)
        pdf.multi_cell(0, 0, '6')
        pdf.set_xy(35, 150)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/NUCPOW')
        pdf.output('online3d02.pdf')

    if prof2=='BIOMECH':
        pdf.set_font_size(12)
        pdf.set_xy(35,140)
        pdf.multi_cell(87, 5, 'Биомеханика')
        pdf.set_font_size(15)
        pdf.set_xy(136, 147)
        pdf.multi_cell(0, 0, '3')
        pdf.set_xy(168, 147)
        pdf.multi_cell(0, 0, '6')
        pdf.set_xy(35, 150)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/BIOMECH')
        pdf.output('online3d02.pdf')

    if prof2=='FUTFACT':
        pdf.set_font_size(12)
        pdf.set_xy(35,140)
        pdf.multi_cell(87, 5, 'Технологии "Фабрик Будущего"')
        pdf.set_font_size(15)
        pdf.set_xy(136, 147)
        pdf.multi_cell(0, 0, '3')
        pdf.set_xy(168, 147)
        pdf.multi_cell(0, 0, '6')
        pdf.set_xy(35, 150)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/FUTFACT')
        pdf.output('online3d02.pdf')

    if prof2=='LTARG':
        pdf.set_font_size(12)
        pdf.set_xy(35,140)
        pdf.multi_cell(87, 5, 'Логика и теория аргументации')
        pdf.set_font_size(15)
        pdf.set_xy(136, 147)
        pdf.multi_cell(0, 0, '3')
        pdf.set_xy(168, 147)
        pdf.multi_cell(0, 0, '6')
        pdf.set_xy(35, 150)
        pdf.set_font_size(8)
        pdf.multi_cell(87, 5, 'http://openedu.ru/course/spbstu/LTARG')
        pdf.output('online3d02.pdf')









