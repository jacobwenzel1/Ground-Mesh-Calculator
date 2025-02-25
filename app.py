def calculate_grid_spacing(total_wires, wire_length_ft, overhang_in):
    # Convert wire length to inches for consistency
    wire_length_in = wire_length_ft * 12
    
    # Subtract total overhang (both sides) from total length
    effective_length = wire_length_in - (2 * overhang_in)
    
    # Assume a roughly square grid to estimate horizontal and vertical wire counts
    horizontal_wires = int((total_wires + 1) // 2)  # Roughly half, rounded up
    vertical_wires = total_wires - horizontal_wires
    
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
    if vertical_wires > 0:
        # Start at the left edge after overhang
        for i in range(vertical_wires):
            position = overhang_in + (i * vertical_spacing)
            vertical_positions.append(position)
    
    # Prepare output
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
    
    # Add positions to output
    for i, pos in enumerate(vertical_positions, 1):
        output += f"  Vertical wire {i}: {pos:.2f} inches\n"
    
    return output

# Get user input
try:
    total_wires = int(input("Enter the total number of wires: "))
    wire_length_ft = float(input("Enter the length of each wire in feet: "))
    overhang_in = float(input("Enter the overhang length in inches: "))
    
    # Validate inputs
    if total_wires < 2:
        print("Error: You need at least 2 wires to form a grid.")
    elif wire_length_ft <= 0:
        print("Error: Wire length must be positive.")
    elif overhang_in < 0 or (overhang_in * 2) >= (wire_length_ft * 12):
        print("Error: Overhang must be non-negative and less than half the wire length.")
    else:
        # Calculate and display result
        result = calculate_grid_spacing(total_wires, wire_length_ft, overhang_in)
        print("\n" + result)

except ValueError:
    print("Error: Please enter valid numbers for all inputs.")