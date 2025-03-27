# %%
import pandas as pd  # type: ignore
from techminer2.database.metrics.performance import DataFrame  # type: ignore

df1 = (
    DataFrame()
    #
    # FIELD:
    .with_field("source_title")
    .having_terms_in_top(10)
    .having_terms_ordered_by("OCC")
    .having_term_occurrences_between(None, None)
    .having_term_citations_between(None, None)
    .having_terms_in(None)
    #
    # DATABASE:
    .where_root_directory_is("../")
    .where_database_is("main")
    .where_record_years_range_is(None, None)
    .where_record_citations_range_is(None, None)
    #
    .run()
)

df2 = (
    DataFrame()
    #
    # FIELD:
    .with_field("source_title")
    .having_terms_in_top(10)
    .having_terms_ordered_by("global_citations")
    .having_term_occurrences_between(None, None)
    .having_term_citations_between(None, None)
    .having_terms_in(None)
    #
    # DATABASE:
    .where_root_directory_is("../")
    .where_database_is("main")
    .where_record_years_range_is(None, None)
    .where_record_citations_range_is(None, None)
    #
    .run()
)

df = pd.concat([df1, df2], axis=0)

df = df[
    [
        "rank_occ",
        "rank_gcs",
        "OCC",
        "global_citations",
        "h_index",
        "g_index",
        "m_index",
    ]
].drop_duplicates()

df.to_csv("../reports/sec.3.2.top_sources.tsv", sep="\t")

# %%
