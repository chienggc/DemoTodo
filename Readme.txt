1. Python is require to be installed in order to run todo test cases
2. Please make sure to download latest chrome driver which is tally with chrome browser version
	and chromedriver.exe can slot under Scripts folder in python, for example : D:\python\Scripts
3. remember to tick add path when install python, or can add python into environment path
	environment variable > system variable > path, BELOWS 3 ITEM NEED TO BE ADDED
	-D:\python\Scripts\ (my python is installed under D drive, so i put this path)
	-D:\python\ (my python is installed under D drive, so i put this path)
	-d:\uiautomation (this is the path) that i put my automation file
4. after python is installed, run bat file to install needed libraries
5. run command to execute robot --outputdir ../../reports/TodoApp -L trace -b debug.log -i "Todo" DemoTodo-main
	ensure your current folder is under cd your current directory to DemoTodo-main before execute
	example , mine location is C:\Users\chien\OneDrive\Desktop\DemoTodo-main under this folder have another folder name DemoTodo-main
	and inside DemoTodo-main folder there is 1 TodoDemo.py file and 1 TodoDemo.robot
6. Test cases is written under TodoDemo.robot with Cucumber Gherkin format
