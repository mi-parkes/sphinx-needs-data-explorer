import sphinx
import os
from os import makedirs, path
import shutil
from docutils import nodes

__version__ = "0.7"
version_info = (0,7)

_ROOT_DIR = path.abspath(path.dirname(__file__))
_FILES = (
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

def add_files(app, config):
    sphinx_needs_data_explorer_installed = getattr(app, "sphinx_needs_data_explorer_installed", False)
    if sphinx.version_info[:2]>=(5,0) and not sphinx_needs_data_explorer_installed:
        makedirs(path.join(app.outdir, '_static'), exist_ok=True)
        for (filename, integrity) in _FILES:
            ifile=path.join(_ROOT_DIR,'_static',filename)
            ofile=path.join(app.outdir,'_static', filename)
            if os.path.isdir(ifile):
                if os.path.exists(ofile):
                    shutil.rmtree(ofile)
                shutil.copytree(
                    ifile,
                    ofile
                )
            elif os.path.isfile(ifile):
                shutil.copyfile(
                    ifile,
                    ofile
                )
        #shutil.copytree(testroot_path,'_static' ,srcdir)
    app.sphinx_needs_data_explorer_installed = True

def SphinxNeedsDataExplorer_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.raw('', f"""<a href="/_static/sphinx_needs_data_explorer.html">{text}</a>""", format='html')
    return [node], []

def setup(app):
    app.connect('config-inited',add_files)
    app.add_role('sphinx_needs_data_explorer', SphinxNeedsDataExplorer_role)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
