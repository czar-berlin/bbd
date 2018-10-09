# bbd
Built By Data Project


Update Log:

#1 >> Refreshed image on Raspberry Pi3 with a fresh install.

#2 >> Upgraded the python libraries for Python 2.7.13


#3 >> Changes in code:

0.0 Check for dependencies.  

3.1 Added new definition for automatic write of sensor data. 

3.2 Sensor csv file included. 

3.2.1 Please take care to save the file as a text csv while saving the file from LibreOffice etc. Maintain UTF-8     Encoding. 
          
          

#4 >> Visualization program:  *plotlib.py*

4.1 A simple code to visualize collected data real time. Edit the code tag ".title()" to change the title of the figure. 

4.2 Right now, each instance of the code just displays visualitzation of one sensor. You will have to copy the program and change the file name in the code to use it for multiple sensors.

4.3 The program displays only 60 records from the csv, larger records will take up more memory as it is continously redrawing the whole graph.

4.4 It waits for the csv to reach 60 values and then changes to a moving graph displaying only last 60 records. 

4.5 Dependecies:

4.5.1 Install matplotlib "sudo apt-get install python-matplotlib"
      
      
      
