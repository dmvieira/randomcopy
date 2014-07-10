from py2deb import Py2deb

##p=Py2deb("randomcopy")
##p["/usr/lib/python2.7/dist-packages"] = ["source.py",]
##p.generate("0.1")
from glob import glob

version="0.7"

p=Py2deb("randomcopy")
p.author="Diogo"
p.mail="diogo.mvieira@gmail.com"
p.description=u"Program to copy random files."
p.depends="bash, python, python-wxversion"
p.license="gpl"
p.section="utils"
p.arch="all"

p["/usr/share/applications"]=["randomcopy.desktop|randomcopy.desktop"]
p["/usr/bin"]=["source.py|randomcopy"]
p["/usr/share/icons/hicolor/48x48/apps"]=["randomcopy.png|randomcopy.png"]
p.generate(version,rpm=True,src=True)
