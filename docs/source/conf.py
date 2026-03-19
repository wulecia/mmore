project = "MMORE"
author = "MMORE contributors"
copyright = "2026, MMORE contributors"

extensions = [
    "myst_parser",
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "furo"
html_static_path = ["_static"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "colon_fence",
]