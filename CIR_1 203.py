# Question 1:BANK TRANSACTION
import numpy as np

# Simulated transaction volumes (rows: branches, columns: months)
transactions = np.array([
    [1200, 1350, 1100, 1450, 1600, 1700],  # Branch 1
    [1000, 1250, 1300, 1400, 1500, 1550],  # Branch 2
    [900, 950, 1000, 1100, 1200, 1300],    # Branch 3
    [1500, 1600, 1700, 1800, 1900, 2000]   # Branch 4
])

 # calculating total transaction per branch
total_per_branch = np.sum(transactions, axis=1)
print("Total transaction per branch",total_per_branch)

# branch with the highest transaction
highest_branch_index = np.argmax(total_per_branch)
print("Branch with the highest transaction:",highest_branch_index + 1)   # Branch numbering starts from 1

# Average monthly transaction volume
average_monthly_volume = np.mean(transactions, axis=0)
print("Average monthly transaction volume:",average_monthly_volume)
# Reshaping the array to 3*8
reshaped = transactions.reshape(3, 8)
print("A reshaped array (3*8):\n",reshaped)
# Implications:
#
# The original shape was (4, 6) = 24 elements.
#
# Reshaping to (3, 8) still preserves all 24 elements but alters the structure.
#
# Rows and columns no longer represent branches and months directly.
#
# This format might be useful for different analytical purposes (e.g., feeding into a machine learning model), but semantic meaning is lost unless carefully tracked.