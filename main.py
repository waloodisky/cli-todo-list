import os
import sys

def clear(): #clears the terminal
	if os.name == "nt":
		os.system("cls")
	if os.name == "posix":
		os.system("clear")

def add(text): #adds a task (add <text of task>)
	with open("todo.txt","a") as file:
		file.write(text+"\n")
		
def remove(task): #removes a task (remove <number of task>)
	with open("todo.txt","r") as file:
		tasks=file.readlines()
		tasks.pop(task)
	with open("todo.txt","w") as file:
		file.writelines(tasks)
		
def removeall(): #removes all tasks (remove all)
	with open("todo.txt","w") as file:
		file.write("")
		
def mark(number): #marks a task (mark <number of task>)
	with open("todo.txt","r") as file:
		tasks=file.readlines()
		if tasks[number].startswith("[MARKED]"):
			return
		marked = "[MARKED]"+ tasks[number]
		tasks.pop(number)
		tasks.insert(0,marked)
	with open("todo.txt","w") as file:
		file.writelines(tasks)
		
def unmark(number): #unmarks a task (unmark <numbrer of task>)
	with open("todo.txt","r") as file:
		tasks=file.readlines()
		if tasks[number].startswith("[MARKED]"):
			with open("todo.txt","w") as file:
				unmarked = tasks[number][8:]
				tasks.pop(number)
				tasks.append(unmarked)
				file.writelines(tasks)
			
		
def main(): #the main fuction
	with open("todo.txt","r") as file:
		tasks = file.readlines()
	clear() #clears previous frames
	if not tasks: #if no tasks exist
		commands=input("")
		if commands.split()[0] == "add":
			try:
				add(commands[4:])
			except IndexError:
				pass
	else: #if tasks do exist
		with open("todo.txt","r") as file:
			tasks = file.readlines()
		for number, task in enumerate(tasks): #printing tasks
			if task.startswith("[MARKED]"):		
				print(f"{number+1}. {task[8:].rstrip()} ☑\n")
			else:
				print(f"{number+1}. {task}")
		commands=input("""
""") #user input
		if commands: #if input exists process it
			match commands.split()[0]:
				case "add": #adding a task
					try:
						add(commands[4:])
					except (IndexError,ValueError):
						pass
				case "remove": #removing a task/all tasks
					try:
						if commands.split()[1] == "all":
							removeall()
						else:
							remove(int(commands.split()[1])-1)
					except (IndexError,ValueError):
						pass
				case "mark": #marking a task
					try:
						if int(commands.split()[1]) > 0:
							mark(int(commands.split()[1])-1)
					except (IndexError,ValueError):
						pass
				case "unmark": #unmarking a task
					try:
						if int(commands.split()[1]) > 0:
							unmark(int(commands.split()[1])-1)
					except (IndexError,ValueError):
						pass
				case "quit"|"exit"|"close"|"leave": #closing the program
					clear()
					sys.exit()

while True:
	main()
