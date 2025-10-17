# list_methods.py
import tkinter as tk
from tkinter import messagebox

# دالة مساعدة: تحويل نص مفصول بفواصل إلى قائمة بأرقام (int/float) أو نصوص
def parse_list(text):
    items = [x.strip() for x in text.split(",") if x.strip()]
    parsed = []
    for x in items:
        # جرّب int
        try:
            parsed.append(int(x))
            continue
        except:
            pass
        # جرّب float
        try:
            parsed.append(float(x))
            continue
        except:
            pass
        # غير رقمي → نص
        parsed.append(x)
    return parsed

def open_list_methods_window():
    win = tk.Toplevel()
    win.title("شرح دوال list")
    win.geometry("780x740")
    win.configure(bg="#fff8dc")  # ثيم أصفر فاتح

    title = tk.Label(
        win, text="مختبر دوال القوائم (List) - Wael_Liza",
        font=("Arial", 18, "bold"), bg="#fff8dc", fg="#333"
    )
    title.pack(pady=8)

    label = tk.Label(
        win, text="اختر دالة لعرض الشرح والمداخل المناسبة:",
        font=("Arial", 14), bg="#fff8dc", fg="#333"
    )
    label.pack(pady=6)

    # صندوق الشرح
    result_box = tk.Text(win, height=8, width=95, font=("Arial", 12), state="disabled", bg="#fffef3")
    result_box.pack(pady=8)

    # أزرار الدوال
    button_frame = tk.Frame(win, bg="#fff8dc")
    button_frame.pack(pady=4)

    # إطار المدخلات
    input_frame = tk.Frame(win, bg="#fff8dc", bd=1, relief="flat")
    input_frame.pack(pady=10, fill="x")

    # صندوق النتيجة
    output_box = tk.Text(win, height=7, width=95, font=("Arial", 12), state="disabled", bg="#f3f3f3")
    output_box.pack(pady=8)

    # زر نسخ الشرح
    def copy_desc():
        code_text = result_box.get("1.0", tk.END)
        win.clipboard_clear()
        win.clipboard_append(code_text)
        win.update()
        messagebox.showinfo("تم النسخ", "✅ تم نسخ الشرح إلى الحافظة!")

    copy_btn = tk.Button(win, text="📋 نسخ الشرح", command=copy_desc, font=("Arial", 12),
                         bg="#ffcc00", fg="black")
    copy_btn.pack(pady=4)

    methods = [
        "append", "extend", "insert", "pop", "clear", "copy",
        "count", "remove", "index", "sort", "reverse",
        "len", "min", "max", "list"
    ]

    # رسم الأزرار

    per_row = 6
    for i, m in enumerate(methods):
        btn = tk.Button(
            button_frame,
            text=m,
            font=("Arial", 12),
            width=10,
            bg="#ffcc00",
            command=lambda method=m: show_example(method)
        )
        btn.grid(row=i // per_row, column=i % per_row, padx=6, pady=6)

    # الشروح
    explanations = {
        "append": "تضيف عنصر إلى نهاية القائمة.",
        "extend": "تضيف عناصر متعددة من قائمة أخرى إلى نهاية القائمة.",
        "insert": "تُدخل عنصر في موقع محدد (index).",
        "pop": "تحذف وتعيد العنصر عند فهرس معيّن (افتراضيًا الأخير).",
        "clear": "تحذف جميع العناصر من القائمة.",
        "copy": "تنشئ نسخة سطحية من القائمة.",
        "count": "تعيد عدد مرات ظهور عنصر معيّن.",
        "remove": "تحذف أول ظهور لعنصر معيّن.",
        "index": "تعيد فهرس أول ظهور لعنصر معيّن.",
        "sort": "ترتب العناصر تصاعديًا (يتطلب عناصر قابلة للمقارنة).",
        "reverse": "تعكس ترتيب العناصر.",
        "len": "تعيد عدد العناصر في القائمة.",
        "min": "تعيد أصغر عنصر (يتطلب عناصر قابلة للمقارنة).",
        "max": "تعيد أكبر عنصر (يتطلب عناصر قابلة للمقارنة).",
        "list": "تحوّل كائن قابل للتكرار إلى قائمة (مثل النص يحوَّل لكل حرف)."
    }

    def show_example(method):
        # مسح المدخلات السابقة
        for w in input_frame.winfo_children():
            w.destroy()

        # عرض الشرح
        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"🔍 الشرح:\n{explanations.get(method, '...')}\n\n")
        # نصائح إدخال
        result_box.insert(tk.END, "💡 أدخل القائمة بصيغة: 1,2,3 أو a,b,c (سيتم تحويل الأرقام تلقائيًا)\n")
        if method in {"count", "index", "remove"}:
            result_box.insert(tk.END, "💡 أدخل العنصر كقيمة مفردة (مثلاً: 2 أو a)\n")
        if method == "insert":
            result_box.insert(tk.END, "💡 الموقع (index) يبدأ من 0. إذا كان أكبر من الطول، يُضاف العنصر في النهاية.\n")
        if method == "pop":
            result_box.insert(tk.END, "💡 فهرس الحذف اختياري. اتركه فارغًا لحذف آخر عنصر.\n")
        result_box.config(state="disabled")

        # أدوات مساعدة
        def add_field(label_text):
            tk.Label(input_frame, text=label_text, font=("Arial", 12), bg="#fff8dc", fg="#333").pack(anchor="w", padx=10, pady=(6,2))
            ent = tk.Entry(input_frame, font=("Arial", 12), bg="#fffef3")
            ent.pack(fill="x", padx=10, pady=(0,6))
            return ent

        def as_number_or_text(s):
            s = s.strip()
            if not s:
                return s
            # حاول int ثم float
            try:
                return int(s)
            except:
                pass
            try:
                return float(s)
            except:
                pass
            return s

        # حقول الإدخال حسب الدالة
        entries = {}
        if method in {"append", "extend", "remove", "count", "index", "sort", "reverse", "clear", "copy", "len", "min", "max"}:
            entries["list"] = add_field("القائمة (مثال: 1,2,3 أو a,b,c):")
            if method in {"append", "remove", "count", "index"}:
                entries["item"] = add_field("العنصر:")
        elif method == "insert":
            entries["list"] = add_field("القائمة (مثال: 1,2,3):")
            entries["index"] = add_field("الموقع (index):")
            entries["item"] = add_field("العنصر:")
        elif method == "pop":
            entries["list"] = add_field("القائمة (مثال: 1,2,3):")
            entries["index"] = add_field("الموقع (اختياري):")
        elif method == "list":
            entries["iterable"] = add_field("كائن قابل للتكرار (مثال: نص abc أو 1,2,3):")

        # زر التنفيذ
        def run_method():
            try:
                # بناء القائمة الأساسية حسب الدالة
                if method == "list":
                    raw = entries["iterable"].get().strip()
                    # إذا المستخدم أدخل نص بفواصل → نحوله لقائمة عناصر
                    if "," in raw:
                        base_list = parse_list(raw)
                        show_result(f"list من مدخل مفصول بفواصل: {base_list}")
                        return
                    else:
                        # النص يحوَّل إلى قائمة حروف
                        base_list = list(raw)
                        show_result(f"تحويل إلى قائمة: {base_list}")
                        return

                # باقي الدوال تعتمد على "list"
                base_list = parse_list(entries["list"].get())

                if method == "append":
                    val = as_number_or_text(entries["item"].get())
                    base_list.append(val)
                    show_result(f"القائمة بعد append: {base_list}")

                elif method == "extend":
                    # نسمح بإدخال عناصر مفصولة بفواصل
                    extra = parse_list(entries["list"].get()) if "item" not in entries else parse_list(entries["item"].get())
                    # إذا ما في حقل item، نستخدم نفس الحقل كمصدر. لكن الأفضل: حقل منفصل
                    if "item" in entries:
                        extra = parse_list(entries["item"].get())
                    else:
                        messagebox.showinfo("ملاحظة", "اكتب العناصر المراد إضافتها في حقل 'العنصر' إن وُجد.")
                        extra = []
                    base_list.extend(extra)
                    show_result(f"القائمة بعد extend: {base_list}")

                elif method == "insert":
                    idx_str = entries["index"].get().strip()
                    if not idx_str:
                        raise ValueError("الرجاء إدخال الموقع (index).")
                    idx = int(idx_str)
                    val = as_number_or_text(entries["item"].get())
                    base_list.insert(idx, val)
                    show_result(f"القائمة بعد insert (عند الفهرس {idx}): {base_list}")

                elif method == "pop":
                    idx_str = entries["index"].get().strip()
                    if idx_str:
                        removed = base_list.pop(int(idx_str))
                    else:
                        removed = base_list.pop()
                    show_result(f"القائمة بعد pop: {base_list}\nالعنصر المحذوف: {removed}")

                elif method == "clear":
                    base_list.clear()
                    show_result(f"القائمة بعد clear: {base_list}")

                elif method == "copy":
                    copied = base_list.copy()
                    show_result(f"نسخة من القائمة: {copied}")

                elif method == "count":
                    val = as_number_or_text(entries["item"].get())
                    c = base_list.count(val)
                    show_result(f"عدد مرات ظهور {repr(val)}: {c}")

                elif method == "remove":
                    val = as_number_or_text(entries["item"].get())
                    base_list.remove(val)
                    show_result(f"القائمة بعد remove({repr(val)}): {base_list}")

                elif method == "index":
                    val = as_number_or_text(entries["item"].get())
                    i = base_list.index(val)
                    show_result(f"فهرس أول ظهور لـ {repr(val)}: {i}")

                elif method == "sort":
                    # محاولة فرز آمن: إذا عناصر غير قابلة للمقارنة، نعرض رسالة
                    try:
                        base_list.sort()
                        show_result(f"القائمة بعد sort: {base_list}")
                    except TypeError:
                        show_result("⚠️ لا يمكن فرز قائمة تحوي أنواع غير قابلة للمقارنة معًا (مثلاً أرقام ونصوص).")

                elif method == "reverse":
                    base_list.reverse()
                    show_result(f"القائمة بعد reverse: {base_list}")

                elif method == "len":
                    show_result(f"عدد العناصر (len): {len(base_list)}")

                elif method == "min":
                    try:
                        show_result(f"أصغر عنصر (min): {min(base_list)}")
                    except TypeError:
                        show_result("⚠️ لا يمكن حساب min لعناصر غير قابلة للمقارنة معًا.")

                elif method == "max":
                    try:
                        show_result(f"أكبر عنصر (max): {max(base_list)}")
                    except TypeError:
                        show_result("⚠️ لا يمكن حساب max لعناصر غير قابلة للمقارنة معًا.")

                else:
                    show_result("❌ دالة غير معروفة")

            except Exception as e:
                show_result(f"⚠️ خطأ: {e}")

        def show_result(text):
            output_box.config(state="normal")
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, text)
            output_box.config(state="disabled")

        tk.Button(input_frame, text="تنفيذ", bg="#ffcc00", fg="black", font=("Arial", 12),
                  command=run_method).pack(pady=8)
