1. Python is require to be installed in order to run todo test cases
2. remember to tick add path when install python, or can add python into environment path
	environment variable > system variable > path, BELOWS 3 ITEM NEED TO BE ADDED
	-D:\python\Scripts\ (my python is installed under D drive, so i put this path)
	-D:\python\ (my python is installed under D drive, so i put this path)
	-d:\uiautomation (this is the path) that i put my automation file
3. after python is installed, run bat file to install needed libraries
4. run command to execute robot --outputdir ../../reports/TodoApp -L trace -b debug.log -i "Todo" DemoTodo
	ensure your current folder is under cd your current directory to TodoTestcases before execute
	example , mine location is C:\Users\chien\OneDrive\Desktop\TodoTestcases under this folder have another folder name DemoTodo
	and inside DemoTodo folder there is 1 TodoDemo.py file and 1 TodoDemo.robot