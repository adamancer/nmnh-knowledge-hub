"""Creates and indexes pages based using YAML files in _data"""

import yaml

from const import BASEPATH
from utils import (
    add_tooltips,
    build_nav,
    compute_urls,
    index_tags,
    read_fms,
)

if __name__ == "__main__":

    with open(BASEPATH / "_config.yml") as f:
        config = yaml.safe_load(f).get("python")

    # Construct the navigation and build a tag index using file front matter. This
    # section should generally not be modified.

    print("Reading front matter")
    fms = read_fms(BASEPATH)

    print("Determining URLs")
    compute_urls(fms)

    print("Indexing tags")
    index_tags(fms, config["tag_name"])

    print("Building navigation")
    exclude = ["explanations.md", "tutorials.md"]
    build_nav(
        fms,
        include_main=[p for p in config["main_nav"] if p not in exclude],
        exclude_sidebar=exclude,
    )

    print("Adding glossary tooltips")
    add_tooltips(BASEPATH)
