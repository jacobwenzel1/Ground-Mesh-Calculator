# Author: Jacob Wenzel
# Date: 02.21.25
# File: app.py

# Objective:
# To determine ground grid mesh dimensions. Given inputs for 
# Wire length, number of wires, and overhand length, the output
# results in the dimensions needed.

import matplotlib.pyplot as plt
import os
import sys

def calculate_grid_spacing(total_wires, wire_length_ft, overhang_in):
    # Convert wire length to inches for consistency
    wire_length_in = wire_length_ft * 12
    
    # Calculate effective length after overhang
    effective_length = wire_length_in - (2 * overhang_in)
    
    # Additional validation
    if effective_length <= 0:
        raise ValueError("Effective length (wire length minus total overhang) must be positive.")
    
    # Assume a roughly square grid to estimate horizontal and vertical wire counts
    horizontal_wires = int((total_wires + 1) // 2)  # Roughly half, rounded up
    vertical_wires = total_wires - horizontal_wires
    
    if vertical_wires < 1 or horizontal_wires < 1:
        raise ValueError("Not enough wires to form a grid (need at least 1 horizontal and 1 vertical).")
    
    # Calculate spacing between wires (in inches)
    if horizontal_wires > 1:
        horizontal_spacing = effective_length / (horizontal_wires - 1)
    else:
        horizontal_spacing = 0  # No spacing if only 1 wire
    
    if vertical_wires > 1:
        vertical_spacing = effective_length / (vertical_wires - 1)
    else:
        vertical_spacing = 0  # No spacing if only 1 wire
    
    # Calculate positions of vertical wires along the top horizontal wire
    vertical_positions = []
    for i in range(vertical_wires):
        position = overhang_in + (i * vertical_spacing)
        vertical_positions.append(position)
    
    # Prepare text output
    output = (
        f"Grid Layout Summary:\n"
        f"Total Wires: {total_wires}\n"
        f"Wire Length: {wire_length_ft} feet\n"
        f"Overhang per side: {overhang_in} inches\n"
        f"Horizontal Wires: {horizontal_wires}\n"
        f"Vertical Wires: {vertical_wires}\n"
        f"Spacing between horizontal wires: {horizontal_spacing:.2f} inches\n"
        f"Spacing between vertical wires: {vertical_spacing:.2f} inches\n"
        f"Vertical wire positions along top horizontal wire (from left edge):\n"
    )
    
    for i, pos in enumerate(vertical_positions, 1):
        output += f"  Vertical wire {i}: {pos:.2f} inches\n"
    
    # Generate image
    plt.figure(figsize=(10, 2))
    plt.plot([0, wire_length_in], [0, 0], 'b-', linewidth=2, label='Top Horizontal Wire')
    for pos in vertical_positions:
        plt.plot([pos, pos], [-0.5, 0.5], 'r-', linewidth=2)
        plt.text(pos, 0.6, f'{pos:.2f} in', ha='center', va='bottom', fontsize=8)
    
    # Add overhang markers
    plt.plot([overhang_in, overhang_in], [-0.3, 0.3], 'g--', label='Overhang Boundary')
    plt.plot([wire_length_in - overhang_in, wire_length_in - overhang_in], [-0.3, 0.3], 'g--')
    
    plt.title("Top Horizontal Wire with Vertical Wire Positions", pad=15)
    plt.xlabel("Distance (inches)")
    plt.yticks([])
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.tight_layout(pad=2.0)
    
    # Save and open the image
    image_path = "grid_layout.png"
    try:
        plt.savefig(image_path)
    except Exception as e:
        raise RuntimeError(f"Failed to save image: {e}")
    finally:
        plt.close()  # Ensure plot is closed even if save fails
    
    try:
        if os.name == 'nt':  # Windows
            os.startfile(image_path)
        elif os.name == 'posix':  # MacOS or Linux
            opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
            os.system(f"{opener} {image_path}")
    except Exception as e:
        output += f"\nImage saved as '{image_path}' but could not be opened automatically: {e}"
    else:
        output += f"\nImage saved and opened as '{image_path}'."
    
    return output

# Get and validate user input
try:
    total_wires = int(input("Enter the total number of wires: "))
    if total_wires <= 0:
        raise ValueError("Total number of wires must be a positive integer.")
    
    wire_length_ft = float(input("Enter the length of each wire in feet: "))
    if wire_length_ft <= 0:
        raise ValueError("Wire length must be a positive number.")
    
    overhang_in = float(input("Enter the overhang length in inches: "))
    if overhang_in < 0:
        raise ValueError("Overhang length cannot be negative.")
    if (overhang_in * 2) >= (wire_length_ft * 12):
        raise ValueError("Total overhang (both sides) must be less than the wire length.")
    
    # Calculate and display result
    result = calculate_grid_spacing(total_wires, wire_length_ft, overhang_in)
    print("\n" + result)

except ValueError as ve:
    print(f"Error: {ve}")
except RuntimeError as re:
    print(f"Error: {re}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")