


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level=0):
        spaces = '  ' * level 
        prefix = spaces + '|__' if self.parent else ""
        print(prefix, self.data)
        for child in self.children:
            child.print_tree(level+1)


def tools_tree():
    root = TreeNode("Tools")  ## Defining the Root (Level 0)

    swords = TreeNode("Swords") ## Level 1
    pickaxes = TreeNode("Pickaxe")
    axes = TreeNode("Axes")
    shovels = TreeNode("Shovels")
    hoes = TreeNode("Hoes")

    swords.add_child(TreeNode("Wooden Sword"))    ## Level 2 for Swords
    swords.add_child(TreeNode("Stone Sword"))  
    swords.add_child(TreeNode("Iron Sword")) 
    swords.add_child(TreeNode("Gold Sword")) 
    swords.add_child(TreeNode("Diamonds Sword")) 

    pickaxes.add_child(TreeNode("Wooden Pickaxe"))    ## Level 2 for Pickaxes
    pickaxes.add_child(TreeNode("Stone Pickaxe"))  
    pickaxes.add_child(TreeNode("Iron Pickaxe")) 
    pickaxes.add_child(TreeNode("Gold Pickaxes")) 
    pickaxes.add_child(TreeNode("Diamonds Pickaxe")) 

    axes.add_child(TreeNode("Wooden Axe"))    ## Level 2 for Axes
    axes.add_child(TreeNode("Stone Axe"))  
    axes.add_child(TreeNode("Iron Axe")) 
    axes.add_child(TreeNode("Gold Axe")) 
    axes.add_child(TreeNode("Diamonds Axe")) 

    shovels.add_child(TreeNode("Wooden Shovel"))    ## Level 2 for Shovels
    shovels.add_child(TreeNode("Stone Shovel"))  
    shovels.add_child(TreeNode("Iron Shovel")) 
    shovels.add_child(TreeNode("Gold Shovel")) 
    shovels.add_child(TreeNode("Diamonds Shovel")) 
    
    hoes.add_child(TreeNode("Wooden Hoe"))    ## Level 2 for Hoes
    hoes.add_child(TreeNode("Stone Hoe"))  
    hoes.add_child(TreeNode("Iron Hoe")) 
    hoes.add_child(TreeNode("Gold Hoe")) 
    hoes.add_child(TreeNode("Diamonds Hoe")) 
        
    root.add_child(swords)
    root.add_child(pickaxes)
    root.add_child(axes)
    root.add_child(shovels)
    root.add_child(hoes)


    return root

if __name__ == "__main__":
    root = tools_tree()
    root.print_tree()


