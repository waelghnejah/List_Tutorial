# operators.py
import tkinter as tk
from tkinter import messagebox

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

def open_operator_window():
    win = tk.Toplevel()
    win.title("شرح العوامل")
    win.geometry("700x600")
    win.configure(bg="#fff8dc")  # ثيم أصفر فاتح

    label = tk.Label(win, text="اختر عامل لعرض المثال:", font=("Arial", 14, "bold"), bg="#fff8dc", fg="#333")
    label.pack(pady=10)

    result_box = tk.Text(win, height=8, width=80, font=("Arial", 12), state="disabled", bg="#fffef3")
    result_box.pack(pady=10)

    button_frame = tk.Frame(win, bg="#fff8dc")
    button_frame.pack(pady=5)

    input_frame = tk.Frame(win, bg="#fff8dc")
    input_frame.pack(pady=10, fill="x")

    output_box = tk.Text(win, height=6, width=80, font=("Arial", 12), state="disabled", bg="#f3f3f3")
    output_box.pack(pady=10)

    operators = ["+", "*", "in", "==", "!=", ">", "<"]

    explanations = {
        "+": "العامل + يدمج قائمتين.",
        "*": "العامل * يكرر عناصر القائمة.",
        "in": "العامل in يتحقق من وجود عنصر داخل القائمة.",
        "==": "العامل == يتحقق من تطابق القائمتين عنصرًا عنصرًا.",
        "!=": "العامل != يتحقق من عدم تطابق القائمتين.",
        ">": "العامل > يقارن القوائم حسب الترتيب القاموسي (المقارنة تُجرى على العناصر المتتالية).",
        "<": "العامل < يقارن القوائم حسب الترتيب القاموسي."
    }

    for i, op in enumerate(operators):
        tk.Button(button_frame, text=op, font=("Arial", 12), width=6,
                  bg="#ffcc00", fg="black", command=lambda o=op: show_example(o)).grid(row=0, column=i, padx=5, pady=5)

    def show_example(op):
        for widget in input_frame.winfo_children():
            widget.destroy()

        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"🔍 الشرح:\n{explanations.get(op,'...')}\n\n")
        result_box.insert(tk.END, "💡 أدخل القوائم بصيغة: 1,2,3 أو أحرف مفصولة بفواصل؛ الإدخالات الرقمية تتحول تلقائيًا.\n")
        result_box.config(state="disabled")

        def add_field(label_text):
            tk.Label(input_frame, text=label_text, font=("Arial", 12), bg="#fff8dc", fg="#333").pack(anchor="w", padx=10, pady=(6,2))
            ent = tk.Entry(input_frame, font=("Arial", 12), bg="#fffef3")
            ent.pack(fill="x", padx=10, pady=(0,6))
            return ent

        entries = {}
        if op in {"+", "==", "!=", ">", "<"}:
            entries["a"] = add_field("القائمة الأولى (مثال: 1,2,3):")
            entries["b"] = add_field("القائمة الثانية:")
        elif op == "*":
            entries["a"] = add_field("القائمة (مثال: 1,2):")
            entries["times"] = add_field("عدد التكرار (مثال: 2):")
        elif op == "in":
            entries["a"] = add_field("القائمة (مثال: 1,2,3):")
            entries["item"] = add_field("العنصر للتحقق منه:")

        def as_number_or_text(s):
            s = s.strip()
            if not s:
                return s
            try: return int(s)
            except: pass
            try: return float(s)
            except: pass
            return s

        def run_operator():
            try:
                if op in {"+", "==", "!=", ">", "<"}:
                    a = parse_list(entries["a"].get())
                    b = parse_list(entries["b"].get())
                    if op == "+": res = a + b
                    elif op == "==": res = a == b
                    elif op == "!=": res = a != b
                    elif op == ">": res = a > b
                    elif op == "<": res = a < b
                elif op == "*":
                    a = parse_list(entries["a"].get())
                    times = int(entries["times"].get())
                    res = a * times
                elif op == "in":
                    a = parse_list(entries["a"].get())
                    item = as_number_or_text(entries["item"].get())
                    res = item in a
                output = f"📤 الناتج: {res}"
                show_result(output)
            except Exception as e:
                show_result(f"⚠️ خطأ: {e}")

        def show_result(text):
            output_box.config(state="normal")
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, text)
            output_box.config(state="disabled")

        tk.Button(input_frame, text="تنفيذ", bg="#ffcc00", fg="black", font=("Arial", 12), command=run_operator).pack(pady=6)

    def copy_code():
        code_text = result_box.get("1.0", tk.END)
        win.clipboard_clear(); win.clipboard_append(code_text); win.update()
        messagebox.showinfo("تم النسخ", "✅ تم نسخ الشرح إلى الحافظة!")

    copy_btn = tk.Button(win, text="📋 نسخ الشرح", command=copy_code, font=("Arial", 12), bg="#ffcc00", fg="black")
    copy_btn.pack(pady=6)