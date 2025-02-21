# Author: Jacob Wenzel
# Date: 02.21.25
# File: app.py

# Objective:
# To determine ground grid mesh dimensions. Given inputs for 
# Wire length, number of wires, and overhand length, the output
# results in the dimensions needed.



def calculate_grid_dimensions():
    # Get user inputs
    num_wires = int(input("Enter the number of wires per side (horizontal and vertical): "))
    wire_length = float(input("Enter the length of each wire (in inches): "))
    overhang = float(input("Enter the overhang on each side (in inches): "))

    # Calculate total overhang (both sides)
    total_overhang = 2 * overhang

    # Total grid size (width and height)
    total_grid_size = wire_length + total_overhang

    # Inner grid size (distance from first to last intersection)
    inner_grid_size = wire_length

    # Number of spaces between wires (one less than number of wires)
    num_spaces = num_wires - 1

    # Spacing between wires (intersection to intersection)
    spacing = inner_grid_size / num_spaces if num_spaces > 0 else 0

    # Calculate wire positions (intersections relative to grid edge)
    wire_positions = []
    for i in range(num_wires):
        position = overhang + (i * spacing)
        wire_positions.append(position)

    # Output results
    print("\n--- Grid Dimensions ---")
    print(f"Total Grid Size: {total_grid_size:.2f} inches x {total_grid_size:.2f} inches")
    print(f"Inner Grid Size (first to last intersection): {inner_grid_size:.2f} inches x {inner_grid_size:.2f} inches")
    print(f"Spacing Between Wires: {spacing:.2f} inches")
    print(f"Overhang: {overhang:.2f} inches on each side")
    print(f"Number of Intersections: {num_wires} x {num_wires} = {num_wires * num_wires}")

    print("\n--- Wire Positions (Horizontal and Vertical) ---")
    for i, pos in enumerate(wire_positions, 1):
        print(f"Wire {i}: Intersection at {pos:.2f} inches (rod extends from {pos-overhang:.2f} to {pos-overhang+wire_length:.2f} inches)")

# Run the program
if __name__ == "__main__":
    print("Copper Mesh Grid Calculator")
    calculate_grid_dimensions()