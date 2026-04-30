import pandas as pd # type: ignore

# a. Read Excel file
df = pd.read_excel("students.xlsx")

# b. Calculate Total and Average
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

# c. Add Result column (initialize first)
df["Result"] = ""

# d. Apply condition to Result column
df.loc[df["Average"] >= 60, "Result"] = "Passed"
df.loc[df["Average"] < 60, "Result"] = "Failed"

# Uses conditional filtering
# loc → selects rows based on condition

# e. Write to new Excel file
df.to_excel("students_result.xlsx", index=False)

print("Processing complete. File saved as students_result.xlsx")