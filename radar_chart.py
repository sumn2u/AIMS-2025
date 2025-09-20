# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Data
# data = {
#     "MobileNet-TL": {"Inference Time": 0.1645, "RSS Memory": 0.011719, "Peak Memory": 0.19, "Model Size": 14.71},
#     "YOLO-v8": {"Inference Time": 0.0316, "RSS Memory": 0.0, "Peak Memory": 1.19, "Model Size": 6.5},
#     "YOLO-v11n": {"Inference Time": 0.0375, "RSS Memory": 0.0125, "Peak Memory": 1.63, "Model Size": 5.42},
#     "EfficientNetV2M-TL": {"Inference Time": 0.2217, "RSS Memory": 0.0125, "Peak Memory": 0.25, "Model Size": 216.03},
#     "EfficientNetV2S-TL": {"Inference Time": 0.206, "RSS Memory": 0.25, "Peak Memory": 0.22, "Model Size": 84.31},
#     "ResNet101-TL": {"Inference Time": 0.2233, "RSS Memory": 0.0, "Peak Memory": 0.21, "Model Size": 174.56},
#     "ResNet50-TL": {"Inference Time": 0.1904, "RSS Memory": -0.013281, "Peak Memory": 0.18, "Model Size": 97.91},
# }

# df = pd.DataFrame(data).T

# # Normalize values (0-1 scale for radar chart)
# df_norm = (df - df.min()) / (df.max() - df.min())

# # Radar chart setup
# labels = df_norm.columns
# num_vars = len(labels)

# angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
# angles += angles[:1]  # complete the loop

# fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# for model, row in df_norm.iterrows():
#     values = row.tolist()
#     values += values[:1]
#     ax.plot(angles, values, label=model)
#     ax.fill(angles, values, alpha=0.1)

# ax.set_xticks(angles[:-1])
# ax.set_xticklabels(labels, fontsize=10)
# ax.set_yticklabels([])
# ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# plt.title("Model Performance Comparison (Normalized)", size=14, weight="bold")
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Data
# data = {
#     "MobileNet-TL": {"Inference Time": 0.1645, "RSS Memory": 0.011719, "Peak Memory": 0.19, "Model Size": 14.71},
#     "YOLO-v8": {"Inference Time": 0.0316, "RSS Memory": 0.0, "Peak Memory": 1.19, "Model Size": 6.5},
#     "YOLO-v11n": {"Inference Time": 0.0375, "RSS Memory": 0.0125, "Peak Memory": 1.63, "Model Size": 5.42},
#     "EfficientNetV2M-TL": {"Inference Time": 0.2217, "RSS Memory": 0.0125, "Peak Memory": 0.25, "Model Size": 216.03},
#     "EfficientNetV2S-TL": {"Inference Time": 0.206, "RSS Memory": 0.25, "Peak Memory": 0.22, "Model Size": 84.31},
#     "ResNet101-TL": {"Inference Time": 0.2233, "RSS Memory": 0.0, "Peak Memory": 0.21, "Model Size": 174.56},
#     "ResNet50-TL": {"Inference Time": 0.1904, "RSS Memory": -0.013281, "Peak Memory": 0.18, "Model Size": 97.91},
# }

# df = pd.DataFrame(data).T

# # Normalize values (0-1 scale for radar chart)
# # Reverse normalization for 'Inference Time' and 'Model Size' because smaller is better
# df_norm = (df - df.min()) / (df.max() - df.min())
# df_norm['Inference Time'] = 1 - df_norm['Inference Time']
# df_norm['Model Size'] = 1 - df_norm['Model Size']

# # Radar chart setup
# labels = df_norm.columns
# num_vars = len(labels)

# angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
# angles += angles[:1]  # complete the loop

# # Stylish plot setup
# plt.style.use('seaborn-v0_8-darkgrid')
# fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# # Set a stylish background color
# ax.set_facecolor('#fafafa')

# # Colors for models
# colors = plt.colormaps['Paired']

# # Plot each model
# for i, (model, row) in enumerate(df_norm.iterrows()):
#     values = row.tolist()
#     values += values[:1]
#     ax.plot(angles, values, label=model, color=colors(i), marker='o', markersize=8, linewidth=2)
#     ax.fill(angles, values, alpha=0.1, color=colors(i))

# # Improve axes labels and grid
# ax.set_xticks(angles[:-1])
# ax.set_xticklabels(labels, fontsize=12, fontweight='bold', color='darkslategray')
# ax.tick_params(axis='x', pad=20)
# ax.set_yticklabels([])

# # Make grid lines more subtle
# ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# # Add a professional title
# plt.title("Model Performance Comparison (Normalized)", size=18, fontweight="bold", color='black', pad=30)

# # Improve legend
# ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize='large', frameon=False)

# # Optional: Add a subtle outer border
# fig.patch.set_facecolor('white')

# plt.tight_layout()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    "MobileNet-TL": {"Inference Time": 0.1645, "RSS Memory": 0.011719, "Peak Memory": 0.19, "Model Size": 14.71},
    "YOLO-v8": {"Inference Time": 0.0316, "RSS Memory": 0.0, "Peak Memory": 1.19, "Model Size": 6.5},
    "YOLO-v11n": {"Inference Time": 0.0375, "RSS Memory": 0.0125, "Peak Memory": 1.63, "Model Size": 5.42},
    "EfficientNetV2M-TL": {"Inference Time": 0.2217, "RSS Memory": 0.0125, "Peak Memory": 0.25, "Model Size": 216.03},
    "EfficientNetV2S-TL": {"Inference Time": 0.206, "RSS Memory": 0.25, "Peak Memory": 0.22, "Model Size": 84.31},
    "ResNet101-TL": {"Inference Time": 0.2233, "RSS Memory": 0.0, "Peak Memory": 0.21, "Model Size": 174.56},
    "ResNet50-TL": {"Inference Time": 0.1904, "RSS Memory": -0.013281, "Peak Memory": 0.18, "Model Size": 97.91},
}

df = pd.DataFrame(data).T

# Normalize values (0-1 scale for radar chart)
# Reverse normalization for 'Inference Time' and 'Model Size' because smaller is better
df_norm = (df - df.min()) / (df.max() - df.min())
df_norm['Inference Time'] = 1 - df_norm['Inference Time']
df_norm['Model Size'] = 1 - df_norm['Model Size']

# Radar chart setup
labels = df_norm.columns
num_vars = len(labels)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # complete the loop

# Stylish plot setup
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Set a stylish background color
ax.set_facecolor('#fafafa')

# Use a different colormap for better contrast
colors = plt.colormaps['viridis']

# Plot each model with thicker lines and markers
for i, (model, row) in enumerate(df_norm.iterrows()):
    values = row.tolist()
    values += values[:1]
    ax.plot(angles, values, label=model, color=colors(i/len(df_norm.index)), marker='o', markersize=4, linewidth=1.5)
    ax.fill(angles, values, alpha=0.1, color=colors(i/len(df_norm.index)))

# Improve axes labels and grid
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=11, fontweight='bold', color='darkslategray')
ax.tick_params(axis='x', pad=25)  # Increased padding
ax.set_yticklabels([])

# Make grid lines more subtle
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Add a professional title
plt.title("Model Performance Comparison (Normalized)", size=18, fontweight="bold", color='black', pad=30)

# Improve legend
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize='large', frameon=False)

plt.tight_layout()

plt.savefig('model_performance.png')

# Display the plot
plt.show()