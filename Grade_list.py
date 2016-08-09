from tkinter import*

window = Tk()
window.title("Grade")


name_frame = Frame(window)	
name_frame.grid(row =0, column =0, sticky = NW)

grade_frame = Frame(window)
grade_frame.grid(row =0, column =1, sticky = E)

button_frame = Frame(window)
button_frame.grid(row = 1 ,columnspan = 2 ,  sticky = S)

data_frame = Frame(window)
data_frame.grid(row = 2, columnspan = 2, sticky = S)

Label(name_frame, text = '이름: ').grid(row=0, column = 0, sticky = W)
entry1 = Entry(name_frame, width = 20, bg = "light green" )
entry1.grid(row =0, column = 1, sticky = W)


Label(grade_frame, text = '점수: ').grid(row=0, column = 0, sticky = E)
entry2 = Entry(grade_frame , width = 7, bg = "light green")
entry2.grid(row = 0, column = 1, sticky= W)

Label(grade_frame, text = '번호: ').grid(row=1, column = 0, sticky = E)
entry3 = Entry(grade_frame, width = 5, bg = "light green")
entry3.grid(row =1, column = 1, sticky = W)

Label(grade_frame, text = '파일이름: ').grid(row=2, column = 0, sticky = E)
entry4 = Entry(grade_frame, width = 20, bg = "light blue")
entry4.grid(row =2, column = 1, sticky = W)

Label(grade_frame, text = '파일이름: ').grid(row=3, column = 0, sticky = E)
entry5 = Entry(grade_frame, width = 20, bg = "light blue")
entry5.grid(row =3, column = 1, sticky = W)

output1 = Text(data_frame, width = 75, height = 10, bg = "light yellow")
output1.grid(row = 0, sticky = S)
output2 = Text(data_frame, width = 75,height = 1, bg = "pink")
output2.grid(row = 1, sticky = S)

button_list1 = ["추가", "삭제", "저장", "열기"]
button_list2 = ["번호순", "이름순", "점수내림차순", "점수오름차순"]

def click(key):
	output2.delete(1.0, END)
	if key == "번호순":
		output2.insert(END, "번호순으로 정렬")
		S_sort(key)
	elif key == "이름순":
		output2.insert(END, "이름순으로 정렬")
		S_sort(key)
	elif key == "점수내림차순":
		output2.insert(END, "점수 내림차순으로 정렬")
		S_sort(key)
	elif key == "점수오름차순":
		output2.insert(END, "점수 오름차순으로 정렬")
		S_sort(key)
	elif key == "추가":
		output2.insert(END, "추가")
		S_insert()
	elif key == "삭제":
		S_delete()
		output2.insert(END, "성공적으로 삭제 하였습니다.")
	elif key == "저장":
		S_save()
	elif key == "열기":
		S_open()

r=0; c = 0
for button in button_list1:
	
	def cmd(x = button):
		click(x)
	Button(grade_frame,text = button, width = 5, command = cmd).grid(row = r, column = 2)
	r = r+1
	
for button in button_list2:
	
	def cmd(x = button):
		click(x)
	if c == 0 or c == 1:
		Button(button_frame, text = button, width=5, command = cmd).grid(row = 0, column = c)
	elif c == 2 or c == 3:
		Button(button_frame, text = button, width=15, command = cmd).grid(row = 0, column = c)
	c= c+1


S_list  = []
def S_insert():
	res = err_msg()
	if entry1.get() == '' or res == 0:
		output2.delete(1.0, END)
		output2.insert(END, "추가 실패")
	elif entry2.get() == '':
		output2.delete(1.0, END)
		output2.insert(END, "[추가 실패]")
	elif entry3.get() == '' or res == 0:
		output2.delete(1.0, END)
		output2.insert(END, "[추가 실패]")
	else:
		sname = entry1.get()
		grade = entry2.get()
		snum = entry3.get()
		entry1.delete(0, END)
		entry2.delete(0, END)
		entry3.delete(0, END)
		S_list.append([snum, sname, grade])
		output2.delete(1.0, END)
		output2.insert(END, "성공적으로 추가하였습니다.")
	S_display()

def err_msg():
	S_name = entry1.get()
	S_num = entry3.get()
	res =1
	for line in S_list:
		if line[0] == S_num:
			res = 0
	for line in S_list:
		if line[1] == S_name:
			res =0	
	return res
	
def S_delete():
	snum = entry3.get()
	for line in S_list:
		if line[0] == snum:
			S_list.remove(line)
		else:
			output2.delete(1.0, END)
			output2.insert(END, "[삭제 실패] 존재하지 않는 번호입니다.")
	S_display()
	
def S_sort(K):
	if K == "번호순":
		S_list.sort(key = lambda x:x[0])
		S_display()
	elif K == "이름순":
		S_list.sort(key = lambda x: x[1])
		S_display()
	elif K == "점수오름차순":
		S_list.sort(key = lambda x: x[2])
		S_display()
	elif K == "점수내림차순":
		S_list.sort(key = lambda x: x[2], reverse = True)
		S_display()
		
def S_display():
	output1.delete(1.0, END)
	for line in S_list:
		output1.insert(END, line[0]+"	"+line[1]+"			"+line[2]+ '\n')

		
		
def S_save():
	file_name = entry4.get()
	data = open(file_name+'.pkl', 'w')
	for line in S_list:
		print(line[0]+"	"+line[1]+"	"+line[2], file = data)
	
	data.close()
	entry4.delete(0, END)
	output2.insert(END, "[파일 저장 완료] 파일이름: "+ file_name)
	
	
def S_open():
	file_name = entry5.get()
	data = open(file_name+'.pkl', 'r')
	while True:
		line = data.readline()
		if line == '':
			break
		a= line.split("	")[2]
		S_list.append([line.split("	")[0], line.split("	")[1],a[:len(a)-1] ])
		
	S_display()
	entry5.delete(0, END)
	output2.insert(END, "[파일 열기 성공] 파일이름: "+file_name)
			
window.mainloop()			
