import pandas as pd

# Load the Excel file
file_path = "Dataset for Data Analytics.xlsx"

df = pd.read_excel(file_path)

# Display the first 5 rows
print(df.head())


# Check the size of the dataset
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])


# Check column names
print("\nColumn Names:")
print(df.columns.tolist())

# Step 4 - Check data types
print("\nData Types:")
print(df.dtypes)

# Step 5 - Check missing values
print("\nMissing Values:")
print(df.isnull().sum())


# Calculate missing percentage for CouponCode
missing_coupon = df["CouponCode"].isnull().sum()
total_records = len(df)

missing_percentage = (missing_coupon / total_records) * 100

print("\nMissing CouponCode:")
print("Number of missing values:", missing_coupon)
print("Percentage missing:", round(missing_percentage, 2), "%")



# Step 5B - Investigate missing CouponCode records
missing_coupon_rows = df[df["CouponCode"].isnull()]

print("\nRecords with missing CouponCode:")
print(missing_coupon_rows.head(10))

print("\nOrder Status of missing CouponCode records:")
print(missing_coupon_rows["OrderStatus"].value_counts())

print("\nPayment Method of missing CouponCode records:")
print(missing_coupon_rows["PaymentMethod"].value_counts())

print("\nReferral Source of missing CouponCode records:")
print(missing_coupon_rows["ReferralSource"].value_counts())


# Step 5C - Handle missing CouponCode values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

print("\nMissing CouponCode after cleaning:")
print(df["CouponCode"].isnull().sum())


# Step 6 - Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())


# Step 7 - Check duplicate Order IDs
print("\nDuplicate Order IDs:")
print(df["OrderID"].duplicated().sum())




# Step 8 - Check categorical values

print("\nPayment Method Categories:")
print(df["PaymentMethod"].value_counts())


print("\nOrder Status Categories:")
print(df["OrderStatus"].value_counts())


print("\nProduct Categories:")
print(df["Product"].value_counts())

print("\nReferral Source Categories:")
print(df["ReferralSource"].value_counts())


# Step 9 - Check date range

print("\nDate Range:")
print("Minimum Date:", df["Date"].min())
print("Maximum Date:", df["Date"].max())


# Step 10 - Check numerical columns

print("\nNumerical Data Summary:")
print(df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].describe())




# Step 11 - Check for outliers using IQR

numeric_columns = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]

print("\nOutlier Check using IQR:")

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print("\n", column)
    print("Lower Limit:", round(lower_limit, 2))
    print("Upper Limit:", round(upper_limit, 2))
    print("Number of potential outliers:", len(outliers))



    # Step 12 - Display potential TotalPrice outliers

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

totalprice_outliers = df[
    (df["TotalPrice"] < lower_limit) |
    (df["TotalPrice"] > upper_limit)
]

print("\nPotential TotalPrice Outliers:")
print(totalprice_outliers[
    ["OrderID", "Date", "Product", "Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]
])




# Step 13 - Verify TotalPrice calculation

df["CalculatedTotal"] = df["Quantity"] * df["UnitPrice"]

df["PriceDifference"] = (
    df["TotalPrice"] - df["CalculatedTotal"]
).round(2)

print("\nIncorrect TotalPrice records:")
print((df["PriceDifference"] != 0).sum())



# Step 14 - Check for negative values

print("\nNegative values check:")

print("Negative Quantity:",
      (df["Quantity"] < 0).sum())

print("Negative UnitPrice:",
      (df["UnitPrice"] < 0).sum())

print("Negative ItemsInCart:",
      (df["ItemsInCart"] < 0).sum())

print("Negative TotalPrice:",
      (df["TotalPrice"] < 0).sum())



# Step 15 - Check text consistency

print("\nText Consistency Check:")

print("\nProduct values:")
print(df["Product"].unique())

print("\nPayment Method values:")
print(df["PaymentMethod"].unique())

print("\nOrder Status values:")
print(df["OrderStatus"].unique())

print("\nReferral Source values:")
print(df["ReferralSource"].unique())



# Step 16 - Save cleaned dataset separately

# Save as Excel
df.to_excel("Cleaned_Data_Analytics.xlsx", index=False)

# Save as CSV
df.to_csv("Cleaned_Data_Analytics.csv", index=False)

print("\nFiles saved successfully!")
print("1. Cleaned_Data_Analytics.xlsx")
print("2. Cleaned_Data_Analytics.csv")