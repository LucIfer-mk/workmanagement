import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
from datetime import datetime
from datetime import date
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def adminpage():
    # --- Main window setup ---
    root = tk.Tk()
    root.title("Admin Dashboard")
    root.state("zoomed")
    root.configure(background="#efefef")
    # Header
    header = tk.Frame(root, bg="#baf7c9")
    header.pack(fill="x")
    title = tk.Label(header, text="Admin Dashboard", bg="#baf7c9",
                    fg="#1d1d1d", font=("Segoe UI", 26, "bold"))
    title.pack(padx=20, pady=16)
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

    #------- Add Staff ---------#
    def add_staff():
        
        root = tk.Tk()
        root.title("Add Staff")
        root.configure(bg="white")

        # Title section
        title_frame = tk.Frame(root, bg="#a7f5c8", height=50)
        title_frame.pack(fill="x")
        title_label = tk.Label(title_frame, text="Add Staff", font=("Arial", 18, "bold"), bg="#a7f5c8")
        title_label.pack(pady=10)

        # Main container
        main_frame = tk.Frame(root, bg="white", padx=20, pady=10)
        main_frame.pack(fill="both", expand=True)

        # ------------------- PERSONAL DETAILS -------------------
        personal_label = tk.Label(main_frame, text="Personal Details:", font=("Arial", 14, "bold"), bg="white")
        personal_label.grid(row=0, column=0, sticky="w", pady=(10, 5))

        tk.Label(main_frame, text="Name:", bg="white").grid(row=1, column=0, sticky="w")
        name_entry = ttk.Entry(main_frame, width=25)
        name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(main_frame, text="Address:", bg="white").grid(row=1, column=2, sticky="w")
        address_entry = ttk.Entry(main_frame, width=25)
        address_entry.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(main_frame, text="Contact:", bg="white").grid(row=1, column=4, sticky="w")
        contact_entry = ttk.Entry(main_frame, width=20)
        contact_entry.grid(row=1, column=5, padx=5, pady=5)

        tk.Label(main_frame, text="DOB:", bg="white").grid(row=2, column=2, sticky="w")
        dob_entry = ttk.Entry(main_frame, width=25)
        dob_entry.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(main_frame, text="Emergency Contact:", bg="white").grid(row=2, column=4, sticky="w")
        emergency_entry = ttk.Entry(main_frame, width=20)
        emergency_entry.grid(row=2, column=5, padx=5, pady=5)

        # ------------------- TAX AND ACCOUNT -------------------
        tax_label = tk.Label(main_frame, text="TAX and Account:", font=("Arial", 14, "bold"), bg="white")
        tax_label.grid(row=3, column=0, sticky="w", pady=(15, 5))

        tk.Label(main_frame, text="Account Number:", bg="white").grid(row=4, column=0, sticky="w")
        accnum_entry = ttk.Entry(main_frame, width=25)
        accnum_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(main_frame, text="Name in Account:", bg="white").grid(row=4, column=2, sticky="w")
        nameacc_entry = ttk.Entry(main_frame, width=25)
        nameacc_entry.grid(row=4, column=3, padx=5, pady=5)

        tk.Label(main_frame, text="Bank Name:", bg="white").grid(row=4, column=4, sticky="w")
        bank_entry = ttk.Entry(main_frame, width=20)
        bank_entry.grid(row=4, column=5, padx=5, pady=5)

        tk.Label(main_frame, text="IRD Number:", bg="white").grid(row=5, column=0, sticky="w")
        ird_entry = ttk.Entry(main_frame, width=25)
        ird_entry.grid(row=5, column=1, padx=5, pady=5)

        # ------------------- WORK DETAILS -------------------
        work_label = tk.Label(main_frame, text="Work Details:", font=("Arial", 14, "bold"), bg="white")
        work_label.grid(row=6, column=0, sticky="w", pady=(15, 5))

        tk.Label(main_frame, text="Position:", bg="white").grid(row=7, column=0, sticky="w")
        position_entry = ttk.Entry(main_frame, width=25)
        position_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(main_frame, text="Pay Rate:", bg="white").grid(row=7, column=2, sticky="w")
        pay_entry = ttk.Entry(main_frame, width=25)
        pay_entry.grid(row=7, column=3, padx=5, pady=5)

        tk.Label(main_frame, text="Work Email:", bg="white").grid(row=7, column=4, sticky="w")
        email_entry = ttk.Entry(main_frame, width=20)
        email_entry.grid(row=7, column=5, padx=5, pady=5)

        tk.Label(main_frame, text="Work Type:", bg="white").grid(row=8, column=0, sticky="w")
        type_entry = ttk.Entry(main_frame, width=25)
        type_entry.grid(row=8, column=1, padx=5, pady=5)

        tk.Label(main_frame, text="Department:", bg="white").grid(row=8, column=2, sticky="w")
        dept_entry = ttk.Entry(main_frame, width=25)
        dept_entry.grid(row=8, column=3, padx=5, pady=5)

        #------------------ Add Staff Section--------------#
        def addstaff_section():
            name = name_entry.get()
            address = address_entry.get()
            dob = dob_entry.get()
            contact = contact_entry.get()
            emergency = emergency_entry.get()
            account = accnum_entry.get()
            ird = ird_entry.get()
            name_acc= nameacc_entry.get()
            bank_name = bank_entry.get()
            position =position_entry.get()
            w_type =type_entry.get()
            rate = pay_entry.get()
            department = dept_entry.get()
            email=  email_entry.get()

            if not all([name, address,dob,contact,emergency, account, ird, name_acc, bank_name, position, w_type, rate, department, email]):
                messagebox.showerror("Error","All The fields must be filled")
            else:
                #___________________ Save Staff _______________
                def save_staff():
                    conn = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="mkkapri",
                    database="workplacedb"
                        )
                    cursor = conn.cursor()
                    sql = """INSERT INTO staff 
                        (name, address, dob, contact, emergency_contact, account_number, ird_number, account_name, bank_name, position, work_type, pay_rate, department, work_email)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(sql, (name, address, dob, contact, emergency, account, ird, name_acc, bank_name, position, w_type, rate, department, email))
                    conn.commit()
                    messagebox.showinfo("Success", "Staff added successfully.")
                    cursor.close()
                    conn.close()
                    root.destroy()
                save_staff()
            
        save_btn = tk.Button(
            main_frame,
            text="Save",
            font=("Helvetica", 12, "bold"),
            bg="#00cc55",
            fg="white",
            bd=0,
            relief=tk.FLAT,
            padx=60,
            pady=10,
            cursor="hand2",
            command=addstaff_section
        )
        save_btn.grid(row=9, column=0,padx=5, pady=20)

        def _cancle():
            root.destroy()

        cancel_btn = tk.Button(
            main_frame,
            text="Cancle",
            font=("Helvetica", 12, "bold"),
            bg="#cc0000",
            fg="white",
            bd=0,
            relief=tk.FLAT,
            padx=60,
            pady=10,
            cursor="hand2",
            command= _cancle
        )
        cancel_btn.grid(row=9, column=1,padx=5, pady=20)
    # add_staff()

    #------------Manage Staff ---------#
    def manage_staff():
        #___________________Fetch data from database 
        try:
            conn = pymysql.connect(
                        host="localhost",
                        user="root",
                        password="mkkapri",
                        database="workplacedb"
                            )
            cursor = conn.cursor()
            
            cursor.execute("SELECT name, contact, department, work_email FROM staff")
            data = cursor.fetchall()
            staff_table_data = []
            for row in data:
                staff_table_data.append({
                    "Name":row[0],
                    "Contact":row[1],
                    "Department":row[2],
                    "Email":row[3]
                    }
                )
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
            return
            
        # Main window
        root = tk.Tk()
        root.title("Manage Staff")
        root.state("zoomed")
        root.configure(bg="#000000")  
        # Title bar
        title_frame = tk.Frame(root, bg="#C2FFD6", height=50, bd=2, relief="solid")
        title_frame.pack(fill="x")
        title_label = tk.Label(title_frame, text="Manage Staff", font=("Arial", 18, "bold"), bg="#C2FFD6")
        title_label.pack(pady=5)

        # Table frame
        table_frame = tk.Frame(root, bg="#d3d3d3", padx=10, pady=10)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Treeview (table)
        columns = ("Name", "Contact", "Department", "Email")
        staff_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        for col in columns:
            staff_table.heading(col, text=col)
            staff_table.column(col, width=150)
        staff_table.pack(fill="both", expand=True)

        for staff in staff_table_data:
            staff_table.insert("", "end", values=(staff["Name"], staff["Contact"], staff["Department"], staff["Email"]))
        # Buttons
        btn_frame = tk.Frame(root, bg="#000000")
        btn_frame.pack(pady=10)

        #____________Remove Staff _______________
        def remove_staff():
            selected = staff_table.selection()
            if not selected:
                messagebox.showwarning("Warning", "Please select a staff member to remove.")
                return  
            # Get the Name of selected item
            staff_name = staff_table.item(selected[0])['values'][0]
            
            # Confirm deletion with warning about related data
            result = messagebox.askyesno("Confirm Delete", 
                f"Are you sure you want to remove {staff_name}?\n\n"
                "WARNING: This will also delete all related records including:\n"
                "- Attendance records\n"
                "- Payment statements\n"
                "- Other associated data\n\n"
                "This action cannot be undone!")
            if not result:
                return
                
            try:
                conn = pymysql.connect(host="localhost", user="root", password="mkkapri", database="workplacedb")
                cursor = conn.cursor()
                
                # First, get the staff ID for the name
                cursor.execute("SELECT id FROM staff WHERE name=%s", (staff_name,))
                staff_result = cursor.fetchone()
                if not staff_result:
                    messagebox.showerror("Error", "Staff member not found!")
                    return
                    
                staff_id = staff_result[0]
                
                # Delete related records first (in order of dependencies)
                # Delete from statement table first
                cursor.execute("DELETE FROM statement WHERE staff_id=%s", (staff_id,))
                
                # Delete from staff_attendance table
                cursor.execute("DELETE FROM staff_attendance WHERE staff_id=%s", (staff_id,))
                
                # Add any other related tables here if they exist
                # cursor.execute("DELETE FROM other_table WHERE staff_id=%s", (staff_id,))
                
                # Finally delete from staff table
                cursor.execute("DELETE FROM staff WHERE id=%s", (staff_id,))
                
                conn.commit()
                cursor.close()
                conn.close()
                
                # Remove from Treeview
                staff_table.delete(selected[0])
                messagebox.showinfo("Success", "Staff member and all related records removed successfully.")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to remove staff: {str(e)}")

        remove_btn = tk.Button(btn_frame, text="Remove Staff", font=("Arial", 10, "bold"), bg="red", fg="white", command=remove_staff,
                            width=15)
        remove_btn.grid(row=0, column=0, padx=10)

        #____________Update Staff 
        def update_staff():
            selected = staff_table.selection()
            if not selected:
                messagebox.showwarning("Warning", "Please select a staff member to update.")
                return  # nothing selected
            values = staff_table.item(selected[0])['values']
            old_name = values[0]  # Store the original name
            
            # Popup window
            popup = tk.Toplevel(root)
            popup.title("Update Staff")
            popup.geometry("300x250")

            # Labels and Entry fields with current values
            tk.Label(popup, text="Name:").pack()
            name_entry = tk.Entry(popup)
            name_entry.insert(0, values[0])  # Pre-fill with current value
            name_entry.pack()

            tk.Label(popup, text="Contact:").pack()
            contact_entry = tk.Entry(popup)
            contact_entry.insert(0, values[1])  # Pre-fill with current value
            contact_entry.pack()

            tk.Label(popup, text="Department:").pack()
            dept_entry = tk.Entry(popup)
            dept_entry.insert(0, values[2])  # Pre-fill with current value
            dept_entry.pack()
    
            tk.Label(popup, text="Email:").pack()
            email_entry = tk.Entry(popup)
            email_entry.insert(0, values[3])  # Pre-fill with current value
            email_entry.pack()

            def save_update():
                new_name = name_entry.get()
                new_contact = contact_entry.get()
                new_dept = dept_entry.get()
                new_email = email_entry.get()

                try:
                    conn = pymysql.connect(host="localhost", user="root", password="mkkapri", database="workplacedb")
                    cursor = conn.cursor()
                    # Update query - using the original name to identify the record
                    sql = """UPDATE staff SET name=%s, contact=%s, department=%s, work_email=%s WHERE name=%s"""
                    cursor.execute(sql, (new_name, new_contact, new_dept, new_email, old_name))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    # Update treeview
                    staff_table.item(selected[0], values=(new_name, new_contact, new_dept, new_email))
                    messagebox.showinfo("Success", "Staff details updated successfully.")
                    popup.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to update staff: {str(e)}")
                    
            tk.Button(popup, text="Save", command=save_update).pack(pady=10)

        update_btn = tk.Button(btn_frame, text="Update Details", font=("Arial", 10, "bold"), bg="red", fg="white",command=update_staff,
                        width=20)
        update_btn.grid(row=0, column=1, padx=10)

        #Exit 
        def exity_():
            root.destroy()

        exit_btn = tk.Button(btn_frame, text="Exit", font=("Arial", 10, "bold"), bg="red", fg="white",command=exity_,
                        width=20)
        exit_btn.grid(row=0, column=2, padx=10)

        root.mainloop()
    # manage_staff()

    #-------------Pay salary _------------#
    def pay_salary():
        from collections import defaultdict

        try:
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password="mkkapri",
                database="workplacedb"   
            )
            cursor = conn.cursor()

            cursor.execute("""SELECT
                                s.id ,
                                s.name, 
                                s.account_number, 
                                s.ird_number, 
                                s.pay_rate,
                                sa.started_reom,
                                sa.end_time
                            FROM staff s
                            INNER JOIN staff_attendance sa 
                            ON s.id = sa.staff_id;""")
            data =  cursor.fetchall()
            
            staff_hours = defaultdict(lambda: {
                "Name": None,
                "Account": None,
                "IRD": None,
                "Pay": None,
                "WorkedHR": 0.0
            })

            for row in data:
                _id = row[0]
                name = row[1]
                account = row[2]
                ird = row[3]
                pay_rate = row[4]
                
                try:
                    start_time = datetime.strptime(str(row[5]), "%H:%M")
                    end_time = datetime.strptime(str(row[6]), "%H:%M")
                    worked_delta = end_time - start_time
                    worked_hours = worked_delta.total_seconds() / 3600
                except (ValueError, TypeError) as e:
                    print(f"Error parsing time for staff {name}: {e}")
                    worked_hours = 0

                if staff_hours[_id]["Name"] is None:
                    staff_hours[_id]["Name"] = name
                    staff_hours[_id]["Account"] = account
                    staff_hours[_id]["IRD"] = ird
                    staff_hours[_id]["Pay"] = pay_rate

                staff_hours[_id]["WorkedHR"] += worked_hours

            staff_table_data = []
            for _id, info in staff_hours.items():
                staff_table_data.append({
                    "ID": _id,
                    "Name": info["Name"],
                    "Account": info["Account"],
                    "IRD": info["IRD"],
                    "Pay": info["Pay"],
                    "WorkedHR": round(info["WorkedHR"], 2)
                })

            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
            return
            
        # Main window
        root = tk.Tk()
        root.title("Pay Salary")
        # root.geometry("800x500")
        root.state("zoomed")
        root.configure(bg="#2B2B2B")  # Dark grey background

        # Title bar
        title_frame = tk.Frame(root, bg="#C2FFD6", height=50, bd=2, relief="solid")
        title_frame.pack(fill="x")
        title_label = tk.Label(title_frame, text="Pay Salary", font=("Arial", 18, "bold"), bg="#C2FFD6")
        title_label.pack(pady=5)

        # Table frame
        table_frame = tk.Frame(root, bg="white", padx=10, pady=10)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Treeview (table)
        columns = ("ID","Name", "Account Number", "IRD", "Worked Hours/Week", "Pay Rate")
        salary_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        for col in columns:
            salary_table.heading(col, text=col)
            salary_table.column(col, width=150)
        salary_table.pack(fill="both", expand=True)

        for staff in staff_table_data:
            salary_table.insert("", "end", values=(staff["ID"], staff["Name"], staff["Account"], staff["IRD"], staff["WorkedHR"],staff["Pay"]))

        #______________ pAY sALARY 
        def paysalary():
            selected_item = salary_table.selection()
            if not selected_item:
                messagebox.showwarning("Warning", "Please select a staff member to pay salary.")
                return
            
            staff_values = salary_table.item(selected_item, "values")
            _id = staff_values[0]
            name = staff_values[1]
            account = staff_values[2]
            ird = staff_values[3]
            worked_hr = float(staff_values[4])
            pay_rate = float(staff_values[5])

            gross_pay = worked_hr * pay_rate
            tax_rate = 0.20
            tax_amount = gross_pay * tax_rate
            net_pay = gross_pay - tax_amount

            popup = tk.Toplevel(root)
            popup.title("Pay Salary")
            popup.configure(bg="white")

            # Header
            tk.Label(popup, text="Work Place Ltd.", font=("Arial", 16, "bold"), bg="white").pack(pady=(15, 0))
            tk.Label(popup, text="Employee Payslip", font=("Arial", 14), bg="white").pack(pady=(0, 10))

            ttk.Separator(popup, orient="horizontal").pack(fill="x", padx=20, pady=5)
            # Employee details frame
            details_frame = tk.Frame(popup, bg="white")
            details_frame.pack(fill="x", padx=20, pady=5)

            tk.Label(details_frame, text=f"Employee Name: {name}", font=("Arial", 12), bg="white").grid(row=0, column=0, sticky="w")
            tk.Label(details_frame, text=f"Bank Account: {account}", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky="w")
            tk.Label(details_frame, text=f"IRD Number: {ird}", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky="w")
            tk.Label(details_frame, text=f"Pay Rate: ${pay_rate:.2f}", font=("Arial", 12), bg="white").grid(row=3, column=0, sticky="w")
            tk.Label(details_frame, text=f"Total Worked Hours: {worked_hr}", font=("Arial", 12), bg="white").grid(row=4, column=0, sticky="w")

            ttk.Separator(popup, orient="horizontal").pack(fill="x", padx=20, pady=10)

            # Pay breakdown frame
            pay_frame = tk.Frame(popup, bg="white")
            pay_frame.pack(fill="x", padx=20, pady=5)

            tk.Label(pay_frame, text="Earnings", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, sticky="w")
            tk.Label(pay_frame, text=f"Gross Pay: ${gross_pay:.2f}", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky="w")

            tk.Label(pay_frame, text="Deductions", font=("Arial", 12, "bold"), bg="white").grid(row=3, column=0, sticky="w", pady=(10, 0))
            tk.Label(pay_frame, text=f"Tax (20%): -${tax_amount:.2f}", font=("Arial", 12), fg="red", bg="white").grid(row=4, column=0, sticky="w")

            ttk.Separator(popup, orient="horizontal").pack(fill="x", padx=20, pady=10)

            # Net pay
            tk.Label(popup, text=f"Net Pay: ${net_pay:.2f}", font=("Arial", 14, "bold"), fg="green", bg="white").pack(pady=5)
            # Footer
            ttk.Separator(popup, orient="horizontal").pack(fill="x", padx=20, pady=10)

            #___________save Statement of payment to data base 
            def save_statement():
                staff_id = _id
                paymentdate = date.today()
                grosspay = gross_pay
                tax_deductions = tax_amount
                netpay = net_pay
                payment_method = "Bank Transfer"
                remarks = f"Salary have been paid for {paymentdate}"
                
                try:
                    conn = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="mkkapri",
                    database="workplacedb"   
                    )
                    cursor = conn.cursor()

                    sql = """
                        INSERT INTO statement 
                        (staff_id, payment_date, gross_pay, tax_deductions, net_pay, payment_method, remarks) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    
                    values = (staff_id, paymentdate, grosspay, tax_deductions, netpay, payment_method, remarks)
                    cursor.execute(sql, values)
                    conn.commit() 
                    cursor.close()
                    conn.close()
                    messagebox.showinfo("Success", "Payment processed successfully!")
                    popup.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save payment: {str(e)}")

            tk.Button(popup, text="Confirm Payment", font=("Arial", 10, "bold"), bg="green", fg="white",
                    command=save_statement).pack(pady=10)

        # Pay Salary button
        pay_btn = tk.Button(root, text="Pay Salary", font=("Arial", 10, "bold"), bg="red", fg="white",
                            command=paysalary, width=15)
        pay_btn.pack(pady=10)

        def exity_():
            root.destroy()

        exit_btn = tk.Button(root, text="Exit", font=("Arial", 10, "bold"), bg="red", fg="white",command=exity_,
                        width=20)
        exit_btn.pack(pady=10)
        root.mainloop()
    # pay_salary()

    #--------------statement ------------#
    def statement():
        try:
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password="mkkapri",
                database="workplacedb"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT staff_id, payment_date, gross_pay, tax_deductions, net_pay, payment_method, remarks FROM statement")
            statements = cursor.fetchall()
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {str(e)}")
            return
            
        root = tk.Tk()
        root.state("zoomed")
        root.title("Statements")

        canvas = tk.Canvas(root)
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for data in statements:
            frame = ttk.Frame(scrollable_frame, relief="raised", borderwidth=1, padding=20)
            frame.pack(padx=10, pady=5, fill="x")
            text = f"Staff ID: {data[0]}\nPayment Date: {data[1]}\nGross Pay: {data[2]}\nTax Deductions: {data[3]}\nNet Pay: {data[4]}\nPayment Method: {data[5]}\nRemarks: {data[6]}"
            label = ttk.Label(frame, text=text, justify="left")
            label.pack()

        def exity_():
            root.destroy()

        exit_btn = tk.Button(root, text="Exit", font=("Arial", 10, "bold"), bg="red", fg="white",command=exity_,width=20)
        exit_btn.pack(padx=10, anchor='ne')
    # statement()

    #----------Settings ---------------#
    def setting():
        root = tk.Tk()
        root.title("Admin Dashboard")
        root.state("zoomed")
        root.configure(background="#efefef")
            # Header
        header = tk.Frame(root, bg="#baf7c9")
        header.pack(fill="x")
        title = tk.Label(header, text="Setting", bg="#baf7c9",
                            fg="#1d1d1d", font=("Segoe UI", 26, "bold"))
        title.pack(padx=20, pady=16)
            # Navigation bar
        nav = tk.Frame(root, bg="#efefef")
        nav.pack(fill="x", padx=16, pady=(12, 6))

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

        def logout():
            root.destroy()

        button_commands = {
                # "Statement": statement,
                # "Clock in Clock Out": clockinclockout,
                "Logout": logout,
            }
        for text in ["Logout"]:
            btn = make_nav_button(text, command=button_commands[text])
            btn.pack(side="left", padx=(0, 12))
    #setting()

    def logout():
            root.destroy()
    # Map texts to commands
    button_commands = {
        "Add Staff": add_staff,
        "Manage Staff": manage_staff,
        "Pay Salary": pay_salary,
        "Statement": statement,
        "Setting": setting,
        "Logout":logout,
    }
    for text in ["Add Staff", "Manage Staff", "Pay Salary", "Statement", "Setting","Logout"]:
        btn = make_nav_button(text, command=button_commands[text])
        btn.pack(side="left", padx=(0, 12))

    # Summary cards container
    container = tk.Frame(root, bg="#efefef")
    container.pack(fill="both", expand=True, padx=16, pady=8)
    cards = tk.Frame(container, bg="#efefef")
    cards.pack(fill="x")
    card_bg = "#f5f5f5"


    card_font_title = ("Segoe UI", 13, "bold")
    card_font_value = ("Segoe UI", 13, "bold")

    def make_card(parent, title, value):
        frame = tk.Frame(parent, bg=card_bg, relief="flat", bd=0)
        frame.pack(side="left", expand=True, fill="both", padx=6, pady=6)
        title_lbl = tk.Label(frame, text=title, bg=card_bg, font=card_font_title)
        title_lbl.pack(anchor="w", padx=18, pady=(16,4))
        value_lbl = tk.Label(frame, text=value, bg=card_bg, font=card_font_value)
        value_lbl.pack(anchor="w", padx=18, pady=(0,16))
        frame.config(width=320, height=110)
        return frame

    make_card(cards, "Budget:", "$ 100,000,000")
    make_card(cards, "Expenses Till Date:", "$ 35,050.79")
    make_card(cards, "Income Till Date:", "$ 75,895.20")

    # Chart area using matplotlib
    chart_wrapper = tk.Frame(container, bg="#efefef")
    chart_wrapper.pack(fill="both", expand=True, pady=(12, 8))
    fig = Figure(figsize=(8, 4), dpi=100)
    ax = fig.add_subplot(111)

    income = [15, 18, 14, 16, 13, 12, 15, 14, 11, 13, 16, 18, 19, 20, 19, 18, 17, 21, 24, 22]
    expenses = [7.5, 6.8, 7.2, 8.0, 9.1, 8.8, 9.5, 10.0, 9.0, 8.7, 8.3, 8.1, 7.6, 7.1, 6.9, 6.8, 7.2, 7.6, 7.9, 7.7]

    ax.plot(income, color="#3b82f6", label="Income")
    ax.plot(expenses, color="#ef4444", label="Expenses")
    ax.set_title("Income Expenses Chart")
    ax.legend()
    ax.grid(True)
    canvas = FigureCanvasTkAgg(fig, master=chart_wrapper)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    root.mainloop()
# adminpage()