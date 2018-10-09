import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd

style.use('fivethirtyeight')

##print (data[0])
##print (data[1])

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

while True:
    data_raw= pd.read_csv("/home/pi/Data/Sensor_4.csv", sep=",", header=None)
    data_len = len(data_raw[0])
    
    
    
    if data_len<=60:
        def animate(i):
            data = pd.read_csv("/home/pi/Data/Sensor_4.csv", sep=",", header=None)
            data[0] = pd.to_datetime(data[0])
            ax1.clear()
            ax1.plot(data[0],data[1])
            plt.xlabel("Time")
            plt.ylabel("Lux - Level")
            plt.title("SensorTag - Surya's Table")

        ani=animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()
    
    else:
        def animate(i):
            data = pd.read_csv("/home/pi/Data/Sensor_4.csv", sep=",", header=None)
            data[0] = pd.to_datetime(data[0])
            ax1.clear()
            ax1.plot(data[0][-60:],data[1][-60:])
            plt.xlabel("Time")
            plt.ylabel("Lux - Level")
            plt.title("SensorTag - Surya's Table")

        ani=animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()
        
