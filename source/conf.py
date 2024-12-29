# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# SPDX-License-Identifier: BSD-3-Clause

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import os
import subprocess

project = 'Labplot Manual'
description = 'The Official Labplot Documentation'
copyright = 'licensed under the  <a href="https://spdx.org/licenses/GPL-3.0-or-later.html">licensed under the terms of the GNU General Public License v3.0 or later</a> unless stated otherwise'
author = 'Labplot Community'
project_url = 'https://labplot.kde.org/'

# The full version, including alpha/beta/rc tags
with open("../VERSION.txt", "r") as version_file:
    version = version_file.read()
release = version

# Get the git description if possible, to put it in the footer.

try:
    gitcommitfriendly = subprocess.check_output(["git", "describe", "--always"]).decode("utf-8").strip()
except subprocess.CalledProcessError as exc:
    gitcommitfriendly = None


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinxcontrib.youtube',
    'sphinx.ext.todo',
    'breathe'
]

# Display todos by setting to True
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['resources/templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store', '.venv*']
html_extra_path = ['404handler.php'] # bring our 404 handler in

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# languages to exclude from smartquotes transformation. Requested by catalan translators due l':ref:`<crop_tool>` getting rendered as l"crop tool.
smartquotes_excludes = {'languages':[
                                    'ja',
                                    'ca',
                                    'fr'
                                    ],
                        'builders': [
                                    'man',
                                    'text'
                                    ]
                        }

# This reStructuredText will be included at the begin of every source file.
#rst_prolog = ""
# This reStructuredText will be included at the end of every source file.
rst_epilog = ""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme' #'alabaster' #'sphinx_rtd_theme' 'insegel'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['resources/static']

html_favicon = 'resources/static/images/favicon.ico'

html_logo = 'resources/static/images/logo-light.svg'

if html_theme == "sphinx_rtd_theme":
    html_css_files = ["css/theme_overrides.css",
                      "css/version_switch.css"]
    html_js_files = ["js/version_switch.js"]

html_context = {
    'build_id': os.getenv('BUILD_NUMBER', None),
    'build_url': os.getenv('BUILD_URL', None),
    'commit' : gitcommitfriendly
}

html_last_updated_fmt = '%Y-%m-%dT%H:%M:%S'

# -- Internationalization Options --------------------------------------------

locale_dirs = ['locale/']   # Where the PO files will be stored at
gettext_compact = False     # optional.
#gettext_additional_targets = ['image', 'index', 'literal-block'] # allows images to be translatable
#figure_language_filename = "{path}{language}/{basename}{ext}"

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
# filename
# epub_basename = project.replace(' ', '_') + '_' + language

epub_title = project+" "+version
epub_description = description

# Technically speaking dublincore accepts multiple author and contributor elements, but
# the sphinx builder only accepts one.
epub_author = author
epub_publisher = project_url
epub_copyright = copyright

epub_cover = ('_static/images/manual_cover.png', '')

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
epub_identifier = project_url

# A unique identification for the text.
#
epub_uid = 'url'

# Not actually used anywhere? Docs say that this should be what the epub uid is used for but...
epub_scheme = 'URL'

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html', '.htaccess', '404.xhtml', '404handler.php', '_static/favicon.ico', '_static/images/favicon.ico']

epub_tocscope = 'includehidden'

breathe_projects = {
    "LabPlot SDK" : "../xml"
}

# Breathe Configuration
breathe_default_project = "LabPlot SDK"