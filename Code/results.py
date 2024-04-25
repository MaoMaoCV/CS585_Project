import pandas as pd
import numpy as np

# Creating the data in a DataFrame
data = {
    "Pair": ["(1, 2)", "(1, 3)", "(1, 4)", "(1, 5)", "(1, 6)", "(1, 7)", "(1, 8)", "(1, 9)",
             "(2, 3)", "(2, 4)", "(2, 5)", "(2, 6)", "(2, 7)", "(2, 8)", "(2, 9)",
             "(3, 4)", "(3, 5)", "(3, 6)", "(3, 7)", "(3, 8)", "(3, 9)",
             "(4, 5)", "(4, 6)", "(4, 7)", "(4, 8)", "(4, 9)",
             "(5, 6)", "(5, 7)", "(5, 8)", "(5, 9)",
             "(6, 7)", "(6, 8)", "(6, 9)", "(7, 8)", "(7, 9)", "(8, 9)"],
    "Cosine Score 1": [0.8659, 0.8682, 0.7605, 0.8108, 0.8052, 0.8401, 0.7548, 0.8556,
                       0.8997, 0.8583, 0.8694, 0.8978, 0.8917, 0.8727, 0.8622,
                       0.8130, 0.8577, 0.8890, 0.8310, 0.8323, 0.9035,
                       0.9333, 0.8711, 0.8310, 0.8821, 0.7432,
                       0.9131, 0.8577, 0.8829, 0.7936,
                       0.8814, 0.8738, 0.8720, 0.8341, 0.7971, 0.7955],
    "Cosine Score 2": [0.8999, 0.8748, 0.8767, 0.8507, 0.8423, 0.8391, 0.8635, 0.8468,
                       0.8854, 0.9198, 0.8617, 0.8718, 0.8557, 0.8537, 0.7836,
                       0.8852, 0.8813, 0.9355, 0.8995, 0.8981, 0.8059,
                       0.8927, 0.8712, 0.8910, 0.8634, 0.8544,
                       0.8718, 0.8867, 0.8488, 0.8186,
                       0.8920, 0.8960, 0.7771, 0.8364, 0.8610, 0.7809],
    "Difference": [-0.0340, -0.0065, -0.1162, -0.0399, -0.0371, 0.0010, -0.1087, 0.0088,
                   0.0143, -0.0615, 0.0077, 0.0260, 0.0360, 0.0190, 0.0786,
                   -0.0722, -0.0236, -0.0465, -0.0685, -0.0658, 0.0976,
                   0.0406, -0.0001, -0.0600, 0.0187, -0.1112,
                   0.0413, -0.0290, 0.0341, -0.0250,
                   -0.0106, -0.0222, 0.0948, -0.0023, -0.0639, 0.0146]
}
df = pd.DataFrame(data)

groups = {
    "Within Group 1": ["(1, 2)", "(1, 3)", "(2, 3)"],
    "Within Group 2": ["(3, 4)", "(5, 3)", "(5, 4)"],
    "Within Group 3": ["(7, 8)", "(7, 9)", "(8, 9)"],
    "Group Setnece 1 with others": ["(1, 2)", "(1, 3)", "(1, 4)", "(1, 5)", "(1, 6)", "(1, 7)", "(1, 8)", "(1, 9)"],
    "Group Setnece 2 with others": ["(1, 2)", "(2, 3)", "(2, 4)", "(2, 5)", "(2, 6)", "(2, 7)", "(2, 8)", "(2, 9)"],
    "Group Setnece 3 with others": ["(3, 1)", "(3, 2)", "(3, 4)", "(3, 5)", "(3, 6)", "(3, 7)", "(3, 8)", "(3, 9)"]
}

# Function to calculate mean and standard deviation for a group
def calculate_stats(group, df):
    # Filtering the DataFrame for the specified group
    group_df = df[df['Pair'].isin(group)]
    # Calculating mean and standard deviation for Cosine Score 1 and 2
    mean_score1 = group_df['Cosine Score 1'].mean()
    std_score1 = group_df['Cosine Score 1'].std()
    mean_score2 = group_df['Cosine Score 2'].mean()
    std_score2 = group_df['Cosine Score 2'].std()
    return mean_score1, std_score1, mean_score2, std_score2

# Calculating stats for each group
stats = {group_name: calculate_stats(group, df) for group_name, group in groups.items()}
print(stats)