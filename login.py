import tkinter as tk
from tkinter import messagebox
import json

from admin import adminpage
from staff import staff

def loginpage():
    # ----------------- Main App Window -----------------
    root = tk.Tk()
    root.title("Login")
    root.state("zoomed")
    root.resizable(False, False)
    root.config(bg="#f2f2f2")

    # ----------------- Styling -----------------
    font_title = ("Helvetica", 22, "bold")
    font_label = ("Helvetica", 12)
    font_entry = ("Helvetica", 12)

    # ----------------- Center Frame -----------------
    frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, bd=0, relief=tk.FLAT)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # ----------------- Title -----------------
    tk.Label(frame, text="Welcome to Work Place Ltd. Login", font=font_title, bg="white", fg="#333").pack(pady=(0, 10))
    tk.Label(frame, text="Please login to continue", font=("Helvetica", 10), bg="white", fg="#666").pack()

    # ----------------- Username Entry -----------------
    tk.Label(frame, text="Username", font=font_label, bg="white", anchor="w").pack(fill="x", pady=(20, 0))
    entry_username = tk.Entry(frame, font=font_entry, bd=0, bg="#f0f0f0", relief=tk.FLAT)
    entry_username.pack(fill="x", pady=5, ipady=8)

    # ----------------- Password Entry -----------------
    tk.Label(frame, text="Password", font=font_label, bg="white", anchor="w").pack(fill="x", pady=(15, 0))
    password_var = tk.StringVar()
    entry_password = tk.Entry(frame, textvariable=password_var, show="*", font=font_entry, bd=0, bg="#f0f0f0", relief=tk.FLAT)
    entry_password.pack(fill="x", pady=5, ipady=8)

    # ----------------- Show or Hide Password -----------------
    def toggle_password():
        if entry_password.cget('show') == '':
            entry_password.config(show='*')
            btn_toggle.config(text="Show")
        else:
            entry_password.config(show='')
            btn_toggle.config(text="Hide")

    btn_toggle = tk.Button(frame, text="Show", command=toggle_password, font=("Helvetica", 9), bg="white", bd=0, fg="#007acc", cursor="hand2")
    btn_toggle.pack(anchor="e")

    #------------- Login action handlen ----------------------------------------#
    def login_action():
        username = entry_username.get()
        password = entry_password.get()

        #------------- Read login.json to get login information----------------------#
        with open("login.json","r") as file:
            data = json.load(file)

        #----------------- Check for user in system ------------#
        user_found = None
        for user in data["user"]:
            if user["name"].lower() == username and user["password"] == password:
                user_found = user
                break
        if user_found:
            user_id = user_found["id"]
            user_role = user_found["rol"]
            # print(user_id)
            if not user_role:
                print("invalid user input")
            
            elif user_role == "admin":
                    root.destroy()
                    adminpage()
                       
            elif user_role == "staff":
                    root.destroy()
                    staff(user_id)
                                    
        else:
            messagebox.showerror("User Not Found", "User Not Found")
                
        return user_found["id"] if user_found else None
    # ----------------- Login Button -----------------#
    btn_login = tk.Button(
        frame,
        text="Login",
        font=("Helvetica", 12, "bold"),
        bg="#007acc",
        fg="white",
        bd=0,
        relief=tk.FLAT,
        padx=10,
        pady=10,
        cursor="hand2",
        command=login_action
    )
    btn_login.pack(fill="x", pady=20)

    # ----------------- 🤣 -----------------
    tk.Label(frame, text="Design and Developed By MK ", font=("Helvetica", 10), bg="white", fg="#999").pack()
    root.mainloop()
# loginpage()