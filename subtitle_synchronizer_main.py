import tkinter as tk
from tkinter import ttk
from synchronizer_func import synchronize as snz

def synchronize_sub():
	file_name = file_name_var.get()
	if file_name == '':
		print('FILE NAME IS EMPTY')
	if time_var.get() == '':
		print('TIME INPUT IS EMPTY')
	time_millis = int(time_var.get())
	new_file_name = file_name.split('.srt')[0] + '_synced' + '.srt'
	snz(file_name, new_file_name, time_millis)
	if '_synced_' in file_name:
	    os.remove(file_name)
	    os.rename(new_file_name, file_name)
	output_text.delete('1.0', 'end')
	output_text.insert(tk.END, "Subtitle synchronized successfully!", 'center')
	output_text.pack(padx=10, pady=(0, 10))

root = tk.Tk()
root.title('Subititle Synchronizer')

file_input_frame = ttk.Frame(root, padding=10)
file_input_frame.pack()

file_input_label = ttk.Label(file_input_frame, text='File Name (with path) ')
file_input_label.pack(side='left')

file_name_var = tk.StringVar()
file_input_box = ttk.Entry(file_input_frame, width=50, textvariable=file_name_var)
file_input_box.pack(side='left')
file_input_box.focus()

time_input_frame = ttk.Frame(root, padding=10)
time_input_frame.pack()

time_input_label = ttk.Label(time_input_frame, text='Time milliseconds to delay ')
time_input_label.pack(side='left')

time_var = tk.StringVar()
time_input_box = ttk.Entry(time_input_frame, width=20, textvariable=time_var)
time_input_box.pack(side='left')

synchronize_button = ttk.Button(root, text='Synchronize', command=synchronize_sub)
synchronize_button.pack(pady=(0, 10))

output_text = tk.Text(root, height=1, width=35, font=('Consolas', 20))
output_text.tag_config('center', justify='center')


root.mainloop()