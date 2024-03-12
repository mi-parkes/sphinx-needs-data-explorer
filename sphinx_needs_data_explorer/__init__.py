import sphinx
from os import makedirs, path
import shutil
from docutils import nodes
import json
from jinja2 import Environment, FileSystemLoader
from sphinx.util import logging
from sphinx.errors import ExtensionError

__version__ = "0.8.8"
version_info = (0,8,8)

logger = logging.getLogger(__name__)

_ROOT_DIR = path.abspath(path.dirname(__file__))
_FILES = ( 
    (
        'sphinx_needs_data_explorer.css',
        '',
    ),
    (
        'sphinx_needs_data_explorer.js',
        '',
    ),
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
static_directory='_static'

class sphinx_needs_data_explorer_ExtensionError(ExtensionError):
    pass

def add_files(app, config):
    #if 'sphinx_needs_data_explorer_config' in app.config:
    #    print("sphinx_needs_data_explorer_config",json.dumps(app.config.sphinx_needs_data_explorer_config,indent=2))

    disable_header_button=False
    if 'sphinx_needs_data_explorer_config' in app.config:
        if 'disable-header-button' in app.config['sphinx_needs_data_explorer_config']:
            disable_header_button_opt=app.config['sphinx_needs_data_explorer_config']['disable-header-button']
            if isinstance(disable_header_button_opt,bool):
                disable_header_button=disable_header_button_opt
    if not disable_header_button:
        if ('html_theme' in app.config) and (app.config['html_theme']=='sphinx_book_theme'):
            if not ('html_js_files' in app.config):
                app.config['html_js_files']=[]
            app.config['html_js_files'].append('js/explorer_button.js')
            if not ('templates_path' in app.config):
                app.config['templates_path']=[]
            app.config['templates_path'].append(path.join(_ROOT_DIR,static_directory,'_templates'))
            if not ('html_static_path' in app.config):
                app.config['html_static_path']=[]
            app.config['html_static_path'].append(path.join(_ROOT_DIR,static_directory,'_static'))

    if sphinx.version_info[:2]>=(5,0) and not getattr(app, "sphinx_needs_data_explorer_installed", False):
        try:
            makedirs(path.join(app.outdir,static_directory),exist_ok=True)
            for (filename, integrity) in _FILES:
                ifile=path.join(_ROOT_DIR,static_directory,filename)
                ofile=path.join(app.outdir,static_directory,filename)
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
        except shutil.Error as err:
            for src, dst, msg in err.args[0]:
                logger.critical(f"Error copying {src} to {dst}: {msg}")
            raise sphinx_needs_data_explorer_ExtensionError("Something went wrong in my extension")
        except OSError as err:
            logger.critical(f"Error: {err}")
            raise sphinx_needs_data_explorer_ExtensionError("Something went wrong in my extension")
        environment = Environment(loader=FileSystemLoader(path.join(_ROOT_DIR,static_directory)))
        filename="sphinx_needs_data_explorer.html"
        ifile=environment.get_template(filename)
        ofile=path.join(app.outdir,static_directory, filename)

        link_types=['links']
        for item in getattr(app.config,"needs_extra_links",[]):
                if 'option' in item:
                    link_types.append(item['option'])
        needs_extra_options=getattr(app.config,"needs_extra_options",[])
        type_color_map={}
        for item in getattr(app.config,"needs_types",[]):
                if ('directive' in item) and ('color' in item):
                    type_color_map[item['directive']]=item['color']
        filters=[]
        if 'sphinx_needs_data_explorer_config' in app.config:
            if 'filters' in app.config['sphinx_needs_data_explorer_config']:
                filters=app.config['sphinx_needs_data_explorer_config']['filters']
        context = {
            "LINK_TYPES": link_types,
            "TYPE2COLOR": type_color_map,
            "FILTERS": filters,
            "EXTRA_OPTIONS":needs_extra_options,
            "VERSION":__version__
        }

        with open(ofile,"w+") as out:
            out.write(ifile.render(context))

    app.sphinx_needs_data_explorer_installed = True

def SphinxNeedsDataExplorer_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    print(inliner.document.current_source)    
    srcdir=str(inliner.document.settings.env.app.srcdir)
    current_source=inliner.document.current_source.replace(srcdir,"")
    nn=current_source.split('/')
    prefix="../"*(len(nn)-2) if len(nn)>1 else  ""
    node = nodes.raw('', 
        f"""<a href="{prefix}{static_directory}/sphinx_needs_data_explorer.html" 
        class="custom-reference" title="Follow this link to explore your sphinx-needs data">{text}</a>""", format='html')
    return [node], []

def setup(app):
    app.connect('config-inited',add_files)
    app.add_role('sphinx_needs_data_explorer', SphinxNeedsDataExplorer_role)
    app.add_config_value('sphinx_needs_data_explorer_config',{'filters':[] },"html")
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
