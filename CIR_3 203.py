# QUESTION 3:TUPLE FOR A PATIENT
patient = ("John Doe", 45, "120/80", 72)

# patient age and heart rate
print("Age:", patient[1])
print("Heart Rate:", patient[3])

# 3. Why tuples are suitable for storing patient vitals
# Immutability: Tuples are immutable, which means once created, the data cannot be accidentally changed—ideal for preserving original medical records.
#
# Structured grouping: They allow grouping related data (like vitals) in a fixed order.
#
# Memory efficiency: Tuples use less memory than lists, which is beneficial when handling large datasets.
#
# Hashable: Tuples can be used as keys in dictionaries if needed, unlike lists.

# Convert to list, update heart rate, convert back to tuple
patient_list = list(patient)
patient_list[3] = 75  # Update heart rate
updated_patient = tuple(patient_list)

# tuple of 5 patients and their names
patients = (
    ("John Doe", 45, "120/80", 72),
    ("Jane Smith", 52, "130/85", 78),
    ("Ali Khan", 38, "110/70", 65),
    ("Maria Lopez", 60, "140/90", 80),
    ("David Kim", 29, "115/75", 70)
)

# Extract all names
names = [patient[0] for patient in patients]
print(names)
