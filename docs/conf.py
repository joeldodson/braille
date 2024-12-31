# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Braille Notes'
copyright = '2024-%Y, Joel Dodson'
author = 'Joel Dodson'
version = '0.1'
release = '0.1.0'
needs_sphinx = '8.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

## extensions = ["myst_parser", "sphinx_book_theme"]
extensions = ["myst_parser", "pydata_sphinx_theme"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]

# links for the sphinx_book_theme
# the 'book' theme is based on the 'pydata' theme thus options derive from there as well.
# pdata-sphinx-theme opsions: https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/layout.html#references
# sphinx-book-theme options: https://sphinx-book-theme.readthedocs.io/en/latest/reference.html

html_title = 'Braille Notes' 
html_last_updated_fmt = ""
html_show_copyright = False
html_show_sphinx = True
html_show_sourcelink = False 
# remove all side bars, only have horizontal nav in header
html_sidebars = {"**": []}
## html_theme = "sphinx_book_theme"
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "navbar_align": "left",
    "use_download_button": False,
    "github_url": "https://github.com/joeldodson/braille",
    "repository_branch": "main",
    "use_issues_button": True,
    "use_repository_button": True,
    "home_page_in_toc": True,
    "footer_start": [],
    "footer_end": [],
    # I've seen footer content items specified in two different ways
    # need to set it to [] to avoid default cruft in the footer.
    "footer_content_items": [],
    "content_footer_items": [],
    "footer_center": ["sphinx-version", "theme-version", "last-updated"],
    "show_version_warning_banner": False,
    # no secondary sidebars for any pages 
    "secondary_sidebar_items": {"**": []},
    # trying to get rid of inaccessible color mode switcher 
    "navbar_end": ["navbar-icon-links"],
}
