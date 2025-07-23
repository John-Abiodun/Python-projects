import tkinter as tk
from tkinter import messagebox
import random

# Initialize main window
root = tk.Tk()
root.title("CU Attendance Portal")
root.geometry("450x500")
root.configure(bg="#f5f5f5")
root.resizable(False, False)

# Global data
student_data = {
    "username": "",
    "password": "",
    "first_name": "",
    "last_name": "",
    "student_id": "",
    "attendance": {"TMC": "Not marked", "AMS": "Not marked", "GST": "Not marked", "ENT": "Not marked"}
}

# Fonts and colors
heading_font = ("Segoe UI", 18, "bold")
label_font = ("Segoe UI", 12)
btn_font = ("Segoe UI", 10, "bold")
bg_color = "#ffffff"
primary_color = "#4A90E2"
btn_color = "#4A90E2"
btn_fg = "#ffffff"

# Frame system
frames = {}
for F in ("create", "login", "dashboard", "attendance", "summary"):
    frame = tk.Frame(root, bg=bg_color)
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    frames[F] = frame

def raise_frame(name):
    frames[name].tkraise()

# ========== CREATE ACCOUNT ==========
def create_account():
    fname = fname_entry.get().strip()
    lname = lname_entry.get().strip()
    pw = pw_entry.get()

    if not fname or not lname or not pw:
        messagebox.showerror("Missing Info", "Please fill all fields")
        return

    id_rand = str(random.randint(1, 9999)).zfill(4)
    student_id = "250" + id_rand
    username = fname[0] + lname + "@" + student_id

    student_data.update({
        "first_name": fname,
        "last_name": lname,
        "password": pw,
        "student_id": student_id,
        "username": username.lower()
    })

    messagebox.showinfo("Success", f"Account created!\n\nUsername: {username}\nStudent ID: {student_id}")
    raise_frame("login")

tk.Label(frames["create"], text="Create Account", font=heading_font, bg=bg_color).pack(pady=20)
for text, var in [("First Name", "fname"), ("Last Name", "lname"), ("Password", "pw")]:
    tk.Label(frames["create"], text=text, font=label_font, bg=bg_color).pack()
    entry = tk.Entry(frames["create"], show="*" if var == "pw" else None, font=label_font)
    entry.pack(pady=5)
    if var == "fname": fname_entry = entry
    elif var == "lname": lname_entry = entry
    elif var == "pw": pw_entry = entry

tk.Button(frames["create"], text="Create Account", font=btn_font, bg=btn_color, fg=btn_fg, width=20, command=create_account).pack(pady=20)

# ========== LOGIN ==========
def login():
    username = username_entry.get().strip().lower()
    password = password_entry.get()

    if username == student_data["username"] and password == student_data["password"]:
        raise_frame("dashboard")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

tk.Label(frames["login"], text="Login", font=heading_font, bg=bg_color).pack(pady=20)
tk.Label(frames["login"], text="Username", font=label_font, bg=bg_color).pack()
username_entry = tk.Entry(frames["login"], font=label_font)
username_entry.pack(pady=5)
tk.Label(frames["login"], text="Password", font=label_font, bg=bg_color).pack()
password_entry = tk.Entry(frames["login"], font=label_font, show="*")
password_entry.pack(pady=5)
tk.Button(frames["login"], text="Login", font=btn_font, bg=btn_color, fg=btn_fg, width=20, command=login).pack(pady=20)

# ========== DASHBOARD ==========
tk.Label(frames["dashboard"], text="Welcome to Your Portal", font=heading_font, bg=bg_color).pack(pady=20)
for text, frame in [("Mark Attendance", "attendance"), ("View Summary", "summary")]:
    tk.Button(frames["dashboard"], text=text, font=btn_font, bg=btn_color, fg=btn_fg,
              width=25, height=2, command=lambda f=frame: raise_frame(f)).pack(pady=10)
tk.Button(frames["dashboard"], text="Logout", font=btn_font, bg="#d9534f", fg="#fff", width=20,
          command=lambda: raise_frame("login")).pack(pady=20)

# ========== ATTENDANCE ==========
def mark_attendance(sub, status):
    student_data["attendance"][sub] = "Present" if status else "Absent"
    messagebox.showinfo("Done", f"{sub} marked as {'Present' if status else 'Absent'}")

tk.Label(frames["attendance"], text="Mark Attendance", font=heading_font, bg=bg_color).pack(pady=20)
for course in ["TMC", "AMS", "GST", "ENT"]:
    c_frame = tk.Frame(frames["attendance"], bg=bg_color)
    c_frame.pack(pady=10)
    tk.Label(c_frame, text=course, font=label_font, bg=bg_color).pack(side="left", padx=10)
    tk.Button(c_frame, text="Present", bg="#5cb85c", fg="white", font=btn_font,
              command=lambda c=course: mark_attendance(c, True)).pack(side="left", padx=5)
    tk.Button(c_frame, text="Absent", bg="#f0ad4e", fg="white", font=btn_font,
              command=lambda c=course: mark_attendance(c, False)).pack(side="left", padx=5)
tk.Button(frames["attendance"], text="Back to Dashboard", font=btn_font, bg=btn_color, fg=btn_fg,
          command=lambda: raise_frame("dashboard")).pack(pady=20)

# ========== SUMMARY ==========
summary_label = tk.Label(frames["summary"], text="", font=label_font, bg=bg_color, justify="left")
summary_label.pack(pady=30)

def update_summary():
    text = f"Attendance Summary for {student_data['first_name']}:\n\n"
    for subject, status in student_data["attendance"].items():
        text += f"{subject}: {status}\n"
    summary_label.config(text=text)
    raise_frame("summary")

tk.Button(frames["summary"], text="Back to Dashboard", font=btn_font, bg=btn_color, fg=btn_fg,
          command=lambda: raise_frame("dashboard")).pack(pady=10)

# Start the UI
raise_frame("create")
root.mainloop()
