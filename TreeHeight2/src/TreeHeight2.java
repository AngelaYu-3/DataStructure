import java.util.*;
import java.time.LocalTime;
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
		boolean isLeaf;
		int nodeHeight;
		
		Node(int data){	
			this.data = data;
			this.parent = null;
			this.isLeaf = true;
			this.nodeHeight = 0;
		}
	}
	
	public class height {
		int n;
		int parent[];
		int numLeaf = 0;
		Node tree[];
		
		void read() throws IOException {
			//FastScanner in = new FastScanner();
			//n = in.nextInt();
			FastScanner in = new FastScanner();
			n = in.nextInt();
			parent = new int[n];
			tree = new Node[n];
			for (int i = 0; i < n; i++) {
				parent[i] = in.nextInt();	
				Node node = new Node(i);
				tree[i] = node;
			    //System.out.println(Arrays.toString(parent));
			}
			
			//testing harder cases--reading files
			/*int i = 0;
			 try {
			      File myObj = new File("23.txt");
			      Scanner myReader = new Scanner(myObj);
			      while (myReader.hasNextLine()) {
			        String data = myReader.nextLine();
			        String[] arr = data.split(" ");
			        for(String a : arr) {
			        	int x = Integer.parseInt(a);	
						parent[i] = x;	
						Node node = new Node(i);
						tree[i] = node;
						i++;		        	
			        }
			        //System.out.println(data);
			      }
			      myReader.close();
			    } catch (FileNotFoundException e) {
			      System.out.println("An error occurred.");
			      e.printStackTrace();
			    }			
			    //System.out.println(Arrays.toString(parent));*/
			}
		
		void tree() {
			//creating array with nodes
		    /*for(int i = 0; i < n; i++) {
		       int data = i;
		       Node node = new Node(data);
		       tree[i] = node;
		    }*/
		    
		    //printing values of tree
		    /*for(int i = 0; i < n; i++) {
		    	System.out.println(tree[i].data);
		    }*/
		    
		    //linking tree[] parent pointer
		    for(int i = 0; i < n; i++) {
		    	int p = parent[i];	
		    	
		    	if(p != -1) {
		    		tree[i].parent = tree[p];
		    		tree[p].isLeaf = false;
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
			height = 1;
			while(x.parent != null) {
				//System.out.print("2");
				height++;
				x = x.parent;
				if(height <= x.nodeHeight) {
					break;
				}
				else {
					x.nodeHeight = height;
				}
			}
		    return height;
		    //while()	       
		}
		
		int computeHeight() {
			for(int i = 0; i < n; i++) {
				if(tree[i].isLeaf == true) {
					numLeaf++;
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
	LocalTime now = LocalTime.now();
    System.out.println(now);
    
	TreeHeight2 test = new TreeHeight2();
	height test2 = test.new height(); 
	
	test2.read();
	now = LocalTime.now();
    System.out.println(now);
    
	test2.tree();
	now = LocalTime.now();
    System.out.println(now);
	System.out.println(test2.computeHeight());
	now = LocalTime.now();
    System.out.println(now);
    System.out.println(test2.numLeaf);
	}
}


