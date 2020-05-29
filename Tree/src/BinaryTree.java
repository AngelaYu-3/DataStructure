public class BinaryTree {
	
	private Node root;
	
    private static class Node{
    	Node left;
    	Node right;
    	int data;
    	
    	Node(int data){
    	    this.data = data;
    	    left = null;
    	    right = null;
    	}
    }
    
    //creating empty binary tree
    public BinaryTree() { 
    	root = null;
    }
    
    //user lookUp
    public boolean lookUp(int data) {
        return lookUp(root, data);	
    }
    
    //through left and right subtrees to check data
    private boolean lookUp(Node node, int data) {
    	if(node == null) {
    		return false;
    	}
    	else if(data == node.data) {
    		return true;
    	}
    	else {
    		if(data < node.data) {
        		return lookUp(node.left, data);
        	}
    		else {
        		return lookUp(node.right, data);
        	}	
    	}	
    }
    
    //user insert
    public void insert(int data) {
        root = insert(root,data);	
    }
    
    //left subtree less than root right subtree greater than
    private Node insert(Node node, int data) {
        if(node == null) {
            node = new Node(data);	
        }
        else {
        	if(data < node.data) {
        		insert(node.left, data);
        	}
        	
        	else {
            	insert(node.right,data);
            }
        }
        return node;	
     }
        

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

