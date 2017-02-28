import sys
import os

sys.path.insert(0, os.path.abspath('..'))
import recommonmark
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

source_parsers = {
    '.md': CommonMarkParser
}

source_suffix = ['.rst', '.md']

master_doc = 'index'
project = u'MacAdmins Community Documentation'
copyright = u'GPL'

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "Shufflepuck", # Username
    "github_repo": "MacAdminsDoc", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/", # Path in the checkout to the docs root
}

# app setup hook
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
