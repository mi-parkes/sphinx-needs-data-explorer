import os, sys
from sphinx.util.console import bold, colorize

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
    'myst_parser',
    'sphinx_needs_data_explorer'
]

needs_build_json = True

exclude_patterns = []
exclude_patterns = ['project','mydir1']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'

html_theme_options = {
    "path_to_docs": "doc/source",
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

needs_extra_options = ["author"]

#templates_path      = ["_templates"]
#html_static_path    = ['_static']
#html_js_files       = ['js/explorer_button.js']

html_css_files      = ['css/custom.css']

env_plantuml = os.getenv("PLANTUML")
if env_plantuml != None:
    plantuml = env_plantuml
else:
    if sys.platform.startswith("linux"):
        plantuml = 'java -jar /usr/share/plantuml/plantuml.jar'
    elif sys.platform == "darwin":
        plantuml = 'java -jar /usr/local/plantuml/plantuml.jar'

env_plantuml_output_format= os.getenv("PLANTUML_OUTPUT_FORMAT")
if env_plantuml_output_format != None:
    plantuml_output_format=env_plantuml_output_format
else:
    plantuml_output_format = 'svg'

suppress_warnings   = ['myst.header']

def setup(app):
    app.connect("source-read",copy_and_modify_readme_md)
    app.connect('build-finished',build_finished)
    app.connect('config-inited',config_inited)

def config_inited(app, config):
    pass

def build_finished(app,docname):
    #return
    ofilename = os.path.join(app.srcdir,'_README.txt')
    try:
        print(f"Removing {colorize('darkgreen',ofilename)}")
        os.remove(ofilename)
    except FileNotFoundError:
        print("File not found:", ofilename)
    except PermissionError:
        print("Insufficient permissions to delete file:", ofilename)
    except OSError as error:
        print("Error deleting file:", error)

def copy_and_modify_readme_md(app, docname, source):
    if docname=="index":
        ifilename = os.path.join(app.srcdir,'..','..','README.md')
        ofilename = os.path.join(app.srcdir,'_README.txt')
        with open(ifilename,encoding='utf-8') as thefile:
            content = thefile.read()
            replacedText = content.replace('doc/source/_static','_static')
            # This needs to be redesigned!!!
            replacedText = replacedText.replace('''![](_static/images/sphinx_needs_data_explorer.svg)''',
            """```{raw} html
<object data="_static/images/sphinx_needs_data_explorer.svg" type="image/svg+xml"></object>
```""")
            if replacedText!=content:
                print(f"Creating {colorize('darkgreen',ofilename)}")
                with open(ofilename,'w',encoding='utf-8') as thefile:
                    thefile.write(replacedText)

needs_statuses = [
    dict(name="open", description="Nothing done yet"),
    dict(name="in progress", description="Someone is working on it"),
    dict(name="implemented", description="Work is done and implemented"),
]

needs_types = [
    dict(directive="req",  title="Requirement",      prefix="R_", color="#DEFFDC", style="node"),
    dict(directive="spec", title="Specification",    prefix="S_", color="#FFFF99", style="node"),
    dict(directive="impl", title="Implementation",   prefix="I_", color="#ffcccc", style="node"),
    dict(directive="test", title="Test Case",        prefix="T_", color="#87CEFA", style="node"),
    dict(directive="need", title="Need",             prefix="N_", color="#668cff", style="node")
]

needs_extra_links = [
    {
        "option": "refines",
        "incoming": "is refined by",
        "outgoing": "refines",
        "copy": False,
        "allow_dead_links": True,
        "style": "#00AA00",
        "style_part": "#00AA00",
        "style_start": "-",
        "style_end": "--o",
    }
]

#needs_show_link_title = True

sphinx_needs_data_explorer_config = {
    "filters":[
        "status=='open'",
        "['15','16'] in id",
        "title ~ /r.*[0-9]+5'$/i"
    ]
}
