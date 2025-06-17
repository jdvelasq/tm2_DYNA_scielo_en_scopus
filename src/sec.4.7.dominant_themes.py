# %%

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

df

# %%
clusters = []
for i, row in df.iterrows():
    clusters.append(row.Terms.split("; "))

clusters

# %%

from techminer2.database.tools import RecordViewer  # type: ignore

for i_cluster, terms in enumerate(clusters):

    documents = (
        RecordViewer()
        #
        .where_root_directory_is("../")
        .where_database_is("main")
        .where_record_years_range_is(None, None)
        .where_record_citations_range_is(None, None)
        .where_records_match(None)
        .where_records_ordered_by("date_newest")
    ).run()[:50]

    # split the list "documents" in groups of 10
    document_groups = [documents[i : i + 10] for i in range(0, len(documents), 10)]

    for i_group, group in enumerate(document_groups):

        with open(
            f"../reports/clusters/0{i_cluster+1}/_group_{i_group}.txt",
            "w",
        ) as f:
            for doc in group:
                print(doc, file=f)
                print("\n\n--\n", file=f)

# %%
for i, row in df.iterrows():
    terms = row.Terms.lower().replace("_", " ")
    print(terms)
    print()
# %%
