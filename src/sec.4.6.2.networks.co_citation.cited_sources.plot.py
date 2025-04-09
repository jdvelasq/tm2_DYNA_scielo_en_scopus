# %%
# grey colors: https://www.w3schools.com/colors/colors_shades.asp

from techminer2.packages.networks.co_citation.cited_sources import (  # type: ignore
    NetworkPlot,
)

plot = (
    NetworkPlot()
    #
    # UNIT OF ANALYSIS:
    .having_terms_in_top(50)
    .having_citation_threshold(0)
    .having_terms_in(None)
    #
    # CLUSTERING:
    .using_clustering_algorithm_or_dict("louvain")
    #
    # NETWORK:
    .using_spring_layout_k(1)
    .using_spring_layout_iterations(50)
    .using_spring_layout_seed(1)
    #
    .using_edge_colors(["#7793a5"])
    .using_edge_width_range(0.5, 2.0)
    .using_node_size_range(10, 20)
    .using_textfont_opacity_range(0.5, 1.00)
    .using_textfont_size_range(12, 20)
    #
    .using_xaxes_range(None, None)
    .using_yaxes_range(None, None)
    .using_axes_visible(False)
    #
    # DATABASE:
    .where_root_directory_is("../")
    .where_database_is("main")
    .where_record_years_range_is(None, None)
    .where_record_citations_range_is(None, None)
    .where_records_match(None)
    #
    .run()
).update_layout(width=1000, height=1000)

plot.write_html("../reports/sec.4.6.2.networks.co_citation.sources.html")

plot

# %%
