# %%
from techminer2.thesaurus.organizations import (  # type: ignore
    ApplyThesaurus,
    CreateThesaurus,
    ExplodeKeys,
    ReduceKeys,
    SortByKeyMatch,
    SortByMatch,
)

CreateThesaurus(root_directory="../").run()

# %%
ExplodeKeys(root_directory="../").run()

# %%
ReduceKeys(root_directory="../").run()

# %%
SortByKeyMatch(pattern=["Tecnológico Nacional de México"], root_directory="../").run()


# %%
SortByMatch(pattern=["Costa"], root_directory="../").run()

# %%
