import sphinx
from os import makedirs, path
import shutil
from docutils import nodes
import json
from jinja2 import Environment, FileSystemLoader
from sphinx.util import logging

__version__ = "0.7"
version_info = (0,7)

logger = logging.getLogger(__name__)

_ROOT_DIR = path.abspath(path.dirname(__file__))
_FILES = (
    (
        'my_custom_role.css',
        '',
    ),    
    (
        'sphinx_needs_data_explorer.html',
        'sha384-vtXRMe3mGCbOeY7l30aIg8H9p3GdeSe4IFlP6G8JMa7o7lXvnz3GFKzPxzJdPfGK',
    ),
    (
        'vis-network',
        '',
    ),    
    (
        'select2',
        '',
    ),    
    (
        'jquery',
        '',
    ),    
    (
        'peg',
        '',
    ),    
)

sphinx_needs_data_explorer_config_link_types_default    =['links']
sphinx_needs_data_explorer_config_type_color_map_default={}

def add_files(app, config):
    if sphinx.version_info[:2]>=(5,0) and not getattr(app, "sphinx_needs_data_explorer_installed", False):
        makedirs(path.join(app.outdir, '_static'), exist_ok=True)
        for (filename, integrity) in _FILES:
            ifile=path.join(_ROOT_DIR,'_static',filename)
            ofile=path.join(app.outdir,'_static', filename)
            if path.isdir(ifile):
                if path.exists(ofile):
                    shutil.rmtree(ofile)
                shutil.copytree(
                    ifile,
                    ofile
                )
            elif path.isfile(ifile):
                shutil.copyfile(
                    ifile,
                    ofile
                )
                
        environment = Environment(loader=FileSystemLoader(path.join(_ROOT_DIR,'_static')))
        filename="sphinx_needs_data_explorer.html"
        ifile=environment.get_template(filename)
        ofile=path.join(app.outdir,'_static', filename)

        link_types=['links']
        for item in getattr(app.config,"needs_extra_links",[]):
                if 'option' in item:
                    link_types.append(item['option'])
        type_color_map={}
        for item in getattr(app.config,"needs_types",[]):
                if ('directive' in item) and ('color' in item):
                    type_color_map[item['directive']]=item['color']
        context = {
            "LINK_TYPES": link_types,
            "TYPE2COLOR": type_color_map,
        }

        with open(ofile,"w+") as out:
            out.write(ifile.render(context))

    app.sphinx_needs_data_explorer_installed = True

def SphinxNeedsDataExplorer_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.raw('', 
        f"""<a href="_static/sphinx_needs_data_explorer.html" 
        class="custom-reference" title="Follow this link to explore your sphinx-needs data">{text}</a>""", format='html')
    return [node], []

def setup(app):
    app.connect('config-inited',add_files)
    app.add_role('sphinx_needs_data_explorer', SphinxNeedsDataExplorer_role)
    app.add_css_file('sphinx_needs_data_explorer.css')
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
