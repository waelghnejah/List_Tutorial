# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from examples import run_example
from operators import open_operator_window
from list_methods import open_list_methods_window

root = tk.Tk()
root.title("Wael_Liza - مختبر القوائم 🧪")
root.geometry("750x750")
root.configure(bg="#fff8dc")  # ثيم أصفر فاتح

# عنوان
title = tk.Label(root, text="مختبر القوائم - Wael_Liza", font=("Arial", 20, "bold"), bg="#fff8dc", fg="#333")
title.pack(pady=12)

# قائمة المواضيع
topics = [
    "تعريف list فارغ",
    "list تحتوي أعداد صحيحة",
    "list تحتوي نصوص",
    "list تحتوي أعداد ونصوص",
    "list بإسم data مع قيم متنوعة",
    "list بإسم numbers بقيم أولية 0",
    "list بإسم str بقيم 'Not Specified'",
    "الوصول لعناصر list",
    "عرض أول وآخر العناصر",
    "عرض عناصر عددية باستخدام for",
    "جمع عناصر عددية باستخدام for مع شرح تفصيلي",
    "حذف عناصر من list",
    "حذف جزء باستخدام slice",
    "حذف list بالكامل",
    "عرض جزء باستخدام slice",
    "نسخ جزء إلى list جديدة",
    "شرح دوال list",
]

selected_topic = tk.StringVar()
topic_menu = ttk.Combobox(root, textvariable=selected_topic, values=topics, font=("Arial", 12), width=55)
topic_menu.set("اختر الموضوع التعليمي")
topic_menu.pack(pady=10)

# مربع إدخال البيانات
input_label = tk.Label(root, text="أدخل البيانات أو المصفوفة:", font=("Arial", 12), bg="#fff8dc")
input_label.pack()
input_box = tk.Text(root, height=5, width=70, font=("Arial", 12), bg="#fffef3")
input_box.pack(pady=6)

# زر تنفيذ
def execute():
    topic = selected_topic.get()
    user_input = input_box.get("1.0", tk.END).strip()
    result, explanation, code = run_example(topic, user_input)
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"🔍 الشرح:\n{explanation}\n\n🧾 الكود:\n{code}\n\n📤 الناتج:\n{result}")
    output_box.config(state="disabled")

execute_btn = tk.Button(root, text="تنفيذ", command=execute, font=("Arial", 12, "bold"), bg="#4caf50", fg="white")
execute_btn.pack(pady=10)

# زر شرح دوال list
methods_btn = tk.Button(root, text="شرح دوال list", command=open_list_methods_window, font=("Arial", 12), bg="#9c27b0", fg="white")
methods_btn.pack()

# زر شرح العوامل
operator_btn = tk.Button(root, text="شرح العوامل", command=open_operator_window, font=("Arial", 12), bg="#2196f3", fg="white")
operator_btn.pack(pady=6)

# زر نسخ الكود من النتائج
def copy_main_output():
    code_text = output_box.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(code_text)
    root.update()
    messagebox.showinfo("تم النسخ", "✅ تم نسخ الشرح والكود والناتج إلى الحافظة!")

copy_btn_main = tk.Button(root, text="📋 نسخ الكود", command=copy_main_output, font=("Arial", 12), bg="#ff9800", fg="white")
copy_btn_main.pack(pady=6)

# مربع النتائج
output_box = tk.Text(root, height=12, width=80, font=("Arial", 12), state="disabled", bg="#fffef3")
output_box.pack(pady=10)

root.mainloop()