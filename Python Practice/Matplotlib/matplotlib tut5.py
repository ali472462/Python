"""
import matplotlib.pyplot as plt
import numpy as np
blood_sugar = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

bins = [80, 100, 125, 150]
plt.hist([blood_sugar, blood_sugar_women], bins=bins, rwidth=0.9, color=["Green", "skyblue"],
         label=['men', 'women'])

plt.xlabel("SUGAR RANGE")
plt.ylabel("No of Patients")
plt.title("Blood Sugar Analysis")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.legend()

# Add labels for each bar's range
for i in range(len(bins) - 1):
    plt.text((bins[i] + bins[i + 1]) / 2, 5, f"{bins[i]} - {bins[i + 1]}", ha='center')

plt.show()"""
#/////////////////////// Practice //////////////////////
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# Create a random number generator with a fixed seed for reproducibility
rng = np.random.default_rng(19680801)
print(rng)
N_points = 100000
n_bins = 20

# Generate two normal distributions
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5
print(dist1)
print(dist2)
fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the *bins* keyword argument.
axs[0].hist(dist1, bins=n_bins)
axs[1].hist(dist2, bins=n_bins)
fig, axs = plt.subplots(1, 2, tight_layout=True)

# N is the count in each bin, bins is the lower-limit of the bin
N, bins, patches = axs[0].hist(dist1, bins=n_bins)

# We'll color code by height, but you could use any scalar
fracs = N / N.max()

# we need to normalize the data to 0..1 for the full range of the colormap
norm = colors.Normalize(fracs.min(), fracs.max())

# Now, we'll loop through our objects and set the color of each accordingly
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# We can also normalize our inputs by the total number of counts
axs[1].hist(dist1, bins=n_bins, density=True)

# Now we format the y-axis to display percentage
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))
plt.show()