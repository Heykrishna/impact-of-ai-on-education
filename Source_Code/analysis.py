import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset/ai_impact_dataset.csv")

print("Dataset Loaded Successfully\n")
print(df.head())

# Group by scenario
summary = df.groupby("Scenario").mean()

print("\n===== Average Impact Analysis =====")
print(summary)

# Calculate improvements
improvement = ((summary.loc["With_AI"] - summary.loc["Without_AI"]) / summary.loc["Without_AI"]) * 100

print("\n===== Percentage Improvement =====")
print(improvement)

# Efficiency Score (custom metric)
summary["Efficiency_Score"] = (
    summary["Concept_Score"] * 0.25 +
    summary["Completion_Rate"] * 0.25 +
    summary["Retention"] * 0.2 +
    summary["Engagement"] * 0.1 -
    summary["Study_Time"] * 0.1 -
    summary["Teacher_Time"] * 0.1
)

print("\n===== Efficiency Score =====")
print(summary["Efficiency_Score"])


# 1. Learning Improvement Graph
plt.figure()
summary[["Concept_Score", "Completion_Rate", "Retention"]].T.plot(kind="bar")
plt.title("Learning Outcomes: Before vs After AI")
plt.ylabel("Score (%)")
plt.xlabel("Metrics")
plt.xticks(rotation=0)
plt.show()

# 2. Time Reduction Graph
plt.figure()
summary[["Study_Time", "Teacher_Time"]].T.plot(kind="bar")
plt.title("Time Reduction Due to AI")
plt.ylabel("Time (minutes/hours)")
plt.xlabel("Metrics")
plt.xticks(rotation=0)
plt.show()

# 3. Engagement Improvement
plt.figure()
summary["Engagement"].plot(kind="bar")
plt.title("Student Engagement Comparison")
plt.ylabel("Engagement Score (1–5)")
plt.xticks(rotation=0)
plt.show()

# 4. Efficiency Score Comparison
plt.figure()
summary["Efficiency_Score"].plot(kind="bar")
plt.title("Overall Educational Efficiency Score")
plt.ylabel("Score")
<<<<<<< HEAD:analysis.py
plt.xticks(rotation=0)
plt.show()


if summary.loc["With_AI", "Efficiency_Score"] > summary.loc["Without_AI", "Efficiency_Score"]:
    print("\nAI significantly improves overall educational efficiency.")
else:
    print("\nAI shows limited impact.")
=======
plt.show()
>>>>>>> 7ee3f8e421e525020c727cebb7491560c9b81aaa:Source_Code/analysis.py
