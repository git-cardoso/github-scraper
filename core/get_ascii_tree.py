from treelib import Node, Tree


def get_ascii_tree(list_tab_dir, project):
    # Return ascii tree
    tree = Tree()
    tree.create_node(project, project)

    for i in range(len(list_tab_dir)):
        list_split = list_tab_dir[i][0].split("/")
        for n in range(len(list_split)):
            if n == 0 and tree.get_node(list_split[n]) == None:
                tree.create_node(list_split[n] + ' ( ' + str(list_tab_dir[i][1]) + ' lines )' , list_split[n], parent=project)
            else:
                if tree.get_node(list_split[n]) == None:
                    tree.create_node(
                        list_split[n] + ' ( ' + str(list_tab_dir[i][1]) + ' lines )' , list_split[n], parent=list_split[n-1])

    return tree
