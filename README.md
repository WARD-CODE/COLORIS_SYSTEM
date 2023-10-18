# COLORIS_SYSTEM
COLORIS SYSTEM a User Interface controlling an Automated Slide Stainer machine
### Preview : 
#### General view
![379657178_980253449758114_1191519280434551168_n](https://github.com/WARD-CODE/COLORIS_SYSTEM/assets/79150916/ea986189-6438-4630-a6c1-76404a212dc5)
#### 1- The main view:
![379983103_173728732433425_4874515797779040628_n](https://github.com/WARD-CODE/COLORIS_SYSTEM/assets/79150916/901a58b9-7063-4c76-965c-a9112a3e650d)
#### 2- Programming Bloc view:
![379630217_332722602456791_7770231704634318623_n](https://github.com/WARD-CODE/COLORIS_SYSTEM/assets/79150916/6ac8b10e-98dd-4460-b801-890c4dea7bc0)
#### 3- Configuration Bloc view:
![379931415_2020022301693270_6763865489431514855_n](https://github.com/WARD-CODE/COLORIS_SYSTEM/assets/79150916/59bbbd84-a543-4379-b1c9-c2208d2fe177)

#### Description:
The Coloration Automate System is one of the important systems used in the Medical Fields, it provides staining flexibility allowing simultaneous 
and automatic staining of various 30-slide racks with identical or different staining protocols.

#### THE IHM (User interface) Section
This UI Control System consists of 3 main parts:
##### 1- the main window:
the main window permit to the user to manipulate the process of the Automate including Running the process, Interuption, and Restart. 
Visualizing each step and timing module and be able to enter the program and configure the system.
##### 2- the program bloc window:
this window is focused on the program(include timers) that should the machine follow to complet the process, it allows you to add a new program, modefy an existing one and select.
##### 3- the configuration bloc window:
this last window allow the user to interact with the machine manually and configure each axe independenly before starting the process.

#### THE Hardware (User interface) Section
##### 1- the Microcontroller board:
In our System we are using Orange Pi LTS 3 microcontroller(raspberry-like) to control and to display the system regarding its ability to display a modern UI and
to manipulate the hardware part.
##### 2- the Stepper motor driver board :
we used TB6600 as a motor driver relating to it's flexibility and adaptation with high current.
##### 3- the Stepper motors:
we have chosen NEMA 17 as  Stepper motor to control the main axes of the robot.
##### 4- Sensors:
the main sensors used in the system are : 
a- position tracking sensor (PhotoTransistor sensor F249)
b- start/end detector (4 limit switches "2 for each axe")
c- temperature and humidity sensor( DHT11)
##### 5- wiring and power supply:
in our case we used Jumpers for wiring and 12V power supply with a converter to 5V.
##### 6- Screen Touch:
we worked with a 5 inch Screen touch which is flexible and has a nice view.

#### Python Modules and Packages:
1 - Tkinter library
2 - Pillow library
3 - Threading library
4 - datetime library
5 - CSV library
6 - Os and subprocess Library
and others...

