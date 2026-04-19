# Temperature Converter

A simple Python program that converts temperatures between Celsius, Fahrenheit, and Kelvin scales.

## Overview

This is a task from **SkillCraft Technology (SCT)** that demonstrates basic temperature conversion between three temperature scales with an interactive user interface.

**Author:** Chethan S.

## Features

- ✅ Convert from **Celsius** to Fahrenheit and Kelvin
- ✅ Convert from **Fahrenheit** to Celsius and Kelvin
- ✅ Convert from **Kelvin** to Celsius and Fahrenheit
- ✅ User-friendly interactive interface
- ✅ Input validation with error handling
- ✅ Results displayed with 2 decimal precision
- ✅ Option to perform multiple conversions in one session

## Requirements

- Python 3.x

## How to Run

1. Navigate to the project directory:
   ```bash
   cd d:\SCT_SD_task_1
   ```

2. Run the script:
   ```bash
   python temperature_converter.py
   ```

3. Follow the on-screen prompts:
   - Enter a temperature value
   - Specify the unit (C, F, or K)
   - View the converted temperatures
   - Choose to convert another value or exit

## Conversion Formulas

### Celsius to Fahrenheit and Kelvin
- **°F = (°C × 9/5) + 32**
- **K = °C + 273.15**

### Fahrenheit to Celsius and Kelvin
- **°C = (°F - 32) × 5/9**
- **K = °C + 273.15**

### Kelvin to Celsius and Fahrenheit
- **°C = K - 273.15**
- **°F = (°C × 9/5) + 32**

## Example Usage

```
=======================================
TEMPERATURE CONVERTER
=======================================

Enter the temperature value: 0
Select the unit (C for Celsius, F for Fahrenheit, K for Kelvin)
Unit: C
--- Results for 0.0°C ---
Fahrenheit: 32.00°F
Kelvin:     273.15K

Do you want to convert another value? (y/n): n
Thank you for using the converter. Goodbye!
```

## Error Handling

The program includes error handling for:
- Invalid numerical input
- Invalid temperature unit selection
- Graceful exit options

## License

This project is part of SkillCraft Technology Task 01.
