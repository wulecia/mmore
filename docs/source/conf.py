project = "MMORE"
author = "MMORE contributors"
copyright = "2026, MMORE contributors"

extensions = [
    "myst_parser",
    "sphinx.ext.githubpages",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = "MMORE Documentation"
# Uncomment if you want to use a project logo placed in docs/source/_static/
# html_logo = "_static/mmore_logo.jpg"

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "substitution",
]

autosummary_generate = True

# Repository information is intentionally omitted here to avoid generating
# incorrect "Edit on GitHub" links while the real repository URL/branch
# are not yet configured. When ready, set html_theme_options with values
# similar to the example below:
#
# html_theme_options = {
#     "source_repository": "https://github.com/ORG/REPO/",
#     "source_branch": "master",
#     "source_directory": "docs/source/",
# }
html_theme_options = {}
