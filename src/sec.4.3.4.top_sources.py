# %%
import pandas as pd  # type: ignore
from techminer2.database.metrics.performance import DataFrame  # type: ignore

df = (
    DataFrame()
    #
    # FIELD:
    .with_field("abbr_source_title")
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

df = df[
    [
        "OCC",
        "global_citations",
        "local_citations",
    ]
].drop_duplicates()

df.to_csv("../reports/sec.4.3.4.top_sources.tsv", sep="\t")
df


# %%
