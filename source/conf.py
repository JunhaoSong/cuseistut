# Configuration file for building the Read the Docs webpage: CUSeisTut project
#
# This file only contains a selection of the most common options. For a full l
# ist see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import datetime

# -- Project information -----------------------------------------------------
master_doc = 'index'
project = 'CUSeisTut'
author = 'CUSeisTut team'
copyright = '2021-{}, {}'.format(datetime.date.today().year, author)
github_user = 'JunhaoSong'
github_repo = 'cuseistut'
github_url = f'https://github.com/{github_user}/{github_repo}'
# The full version, including alpha/beta/rc tags
version = '0.0.1'
release = version


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "prev_next_buttons_location": "bottom",
    "sticky_navigation": False,
    "navigation_depth": -1
}
html_css_files = ["custom.css"]
html_static_path = ["_static"]
html_extra_path = []
html_last_updated_fmt = "%Y-%m-%d"
html_search_language = "en"
html_title = "CUSeisTut"



