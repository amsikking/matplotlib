import numpy as np
import matplotlib.pyplot as plt

# Data:
rows, cols = 3, 5
data = np.zeros((rows, cols))
data_string = [[str(col) for col in row] for row in data] # convert to string

# Plot:
fig, ax = plt.subplots()
ax.set_axis_off()                               # hide all axis components

# Adjust figure as needed: 6.4x4.8" is default:
fig.set_size_inches(6.4, 4.8)

# Add 'super' title that is centered:
plt.suptitle('Title')

# Make row and column labels and color arrays:
rlabels = ['  row%i  '%i for i in range(rows)]  # optionally pad with space
clabels = ['col%i'%i for i in range(cols)]
rcolors = ['0.8' for i in range(rows)]          # 0-1 float for gray level
ccolors = ['0.8' for i in range(cols)]

# optionally adjust column widths (values should sum to 1)
relative_widths = range(1, cols + 1)
cwidths = [w/sum(relative_widths) for w in relative_widths]

# Add a table under the hiden x axis:
tbl = ax.table(
    cellText=data_string,
    cellLoc='center',
    rowLabels=rlabels,
    rowLoc='center',
    rowColours=rcolors,
    colLabels=clabels,
    colLoc='center',
    colColours=ccolors,
    colWidths=cwidths,
    loc='center',
    )
tbl.scale(1, 1.5) # adjust cell padding (x, y)

# Optionally set font size:
##tbl.auto_set_font_size(False)
##tbl.set_fontsize(12)

plt.tight_layout(pad=1)
plt.savefig('table.png', dpi=150)
plt.show()
