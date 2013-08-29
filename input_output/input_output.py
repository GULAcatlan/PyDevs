#! /usr/local/bin/python3.3
""" 
    Author: Sinuhé Jaime Valencia a.k.a Sier <sierisimo@gmail.com>
    Description: Unicamente con fines educativos.
    Last_Update: 28/agosto/2013 12:34 a.m. 
    Last_Update_By: Sier
    
 """
# El modulo de sys sirve para System, y argv, es Arguments Values, representa, 
# los valores recibidos por el Systema para este programa
from sys import argv

def read_file(name):
    """Just Read a file and says if it was ok or not"""
    file = open(name,'r')
    if file.read :
    	print('Success')
    else:
        # Implementar otra manera de enviar mensaje, un 'try-catch' o un 'with' serian buenas opciones.
    	print('You suck')
    # you close the file, just in case...
    file.close()

def show_arguments():
	"""Checks for values in argv and prints them"""
	if len(argv) >= 2:
		i=0
		for a in argv:
			print("Argument {} is: {}".format(i,argv[i]))
			i = i + 1
        
read_file(input("Insert name file: "))
show_arguments()