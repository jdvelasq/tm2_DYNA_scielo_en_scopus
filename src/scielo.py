import pandas as pd  # type: ignore

df = pd.read_csv("scielo.csv")
# print(df.loc[0, "status"])
df = df[df["status"].map(lambda x: x == "current")]
df["scielo_url"] = df["scielo_url"].str.split("&").str[-2].str.replace("pid=", "")
df = df[["revistas", "scielo_url"]]

with open("issn.txt", "w", encoding="utf-8") as f:
    print(df.to_string(index=False, header=False), file=f)
