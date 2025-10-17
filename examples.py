# examples.py
from list_methods import open_list_methods_window
import ast

def parse_list(text):
    items = [x.strip() for x in text.split(",") if x.strip()]
    parsed = []
    for x in items:
        try:
            parsed.append(int(x)); continue
        except: pass
        try:
            parsed.append(float(x)); continue
        except: pass
        parsed.append(x)
    return parsed

def run_example(topic, user_input):
    try:
        if topic == "تعريف list فارغ":
            lst = []
            return lst, "أنشأنا قائمة فارغة بدون عناصر.", "lst = []"

        elif topic == "list تحتوي أعداد صحيحة":
            if user_input.strip():
                lst = parse_list(user_input)
            else:
                lst = [1,2,3]
            return lst, "أنشأنا قائمة تحتوي أعداد صحيحة.", f"lst = {lst}"

        elif topic == "list تحتوي نصوص":
            if user_input.strip():
                lst = [x.strip() for x in user_input.split(",") if x.strip()]
            else:
                lst = ["a","b","c"]
            return lst, "أنشأنا قائمة تحتوي نصوص.", f"lst = {lst}"

        elif topic == "list تحتوي أعداد ونصوص":
            lst = ast.literal_eval(user_input) if user_input.strip() else [1,"a",3]
            return lst, "أنشأنا قائمة تحتوي أعداد ونصوص.", f"lst = {lst}"

        elif topic == "list بإسم data مع قيم متنوعة":
            values = ast.literal_eval(user_input) if user_input.strip() else [1, "x", 3.5]
            data = [None] * len(values)
            for i in range(len(values)):
                data[i] = values[i]
            detailed = "\n".join([
                f"- العنصر رقم {i} أصبح {repr(values[i])} ({type(values[i]).__name__})"
                for i in range(len(values))
            ])
            explanation = (
                f"قمنا بتعريف قائمة اسمها data تحتوي {len(values)} عنصر.\n"
                f"ثم استخدمنا القيم التي أدخلتها لتعديل عناصر القائمة:\n{detailed}"
            )
            code = f"data = [None] * {len(values)}\n" + "\n".join([f"data[{i}] = {repr(values[i])}" for i in range(len(values))]) + "\nprint(data)"
            return data, explanation, code

        elif topic == "list بإسم numbers بقيم أولية 0":
            values = ast.literal_eval(user_input) if user_input.strip() else [5,6,7]
            numbers = [0] * len(values)
            for i in range(len(values)):
                numbers[i] = values[i]
            explanation = f"قمنا بتعريف قائمة اسمها numbers تحتوي {len(values)} عنصر ثم عدلناها بالقيم المدخلة."
            code = f"numbers = [0] * {len(values)}\n" + "\n".join([f"numbers[{i}] = {repr(values[i])}" for i in range(len(values))]) + "\nprint(numbers)"
            return numbers, explanation, code

        elif topic == "list بإسم str بقيم 'Not Specified'":
            values = ast.literal_eval(user_input) if user_input.strip() else ["x","y"]
            str_list = ['Not Specified'] * len(values)
            for i in range(len(values)):
                str_list[i] = values[i]
            explanation = f"قمنا بتعريف قائمة اسمها str ثم عدلنا قيمها بالقيم المدخلة: {values}"
            code = f"str = ['Not Specified'] * {len(values)}\n" + "\n".join([f"str[{i}] = {repr(values[i])}" for i in range(len(values))]) + "\nprint(str)"
            return str_list, explanation, code

        elif topic == "الوصول لعناصر list":
            lst = ast.literal_eval(user_input) if user_input.strip() else [10,20,30]
            return [lst[0], lst[1]], "عرضنا أول عنصرين باستخدام الفهرس.", "lst[0], lst[1]"

        elif topic == "عرض أول وآخر العناصر":
            lst = ast.literal_eval(user_input) if user_input.strip() else [10,20,30]
            return [lst[0], lst[-1]], "عرضنا أول وآخر عنصر.", "lst[0], lst[-1]"

        elif topic == "عرض عناصر عددية باستخدام for":
            if user_input.strip().startswith("["):
                lst = ast.literal_eval(user_input)
            else:
                lst = parse_list(user_input) if user_input.strip() else [1,2,3]
            result = "\n".join(str(x) for x in lst)
            explanation = f"استخدمنا حلقة for لعرض كل عنصر.\nعدد العناصر: {len(lst)}"
            code = f"lst = {lst}\nfor x in lst:\n    print(x)"
            return result, explanation, code

        elif topic == "جمع عناصر عددية باستخدام for مع شرح تفصيلي":
            if user_input.strip().startswith("["):
                numbers = ast.literal_eval(user_input)
            else:
                numbers = parse_list(user_input) if user_input.strip() else [1,2,3]
            total = 0
            detailed = ""
            for i, x in enumerate(numbers):
                total += x
                detailed += f"- أضفنا {x} إلى المجموع (المجموع الحالي: {sum(numbers[:i+1])})\n"
            explanation = f"استخدمنا حلقة for لحساب مجموع العناصر.\nعدد العناصر: {len(numbers)}\n{detailed}"
            code = f"numbers = {numbers}\ntotal = 0\nfor x in numbers:\n    total += x\nprint('Total sum is:', total)"
            return f"Total sum is: {total}", explanation, code

        elif topic == "حذف عناصر من list":
            lst = ast.literal_eval(user_input) if user_input.strip() else [1,2,3,4]
            del lst[0]; del lst[1]
            return lst, "حذفنا أول عنصرين.", "del lst[0]; del lst[1]"

        elif topic == "حذف جزء باستخدام slice":
            lst = ast.literal_eval(user_input) if user_input.strip() else [1,2,3,4,5]
            del lst[0:3]
            return lst, "حذفنا العناصر من الفهرس 0 إلى 2.", "del lst[0:3]"

        elif topic == "حذف list بالكامل":
            lst = ast.literal_eval(user_input) if user_input.strip() else [1,2]
            del lst
            return "تم حذف القائمة", "حذفنا القائمة من الذاكرة.", "del lst"

        elif topic == "عرض جزء باستخدام slice":
            lst = ast.literal_eval(user_input) if user_input.strip() else [1,2,3,4]
            part = lst[0:3]
            return part, "عرضنا جزء من القائمة.", "lst[0:3]"

        elif topic == "نسخ جزء إلى list جديدة":
            lst = ast.literal_eval(user_input) if user_input.strip() else [1,2,3,4,5]
            new_lst = lst[1:4]
            return new_lst, "نسخنا جزء من القائمة إلى قائمة جديدة.", "new_lst = lst[1:4]"

        elif topic == "شرح دوال list":
            open_list_methods_window()
            return "تم فتح نافذة شرح الدوال", "اختر أي دالة من النافذة الجديدة.", "open_list_methods_window()"

        else:
            return "❌ الموضوع غير معروف", "يرجى اختيار موضوع صحيح.", ""
    except Exception as e:
        return f"⚠️ خطأ: {e}", "حدث خطأ أثناء التنفيذ.", ""