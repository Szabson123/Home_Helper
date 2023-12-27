import tkinter


def conf_def():
    root = tkinter.Tk()
    root.title = "Config File"
    root.geometry("700x400")

    frame_title = tkinter.Frame(root)

    frame_title.grid(row=0, column=0)
    root.grid_columnconfigure(0, weight=1)
    title = tkinter.Label(frame_title, text="Conf File", font=("Helvetica", 24))
    title.grid(row=0, column=0, pady=10)

    root.mainloop()