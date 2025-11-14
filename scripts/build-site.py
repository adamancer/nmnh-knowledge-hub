"""Creates and indexes pages based using YAML files in _data"""

import re
import shutil
from pathlib import Path

import html5lib
import pandas as pd
import requests
import yaml
from bs4 import BeautifulSoup

try:
    import requests_cache
except ModuleNotFoundError:
    pass

from const import BASEPATH, GLOSSARY
from utils import (
    add_tooltips,
    autodate,
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
