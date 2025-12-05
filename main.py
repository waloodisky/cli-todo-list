import os
import sys

def add(text):
	with open("todo.txt","a") as file:
		file.write(text+"\n")
		
def remove(task):
	with open("todo.txt","r") as file:
		tasks=file.readlines()
		tasks.pop(task)
	with open("todo.txt","w") as file:
		file.writelines(tasks)
		
def removeall():
	with open("todo.txt","w") as file:
		file.write("")
		
def mark(number):
	with open("todo.txt","r") as file:
		tasks=file.readlines()
		if tasks[number].startswith("[MARKED]"):
			return
		marked = "[MARKED]"+ tasks[number]
		tasks.pop(number)
		tasks.insert(0,marked)
	with open("todo.txt","w") as file:
		file.writelines(tasks)
		
def unmark(number):
	with open("todo.txt","r") as file:
		tasks=file.readlines()
		if tasks[number].startswith("[MARKED]"):
			with open("todo.txt","w") as file:
				unmarked = tasks[number][8:]
				tasks.pop(number)
				tasks.append(unmarked)
				file.writelines(tasks)
			
		
def main():
	with open("todo.txt","r") as file:
		lines = file.readlines()
	os.system("clear")
	if not lines:
		commands=input("")
		if commands.split()[0] == "add":
			try:
				add(commands.split()[1])
			except IndexError:
				print("please use the following syntax: add <text>")
	else:
		with open("todo.txt","r") as file:
			lines = file.readlines()
		for number, task in enumerate(lines):
			if task.startswith("[MARKED]"):		
				print(f"{number+1}. {task[8:].rstrip()} ☑\n")
			else:
				print(f"{number+1}. {task}")
		commands=input("""
""")
		if commands:
			match commands.split()[0]:
				case "add":
					try:
						add(commands[4:])
					except (IndexError,ValueError):
						pass
				case "remove":
					try:
						if commands.split()[1] == "all":
							removeall()
						else:
							remove(int(commands.split()[1])-1)
					except (IndexError,ValueError):
						pass
				case "mark":
					try:
						if int(commands.split()[1]) > 0:
							mark(int(commands.split()[1])-1)
					except (IndexError,ValueError):
						pass
				case "unmark":
					try:
						if int(commands.split()[1]) > 0:
							unmark(int(commands.split()[1])-1)
					except (IndexError,ValueError):
						pass
				case "quit"|"exit":
					os.system("clear")
					sys.exit()

while True:
	main() 
