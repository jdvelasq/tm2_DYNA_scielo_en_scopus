# %%
from techminer2.database.metrics.trending_terms_by_year.user import (  # type: ignore
    BarChart,
)

plot = (
    BarChart()
    #
    # FIELD:
    .with_field("author_keywords")
    .having_terms_ordered_by("OCC")
    .having_terms_per_year(6)
    .having_terms_in(None)
    #
    # DATABASE:
    .where_root_directory_is("../")
    .where_database_is("main")
    .where_record_years_range_is(None, None)
    .where_record_citations_range_is(None, None)
    .where_records_match(None)
    .run()
).update_layout(width=700, height=1100)

plot.write_html("../reports/sec.4.4.dominant_author_keywords.html")
plot

# %%

from techminer2.database.metrics.trending_terms_by_year.user import (  # type: ignore
    DataFrame,
)

df = (
    DataFrame()
    #
    # FIELD:
    .with_field("author_keywords")
    .having_terms_ordered_by("OCC")
    .having_terms_per_year(6)
    .having_terms_in(None)
    #
    # DATABASE:
    .where_root_directory_is("../")
    .where_database_is("main")
    .where_record_years_range_is(None, None)
    .where_record_citations_range_is(None, None)
    .where_records_match(None)
    .run()
)

df = df[["OCC", "global_citations", "year_q1", "year_q3"]]
df
# %%
