# %%
# grey colors: https://www.w3schools.com/colors/colors_shades.asp

from techminer2.packages.correlation.cross import NetworkMapPlot  # type: ignore

plot = (
    NetworkMapPlot()
    #
    # FIELD:
    .with_field("source_title")
    .having_terms_in_top(20)
    .having_terms_ordered_by("OCC")
    .having_term_occurrences_between(None, None)
    .having_term_citations_between(None, None)
    .having_terms_in(None)
    #
    # CROSS WITH:
    .with_other_field("countries")
    #
    .with_correlation_method("pearson")
    #
    # NETWORK:
    .using_spring_layout_k(0.20)
    .using_spring_layout_iterations(10)
    .using_spring_layout_seed(0)
    #
    .using_edge_colors(["#F5F5F5", "#F0F0F0", "#E8E8E8", "#C0C0C0"])
    .using_edge_similarity_threshold(0)
    .using_edge_top_n(None)
    .using_edge_widths([0.5, 0.5, 1, 2])
    #
    .using_node_colors(["#C0C0C0"])
    .using_node_size_range(8, 20)
    #
    .using_textfont_opacity_range(0.9, 1.0)
    .using_textfont_size_range(8, 12)
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
)
plot.write_html("../reports/sec.4.3.1.corr_map.countries.html")

# plot

# %%
