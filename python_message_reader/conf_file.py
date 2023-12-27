import tkinter as tk


def conf_def():
    root = tk.Tk()
    root.title("Config File")
    root.geometry("700x400")

    frame_title = tk.Frame(root)
    frame_content = tk.Frame(root)

    root.grid_columnconfigure(0, weight=1)
    
    frame_title.grid(row=0, column=0, sticky="ew", columnspan=2)  # Rozszerzamy frame_title na dwie kolumny
    frame_title.grid_columnconfigure(0, weight=1)
    title = tk.Label(frame_title, text="Conf File", font=("Helvetica", 24))
    title.grid(row=0, column=0, pady=10, sticky="ew")
    
    frame_content.grid(row=1, column=0, sticky="w")
    page1 = tk.Label(frame_content, text='Messenger', font=("Helvetica", 15))
    page1.grid(row=0, column=0, sticky='w')
    
    page1_text = tk.Entry(frame_content)
    page1_text.grid(row=0, column=1, padx=10, sticky='w')  # Dodajemy trochę miejsca po lewej stronie pola Entry
    
    root.mainloop()

conf_def()