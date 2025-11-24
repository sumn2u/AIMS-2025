# import matplotlib.pyplot as plt
# import numpy as np

# # Updated model list
# models = [
#     'EfficientNetV2M', 'EfficientNetV2S', 'MobileNet', 'ResNet50', 'ResNet101',
#     'YOLO-11n', 'YOLO-8n'
# ]

# # Prepare Data emissions (kg CO₂)
# prepare_data = np.array([
#     0.0006707278, 
#     0.0002248349, 
#     0.0009992197, 
#     0.0010812484, 
#     0.0007863351,
#     0.0007320325,
#     0.0016524806
# ])

# # Develop Model emissions (kg CO₂)
# develop_model = np.array([
#     0.0557422935,
#     0.0197688407,
#     0.0392702831,
#     0.0852752304,
#     0.1084011005,
#     0.0490018958,
#     0.0654282921
# ])

# # Deploy Model emissions (for first image) — used in line plot
# deploy_model = np.array([
#     0.0582950112,
#     0.0204320201,
#     0.0409393206,
#     0.0875567535,
#     0.1107930351,
#     0.000001,
#     0.000003
# ])

# x = np.arange(len(models))
# width = 0.5

# # High-contrast colors
# colors = {
#     "prepare": "#FFA500",     # Bright Orange
#     "develop": "#0047AB",     # Deep Blue
#     "deploy": "#228B22"       # Forest Green
# }

# # Create plot
# fig, ax = plt.subplots(figsize=(12, 6))

# # Stacked bars for Prepare + Develop stages
# ax.bar(x, prepare_data, width, label='Prepare Data', color=colors["prepare"])
# ax.bar(x, develop_model, width, bottom=prepare_data, label='Develop Model', color=colors["develop"])

# # Line for Deploy Model (first image emissions)
# ax.plot(x, prepare_data + develop_model + deploy_model,
#         color=colors["deploy"], marker='o', linestyle='--', linewidth=2, label='Deploy Model')

# # Customize plot
# ax.set_xlabel('Model')
# ax.set_ylabel('Carbon Emission (kg CO₂)')
# ax.set_title('Carbon Emission by Stage for Each Model (20 Epochs)')
# ax.set_xticks(x)
# ax.set_xticklabels(models, rotation=45)
# ax.legend()

# # Clean styling
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.grid(False)

# plt.tight_layout()
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# # Model names
# models = [
#     'EffNetV2M', 'EffNetV2S', 'MobileNet',
#     'ResNet50', 'ResNet101', 'YOLO-11n', 'YOLO-8n'
# ]

# # Emissions in kg CO₂
# prepare = np.array([
#     0.0006707278, 0.0002248349, 0.0009992197,
#     0.0010812484, 0.0007863351, 0.0007320325, 0.0016524806
# ])
# develop = np.array([
#     0.0557422935, 0.0197688407, 0.0392702831,
#     0.0852752304, 0.1084011005, 0.0490018958, 0.0654282921
# ])
# deploy = np.array([
#     0.0582950112, 0.0204320201, 0.0409393206,
#     0.0875567535, 0.1107930351, 0.000001, 0.000003
# ])

# x = np.arange(len(models))
# width = 0.25

# # Colors for each stage
# colors = {
#     "prepare": "#F4A261",  # Orange
#     "develop": "#2A9D8F",  # Teal
#     "deploy": "#264653"    # Deep Gray-Blue
# }

# # Plot setup
# fig, ax = plt.subplots(figsize=(14, 7), dpi=120)

# # Grouped bars
# ax.bar(x - width, prepare, width, label='Prepare', color=colors['prepare'])
# ax.bar(x, develop, width, label='Develop', color=colors['develop'])
# ax.bar(x + width, deploy, width, label='Deploy', color=colors['deploy'])

# # Add annotations on top of bars
# for i in range(len(models)):
#     ax.text(x[i] - width, prepare[i] + 0.001, f'{prepare[i]:.1e}', ha='center', fontsize=10)
#     ax.text(x[i], develop[i] + 0.001, f'{develop[i]:.2f}', ha='center', fontsize=10)
#     ax.text(x[i] + width, deploy[i] + 0.001, f'{deploy[i]:.1e}', ha='center', fontsize=10)

# # Title and labels
# ax.set_title('Carbon Emission by Stage for Each Model', fontsize=20, fontweight='bold', pad=20)
# ax.set_ylabel('CO₂ Emissions (kg)', fontsize=14, fontweight='bold')
# ax.set_xticks(x)
# ax.set_xticklabels(models, fontsize=12, fontweight='bold', rotation=15)

# # Minimalist design (remove background)
# ax.set_facecolor('white')
# fig.patch.set_facecolor('white')
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)



# # Grid for readability
# ax.yaxis.grid(True, linestyle='--', alpha=0.3)
# ax.legend(fontsize=12, frameon=False)

# plt.tight_layout()
# # To export:
# # plt.savefig("carbon_emission_grouped_clean.svg", bbox_inches='tight', dpi=300)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Model names
models = [
    'EffNetV2M', 'EffNetV2S', 'MobileNet',
    'ResNet50', 'ResNet101', 'YOLO-11n', 'YOLO-8n', 'YOLOv8n-CBAM'
]

# Emissions in kg CO₂
prepare = np.array([
    0.0008878775, 0.0009977272, 0.0016833768,
    0.0013690235, 0.0008006676, 0.0011266289, 0.0012779421,
    0.0009241202
])
develop = np.array([
    0.0575157394, 0.0802748723, 0.0336183266,
    0.0847173574, 0.0700260162, 0.0846065945, 0.0613673131,
    0.0945778858
])
deploy = np.array([
    0.0603698626, 0.0827354819, 0.0359147953,
    0.0872453316, 0.0723765033, 0.000003, 0.000003,
    0.000001
])

x = np.arange(len(models))
width = 0.25

# Colors
colors = {
    "prepare": "#F4A261",
    "develop": "#2A9D8F",
    "deploy": "#264653"
}

fig, ax = plt.subplots(figsize=(14, 7), dpi=120)

# Grouped bars
ax.bar(x - width, prepare, width, label='Prepare', color=colors['prepare'])
ax.bar(x, develop, width, label='Develop', color=colors['develop'])
ax.bar(x + width, deploy, width, label='Deploy', color=colors['deploy'])

# Add annotations on top of bars
for i in range(len(models)):
    ax.text(x[i] - width, prepare[i] + 0.001, f'{prepare[i]:.1e}', ha='center', fontsize=10)
    ax.text(x[i], develop[i] + 0.001, f'{develop[i]:.2f}', ha='center', fontsize=10)
    ax.text(x[i] + width, deploy[i] + 0.001, f'{deploy[i]:.1e}', ha='center', fontsize=10)

# Format axes and labels
# Title and labels
ax.set_title('Carbon Emission by Stage for Each Model', fontsize=20, pad=20)
ax.set_ylabel('CO₂ Emissions (kg)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=12, rotation=15)
ax.set_facecolor('white')
fig.patch.set_facecolor('white')

# Clean design
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.yaxis.grid(False)

# Legend with box
legend = ax.legend(frameon=True, fontsize=12)
frame = legend.get_frame()
frame.set_edgecolor('black')
frame.set_linewidth(1.5)
frame.set_boxstyle('round,pad=0.5')
frame.set_alpha(0.9)

plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for suptitle
plt.savefig("carbon_emission_grouped_boxed_legend.svg", bbox_inches='tight', dpi=300)
plt.show()
