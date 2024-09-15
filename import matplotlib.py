import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Drawing parameters
x_primary = 1
x_secondary = 6
y_offset = 0.8

# Drawing the exact equivalent circuit
# Primary Side
ax.plot([x_primary, x_primary + 1], [2, 2], 'k', lw=2)  # Wire from source to primary
ax.plot([x_primary, x_primary], [2, 3.5], 'k', lw=2)  # Vertical wire to resistance
ax.plot([x_primary, x_primary + 1.5], [3.5, 3.5], 'k', lw=2)  # Horizontal wire (Resistor)
ax.text(x_primary + 1.6, 3.5, r"$R_1$", fontsize=12, verticalalignment='center')

# Inductor (X1)
ax.plot([x_primary + 1.5, x_primary + 2.7], [3.5, 3.5], 'k', lw=2)  # Horizontal wire (Inductor)
ax.text(x_primary + 2.9, 3.5, r"$X_1$", fontsize=12, verticalalignment='center')

# Magnetizing Branch (Xm)
ax.plot([x_primary + 1.5, x_primary + 1.5], [3.5, 0.5], 'k--', lw=2)  # Vertical wire (Xm)
ax.plot([x_primary + 1.5, x_primary + 2.7], [0.5, 0.5], 'k--', lw=2)  # Horizontal wire (Rc)
ax.text(x_primary + 2.8, 0.5, r"$X_m$", fontsize=12, verticalalignment='center')

# Core Loss Resistance (Rc)
ax.plot([x_primary + 1.5, x_primary + 2.7], [2, 2], 'k--', lw=2)  # Wire for Rc
ax.text(x_primary + 2.8, 2, r"$R_c$", fontsize=12, verticalalignment='center')

# Secondary Side
ax.plot([x_secondary, x_secondary - 1], [2, 2], 'k', lw=2)  # Wire to secondary
ax.plot([x_secondary, x_secondary], [2, 3.5], 'k', lw=2)  # Vertical wire to resistance
ax.plot([x_secondary, x_secondary + 1.5], [3.5, 3.5], 'k', lw=2)  # Horizontal wire (Resistor)
ax.text(x_secondary + 1.6, 3.5, r"$R_2'$", fontsize=12, verticalalignment='center')

# Inductor (X2)
ax.plot([x_secondary + 1.5, x_secondary + 2.7], [3.5, 3.5], 'k', lw=2)  # Horizontal wire (Inductor)
ax.text(x_secondary + 2.9, 3.5, r"$X_2'$", fontsize=12, verticalalignment='center')

# Final Connection
ax.plot([x_secondary + 2.7, x_secondary + 4], [3.5, 3.5], 'k', lw=2)  # Final connection

# Labels
ax.text(x_primary - 0.5, 2, r"$V_1$", fontsize=12, verticalalignment='center')
ax.text(x_secondary + 4.2, 3.5, r"$V_2'$", fontsize=12, verticalalignment='center')

# Axis and display settings
ax.axis('off')
plt.title('Exact Equivalent Circuit of a Single-Phase Transformer', fontsize=14)
plt.show()
