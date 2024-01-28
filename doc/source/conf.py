import os, sys

project = 'Sphinx Needs Data Explorer'
copyright = '2024, MP'
author  = 'MP'
release = '0.7'
version = '0.7'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_needs',
    'sphinx_copybutton',
    'sphinx.ext.githubpages',
    'sphinxcontrib.plantuml',
    'sphinx_needs_data_explorer'
]

needs_build_json = True

exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'

html_theme_options = {
    "path_to_docs": "source",
    "repository_url": "https://github.com/mi-parkes/sphinx-needs-data-explorer",
    "repository_branch": "main",
    "show_navbar_depth": 2,
    "show_toc_level": 1,  
    "use_repository_button": True,
    "use_source_button": True,
    "home_page_in_toc" : True,
    "use_issues_button": True,
    "use_edit_page_button": True, 
}

env_plantuml = os.getenv("PLANTUML")
if env_plantuml != None:
    plantuml = env_plantuml
else:
    if sys.platform.startswith("linux"):
        plantuml = 'java -jar /usr/share/plantuml/plantuml.jar'
    elif sys.platform == "darwin":
        plantuml = 'java -jar /usr/local/plantuml/plantuml.jar'

plantuml_output_format = 'svg'

sphinx_needs_data_explorer_config={
    'link_types':['links'],
    'type_color_map': {
        'req'   :'#DEFFDC',
        'spec'  :'#FFFF99',
        'test'  :'#87CEFA'
    }
}
