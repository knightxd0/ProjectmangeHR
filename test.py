import tkinter as tk

def clear_search(event):
    search.delete(0, tk.END)

root = tk.Tk()

search = tk.Entry(root, width=100)
search.insert(0, "Enter the value to search")
search.pack()
search.bind("<Button-1>", clear_search)

root.mainloop()