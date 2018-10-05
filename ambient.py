import RPi.GPIO as GPIO
import socket
import matplotlib.pyplot as plt

def sensordata():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    sensor=Adafruit_DHT.AM2302
    humidity,temperature=Adafruit_DHT.read_retry(sensor,17)
    return(humidity,temperature)

sock=socket.socket(socket.AF_INRT,socket.SOCK_DGRAM)
server_address=('address',portno)#put add and port no

try:
    while(1):
        h,t=sensordata()
        message=str(h)+','+str(t)
        print>>(sys.sterr,'Sending "%s" % message')
        sent=sock.sendto(message,server_address)

finally:
    print>>sys.stderr,'closing socket'
    sock.close()

def coverage_plot(data,i):
    hum=data.split(",")[0]
    tem=data.split(",")[1]
    print('temp'+(str(tem))+'iter'+(str(i)))
    plt.ion()
    fig=plt.figure(num=1,figsize=(6,6))
    plt.title("HUMIDITY AND TEMPERATURE")
    ax=fig.add_subplot(121)
    ax.plot(tem,i,c='r',marker=r'$\Theta$')
    plt.xlabel('Temp($^0 C$)')
    ax.grid()
    ax=fig.add_support_subplot(122)
    ax.plot(tem,i,c='b',marker=r'$\Phi$')
    plt.xlabel('Humidity($\%$)')
    ax.grid()
    fig.show()
    fig.canvas.draw()

sock=socket.socket(socket.AF_INRT,socket.SOCK_DGRAM)
server_address=('address',portno)#put add and port no
sock.bind(server_address)

i=0;
while True:
    data,address=sock.recvfrom(4096)
    with open("Filename.txt","a") as f:
        mess=str(data)
        f.write(mess)
        coverage_plot(mess,i)
        print mess
        i+=1
        f.close()
        
    

