# PROGRAMMING AND ALGIRITHMS 2
# NAME - ROHAN JOSHI
# STUDENT ID - 210307
# COURSEWORK ASSIGNMENT 2
#                         MENU DRIVEN PORT SCANNER


import customtkinter as ct
import socket
from tkinter import messagebox

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")


window = ct.CTk()
window.title("Port Scanner")
window.geometry("670x480")


def third_window():

    for widget in window.winfo_children():
        widget.destroy()
    text_area = ct.CTkTextbox(window)
    text_area.configure(width=415, height=230)
    text_area.pack(pady=46)
    text_area.configure(font=("Arial", 15))

    def user_defined():
        '''The user defined function is used for scanning the localhost with 
        ports from 135 whose value are given while calling the function.'''
        target = '127.0.0.1'
        open_number = 0
        close_number = 0
        for port in range(134, 138):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((target, port))
            if result == 0:
                text_area.insert(
                    ct.END, f"[+] The port {port} is open on {target}\n")
                open_number += 1

            else:
                text_area.insert(
                    ct.END, f"[-] The port {port} is closed on {target}\n")
                close_number += 1
        text_area.insert(ct.END, "\n")
        text_area.insert(
            ct.END, f"[-] The closed ports are {close_number} and open ports are {open_number}\n")
        text_area.insert(ct.END, "\n")
        text_area.insert(ct.END, "\n")
        text_area.insert(ct.END,
                         "Scanning the ports from range 134 to 137 was successful !!!\n")

        s.close()
        back = ct.CTkButton(window, text="Take me back", command=second_window,
                            font=('Helvetica', 15))
        back.pack(pady=15)

        exit_button = ct.CTkButton(
            window, text="Exit the program", command=terminate)
    # font=('Helvetica', 15))
        exit_button.pack(pady=15)

    user_defined()


def second_window():
    for widget in window.winfo_children():
        widget.destroy()

    text2 = ct.CTkLabel(window, text="Your scanning options are:",
                        font=('Helvetica', 19, 'bold'))
    text2.pack(pady=4)

    user_defined_button = ct.CTkButton(window, text="scanning the localhost with ports from 134",
                                       font=('Helvetica', 15), command=third_window)
    user_defined_button.pack(pady=15)

    single_port_button = ct.CTkButton(
        window, text="scanning the single port of the given target through the user input", command=fourth_window, font=('Helvetica', 15))

    single_port_button.pack(pady=15)

    multi_port_button = ct.CTkButton(
        window, text=" scanning the list of ports of the given target", command=fifth_window, font=('Helvetica', 15))

    multi_port_button.pack(pady=15)

    range_port_button = ct.CTkButton(
        window, text="Scan ports of specific range", command=sixth_window, font=('Helvetica', 15))

    range_port_button.pack(pady=15)

    all_port_button = ct.CTkButton(window, text="scan all the ports of the given target",
                                   command=seventh_window, font=('Helvetica', 15))
    all_port_button.pack(pady=15)

    back = ct.CTkButton(window, text="Take me back",
                        command=first, font=('Helvetica', 15))
    back.pack(pady=15)

    exit_button = ct.CTkButton(
        window, text="Exit the program", command=terminate, font=('Helvetica', 15))
    exit_button.pack(pady=15)


def first():
    for widget in window.winfo_children():
        widget.destroy()

    text1 = ct.CTkLabel(window, text="Programming and Algorithms 2",
                        font=('Bahnschrift SemiBold Condensed', 46, 'bold'))
    text1.pack(pady=30)

    text1 = ct.CTkLabel(window, text="Port Scanning",
                        font=('Times New Roman', 34, 'bold'))
    text1.pack(pady=12)

    text2 = ct.CTkLabel(window, text="Created by Rohan Joshi",
                        font=('Times New Roman', 20, 'italic'))
    text2.pack(pady=4)

    scan_button = ct.CTkButton(window, text="Scanning Options", fg_color=("#564ba4"),
                               font=('Helvetica', 15), command=second_window)
    scan_button.pack(pady=18)


first()


def singleportinput(ip_entry, port_entry, root):
    '''The function is used for scanning the single port of the 
    given target through the user input.'''

    open_number = 0
    close_number = 0

    target = ip_entry.get()
    port = port_entry.get()

    if target == "" and port == "":
        messagebox.showerror('Error', "entry field can not be empty")

    else:
        open_number = 0
        close_number = 0

        if target.count(".") != 3 or port.isdigit() == False:
            messagebox.showerror(
                'Error', "Please enter a valid IP address and port number")
        else:
            text_area = ct.CTkTextbox(window)
            text_area.configure(width=400, height=250)
            text_area.pack(pady=46)
            text_area.configure(font=("Arial", 15))

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((target, int(port)))
            if result == 0:
                text_area.insert(
                    ct.END, f"[-] The port {port} is open on {target}\n")
                open_number += 1

            else:
                text_area.insert(
                    ct.END, f"[-] The port {port} is closed on {target}\n")
                close_number += 1

            text_area.insert(ct.END, "\n")
            text_area.insert(
                ct.END, f"[-] The closed ports are {close_number} and open ports are {open_number}\n")
            text_area.insert(ct.END, "\n")
            text_area.insert(ct.END, "\n")
            text_area.insert(ct.END,
                             f"Scanning the singleport {port} of ip address {target} was successful !!!\n")

            s.close()
            back = ct.CTkButton(window, text="Take me back", command=second_window,
                                font=('Arial', 15))
            back.pack(pady=15)

            exit_button = ct.CTkButton(
                window, text="Exit the program", command=terminate, font=('Helvetica', 15))
            exit_button.pack(pady=15)

            root.destroy()


def fourth_window():

    root = ct.CTk()
    root.geometry("200x150")

    for widget in window.winfo_children():
        widget.destroy()
    ip_label = ct.CTkLabel(root, text="IP Address:")
    ip_label.pack()

    ip_entry = ct.CTkEntry(root)
    ip_entry.pack()

    port_label = ct.CTkLabel(root, text="Port:")
    port_label.pack()

    port_entry = ct.CTkEntry(root)
    port_entry.pack()

    submit_button = ct.CTkButton(
        root, text="Submit", command=lambda: singleportinput(ip_entry, port_entry, root))
    submit_button.pack()

    root.mainloop()


def multiportinput(ip_entry, port_entry, root):
    '''The function is used for scanning the list of ports of the given target.'''
    print('\n')

    target = ip_entry.get()
    portt = port_entry.get()

    if target == "" and portt == "":
        messagebox.showerror('Error', "entry field can not be empty")

    else:
        open_number = 0
        close_number = 0

        if target.count(".") != 3:
            messagebox.showerror(
                'Error', "Please enter a valid IP address and port number")
        else:
            text_area = ct.CTkTextbox(window)
            text_area.configure(width=443, height=300)
            text_area.pack(pady=46)
            text_area.configure(font=("Arial", 15))

            ports_collection = portt.replace(" ", ",")
            ports = ports_collection.split(',')

    # convert all elements to int
            ports = [int(i) for i in ports]
    # sort the ports using bubble sort
            for i in range(len(ports)):
                for j in range(0, len(ports)-i-1):
                    if ports[j] > ports[j+1]:
                        # sorting the range in ascending order using bubble sort
                        ports[j], ports[j+1] = ports[j+1], ports[j]

     # scan ports
            for port in ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((target, port))
                if result == 0:
                    # print(f"{GREEN}[+] The port {port} is open on {target}{RESET}")
                    text_area.insert(
                        ct.END, f"[-] The port {port} is open on {target}\n")
                    text_area.insert(ct.END, "\n")
                    open_number += 1
                else:
                    text_area.insert(
                        ct.END, f"[-] The port {port} is closed on {target}\n")
                    text_area.insert(ct.END, "\n")
                    close_number += 1

            text_area.insert(
                ct.END, f"[-] The closed ports are {close_number} and open ports are {open_number}\n")
            text_area.insert(ct.END, "\n")
            text_area.insert(ct.END, "\n")
            text_area.insert(ct.END,
                             f"Scanning the multiports {ports} of ip address {target} was successful !!!\n")

            s.close()
            back = ct.CTkButton(window, text="Take me back", command=second_window,
                                font=('Helvetica', 15))
            back.pack(pady=15)

            exit_button = ct.CTkButton(
                window, text="Exit the program", command=terminate, font=('Helvetica', 15))
            exit_button.pack(pady=15)

            root.destroy()


def fifth_window():

    root = ct.CTk()
    root.geometry("320x190")

    for widget in window.winfo_children():
        widget.destroy()
    ip_label = ct.CTkLabel(root, text="IP Address:")
    ip_label.pack()

    ip_entry = ct.CTkEntry(root)
    ip_entry.pack()

    port_label = ct.CTkLabel(
        root, text="Port: Enter multiple ports seperated by ','")
    port_label.pack()

    port_entry = ct.CTkEntry(root)
    port_entry.pack()

    submit_button = ct.CTkButton(
        root, text="Submit", command=lambda: multiportinput(ip_entry, port_entry, root))
    submit_button.pack()

    root.mainloop()


def rangeportinput(ip_entry, port_entry, root):
    '''The function is used to scan the range of ports of the given target.'''
    print('\n')
    target = ip_entry.get()
    portt = port_entry.get()

    if target == "" and portt == "":
        messagebox.showerror('Error', "entry field can not be empty")

    else:
        op = 0
        cp = 0

        if target.count(".") != 3:
            messagebox.showerror(
                'Error', "Please enter a valid IP address and port number")
        else:
            text_area = ct.CTkTextbox(window)
            text_area.configure(width=400, height=240)
            text_area.pack(pady=46)
            text_area.configure(font=("Arial", 15))
            ports_collection = portt.replace(" " and ",", "-")
            ports = ports_collection.split('-')

        # Convert the ports to a list of integers
            ports = list(map(int, ports))
            swap = False

            for i in range(len(ports)):

                for j in range(len(ports)-1):

                    if ports[j] > ports[j+1]:

                        # Swap the ports
                        temp = ports[j]
                        ports[j] = ports[j+1]
                        ports[j+1] = temp
                        swap = True
                if swap == False:
                    break

    # helps to scan ports in ascending manner
            for i in range(int(ports[0]), int(ports[1])+1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((target, i))
                if result == 0:
                    text_area.insert(
                        ct.END, f"[-] The port {i} is open on {target}\n")
                    text_area.insert(ct.END, "\n")
                    op += 1
                else:
                    text_area.insert(
                        ct.END, f"[-] The port {i} is closed on {target}\n")
                    text_area.insert(ct.END, "\n")

                    cp += 1

                s.close()
            text_area.insert(
                ct.END, f"[-] The closed ports are {cp} and open ports are {op}\n")

            text_area.insert(ct.END, "\n")
            text_area.insert(ct.END, "\n")
            text_area.insert(ct.END,
                             f"Scanning the ports of specific range of user choice of ip address {target} was successful !!!\n")
            back = ct.CTkButton(window, text="Take me back", command=second_window,
                                font=('Helvetica', 15))
            back.pack(pady=15)

            exit_button = ct.CTkButton(
                window, text="Exit the program", command=terminate, font=('Helvetica', 15))
            exit_button.pack(pady=15)

            root.destroy()


def sixth_window():

    root = ct.CTk()
    root.geometry("320x190")

    for widget in window.winfo_children():
        widget.destroy()
    ip_label = ct.CTkLabel(root, text="IP Address:")
    ip_label.pack()

    ip_entry = ct.CTkEntry(root)
    ip_entry.pack()

    port_label = ct.CTkLabel(
        root, text="Port: Enter range of ports seperated by '-'")
    port_label.pack()

    port_entry = ct.CTkEntry(root)
    port_entry.pack()

    submit_button = ct.CTkButton(
        root, text="Submit", command=lambda: rangeportinput(ip_entry, port_entry, root))
    submit_button.pack()

    root.mainloop()


def allportscan(ip_entry, root):
    '''The function is used to scan all the ports of the given target.'''
    print('\n')

    target = ip_entry.get()
    if target == "":
        messagebox.showerror('Error', "entry field can not be empty")
    else:
        op = 0
        cp = 0
        if target.count(".") != 3:
            messagebox.showerror(
                'Error', "Please enter a valid IP address and port number")
        else:
            text_area = ct.CTkTextbox(window)
            text_area.configure(width=379, height=210)
            text_area.pack(pady=46)
            text_area.configure(font=("Arial", 15))

            for port in range(1, 65536):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((target, port))
                if result == 0:
                    text_area.insert(
                        ct.END, f"[-] The port {port} is open on {target}\n")
                    text_area.insert(ct.END, "\n")

                    op += 1

                else:
                    text_area.insert(
                        ct.END, f"[-] The port {port} is closed on {target}\n")
                    text_area.insert(ct.END, "\n")

                    cp += 1
                s.close()
                text_area.insert(ct.END, "\n")
                text_area.insert(ct.END, "\n")
                text_area.insert(ct.END,
                                 f"Scanning the ports of specific range of user choice of ip address {target} was successful !!!\n")
                back = ct.CTkButton(window, text="Take me back", command=second_window,
                                    font=('Helvetica', 15))
                back.pack(pady=15)

                exit_button = ct.CTkButton(
                    window, text="Exit the program", command=terminate, font=('Helvetica', 15))
                exit_button.pack(pady=15)
                root.destroy()


def seventh_window():

    root = ct.CTk()
    root.geometry("220x150")

    for widget in window.winfo_children():
        widget.destroy()
    ip_label = ct.CTkLabel(
        root, text="IP Address: Enter IP address of your choice")
    ip_label.pack()

    ip_entry = ct.CTkEntry(root)
    ip_entry.pack()

    submit_button = ct.CTkButton(
        root, text="Submit", command=lambda: allportscan(ip_entry, root))
    submit_button.pack()

    root.mainloop()


def terminate():
    exit()


window.mainloop()
