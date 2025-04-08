from techminer2._internals import Params  # type: ignore
from techminer2.database._internals.io import (  # type: ignore
    internal__load_all_records_from_database,
)
from techminer2.thesaurus._internals import (  # type: ignore
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
)

# prepare author keywords
records = internal__load_all_records_from_database(Params(root_directory="./"))
keywords = records["author_keywords"]

# explode keywords
keywords = keywords.str.split("; ")
keywords = keywords.explode()
keywords = keywords.str.strip()

# exttract words
keywords = keywords.str.replace(r"\(.*?\)", "", regex=True)
keywords = keywords.str.strip()
keywords = keywords.str.replace(r"\s\s+", " ", regex=False)
keywords = keywords.str.replace(r" ", "_", regex=False)
keywords = keywords.str.replace(r"___", "_", regex=False)
keywords = keywords.str.replace(r"__", "_", regex=False)
keywords = keywords.str.replace(r"_$", "", regex=False)
keywords = keywords.str.replace(r"^_", "", regex=False)
keywords = keywords.str.split("_")
keywords = keywords.explode()
keywords = keywords.to_list()
keywords = set(keywords)


th_path = internal__generate_user_thesaurus_file_path(
    Params(root_directory="./", thesaurus_file="abbreviations.the.txt")
)
th = internal__load_thesaurus_as_mapping(th_path)
keys = list(th.keys())
print("Original keys: ", len(keys))

new_keys = [k for k in keys if k in keywords]
print("Reduced keys: ", len(new_keys))

with open("new_abbreviations.the.txt", "w") as f:
    for k in new_keys:
        f.write(f"{k}\n")
        for v in th[k]:
            f.write(f"    {v}\n")
print("finished")
