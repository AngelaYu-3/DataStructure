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
		Node next;
		Node child;
		
		Node(int data){
			this.next = null;	
			this.child = null;
		}
	}
	
	public class height {
		int n;
		int parent[];
		int root;
		
		void read() throws IOException {
			FastScanner in = new FastScanner();
			n = in.nextInt();
			parent = new int[n];
			for (int i = 0; i < n; i++) {
				parent[i] = in.nextInt();
			    //System.out.println(Arrays.toString(parent));
			}
		}
		
		void computeHeight() {
			//creating a linked list
			Node n1 = new Node(n-1);
		    for(int i = n-2; i < 0; i --) {
		    	Node node = new Node(i);
		    	node.next = n1;
		    	n1 = node;
		    }
		    
		    
		}

     }
	
static public void main(String[] args) throws IOException {
	TreeHeight2 test = new TreeHeight2();
	height test1 = test.new height(); 
	test1.read();
	test1.computeHeight();
	}}

