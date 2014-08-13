from IPython.nbconvert.exporters import SlidesExporter
from IPython.config import Config

from IPython.nbformat import current as nbformat

infile = "RL.ipynb" # load the name of your slideshow
outfile = "RL.slides.html"

notebook = open(infile).read()
notebook_json = nbformat.reads_json(notebook)

# This is the config object I talked before: 
# After the 'url_prefix', you can set the location of your 
# local reveal.js library, i.e. if the reveal.js is located 
# in the same directory as your talk.slides.html, then 
# set 'url_prefix':'reveal.js'.

c = Config({
            'RevealHelpTransformer':{
                'enabled':True,
                'url_prefix':'reveal.js',
                },                
            })

exportHtml = SlidesExporter(config=c)

exportHtml.template_file = "rvl.tpl"

(body,resources) = exportHtml.from_notebook_node(notebook_json)

open(outfile, 'w').write(body.encode('utf-8'))


