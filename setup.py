from setuptools import setup

setup(
    name			= "versioning",
    packages			= [
        "versioning",
        "versioning/utils",
    ],
    package_dir			= {
        "versioning":		".", 
        "versioning/utils":	"./utils", 
    },
    version			= "0.1.0",
    description			= "Python version sorting tool",
    author			= "Matthew Brisebois",
    author_email		= "matthew@webheroes.ca",
    url				= "https://github.com/mjbrisebois/pyversioning",
    keywords			= ["pyversioning", "versioning", "version", "version sorting"],
    classifiers			= [],
)