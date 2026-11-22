import pandas as pd

# ----------Load and Read the data ----------
df = pd.read_csv("dirty_cafe_sales.csv", dtype=str)

print("Raw shape:", df.shape)
print(df.isna().sum())

# ---------- 1. Checking for missing values and store it as NA ----------
MISSING_TOKENS = {"ERROR", "UNKNOWN", "", "NAN", "NULL", "NONE"}
for col in df.columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .replace(list(MISSING_TOKENS), pd.NA)
    )
# remove the white space and replace empty strings with NA ^ start , $ end
df = df.replace(r"^\s*$", pd.NA, regex=True)

# ---------- 2. Drop rows without Transaction ID ----------
df = df.dropna(subset=["Transaction ID"])

# ---------- 3. Fix duplicate Transaction IDs ----------
before = len(df)
df = df.drop_duplicates(subset="Transaction ID", keep="first")
print(f"Removed {before - len(df)} duplicate Transaction ID(s)")

# ---------- 4. Convert to numeric using coerce so that non-numeric values are converted to NaN ----------
num_cols = ["Quantity", "Price Per Unit", "Total Spent"]
for c in num_cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# ---------- 5. Recompute / impute using the fixed price catalogue ----------
PRICE_MAP = {
    "Coffee": 2.0, "Cake": 3.0, "Cookie": 1.0, "Salad": 5.0,
    "Sandwich": 4.0, "Smoothie": 4.0, "Juice": 3.0, "Tea": 1.5,
}

# 5a. Fill missing price from catalogue
mask = df["Price Per Unit"].isna() & df["Item"].isin(PRICE_MAP)
df.loc[mask, "Price Per Unit"] = df.loc[mask, "Item"].map(PRICE_MAP)

# 5b. Recompute Total = Quantity * Price when possible
mask = (
    df["Total Spent"].isna()
    & df["Quantity"].notna()
    & df["Price Per Unit"].notna()
)
df.loc[mask, "Total Spent"] = df.loc[mask, "Quantity"] * df.loc[mask, "Price Per Unit"]

# 5c. Infer Quantity = Total / Price when possible
mask = (
    df["Quantity"].isna()
    & df["Total Spent"].notna()
    & df["Price Per Unit"].notna()
)
df.loc[mask, "Quantity"] = (df.loc[mask, "Total Spent"] / df.loc[mask, "Price Per Unit"]).round()

# ---------- 6. Sanity: Total == Quantity * Price ----------
mask_all_present = (
    df["Quantity"].notna()
    & df["Price Per Unit"].notna()
    & df["Total Spent"].notna()
)
expected = df.loc[mask_all_present, "Quantity"] * df.loc[mask_all_present, "Price Per Unit"]
mismatch_mask = mask_all_present & ((df["Total Spent"] - expected).abs() > 1e-9)
print("Rows where Total != Qty*Price:", int(mismatch_mask.sum()))
df.loc[mismatch_mask, "Total Spent"] = (
    df.loc[mismatch_mask, "Quantity"] * df.loc[mismatch_mask, "Price Per Unit"]
)

# ---------- 7. Parse dates ----------
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce")

# ---------- 8. Final dtype coercion ----------
df["Quantity"] = df["Quantity"].astype("Int64")   # nullable integer
df["Price Per Unit"] = df["Price Per Unit"].astype("Float64")
df["Total Spent"] = df["Total Spent"].astype("Float64")

# ---------- 9. Report remaining missingness ----------
print("\nRemaining missing values per column:")
print(df.isna().sum())
print("\nCleaned shape:", df.shape)

# ---------- 10. Save ----------
df.to_csv("cleaned_cafe_sales.csv", index=False)