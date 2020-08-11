import java.util.*;
import java.io.*;


public class TreeHeight {
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
	
	public class height {
		int n;
		int parent[];
		int leaf[];
		
		void read() throws IOException {
			FastScanner in = new FastScanner();
			n = in.nextInt();
			parent = new int[n];
			for (int i = 0; i < n; i++) {
				parent[i] = in.nextInt();
			}
		}
		
		void computeHeight() {
			//checking which values are leaves
		    leaf = new int[n];
		    for( int i = 0; i < n; i++) {
		    	boolean check = Arrays.asList(parent).contains(i);
		    	if (check == true){
		    	   leaf[i] = 0;	
		    	}
		    	else {
		    		leaf[i] = 1;
		    	}
		    }
		    System.out.println(Arrays.toString(parent));
		    System.out.println(Arrays.toString(leaf));
		    
		}

     }
	
	static public void main(String[] args) throws IOException {
		TreeHeight test = new TreeHeight();
		height test1 = test.new height(); //?
		test1.computeHeight();
		
		
	}
}
