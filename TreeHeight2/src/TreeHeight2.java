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
		Node parent;
		int data;
		boolean internal;
		
		Node(int data){	
			this.data = data;
			this.parent = null;
			this.internal = false;
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
		    
		    //linking tree[] parent pointer
		    for(int i = 0; i < n; i++) {
		    	int p = parent[i];	
		    	
		    	if(p != -1) {
		    		tree[i].parent = tree[p];
		    		tree[p].internal = true;
		    	}		    	
		    }
		    
		    //printing tree with parent
		    /*for(int i = 0; i < n; i++) {
		    	if(tree[i].parent != null) {
		    		System.out.println(tree[i].data + " P: " + tree[i].parent.data);
		    	}
		    	else {
		    		System.out.println(tree[i].data + " P: " + "null");
		    	}
		    }
		    
		    //printing leaves
		    for(int i = 0; i < n; i++) {
		    	if(tree[i].internal == false) {
		    		System.out.println(tree[i].data);
		    	}
		    }*/
		}
		
		int maxHeight = 1;
		int height = 1;
		int helperCompHeight(Node leaf) {
			Node x = leaf;
			while(x.parent != null) {
				//System.out.print("2");
				height++;
				x = x.parent;
			}
		    return height;
		    //while()	       
		}
		
		int computeHeight() {
			for(int i = 0; i < n; i++) {
				if(tree[i].internal == false) {
					height = 1;
					int pHeight = helperCompHeight(tree[i]);
					maxHeight = Math.max(pHeight, maxHeight);
				}
				else {
					continue;
				}
			}
			
			return maxHeight;
		}

     }
	
static public void main(String[] args) throws IOException {
	TreeHeight2 test = new TreeHeight2();
	height test2 = test.new height(); 
	test2.read();
	test2.tree();
	System.out.println(test2.computeHeight());
	}}


