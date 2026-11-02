import pandas as pd


file = input("Enter CSV/XLS file name: ")


if file.endswith(".csv"):
    df = pd.read_csv(file)
elif file.endswith(".xls") or file.endswith(".xlsx"):
    df = pd.read_excel(file)
else:
    print("Invalid file format")
    exit()


print("Original Data:")
print(df)


print("\nMissing Values:")
print(df.isnull().sum())


df = df.drop_duplicates()


for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())


for col in df.select_dtypes(include="object").columns:
    if df[col].isnull().any() and not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])


print("\nCleaned Data:")
print(df)


df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved to cleaned_data.csv")
