from temperature.celsius import c_to_f, c_to_k
from temperature.farenheit import f_to_c
from temperature.kelvin import k_to_c

def main():
    print("Temprature Conversion Options :" )
    print("1. Celsius to Fahrenhite" )
    print("2. Fahrenhite to Celsius" )
    print("3. print Celsius to Kelvin" )

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1 :
        celsius = float(input("Enter temprature in Celsius : "))
        print(f"{celsius}  = {c_to_f(celsius)}C ")
    
    elif choice == 2 :
        fahrenhit = float(input("Enter temprature in Fahrenhit : "))
        print(f"{fahrenhit}  = {c_to_f(fahrenhit)}F ")
        
    elif choice == 1 :
        celsius = float(input("Enter temprature in Celsius : "))
        print(f"{celsius}  = {c_to_k(kelvin)}K ")

    else:
        print("Invalid choice")

main()
        