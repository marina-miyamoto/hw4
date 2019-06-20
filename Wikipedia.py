temporary_nodes = []
temporary_edges = []
adjacency_list = []
nodes = []
with open('.gitignore/links.txt','r') as links:
    with open('.gitignore/nicknames.txt', 'r', encoding = "utf-8_sig") as pages:
        for link in links:
            link = link.strip().split('\t')   
            temporary_nodes.append(link[0])
            temporary_edges.append(link[1])

        for page in pages:
            page = page.strip().split('\t')
            nodes.append(page[0])
        
        for i in range(len(nodes)):
            edge = []
            for j in range(len(temporary_nodes)):
                if nodes[i] == temporary_nodes[j]:
                    edge.append(temporary_edges[j])
                    print(edge)
                adjacency_list.append(edge)
        print(adjacency_list)

