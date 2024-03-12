from setuptools import setup, find_packages

with open('README_pypi.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sphinx-needs-data-explorer',
    version='0.8.8',
    packages=find_packages(),
    author='Michael Parkes',
    author_email='mparkes@post.cz',
    description='Sphinx-needs-data-explorer is a Sphinx extension to visualize Sphinx-Needs data',
    url='https://github.com/mi-parkes/sphinx-needs-data-explorer',
    license="MIT License",
    package_data={
        "sphinx_needs_data_explorer": [
            "_static/_static/js/explorer_button.js",
            "_static/_templates/article-header-buttons.html",
            "_static/_templates/explorer-button.html",
            "_static/sphinx_needs_data_explorer.css",
            "_static/sphinx_needs_data_explorer.js",
            "_static/sphinx_needs_data_explorer.html",
            "_static/jquery/jquery-3.7.1.min",
            "_static/jquery/LICENSE.txt",
            "_static/peg/LICENSE.txt",
            "_static/peg/peg-0.10.0.min.js",
            "_static/select2/select2.min.js",
            "_static/select2/LICENSE.md",
            "_static/select2/select2.min.css",
            "_static/select2/package.json",
            "_static/vis-network/vis-network.min.js",
            "_static/vis-network/vis-network.min.js.map",
            "_static/vis-network/LICENSE-APACHE-2.0",
            "_static/vis-network/package.json",
            "_static/vis-network/LICENSE-MIT"
        ]
    },
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=["Sphinx>=5.3.0"],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
