import sys
import copy

def first_part(output_file):
    f = open(output_file, 'w')
    f.write("<!doctype html>\n")
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("    <title>Network | Interaction events</title>\n")
    f.write("\n")
    f.write("    <script type=\"text/javascript\" src=\"/home/matho/node_modules/vis/dist/vis.js\"></script>\n")
    f.write("    <link href=\"/home/matho/node_modules/vis/dist/vis.css\" rel=\"stylesheet\" type=\"text/css\"/>\n")
    f.write("\n")
    f.write("    <style type=\"text/css\">\n")
    f.write("       #mynetwork {\n")
    f.write("            width: 800px;\n")
    f.write("            height: 500px;\n")
    f.write("            border: 1px solid lightgray;\n")
    f.write("        }\n")
    f.write("	    #rectangle {\n")
    f.write("		    text-align: center;\n")
    f.write("		    font-weight: bold;\n")
    f.write("	    }\n")
    f.write("}\n")
    f.write("    </style>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("\n")
    f.write("<div id=\"mynetwork\"></div>\n")
    f.write("<div id=\"rectangle\"style=\"width:800px;height:100%;border:1px solid #000;\"> </div>\n")
    f.write("\n")
    f.write("<script type=\"text/javascript\">\n")
    f.write("    // create an array with nodes\n")
    f.write("        var nodes = new vis.DataSet([\n")
    f.close()

def second_part(output_file):
    f = open(output_file, 'a')
    f.write("	]);\n")
    f.write("\n")
    f.write("    // create a network\n")
    f.write("    var container = document.getElementById('mynetwork');\n")
    f.write("    var data = {\n")
    f.write("        nodes: nodes,\n")
    f.write("        edges: edges\n")
    f.write("    };\n")
    f.write("    var options = {\n")
    f.write("		layout:{randomSeed:2},\n")
    f.write("		physics: {\n")
    f.write("			stabilization: false,\n")
    f.write("			barnesHut: {\n")
    f.write("				gravitationalConstant: -10000,\n")
    f.write("				centralGravity: 0.75,\n")
    f.write("				springConstant: 0.08,\n")
    f.write("				springLength: 150\n")
    f.write("			},\n")
    f.write("			maxVelocity: 146,\n")
    f.write("            solver: 'barnesHut',\n")
    f.write("            timestep: 0.50,\n")
    f.write("            stabilization: {iterations: 150}\n")
    f.write("        },\n")
    f.write("		nodes: {\n")
    f.write("            size: 15,\n")
    f.write("            font: {\n")
    f.write("                size: 20\n")
    f.write("            },\n")
    f.write("            borderWidth: 2,\n")
    f.write("			borderWidthSelected: 4\n")
    f.write("        },\n")
    f.write("        edges: {\n")
    f.write("            width: 4,\n")
    f.write("			selectionWidth: function (width) {return width*2.5;}\n")
    f.write("        },\n")
    f.write("		interaction: {\n")
    f.write("          navigationButtons: true,\n")
    f.write("          keyboard: true,\n")
    f.write("		  hover: true,\n")
    f.write("		  tooltipDelay: 500,\n")
    f.write("        }\n")
    f.write("	};\n")
    f.write("    var network = new vis.Network(container, data, options);\n")
    f.write("	var stabil = true;\n")
    f.write("\n")
    f.write("    network.on(\"click\", function (params) {\n")
    f.write("        params.event = \"[original event]\";\n")
    f.write("		var tmp = \" \";\n")
    f.write("	\n")
    f.write("	\n")
    f.write("		for (var i = 1; i <= nodes.length; i++) {\n")
    f.write("        	if (nodes.get(i).id == params.nodes) {\n")
    f.write("				tmp = nodes.get(i).text;\n")
    f.write("			};\n")
    f.write("    	};\n")
    f.write("		\n")
    f.write("		if(params.nodes.length === 0 && params.edges.length > 0) {\n")
    f.write("			for (var i = 1; i <= edges.length; i++) {\n")
    f.write("				if (edges.get(i).id == params.edges) {\n")
    f.write("					tmp = edges.get(i).text;\n")
    f.write("				};\n")
    f.write("			};\n")
    f.write("		};\n")
    f.write("		\n")
    f.write("		document.getElementById('rectangle').innerHTML = '<div style=\"width:800px;height:100%;text-align:center;border:0px solid #000;\">' + tmp + '</div>';\n")
    f.write("    });\n")
    f.write("	\n")
    f.write("	network.on(\"stabilized\", function (params) {\n")
    f.write("	if(stabil) {\n")
    f.write("		network.fit();\n")
    f.write("		stabil = false;\n")
    f.write("	};	\n")
    f.write("	});\n")
    f.write("	\n")
    f.write("	network.on(\"doubleClick\", function (params) {\n")
    f.write("        params.event = \"[original event]\";\n")
    f.write("		network.focus(params.nodes);\n")
    f.write("	});\n")
    f.write("\n")
    f.write("</script>\n")
    f.write("\n")
    f.write("<script src=\"../../googleAnalytics.js\"></script>\n")
    f.write("</body>\n")
    f.write("</html>\n")
    f.close()

def create_reaction(From, To):
    From = From.split(" + ")
    To = To.split(" + ")

    from_back = copy.deepcopy(From)
    to_back = copy.deepcopy(To)

    new_from = []
    new_to = []

    for left_item in From:
        left_items = left_item.split(" ")
        for right_item in To:
            right_items = right_item.split(" ")
            if left_items[1] == right_items[1]:
                if int(left_items[0]) > int(right_items[0]):
                    new_from.append(str(int(left_items[0]) - int(right_items[0])) + " " + left_items[1])
                elif int(left_items[0]) < int(right_items[0]):
                    new_to.append(str(int(right_items[0]) - int(left_items[0])) + " " + left_items[1])
                from_back.remove(left_item)
                to_back.remove(right_item)

    new_from += from_back
    new_to += to_back

    return " + ".join(new_from), " + ".join(new_to)

vertices_file = sys.argv[-3]
edges_file = sys.argv[-2]
output_file = sys.argv[-1]

first_part(output_file)

output = open(output_file, 'a')

labels = []
IDs = []

label = ""
the_first_time = True
vertex_id = 0
for_edge_label = ""
ID = 0

'''
Import vertices
'''
with open(vertices_file) as vertices:
    for line in vertices:
        line = line.rstrip()
        if line:
            if line.find("vertex") != -1:
                if the_first_time:
                    the_first_time = False
                else:
                    label = label[:-4]
                    output.write("\t{id: " + vertex_id.__str__() + ", label: '" + vertex_id.__str__() + "', title: 'ID " + ID.__str__() + "', text: '" + label.__str__() + "'},\n")
                    for_edge_label = for_edge_label[:-3]
                    labels.append(for_edge_label)
                    for_edge_label = ""
                    label = ""
                parts = line.split(" ")
                ID = parts[2]
                IDs.append(ID)
                vertex_id += 1
            else:
                label += line.__str__() + "<br>"
                for_edge_label += line.__str__() + " + "

output.write("\t{id: " + vertex_id.__str__() + ", label: '" + vertex_id.__str__() + "', title: 'ID " + ID.__str__() + "', text: '" + label.__str__() + "'},\n")
for_edge_label = for_edge_label[:-3]
labels.append(for_edge_label)

output.write("\t]);\n\n\t// create an array with edges\n\tvar edges = new vis.DataSet([\n")

'''
Import edges
'''

edge_id = 0
with open(edges_file) as edges:
    for line in edges:
        line = line.rstrip()
        edge_id += 1
        parts = line.split(" ")
        left_index = IDs.index(parts[0])
        right_index = IDs.index(parts[2])

        From, To = create_reaction(labels[left_index], labels[right_index])

        left_index += 1
        right_index += 1

        output.write("\t{id: " + edge_id.__str__() + ", from: " + left_index.__str__() + ", to: " + right_index.__str__() + ", arrows:'to', text: '" + From.__str__() + " => " + To.__str__() + "'},\n")

output.close()

second_part(output_file)