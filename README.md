# NetworkVISUAL
Script for visualizing reaction network using vis.js library.

# Installation
1. Install [vis.js](http://visjs.org/) library
2. Use set_path.py to change path to folder with installed vis.js

Example:

      python set_path.py "/my/path/before/folder/vis/"

# Usage
Run script create_graph.py with passed input vertices, edges and output html file.

Example:

      python create_graph.py vertices.txt edges.txt output.html

Run script set_path.py to change path in an exisiting .html file (if you did not created it)

Example:

      python set_path.py network.html "/my/path/before/folder/vis/"
