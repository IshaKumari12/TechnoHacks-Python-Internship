def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def main():
    print("Temperature Conversion Program")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    
    try:
        choice = int(input("Enter your choice (1/2): "))
        
        if choice == 1:
            f_temp = float(input("Enter temperature in Fahrenheit: "))
            c_temp = fahrenheit_to_celsius(f_temp)
            print(f"{f_temp:.2f} Fahrenheit is {c_temp:.2f} Celsius")
        elif choice == 2:
            c_temp = float(input("Enter temperature in Celsius: "))
            f_temp = celsius_to_fahrenheit(c_temp)
            print(f"{c_temp:.2f} Celsius is {f_temp:.2f} Fahrenheit")
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input. Please enter a valid choice and temperature.")

if __name__ == "__main__":
    main()