import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pymysql

def staff(staff_id):

    root = tk.Tk()
    root.state("zoomed")
    root.title("Staff Login")

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="mkkapri",
        database="workplacedb"
    )
    cursor = conn.cursor()
    cursor.execute(f""" 
    SELECT name FROM staff WHERE id ={staff_id}

""")
    row = cursor.fetchall()
    name = row[0][0]
    # print(name)
    cursor.close()
    conn.close()

    #------------ Main Application ------------

    header = tk.Frame(root, bg="#baf7c9")
    header.pack(fill="x")
    title = tk.Label(header, text="Staff Dashboard", bg="#baf7c9",
                        fg="#1d1d1d", font=("Segoe UI", 26, "bold"))
    title.pack(padx=20, pady=16)
    sub = tk.Label(header, text=f"Welcome {name}",bg="#baf7c9",
                        fg="#6b6b6b", font=("Segoe UI",15 , "bold"))
    sub.pack(padx=20, pady=10)
        # Navigation bar
    nav = tk.Frame(root, bg="#efefef")
    nav.pack(fill="x", padx=16, pady=(12, 6))

    def make_nav_button(text, command=None):
        btn = tk.Button(nav, text=text, font=("Segoe UI", 10, "bold"),
                            bg="#dedede", activebackground="#cfcfcf",
                            fg="#1d1d1d", relief="flat", bd=0,
                            padx=20, pady=10, cursor="hand2",
                            command=command)  # pass the command here
        btn.bind("<Enter>", lambda e: btn.config(bg="#d2d2d2"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#dedede"))
        return btn

    #------------- Add Tasks -------------
    def add_task():
        root = tk.Tk()
        root.title("Add Tasks")

        header = tk.Frame(root, bg="#baf7c9")
        header.pack(fill="x")

        title = tk.Label(header, text="Add Tasks", bg="#baf7c9",
                    fg="#1d1d1d", font=("Segoe UI", 26, "bold"))
        title.pack(padx=20, pady=16)
        # Title
        ttk.Label(root, text="Task Title:").pack(pady=(10, 0), anchor="w", padx=20)
        title_entry = ttk.Entry(root, width=50)
        title_entry.pack(pady=5, padx=20)
        # Description
        ttk.Label(root, text="Description:").pack(pady=(10, 0), anchor="w", padx=20)
        desc_text = tk.Text(root, width=50, height=5)
        desc_text.pack(pady=5, padx=20)

        # Assigned Date
        ttk.Label(root, text="Assigned Date (YYYY-MM-DD):").pack(pady=(10, 0), anchor="w", padx=20)
        assigned_entry = ttk.Entry(root, width=50)
        assigned_entry.pack(pady=5, padx=20)

        # Due Date
        ttk.Label(root, text="Due Date (YYYY-MM-DD):").pack(pady=(10, 0), anchor="w", padx=20)
        due_entry = ttk.Entry(root, width=50)
        due_entry.pack(pady=5, padx=20)

        def save_task():
            _id = staff_id 
            title = title_entry.get().strip()
            description = desc_text.get("1.0", tk.END).strip()
            assigned = assigned_entry.get().strip()
            due = due_entry.get().strip()

            if not all([title, description, assigned, due]):
                messagebox.showerror("Error", "Please fill all the fields")
                root.destroy()
                return 
            conn = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="mkkapri",
                    database="workplacedb"
                )
            cursor = conn.cursor()
            sql = """
                INSERT INTO staff_task (staff_id, assigned_date, due_date, task_title, task_details)
                VALUES (%s, %s, %s, %s, %s)
                """
            cursor.execute(sql, (_id, assigned, due, title, description))
            conn.commit()
            messagebox.showinfo("Success", "Task saved successfully!")
            cursor.close()
            conn.close()
            root.destroy()
        # Save Button       
        save_btn = tk.Button(
        root,
        text="Save Task",
        font=("Arial", 15, "bold"),
        bg="red",
        fg="white",
        command=save_task,
        width=15
         )
        save_btn.pack(pady=20)

#------- Clockout -------------------
    def clockinclockout():
        popup = tk.Tk()
        popup.title("Clock in Clock Out")

        def clock_in():
            from datetime import datetime
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d")
            formatted_time = now.strftime("%H:%M")
            print(formatted_date)
            print("Current time:", formatted_time)

            # Save clock in in data base 
            conn = pymysql.connect(
                host="localhost",
                user="root",
                passwd="mkkapri",
                database="workplacedb"
            )
            cursor = conn.cursor()

            cursor.execute("""
                          INSERT INTO staff_attendance (staff_id, attendance_date, end_time, started_reom) VALUES (%s, %s, %s, %s)
                           """,(staff_id, formatted_date, 0, formatted_time))
            conn.commit()
            cursor.close()
            conn.close()

        clockin = tk.Button(
            popup,
            text="Clock in",
            font=("Helvetica", 12, "bold"),
            bg="#00cc55",
            fg="white",
            bd=0,
            relief=tk.FLAT,
            padx=60,
            pady=10,
            cursor="hand2",
            command= clock_in
        )
        clockin.grid(row=0, column=0,padx=5, pady=20)

        def clock_out():
            from datetime import datetime
            now = datetime.now()
            formatted_time = now.strftime("%H:%M")
            formatted_date = now.strftime("%Y-%m-%d")
            # print(f"Clock out at {formatted_time}")
            conn = pymysql.connect(
                host="localhost",
                user="root",
                passwd="mkkapri",
                database="workplacedb"
            )
            cursor = conn.cursor()

            sql = """
                UPDATE staff_attendance
                SET end_time = %s
                WHERE staff_id = %s
                AND attendance_date = %s
                AND (end_time IS NULL OR end_time = '0' OR end_time = '')
                LIMIT 1
            """
            cursor.execute(sql, (formatted_time, staff_id, formatted_date))
            conn.commit()
            cursor.close()
            conn.close()

        clock_out = tk.Button(
            popup,
            text="Clock Out",
            font=("Helvetica", 12, "bold"),
            bg="#cc0000",
            fg="white",
            bd=0,
            relief=tk.FLAT,
            padx=60,
            pady=10,
            cursor="hand2",
            command= clock_out
        )
        clock_out.grid(row=0, column=1,padx=5, pady=20)

    def logout():
         root.destroy()

    button_commands = {
            "Add Task": add_task,
            "Clock in Clock Out": clockinclockout,
            "Logout":logout,  
        }
    for text in ["Add Task","Clock in Clock Out",  "Logout"]:
            btn = make_nav_button(text, command=button_commands[text])
            btn.pack(side="left", padx=(0, 12))

    # Get user task from DB
    conn = pymysql.connect(
            host="localhost",
            user="root",
            password="mkkapri",
            database="workplacedb"   
        )
    cursor = conn.cursor()
    # join data from db hhhhhhhhhhhhhh
    cursor.execute("""
        SELECT s.name, 
            st.assigned_date, 
            st.due_date, 
            st.task_title, 
            st.task_details,
            st.status,
            st.task_id
        FROM staff_task st
        INNER JOIN staff s ON st.staff_id = s.id
        Where st.staff_id = %s   """,(staff_id))
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()

    # Scrollable Frame
    canvas = tk.Canvas(root, bg="#dcdcdc", highlightthickness=0)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="#dcdcdc")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True, padx=20, pady=10)
    scrollbar.pack(side="right", fill="y")

    # Store checkboxes for update
    task_check_vars = {}

    # Function to create task card
    def create_task_card(parent, title, description, start_date, due_date, status, task_id):
        bg_color = "#00ff00" if status.lower() == "completed" else "#ff0000"
        
        card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid", padx=10, pady=5)
        card.pack(fill="x", pady=10, ipadx=5)

        # Title row
        title_frame = tk.Frame(card, bg=bg_color)
        title_frame.pack(fill="x")
        
        tk.Label(title_frame, text=title, font=("Arial", 14, "bold"), bg=bg_color).pack(side="left")

        if status.lower() != "completed":
            var = tk.BooleanVar()
            task_check_vars[task_id] = var
            tk.Checkbutton(title_frame, text="Mark Complete", variable=var, bg=bg_color).pack(side="right")

        # Description
        tk.Label(card, text=description, font=("Arial", 12, "bold"),
                bg=bg_color, wraplength=800, justify="left").pack(anchor="w", pady=5)

        # Dates
        date_frame = tk.Frame(card, bg=bg_color)
        date_frame.pack(fill="x")
        tk.Label(date_frame, text=f"Due: {start_date}", bg=bg_color, font=("Arial", 10)).pack(side="left")
        tk.Label(date_frame, text=f"Due: {due_date}", bg=bg_color, font=("Arial", 10)).pack(side="right")

    # Create task cards
    for task in tasks:
        staff_name, assigned_date, due_date, title, details, status, task_id = task
        create_task_card(scroll_frame, title, details, assigned_date, due_date, status, task_id)

    # Function to update DB
    def update_tasks():
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="mkkapri",
            database="workplacedb"
        )
        cursor = conn.cursor()

        for task_id, var in task_check_vars.items():
            if var.get():
                cursor.execute("UPDATE staff_task SET status='completed' WHERE task_id=%s", (task_id,))
        conn.commit()

        # Clear old task cards
        for widget in scroll_frame.winfo_children():
            widget.destroy()

        # Reload updated tasks
        cursor.execute("""
            SELECT s.name, 
                st.assigned_date, 
                st.due_date, 
                st.task_title, 
                st.task_details,
                st.status,
                st.task_id
            FROM staff_task st
            INNER JOIN staff s ON st.staff_id = s.id
            WHERE st.staff_id = %s
        """, (staff_id,))
        updated_tasks = cursor.fetchall()

        # Recreate task cards
        task_check_vars.clear()
        for task in updated_tasks:
            staff_name, assigned_date, due_date, title, details, status, task_id = task
            create_task_card(scroll_frame, title, details, assigned_date, due_date, status, task_id)

        tk.messagebox.showinfo("Update", "Selected tasks marked as completed.")

        cursor.close()
        conn.close()

    # Update button
    update_btn = tk.Button(root, text="Update", font=("Arial", 16, "bold"), bg="#ff0000", fg="black",
                        width=15, height=2, command=update_tasks)
    update_btn.pack(pady=20)

    root.mainloop()
# staff()