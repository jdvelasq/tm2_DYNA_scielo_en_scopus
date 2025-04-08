from techminer2.database.tools import RecordViewer  # type: ignore

viewer = (
    RecordViewer()
    #
    .where_root_directory_is("../")
    .where_database_is("main")
    .where_record_years_range_is(None, None)
    .where_record_citations_range_is(None, None)
    .where_records_match(None)
)
records = viewer.run()

with open("../reports/abstracts.txt", "w") as f:
    for record in records:
        f.write(record)
        f.write("\n")
