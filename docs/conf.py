# docs/conf.py
import os
import sys

import moodle_docs_theme

sys.path.insert(0, os.path.abspath(".."))

project = "moodle-theme_govbr"

extensions = [
    "sphinx.ext.githubpages",
    "moodle_docs_theme",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

root_doc = "index"

html_theme = "moodle_docs_theme"
html_theme_path = [moodle_docs_theme.get_html_theme_path()]
html_static_path = ["_static"]

html_theme_options = {
    "project_name": "moodle-theme_govbr",
    "tagline": "Tema Moodle DSGovBR — govbr-moodletheme-suite",
    "github_url": "https://github.com/govbr-moodletheme-suite/moodle-theme_govbr",
    "github_repo": "govbr-moodletheme-suite/moodle-theme_govbr",
    "github_version": "main",
    "doc_path": "docs/",
    "show_edit_on_github": True,
    "enable_dark_mode": True,
    "navigation_links": (
        "Início|index, Visão geral|overview, Instalação|installation, "
        "Testes|testing, Plano de teste de usabilidade|usability-test-plan, "
        "Desenvolvimento|development"
    ),
}
