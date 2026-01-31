# SOLUTION: Complete analysis of petal width

print("=" * 60)
print("PETAL WIDTH ANALYSIS")
print("=" * 60)

# 1. Statistics
mean_pw = df['petal_width'].mean()
median_pw = df['petal_width'].median()
print(f"\nMean: {mean_pw:.2f} cm")
print(f"Median: {median_pw:.2f} cm")
print(f"Difference: {abs(mean_pw - median_pw):.2f} cm")
print("→ Mean and median are fairly close, slight right skew")

# 2 & 3. Visualizations
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Histogram
sns.histplot(data=df, x='petal_width', bins=15, kde=True, ax=axes[0])
axes[0].axvline(mean_pw, color='red', linestyle='--', label=f'Mean: {mean_pw:.2f}')
axes[0].axvline(median_pw, color='green', linestyle='--', label=f'Median: {median_pw:.2f}')
axes[0].set_title('Distribution of Petal Width')
axes[0].legend()

# Box plot
sns.boxplot(data=df, x='species', y='petal_width', palette='Set2', ax=axes[1])
axes[1].set_title('Petal Width by Species')

plt.tight_layout()
plt.show()

print("\n" + "=" * 60)
print("CONCLUSIONS")
print("=" * 60)
print("""
• Setosa has very narrow petals (0.1-0.6 cm) - barely any variation!
• Versicolor: medium width (1.0-1.8 cm)
• Virginica: widest (1.4-2.5 cm)

SURPRISING FINDING:
• Setosa's petal width is EXTREMELY consistent (tiny box!)
• This makes petal width a great feature for identifying Setosa
• Just one measurement (petal width < 0.75) separates Setosa perfectly!
""")