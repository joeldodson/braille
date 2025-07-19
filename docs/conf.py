# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Braille Codes'
copyright = '2024-%Y, Joel Dodson'
author = 'Joel Dodson'
version = '0.2'
release = '0.1.1'
needs_sphinx = '8.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "pydata_sphinx_theme",
    ## "sphinx.ext.autosectionlabel",
]

## have link refs auto created for headings up to level 3 
myst_heading_anchors = 3

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]

html_title = "Braille Codes"
html_short_title = "BraCo"
html_last_updated_fmt = ""
html_show_copyright = False
html_show_sphinx = True
html_show_sourcelink = False 
# include the in page TOC in the left (main) sidebar
html_sidebars = {
    "**": [
        ## "sidebar-collapse",
        ## "sidebar-nav-bs" ,
        "page-toc",
    ]
}

# links for the pydata_sphinx_theme
# pdata-sphinx-theme opsions: https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/layout.html#references

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "navbar_align": "left",
    "github_url": "https://github.com/joeldodson/braille",
    "article_header_start": [],  ## gets rid of breadcrumbs links 
    "primary_sidebar_end":  [],
    "secondary_sidebar_items":  [],
    "content_footer_items": [],
    "footer_start": [],
    "footer_end": [],
    "footer_center": ["sphinx-version", "theme-version", "last-updated"],
    "show_version_warning_banner": False,
    # trying to get rid of inaccessible color mode switcher
    "navbar_end": ["navbar-icon-links"],
}
