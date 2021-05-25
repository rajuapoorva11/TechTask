Signant Health task 
        Instructions:
                1.To start Flask app
			Using the Flasy-master file. open a terminal in the same folder.
                        Install Python3 : sudo apt install python3.8
			Start Flask app on 127.0.0.1:8080 (Look into the readme file in the Flask app folder)
			 
       		2.Install Pycharm or a code editor of choice
                  Install required packages for Robotframework
		  Install Selenium Library, Requests Library, JSON Library, JSONPath Library.
	          Install Coverage for checking code coverage.
                  Under Code folder, open Locator.py'(TestDemo/Code/Locator.py) and add absolute path for 'Locators.json'(TestDemo/Data/Locator.json)
        Folders to run test cases :
        UI Test Automation using RobotFramework: 
       		- Path : TaskDemo/TestCases/UITestCases
                - Run UITestCases folder using command : robot -d --Results TestCases/UITestCases 
		- Results : TaskDemo/--results
        Unit Tests using python:
		- Path : TaskDemo/Tests/Unittest.py
                - Run Unit Test : Run python file Unittest.py
		- For coverge report run : coverage report -m Tests/Unittest.py
	API Tests using python:
		- Path : TaskDemo/Tests/APITest.py
                - Run Unit Test : Run python file APITest.py
		- For coverge report run : coverage report -m Tests/APITest.py



		  	
