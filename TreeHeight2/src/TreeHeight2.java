import java.util.*;
import java.io.*;


public class TreeHeight2 {
	class FastScanner {
		StringTokenizer tok = new StringTokenizer("");
		BufferedReader in;

		FastScanner() {
			in = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() throws IOException {
			while (!tok.hasMoreElements())
				tok = new StringTokenizer(in.readLine());
			return tok.nextToken();
		}
		int nextInt() throws IOException {
			return Integer.parseInt(next());
		}
	}
	
	class Node {
		Node childL;
		Node childR;
		int data;
		
		Node(int data){	
			this.data = data;
			this.childL = null;
			this.childR = null;
		}
		
		void child(Node node) {
		    node ;	
		}
	}
	
	public class height {
		int n;
		int parent[];
		Node tree[];
		Node root;
		
		void read() throws IOException {
			FastScanner in = new FastScanner();
			n = in.nextInt();
			parent = new int[n];
			for (int i = 0; i < n; i++) {
				parent[i] = in.nextInt();
			    //System.out.println(Arrays.toString(parent));
			}
		}
		
		void tree() {
			//creating array with nodes
			tree = new Node[n];
		    for(int i = 0; i < n; i++) {
		       int data = i;
		       Node node = new Node(data);
		       tree[i] = node;
		    }
		    
		    //printing values of tree
		    /*for(int i = 0; i < n; i++) {
		    	System.out.println(tree[i].data);
		    }*/
		    
		    //linking tree[] child pointer
		    for(int i = 0; i < n; i++) {
		    	int p = parent[i];	
		    	if (p == -1){
		    		root = tree[i];
		    	}
		    	else {
		    		
		    		if(tree[p].childL == null) {
		    			tree[p].childL = tree[i];
		    		}
		    		else {
		    			tree[p].childR = tree[i];
		    		}		    			
		    	}		    	
		    }
		    
		    //printing tree with left and right children
		    for(int i = 0; i < n; i++) {
		    	//-1 means no children
		    	int left = -1;
		    	int right = -1;
		    	if(tree[i].childL != null) {
		    		left = tree[i].childL.data;
		    	}
		    	if(tree[i].childR != null) {
		    		right = tree[i].childR.data;
		    	} 		
		    	System.out.println(tree[i].data + " L: " + left + " R: " + right);		    	
		    }
		}
		
		int maxHeight = 1;
		int height = 1;
		
		int computeHeight(Node x) {	
			if(x.childL == null && x.childR == null) {
				//System.out.println(height);
			    maxHeight = Math.max(maxHeight, height); 
			}
			else {
			   height++;
			   //System.out.println(height);
			   if(x.childL != null) {
				  computeHeight(x.childL);  
			   }
			   if(x.childR != null) {
				  computeHeight(x.childR);  
			   }
			   //height = 1;
			   
			}
		    return maxHeight;
		    //while()
		       
		}

     }
	
static public void main(String[] args) throws IOException {
	TreeHeight2 test = new TreeHeight2();
	height test2 = test.new height(); 
	test2.read();
	test2.tree();
	System.out.println(test2.computeHeight(test2.root));
	}}

