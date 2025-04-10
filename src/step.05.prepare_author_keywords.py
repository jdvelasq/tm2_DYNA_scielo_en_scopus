# %% --- PREPARATION ----------------------------------------------------------
import pandas as pd  # type: ignore

pd.set_option("display.max_rows", 100, "display.max_columns", 100)

from techminer2.packages.networks.co_occurrence.author_keywords import (  # type: ignore
    TermsByClusterDataFrame,
)
from techminer2.thesaurus.descriptors import *  # type: ignore

# %%
# CreateThesaurus().where_root_directory_is("../").run()

# %% --- REPLACE WORDS -------------------------------------------------------------


ReplaceWord(  #  type: ignore
    root_directory="../",
    word=abbr,
    replacement=text,
).run()
print("Done!")

# %% ---- DOMINANT CLUSTERS ---------------------------------------------------

# ReduceKeys(root_directory="../").run()  #  type: ignore
# ApplyThesaurus(root_directory="../").run()  #  type: ignore

df = (
    TermsByClusterDataFrame()
    #
    # FIELD:
    .having_term_occurrences_between(5, None)
    .having_terms_ordered_by("OCC")
    .using_clustering_algorithm_or_dict("louvain")
    .using_association_index("association")
    .where_root_directory_is("../")
    .where_database_is("main")
    .run()
)

df.head(100)


# %% ---- INTEGRITY CHECK -----------------------------------------------------

IntegrityCheck(root_directory="../").run()  #  type: ignore


# %%
## CollectDescriptors(root_directory="../").run()

# %%
## ReplaceAbbreviations(root_directory="../").run()  #  type: ignore
# RemoveParentheses(root_directory="../").run()  #  type: ignore
# ReplaceHyphenatedWords(root_directory="../").run()  #  type: ignore
# BritishToAmericanSpelling(root_directory="../").run()  #  type: ignore
# RemoveInitialDeterminers(root_directory="../").run()  #  type: ignore
# RemoveInitialStopwords(root_directory="../").run()  #  type: ignore
# RemoveCommonInitialWords(root_directory="../").run()  #  type: ignore
# RemoveCommonLastWords(root_directory="../").run()  #  type: ignore
# CleanupThesaurus(root_directory="../").run()  #  type: ignore
# ReduceKeys(root_directory="../").run()  #  type: ignore

# %% --------------------------------------------------------------------------


# %%
SortByKeyMatch(  #  type: ignore
    root_directory="../",
    pattern=[
        "GAME_THEORY",
    ],
).run()


# %%
SortByStartsWithKeyMatch(  #  type: ignore
    root_directory="../",
    pattern=[
        "GAME_THEORY",
    ],
).run()


# %%

# %%
text = """
    2E_CVRP
    GENERALIZED_VEHICLE_ROUTING_PROBLEMS
    TWO_ECHELA_DISTRIBUTION_SYSTEM
    TWO_ECHELON_DISTRIBUTION_SYSTEMS
    TWO_ECHELON_VEHICLE_ROUTING_PROBLEM
    TWO_ECHELON_VEHICLE_ROUTING_PROBLEMS
    TWO_ECHELON_VRP
    VEHICLE_ROUTING_PROBLEM
    VEHICLE_ROUTING_PROBLEMS
"""

text = text.split("\n")
text = [x.strip() for x in text if x.strip() != ""]
SortByKeyMatch(  #  type: ignore
    root_directory="../",
    pattern=text,
).run()


# %%
