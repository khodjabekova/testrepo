from PIL import Image
import io
import xlsxwriter
from .models import InternUser, InternshipExpenses
import re
CLEANR = re.compile('<.*?>')


def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext


def WriteToExcel():
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet("Statistics")

    worksheet.set_column(0, 6, 20)
    worksheet.set_column(5, 5, 30)
    worksheet.set_column(7, 16, 40)
    bold = workbook.add_format({'bold': True})
    worksheet.write(0, 0, "Фамилия", bold)
    worksheet.write(0, 1, "Исм", bold)
    worksheet.write(0, 2, "Отасининг исми", bold)
    worksheet.write(0, 3, "Телефон раками", bold)
    worksheet.write(0, 4, "Электрон почта", bold)
    worksheet.write(0, 5, "Yashash manzili", bold)
    worksheet.write(0, 6, "Jinsi", bold)
    worksheet.write(0, 7, "Fuqarolik", bold)
    worksheet.write(0, 8, "JSH SHIR", bold)
    worksheet.write(0, 9, "Pasport seriyasi va raqami", bold)
    worksheet.write(0, 10, "Tug‘ilgan sanasi", bold)
    worksheet.write(0, 11, "Hudud", bold)
    worksheet.write(0, 12, "Muassasa", bold)
    worksheet.write(0, 13, "Ish hududi", bold)
    worksheet.write(0, 14, "Ish joyining manzili", bold)
    worksheet.write(0, 15, "Ta'lim", bold)
    worksheet.write(0, 16, "Mutaxassisligi", bold)

    interns = InternUser.objects.filter(status=2)
    date_format = workbook.add_format({'num_format': 'dd/mm/yyyy'})
    i = 1
    for j in interns:
        worksheet.set_row(i, 20)
        worksheet.write(i, 0, j.lastname)
        worksheet.write(i, 1, j.firstname)
        worksheet.write(i, 2, j.patronymic)
        worksheet.write(i, 3, j.phone)
        worksheet.write(i, 4, j.email)
        worksheet.write(i, 5, j.address)
        worksheet.write(i, 6, j.GENDER_CHOICE[j.gender][1])
        worksheet.write(i, 7, j.citizenship)
        worksheet.write(i, 8, j.pnfl)
        worksheet.write(i, 9, j.passport_no)
        worksheet.write(i, 10, j.date_of_birth, date_format)
        worksheet.write(i, 11, j.region)
        worksheet.write(i, 12, j.work)
        worksheet.write(i, 13, j.work_region)
        worksheet.write(i, 14, j.work_address)
        worksheet.write(i, 15,  j.EDU_CHOICE[j.education][1])
        worksheet.write(i, 16, j.specialization)

        i += 1

    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data


def InternshipExpensesExcel(object_id):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    cell_format = workbook.add_format({'align': 'center',
                                       'valign': 'vcenter',
                                       'text_wrap': True, })
    worksheet = workbook.add_worksheet("Xarajatlar asosnomasi")

    merge_format = workbook.add_format({
        'bold': 1,
        'align': 'center',
        'valign': 'vcenter',
        'bg_color': '#c0e399',
        'text_wrap': True,
    })

    # Merge 3 cells.
    head = "Ўзбекистон Республикаси Фанлар Академияси Тарих институти докторанти Ражапов Мардонбек Косимбой ўғлининг 2022 йил 1-мартдан-2022 йил 1 майгача Германия Федератив Республикаси Берлин шахридаги Хумболдт"
    # worksheet.write(0, 0, head, bold)
    worksheet.merge_range('A1:F1', head, merge_format)

    sub_head = "Университетига  стажировкаси харажатлари асосномаси"
    worksheet.merge_range('A2:F2', sub_head, merge_format)

    worksheet.set_row(0, 50)
    worksheet.set_row(1, 25)

    head_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
    })

    # worksheet.set_row(2, 50, head_format)

    worksheet.set_column(0, 0, 5)
    worksheet.set_column(1, 3, 13)
    worksheet.set_column(4, 4, 50)
    worksheet.set_column(5, 5, 50)

    default = workbook.add_format({
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
    })
    green = workbook.add_format({
        'border': 1,
        'bg_color': '#c0e399',
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'text_justlast': True,
    })

    worksheet.write(2, 0, "№", default)
    worksheet.write(2, 1, "Харажатлар йўналишлари", green)
    worksheet.write(2, 2, "Калькуляция", default)
    worksheet.write(2, 3, "Сумма", default)
    worksheet.write(2, 4, "Асоснома", default)
    worksheet.write(2, 5, "Screenshot", default)

    expenses = InternshipExpenses.objects.prefetch_related(
        'cost_statements').get(pk=object_id)

    i = 3

    for j in expenses.cost_statements.all():

        if i == 3:
            formatter = green
        else:
            formatter = default

        if j.screenshot:
            worksheet.set_row(i, 200)
            im = Image.open(j.screenshot.path)

            if im.info['dpi'][0] > 200:
                cell_height = 700
                cell_width = 800
            else:
                cell_height = 250
                cell_width = 350

            if im.width > im.height:
                scale = cell_width/im.width
            else:
                scale = cell_height/im.height

            offset = {
                'x_offset':        1,
                'y_offset':        1,
                'x_scale':         scale,
                'y_scale':         scale,
            }
            worksheet.insert_image(i, 5, j.screenshot.path, offset)
            worksheet.write(i, 5, '', formatter)

            worksheet.write(i, 0, i-2, formatter)
            worksheet.write(i, 1, j.type.name_uzb, green)
            worksheet.write(i, 2, j.days, formatter)
            worksheet.write(i, 3, j.cost, formatter)
            if j.note and j.link:
                worksheet.write(i, 4, j.note + " " + j.link, formatter)
            elif j.note:
                worksheet.write(i, 4, j.note, formatter)
            elif j.link:
                worksheet.write(i, 4, j.link, formatter)
        else:
            worksheet.set_row(i, 100)

            worksheet.write(i, 0, i-2, formatter)
            worksheet.write(i, 1, j.type.name_uzb, green)
            worksheet.write(i, 2, j.days, formatter)
            worksheet.write(i, 3, j.cost, formatter)
            if j.note and j.link:
                worksheet.write(i, 4, j.note + " " + j.link, formatter)
            elif j.note:
                worksheet.write(i, 4, j.note, formatter)
            elif j.link:
                worksheet.write(i, 4, j.link, formatter)
            else:
                worksheet.write(i, 4, '', formatter)
            worksheet.write(i, 5, '', formatter)
        i += 1

    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data
