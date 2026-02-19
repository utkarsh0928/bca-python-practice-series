import os

# Your naming convention: prog_XX_name.py
# Based on your PDF content
program_names = {
    1: "hello_world", 2: "arithmetic", 3: "area_triangle", 
    4: "swap_variables", 5: "random_number", 6: "km_to_miles",
    7: "celsius_to_fahrenheit", 8: "display_calendar", 9: "quadratic_equation",
    10: "swap_no_temp"
}

def create_files(total_programs=141):
    for i in range(1, total_programs + 1):
        # Use name from dict if exists, else use 'program'
        name = program_names.get(i, f"program_{i}")
        filename = f"prog_{i:02d}_{name}.py"
        
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write(f'# Program {i}: {name.replace("_", " ").capitalize()}\n')
                f.write('# Part of the 140+ Daily Python Challenge\n')
            print(f"Created: {filename}")

if __name__ == "__main__":
    create_files()