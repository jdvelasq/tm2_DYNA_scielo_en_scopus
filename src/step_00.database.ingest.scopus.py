from techminer2.database.ingest import ImportScopusData  # type: ignore

ImportScopusData(root_directory="./").run()

# from techminer2.database.tools import RecordMapping # type: ignore


# mapper = (
#     RecordMapping()
#     #
#     .where_root_directory_is("../")
#     .where_database_is("main")
#     .where_record_years_range_is(None, None)
#     .where_record_citations_range_is(None, None)
#     .where_records_match(None)
# )
# docs = mapper.run()

# texts = [doc["AB"] for doc in docs if isinstance(doc["AB"], str) ]
# texts = [text[-170:] for text in texts]
# texts = [text[::-1]  for text in texts]
# texts = sorted(texts)
# texts = [text[::-1] for text in texts]
# # texts = [text for text in texts if "author" in text.lower()]

# with open("./results/abstract_end.txt", "w") as f:
#     for text in texts:
#         f.write(text)
#         f.write("\n")
