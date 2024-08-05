import requests
import os
import re
from bs4 import BeautifulSoup

ifilename = "doc/build/html/_static/sphinx_needs_data_explorer.html"
ofilename = "doc/source/_static/sphinx_needs_data_explorer_help.html"

with open(ifilename) as ifp:
    soup = BeautifulSoup(ifp, "html.parser")
    helpNode = soup.find("div", class_="modal")
    if helpNode:
        helpNode.attrs["style"] = "display: block;"
        html_template = f"""
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Sphinx_Needs Data Explorer Help</title>
                <link href="sphinx_needs_data_explorer.css" rel="stylesheet"/>
            </head>
            <body>
                {helpNode.prettify(formatter=None)}
            </body>
        </html>
        """
        soup = BeautifulSoup(html_template, "html.parser")
        print(f"Creating file:'{ofilename}'")
        with open(ofilename, "w") as ofp:
            ofp.write(str(soup.prettify()))
    else:
        print("Failed to find help content!")
        exit(-1)
