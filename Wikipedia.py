temporary_nodes = []
temporary_edges = []
adjacency_list = []
nodes = []
with open('.gitignore/links.txt','r') as links:
    with open('.gitignore/nicknames.txt', 'r', encoding = "utf-8_sig") as pages:
        for page in pages:
            page = page.strip().split('\t')
            nodes.append(page[0])

        wiki_links = []
        for link in links:
            wiki_links.append(link.strip().split('\t')) 
            print(wiki_links)
            edge = []  
            for i in range(len(nodes)):
                 
            #temporary_nodes.append(link[0])
            #temporary_edges.append(link[1])
                if nodes[i] == link[0]:
                    edge.append(link[1])
                    print(nodes[i], edge)
                adjacency_list.append(edge)
        #print(adjacency_list)
            
                
                #for j in range(len(temporary_edges)):
                    
                    #print(edge)
                   
                
        
        
        

