# %%
# grey colors: https://www.w3schools.com/colors/colors_shades.asp

from techminer2.packages.networks.coupling.sources import NetworkPlot  # type: ignore

plot = (
    NetworkPlot()
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
    # NETWORK:
    .using_spring_layout_k(0.6)
    .using_spring_layout_iterations(40)
    .using_spring_layout_seed(0)
    #
    .using_edge_colors(["#7793a5"])
    .using_edge_width_range(0.5, 3.0)
    .using_node_size_range(8, 20)
    .using_textfont_opacity_range(0.6, 1.0)
    .using_textfont_size_range(8, 14)
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

plot.write_html("../reports/sec.4.6.3.networks.coupling.sources.html")

plot


# %%
