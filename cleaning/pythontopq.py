
import pandas as pd
import psycopg2

# Step 1: Read CSV
df = pd.read_csv("cleaned_cafe_sales.csv")

# Step 2: Convert missing values to None
df = df.astype(object).where(pd.notna(df), None)

# Step 3: Convert transaction date
df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"],
    errors="coerce"
).dt.date

# Replace invalid dates with None
df["Transaction Date"] = df["Transaction Date"].where(
    pd.notna(df["Transaction Date"]), None
)

# Step 4: Connect PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="cleantable",
    user="postgres",
    password="root",
    port="5432"
)

cursor = conn.cursor()

print("Connected successfully!")

# Step 5: Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id VARCHAR(50) PRIMARY KEY,
        item VARCHAR(100),
        quantity INTEGER,
        price_per_unit NUMERIC(10,2),
        total_spent NUMERIC(10,2),
        payment_method VARCHAR(50),
        location VARCHAR(50),
        transaction_date DATE
    )
""")

# Step 6: Insert data
for row in df.itertuples(index=False, name=None):

    cursor.execute("""
        INSERT INTO transactions (
            transaction_id,
            item,
            quantity,
            price_per_unit,
            total_spent,
            payment_method,
            location,
            transaction_date
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (transaction_id) DO NOTHING
    """, row)

# Step 7: Commit
conn.commit()

print("Data imported successfully!")

# Step 8: Verify records
cursor.execute("SELECT COUNT(*) FROM transactions")

print("Total records:", cursor.fetchone()[0])

# Step 9: Close connection
cursor.close()
conn.close()
