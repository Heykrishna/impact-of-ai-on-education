import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ai_tools_comparison.csv")

# Show basic info
print("Dataset Loaded Successfully")
print(df.head())

# ---- Analysis ----

# Group by tool
summary = df.groupby("Tool").mean()

print("\nAverage Performance:")
print(summary)

# Normalize response time
summary["Normalized_Time"] = (
    summary["Response_Time"].max() - summary["Response_Time"]
)

# Calculate overall score
summary["Overall_Score"] = (
    summary["Accuracy"] * 0.3 +
    summary["Task_Completion"] * 0.25 +
    summary["Engagement"] * 0.2 +
    summary["Usability"] * 0.15 +
    summary["Normalized_Time"] * 0.1
)

print("\nOverall Scores:")
print(summary["Overall_Score"])

# Best tool
best_tool = summary["Overall_Score"].idxmax()
print(f"\nBest Performing Tool: {best_tool}")

# ---- Visualization ----

# Accuracy comparison
summary["Accuracy"].plot(kind="bar", title="Accuracy Comparison")
plt.ylabel("Accuracy (%)")
plt.show()

# Response time comparison
summary["Response_Time"].plot(kind="bar", title="Response Time Comparison")
plt.ylabel("Time (sec)")
plt.show()

# Overall score comparison
summary["Overall_Score"].plot(kind="bar", title="Overall Performance Score")
plt.ylabel("Score")
plt.show()
