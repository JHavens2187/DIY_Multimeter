import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

# Define the parameters
threshold_voltage = 2.5  # Ideal threshold voltage
transistor_drop = 0.7    # Voltage drop across base-emitter junction of the transistor
adjusted_threshold = threshold_voltage + transistor_drop  # Adjusted threshold voltage
noise_std_dev = 0.1      # Standard deviation of noise (voltage fluctuation)
voltages = np.linspace(2.3, 4, 400)  # Range of voltages around the threshold

# Calculate the error function for reading HIGH
prob_high = 0.5 * (1 + erf((voltages - adjusted_threshold) / (noise_std_dev * np.sqrt(2))))
# Combined error rate: false positive below threshold, false negative above threshold
error_rate = np.where(voltages < adjusted_threshold, prob_high, 1 - prob_high)

# Update to use a dark background
plt.style.use('dark_background')
plt.rcParams.update({
    "text.usetex": True,
    "font.sans-serif": ["Helvetica"],
    "axes.facecolor": '#1c1c1c',
    "figure.facecolor": '#1c1c1c',
    "axes.edgecolor": 'white',
    "xtick.color": 'white',
    "ytick.color": 'white',
    "grid.color": 'grey',
})

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the combined error rate with the transistor's effect
ax.plot(voltages, error_rate, label=r'Error Rate with Transistor Effect', color='orange', linestyle='-', linewidth=2, alpha=0.7)

# Customize the plot aesthetics
ax.set_title('False Positive and False Negative Rates with Transistor Effect', fontsize=16, color='white')
ax.set_xlabel('Voltage (V)', fontsize=14, color='white')
ax.set_ylabel('Error Rate', fontsize=14, color='white')
ax.legend(fontsize=12, loc='upper left')
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Customize the ticks
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

# Highlight the adjusted threshold voltage
ax.axvline(x=adjusted_threshold, color='red', linestyle='--', linewidth=1)
ax.annotate(f'Threshold Voltage = {adjusted_threshold}V', xy=(adjusted_threshold, 0.12), xytext=(adjusted_threshold + 0.02, 0.1),
            arrowprops=dict(facecolor='red', shrink=0.05), fontsize=12, color='red')

# Show the plot
plt.tight_layout()
plt.show()
