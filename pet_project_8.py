# 8.  Приложение для записи заметок
from tkinter import *
import datetime

def clear_search(event):
    if search_entry.get() == "Поиск...":
        search_entry.delete(0, END)
        search_entry.configure(fg='white')


def restore_search(event):
    if not search_entry.get():
        search_entry.insert(0, 'Поиск...')
        search_entry.configure(fg='#949494')


def scroll_canvas(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")


window = Tk()
window.geometry('312x632')
window.title('Заметки')
window.configure(bg='#202020')

gl = Frame(window, bg='#202020', bd=0, width=322, height=632)
gl.place(x=0, y=120)

# Создание вертикального скроллбара
scrollbar = Scrollbar(gl, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Создание холста (canvas) для размещения виджетов
canvas = Canvas(window, yscrollcommand=scrollbar.set, bg='#202020', bd=0, width=300, height=510, highlightthickness=0)
canvas.place(x=0, y=120)

scrollbar.config(command=canvas.yview)

# Создание фрейма на холсте для размещения виджетов
frame = Frame(canvas, bg='#202020')
canvas.create_window((0, 0), window=frame, anchor="nw")


# Добавление обработчика прокрутки колесом мыши
canvas.bind_all("<MouseWheel>", scroll_canvas)



x = 0
text = {}


def add_note():


    def del_note():
        pass

    value_to_find = 2
    def edit_note():
        pass

    # Вложенная функция для обработки вставки текста в заметку
    def add_text_in_note(event):
        current_time = datetime.datetime.now().time()
        hours = current_time.hour
        minutes = current_time.minute
        ant = add_note_text.get('1.0', END)
        label.get('1.0', END)
        label.delete('1.0', END)
        label.insert('1.0', f'{hours}:{minutes}     ')
        label.insert(END, ant)

    def ok_note():
        ant = add_note_text.get('1.0', END)
        text[x] = ant
        print(text)

    global x, text
    x += 1
    # Создание окна для заметки
    root = Toplevel()
    root.geometry('300x313')
    root.configure(bg='#333333')

    def close_note():
        root.destroy()

    # Создание фрейма для кнопок в окне заметки
    new_set_field = Frame(root, bg='#E7B806', width=301, height=40)
    new_set_field.place(x=0, y=0)
    new_photo_add_note = PhotoImage(file='icons8-плюс-40.png')
    Button(new_set_field, image=new_photo_add_note, height=40, bd=0, bg='#E7B806', command=add_note).place(x=0, y=0)

    new_photo_close_note = PhotoImage(file='icons8-крестик-40.png')
    Button(new_set_field, image=new_photo_close_note, height=40, bd=0, bg='#E7B806', command=close_note).place(x=261,
                                                                                                               y=0)

    new_photo_ok_note = PhotoImage(file='ок-40.png')
    Button(new_set_field, image=new_photo_ok_note, height=40, bd=0, bg='#E7B806', command=ok_note).place(x=130, y=0)

    win = Frame(frame, bg='#404040', bd=0,  width=290, height=92)
    win.pack(pady=5, padx=13)

    label = Text(win, bg='#404040', bd=0, fg='#949494', font=("Arial", 12), width=28, height=5)
    label.place(x=0, y=0)

    del_note_button = PhotoImage(file='удалить-30.png')
    Button(win, image=del_note_button, height=30, bd=0, bg='#404040', command=del_note).place(x=255, y=10)

    edit_note_button = PhotoImage(file='редактировать-30.png')
    Button(win, image=edit_note_button, height=30, bd=0, bg='#404040', command=edit_note).place(x=255, y=50)


    # Создание текстового виджета для ввода текста заметки в окне
    add_note_text = Text(root, width=33, height=15, bg='#333333', fg='white', wrap=WORD, font=("Arial", 12), bd=0)
    add_note_text.place(x=0, y=40)
    add_note_text.bind("<Key>", add_text_in_note)
    root.mainloop()

set_field = Frame(window, bg='#202020', width=302, height=40)
set_field.place(x=0, y=0)
photo_add_note = PhotoImage(file='плюс-40.png')
Button(set_field, image=photo_add_note, height=40, bd=0, bg='#202020', command=add_note).place(x=10, y=0)

photo_set_note = PhotoImage(file='настройки-40.png')
Button(set_field, image=photo_set_note, height=40, bd=0, bg='#202020').place(x=222, y=0)

photo_close_note = PhotoImage(file='крестик-40.png')
Button(set_field, image=photo_close_note, height=40, bd=0, bg='#202020').place(x=262, y=0)

Label(window, text='Записки', width=7, height=1, bg='#212121', fg='#FFFFFF', font=('Arial', 14, 'bold')).place(x=10,
                                                                                                               y=40)

search_field = Frame(window, bg='#404040', width=286, height=32)
search_field.place(x=13, y=78)
photo_search_field = PhotoImage(file='поиск-32.png')
Button(search_field, image=photo_search_field, height=33, bd=0, bg='#404040').place(x=253, y=0)
search_entry = Entry(search_field, bg='#404040', bd=0, width=35)
search_entry.place(x=15, y=6)
search_entry.insert(END, 'Поиск...')
search_entry.configure(fg='#949494')
search_entry.bind("<FocusIn>", clear_search)
search_entry.bind("<FocusOut>", restore_search)

photo_del_field = PhotoImage(file='крестик-32.png')
Button(search_field, image=photo_del_field, height=33, bd=0, bg='#404040').place(x=231, y=0)

window.mainloop()
