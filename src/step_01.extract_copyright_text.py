"""Clean copyright text from abstracats."""

# %%
from techminer2.database.tools import CollectDescriptors  # type: ignore
from techminer2.database.tools import ExtractCopyrightText  # type: ignore


def generate_copyright_text():
    text = ExtractCopyrightText(
        pattern=None,
        n_chars=140,
        root_directory="./",
    ).run()

    with open("../temp/copyright_text.txt", "w") as f:
        for t in text:
            f.write(t)
            f.write("\n")


def collect_descriptors():
    CollectDescriptors(root_directory="./").run()


collect_descriptors()
generate_copyright_text()

# %%
