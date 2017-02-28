from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "Shufflepuck", # Username
    "github_repo": "MacAdminsDoc", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/", # Path in the checkout to the docs root
}


