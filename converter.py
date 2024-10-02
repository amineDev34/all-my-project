#convertisseur temperature
choice = input (" type 'C' to convert from celsius to fahrenheit, or 'F' to convert from fahrenheit to celsius ")

if choice == 'C':
    celsius = float ( input ("enter the temperature in celsius : ") ) 
    fahrenheit = ( celsius * 9/5 ) + 32
    print (f"{celsius}c° is equal to {fahrenheit}°F" ) 

elif choice == 'F' :
    fahrenheit = float( input ("enter the temperature in fahrenheit : "))
    celsius = (fahrenheit - 32 ) * 5/9 
    print ( f"{fahrenheit}°F is equal to {celsius}c°") 

else:
    print ( "invalid choice, please enter 'c' or 'F' " )
             
