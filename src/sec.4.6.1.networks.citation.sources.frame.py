# %%
# grey colors: https://www.w3schools.com/colors/colors_shades.asp

from techminer2.packages.networks.citation.sources import (  # type: ignore
    TermsByClusterDataFrame,
)

df = (
    TermsByClusterDataFrame()
    #
    # UNIT OF ANALYSIS:
    .having_terms_in_top(50)
    .having_terms_ordered_by("OCC")
    .having_citation_threshold(0)
    .having_occurrence_threshold(2)
    .having_terms_in(None)
    #
    # CLUSTERING:
    .using_clustering_algorithm_or_dict("louvain")
    #
    # DATABASE:
    .where_root_directory_is("../")
    .where_database_is("main")
    .where_record_years_range_is(None, None)
    .where_record_citations_range_is(None, None)
    .where_records_match(None)
    #
    .run()
)


with open("../reports/sec.4.6.1.networks.citation.sources.frame.html", "w") as f:
    f.write(df.to_html())


df

# %%
