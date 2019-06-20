nodes = []
adjacency_list = []

with open('.gitignore/wiki-links.txt','r') as links:
    with open('.gitignore/pages.txt', 'r', encoding = "utf-8_sig") as pages:
        for page in pages:
            page = page.strip().split('\t')
            nodes.append(page[0])

        tmp = []
        
        for line in links:
            tmp.append(line.strip().split('\t')) 

        for i in range(len(nodes)):
            edge = []
            for j in range(len(tmp)):
                if nodes[i] == tmp[j][0]:
                    edge.append(int(tmp[j][1]))
            adjacency_list.append(edge)
        print(adjacency_list)
       
                   
                
        
        
        

