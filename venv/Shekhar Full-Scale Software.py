## shekhar adhikari

import tkinter as tk
from tkinter import ttk, Tk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application  = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Shekhar Text Editor')

###############################################################main menu###############################################
# --------------------------------------------------- &&&&&& End main menu ############################################

main_menu = tk.Menu() ### making main menu for file first
#adding files icon inside the file menu
new_icon = tk.PhotoImage(file= 'new.png')
open_icon = tk.PhotoImage(file= 'open.png')
save_icon = tk.PhotoImage(file= 'save.png')
save_as_icon = tk.PhotoImage(file= 'save_as.png')
exit_icon = tk.PhotoImage(file= 'exit.png')

## making a tear off because if you do not have it user can use the cursor to move it around
file = tk.Menu(main_menu,tearoff=False)

######################################################################file #############################################

#################################################### Edit Fie ##########################################################


#### Adding a tear off because you do not want users to move edit from the main menu
edit = tk.Menu(main_menu, tearoff=False)

###copy, cut, clear,paste, find



copy_icon = tk.PhotoImage(file='copy.png')
cut_icon = tk.PhotoImage(file='cut.png')
clear_icon = tk.PhotoImage(file='clear_all.png')
paste_icon = tk.PhotoImage(file='paste.png')
find_icon = tk.PhotoImage(file='find.png')

############################### END OF EDIT MENU########################################################################

############################## Working on VIEW MENU NOW ################################################################


tool_bar_icon = tk.PhotoImage(file='tool_bar.png')
status_bar_icon = tk.PhotoImage(file='status_bar.png')


view = tk.Menu(main_menu, tearoff=False)



################################END OF VIEW MENU #######################################################################

################################### Color Theme#########################################################################

light_default_icon = tk.PhotoImage(file='light_default.png')
light_plus_icon = tk.PhotoImage(file='light_plus.png')
dark_icon = tk.PhotoImage(file='dark.png')
red_icon = tk.PhotoImage(file='red.png')
night_blue_icon = tk.PhotoImage(file='night_blue.png')
monokai_icon = tk.PhotoImage(file='monokai.png')
color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar() ### variable to see what color user has selected
color_icons = (light_default_icon,light_plus_icon,dark_icon,red_icon,night_blue_icon,monokai_icon)

color_dict = {

    'Light Default' :('#000000','#ffffff'),#text color is 000 white and background color would be fffff
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
}




###############################################END OF COLOR THEME#######################################################


##cascade this will help us to show file, edit, color themes on top

main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Themes',menu=color_theme)

#########################################ADDDING FONT FAMALIES NOW######################################################

tool_bar = ttk.Label(main_application)
#we are using grid and pack in this software
tool_bar.pack(side=tk.TOP,fill=tk.X) #horizontal = tk.x #vertical = tk.y #if you want both it is just fill both



### font box
font_tuples = tk.font.families() #variable
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=30, textvariable=font_family,stat='readonly')
font_box['values'] = font_tuples
font_box.grid(row=0, column=0, padx=5)
font_box.current(font_tuples.index('Arial'))

##### size box

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width = 14, textvariable = size_var, state = 'readonly')
font_size['values'] = tuple(range(8,80,2))####range for font size tuples is great wow
font_size.current(2) ###this changes the font size in the screen
font_size.grid(row=0,column=1, padx=5)

##### bold button
#making a icon called bold icon from pictures
bold_icon = tk.PhotoImage(file='bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row = 0, column = 2, padx=5)

####m italic button
italic_icon = tk.PhotoImage(file='italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column = 3, padx = 5)

###underline button

underline_icon = tk.PhotoImage(file='underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row =0, column =4, padx = 5)

### Font-Color Button

font_color_icon = tk.PhotoImage(file='font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column = 5, padx = 5)

### align-left button

align_left_icon = tk.PhotoImage(file='align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row = 0, column =6, padx=5)

###center-button

align_center_icon = tk.PhotoImage(file='align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row = 0, column =7, padx=5)


###aling-right button

align_right_icon = tk.PhotoImage(file='align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column = 8, padx=5)


###################TEXT EDITOR##########################################################################################

text_editor = tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview) #y because we want it horizontally
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and font size functionality
current_font_family = 'Arial'
current_font_size = 12  #we gonna use this in global


### fhunction to change the font

def change_font(main_application): #argument = main application
    global current_font_family
    current_font_family = font_family.get() #to see what font user selected
    text_editor.configure(font=(current_font_family,current_font_size))
    ###how to bind this funtction with combo box


#### function to change the size now

def change_fontsize(main_application): #you can also write event=None it is not really important
    global current_font_size #using global variable value from inside function it is possible in python
    current_font_size = size_var.get() #to see what font size user has selected
    text_editor.configure(font=(current_font_family,current_font_size))
    ###how to bind this funtction with combo box
font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>",change_fontsize)



text_editor.configure(font=('Arial',12))
######### buttons functionality

## bold buttons functionality
##actual()gives answers in dictionary so we have to change the key in dictionary
#.actual() gives the default status of the application in dictionary form


#very very important
print(tk.font.Font(font=text_editor['font']).actual())

###bold functionality

def change_bold():#function to change the font
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] =='normal':####key value is weight
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] =='bold': ####key value is weight
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command=change_bold) #our function name def change_bold #function to change the shape of the font

### italic functionality

def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':#key value is slant
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_font_size, 'normal'))
italic_btn.configure(command=change_italic)

### underlined functionality

def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0: #key value is underline
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size, 'normal'))

underline_btn.configure(command=change_underline)


#### font color functionality
def change_font_color(): #defining a function called change_font color
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1]) #setting it to first index
font_color_btn.configure(command=change_font_color)

### align left, align right, center functionality

def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
align_left_btn.configure(command=align_left)

def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')
align_center_btn.configure(command=align_center)

def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')
align_right_btn.configure(command=align_right)




################################################END OF TEXT EDITOR ####################################################

################################################STATUS BAR##############################################################

status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Characters: {characters} Words: {words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)




###############################################END OF STATUS BAR########################################################

################################################file commands###########################################################

#### variable


url = ''

### new functionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)

#open functionality
def open_file(event=None): #because we wanna bind it with shortcut keys
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt',),('All files','*.*'),('Python File','*.py')))
    try:
        with open(url, 'r') as fr: #file reader
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

### save functionality

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w',encoding='utf-8') as fw: #w as in write
                fw.write(content)
        else:
             url = filedialog.asksaveasfile(mode= 'w', defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
             content2 = text_editor.get(1.0,tk.END)
             url.write(content2)
             url.close()
    except:
        return




### file commands

file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator ='Ctrl+N',command=new_file)


file.add_command(label='Open',image=open_icon, compound = tk.LEFT, accelerator = 'Cttrl+0', command=open_file)

#### save functionality
file.add_command(label='Save',image=save_icon, compound=tk.LEFT, accelerator = 'Ctrl+S',command=save_file)


def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w',encoding='utf-8') as fw: #w as in write
                fw.write(content)
        else:
             url = filedialog.asksaveasfile(mode= 'w', defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
             content2 = text_editor.get(1.0,tk.END)
             url.write(content2)
             url.close()
    except:
        return

### Save As functionality now


def save_as_file(event=None):
    global url
    try:
        content = (text_editor.get(1.0, tk.END))
        url = filedialog.asksaveasfile(mode= 'w', defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
        url.write(content)
        url.close()
    except:
        return
file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT, accelerator = 'Ctrl+Alt+S',command=save_as_file)

### Exit functionality





##########################################file commands#################################################################

##########################################edit commands#################################################################
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)

### find functionality

def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0, 0)

    ## frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    ## entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    ## label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()


####applying label for edit commands

edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT, accelerator = 'Ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT, accelerator = 'Ctrl+X',command=lambda:text_editor.event_generate("<Control X>"))
edit.add_command(label='Clear',image=clear_icon,compound=tk.LEFT, accelerator = 'Ctrl+Alt+X',command=lambda:text_editor.delete(1.0, tk.END))# will delete from 1st line toend
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT, accelerator = 'Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command = find_func)

#######################################edit commands####################################################################

#######################################view commands####################################################################
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else :
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


view.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0,variable = show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1, offvalue=False,variable = show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)


## color theme
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1



#### bind shortcut keys for main menu
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as_file)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)


main_application.config(menu=main_menu)

# -------------------------------------&&&&&&&& End main menu  functinality&&&&&&&&&&& ----------------------------------














main_application.config(menu=main_menu)
main_application.mainloop()
