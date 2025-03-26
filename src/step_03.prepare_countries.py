"""Country thesaurus cleaning and preparation"""

# %%
from techminer2.thesaurus.countries import (  # type: ignore
    ApplyThesaurus,
    ExplodeKeys,
    ReduceKeys,
)

# %%
ExplodeKeys(root_directory="../").run()


# %%
ReduceKeys(root_directory="../").run()
ApplyThesaurus(root_directory="../").run()

# %%
