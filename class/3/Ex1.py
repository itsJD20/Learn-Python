'''
Write a class named Monitor 
Attributes:
    brand: string 
        brand of the Monitor Ex: LG, Samsung, ....
    power: boolean
        stores True if power is on else False
    brightness: integer Between 1 to 100
        Stores the brightness
Methods:
    switchPower: 
        A method when called changes power to False if it was True and Vice Versa
    changeBrightness: Accepts newBrightness integer
        Changes the brightness to new brightness

Write a class named CPU
Attributes:
    brand: string 
        brand of the Monitor Ex: LG, Samsung, ....
    power: boolean
        stores True if power is on else False
    numberOfCoolers: integer
        stores the number of coolers in the CPU
    Temperature: integer
        stores temperature in F.
Methods:
    switchPower: 
        A method when called changes power to False if it was True and Vice Versa
    increaseTemp:
        A method to increse temperature by 1
        if temperature increases above 50, then switchPower to Off
    rest: Accepts an integer numberOfSeconds of rest 
        A method puts CPU power Off for numberOfSeconds and reduces the 
        temperature to 20 if number of Seconds > 20 else reduces the temperature by numberOfSeconds

Write a class named Computer
Attributes:
    brand: string 
        brand of the Monitor Ex: LG, Samsung, ....
    power: boolean
        stores True if power is on else False
    cpu: object of CPU class
    monitor: object of Monitor class
Methods:
    switchPower: 
        A method when called changes power to False if it was True and Vice Versa.
        Note: A computer is on only if both cpu and monitor is on
    doTask: accept an integer num
        This will print all prime numbers from 1 to num and the cpu will increaseTemp 
        after printing each prime number. CPU will rest after printing 20 prime numbers for 5s 
        and then start again 

'''