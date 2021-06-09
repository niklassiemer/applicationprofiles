import os
import shutil

from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme

from MetaDataFiles.TurtleSchemeGenerator.gen_experimental_schemes import schemes_to_write as exp_schemes_to_write
from MetaDataFiles.TurtleSchemeGenerator.gen_digital_schemes import schemes_to_write as comp_schemes_to_write

web_dir = os.path.join(os.getcwd(), 'website')
try:
    os.mkdir(web_dir)
except FileExistsError:
    shutil.rmtree(web_dir)
    os.mkdir(web_dir)

web_digital_dir = os.path.join(web_dir, 'digital')
os.mkdir(web_digital_dir)

web_physical_dir = os.path.join(web_dir, 'physical')
os.mkdir(web_physical_dir)

index_html = """<html>
 <head>
  <title>SFB1394 Meta Data Schemes</title>
 </head> 
 <body>
  <H1> Meta Data Scheme Collection in the SFB1394 </H1> <hr>
"""

index_html += "  <H2> Physical Meta Data Schemes: </H2> <hr>\n"
for key, value in sorted(exp_schemes_to_write.items()):
    index_html += '   <a href="physical/' + key + '.html"> ' + key + '</a> <br>\n'
    scheme = Scheme(key)
    scheme.fields = value()
    scheme.write(filename=os.path.join(web_physical_dir, key), file_extension='html')

index_html += "  <H2> Digital Meta Data Schemes: </H2> <hr>\n"
for key, value in sorted(comp_schemes_to_write.items()):
    index_html += '   <a href="digital/' + key + '.html"> ' + key + '</a> <br>\n'
    scheme = Scheme(key)
    scheme.fields = value()
    scheme.write(filename=os.path.join(web_digital_dir, key), file_extension='html')

index_html += " </body>\n</html>"

with open(os.path.join(web_dir, 'index.html'), 'w') as f:
    f.write(index_html)
