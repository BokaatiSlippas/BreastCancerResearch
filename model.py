import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers

# Load your encoded data
df = pd.read_csv('metabric_encoded.csv')

# Identify numerical columns for input
numerical_columns = [
    'age_at_diagnosis', 'pten', 'tp53', 'tp53bp1', 'aurka', 
    'egfr', 'erbb2', 'rpgr', 'overall_survival'
]

# Identify encoded columns for INPUT (including pam50_encoded)
input_encoded_columns = ['pam50_encoded']  # This goes into X

# The target is cancer_type_detailed_encoded (this becomes y)
target_column = 'cancer_type_detailed_encoded'

# Extract numerical features for input
X_numerical = df[numerical_columns].values

# Extract and split INPUT encoded features into individual bits
X_input_encoded_bits = []
for col in input_encoded_columns:
    encoded_bits = df[col].apply(lambda x: [int(bit) for bit in x])
    encoded_array = np.array(encoded_bits.tolist())
    X_input_encoded_bits.append(encoded_array)

# Combine all INPUT features
X_combined = np.concatenate([X_numerical] + X_input_encoded_bits, axis=1)

# Prepare TARGET: Split cancer_type_detailed_encoded into bits
y_bits = df[target_column].apply(lambda x: [int(bit) for bit in x])
y = np.array(y_bits.tolist())  # This is already in one-hot format!

print(f"Input features shape: {X_combined.shape}")
print(f"Target shape: {y.shape}")
print(f"Number of output nodes: {y.shape[1]}")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X_combined, y, test_size=0.2, random_state=42
)

# Scale only the numerical features (first len(numerical_columns) features)
scaler = StandardScaler()
X_train[:, :len(numerical_columns)] = scaler.fit_transform(X_train[:, :len(numerical_columns)])
X_test[:, :len(numerical_columns)] = scaler.transform(X_test[:, :len(numerical_columns)])

# Print feature information
print(f"\nFeature structure:")
print(f"Numerical features: {len(numerical_columns)}")
print(f"PAM50 encoded bits: {X_input_encoded_bits[0].shape[1] if X_input_encoded_bits else 0}")
print(f"Total input nodes: {X_combined.shape[1]}")
print(f"Output nodes: {y.shape[1]}")