# ---------------------------------------------------------
# Program: Temperature Converter
# Task: 01 - SkillCraft Technology
# Author: Chethan S.
# Description: Converts temperatures between C, F, and K.
# ---------------------------------------------------------

def main():
    print("=======================================")
    print("TEMPERATURE CONVERTER")
    print("=======================================")

    while True:
        try:
            # 1. Get input value
            temp = float(input("\nEnter the temperature value: "))
            
            # 2. Get input unit
            print("Select the unit (C for Celsius, F for Fahrenheit, K for Kelvin)")
            unit = input("Unit: ").strip().upper()

            # 3. Perform Conversions
            if unit == 'C':
                f = (temp * 9/5) + 32
                k = temp + 273.15
                print(f"--- Results for {temp}°C ---")
                print(f"Fahrenheit: {f:.2f}°F")
                print(f"Kelvin:     {k:.2f}K")

            elif unit == 'F':
                c = (temp - 32) * 5/9
                k = c + 273.15
                print(f"--- Results for {temp}°F ---")
                print(f"Celsius: {c:.2f}°C")
                print(f"Kelvin:  {k:.2f}K")

            elif unit == 'K':
                c = temp - 273.15
                f = (c * 9/5) + 32
                print(f"--- Results for {temp}K ---")
                print(f"Celsius:    {c:.2f}°C")
                print(f"Fahrenheit: {f:.2f}°F")

            else:
                print("Error: Invalid unit. Please enter C, F, or K.")
                continue

            # 4. Ask to continue
            choice = input("\nDo you want to convert another value? (y/n): ").lower()
            if choice != 'y':
                print("Thank you for using the converter. Goodbye!")
                break

        except ValueError:
            print("Error: Please enter a valid numerical value.")

if __name__ == "__main__":
    main()
