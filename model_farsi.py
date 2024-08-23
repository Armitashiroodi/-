import svgwrite

# تابع برای اضافه کردن باکس
def add_box(dwg, text, insert, size):
    dwg.add(dwg.rect(insert=insert, size=size, fill='white', stroke='black'))
    dwg.add(dwg.text(text, insert=(insert[0] + 10, insert[1] + 25), fill='black', font_size='15'))

# ابعاد باکس‌ها و فاصله بین آنها
box_width = 160
box_height = 40
gap_y = 80

# ایجاد فایل SVG
dwg = svgwrite.Drawing('model_farsi.svg', profile='tiny', size=("800px", "600px"))

# لایه‌های مختلف مدل
add_box(dwg, "آموزش و پژوهش", (320, 20), (box_width, box_height))
add_box(dwg, "تعاملات اجتماعی", (320, 20 + gap_y), (box_width, box_height))
add_box(dwg, "پایداری زیست‌محیطی", (320, 20 + 2 * gap_y), (box_width, box_height))
add_box(dwg, "عدالت اجتماعی و دسترسی به آموزش", (320, 20 + 3 * gap_y), (box_width, box_height))
add_box(dwg, "تجاری‌سازی و نوآوری", (320, 20 + 4 * gap_y), (box_width, box_height))
add_box(dwg, "شفافیت و پاسخگویی", (320, 20 + 5 * gap_y), (box_width, box_height))

# خطوط اتصال بین باکس‌ها
for i in range(6):
    dwg.add(dwg.line((320, 40 + i * gap_y), (280, 40 + i * gap_y), stroke=svgwrite.rgb(0, 0, 0, '%')))

# ذخیره فایل SVG
dwg.save()
