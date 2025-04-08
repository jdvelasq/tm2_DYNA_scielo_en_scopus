# %%
from techminer2.database.tools import Coverage  # type: ignore

(
    Coverage()
    #
    .with_field("author_keywords")
    #
    .where_root_directory_is("../")
    .where_database_is("main")
    .where_record_years_range_is(None, None)
    .where_record_citations_range_is(None, None)
    #
    .run()
)


# %%
