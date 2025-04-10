# %%
import pandas as pd  # type: ignore

pd.set_option("display.max_rows", 100, "display.max_columns", 100)

from techminer2.packages.networks.co_occurrence.author_keywords import (  # type: ignore
    TermsByClusterSummary,
)

df = (
    TermsByClusterSummary()
    #
    # FIELD:
    .having_term_occurrences_between(5, None)
    .having_terms_ordered_by("OCC")
    #
    # NETWORK:
    .using_clustering_algorithm_or_dict("louvain")
    .using_association_index("association")
    #
    # DATABASE:
    .where_root_directory_is("../")
    .where_database_is("main")
    .run()
)

df["Terms"] = df["Terms"].str.split("; ").str[:15]
df["Terms"] = df["Terms"].map(lambda x: [y.split(" ")[0] for y in x])
df["Terms"] = df["Terms"].str.join("; ")
df["Terms"] = df["Terms"].str.replace("_", " ", regex=False)

with open("../reports/dominant_themes.txt", "w") as f:
    print(df.to_string(), file=f)


df

# %%


# %%
