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
			    //System.out.println(Arrays.toString(parent));
			}
		}
		
		//checking if value in array
		boolean useLoop(int[] arr, int i) {
			for(int s: arr){
				if(s == i)
					return true;
			}
			return false;
		}
		
		int computeHeight() {
			//checking which values are leaves
		    leaf = new int[n];
		    ArrayList<Integer> height = new ArrayList<>();
		    
		    for( int i = 0; i < n; i++) {
		    	boolean check = useLoop(parent, i);
		    	//System.out.println(check);
		    	if (check == false){
		    	   leaf[i] = 1;	//there is a leaf
		    	}
		    	else {
		    	   leaf[i] = 0; //no leaf
		    	}
		    }
		    //System.out.println(Arrays.toString(leaf));
		    
		    //finding height from each leaf
		    for(int i = 0; i < n; i++) {
		    	if(leaf[i] == 1) {
		    	   int h = 0;
		    	   for(int j = i; j != -1; j = parent[j]) {
		    	       h++;   
		    	   }
		    	   height.add(h);
		    	}
		    	else {
		    		continue;
		    	}
		    	
		    	
		    }
		    /*for(int x = 0; x < height.size(); x++) {
	    	    System.out.println(height.get(x));	
	    	}*/
		    
		    //finding max height from all leaf heights
		    int maxHeight = 0;
		    for(int i = 0; i < height.size(); i++) {
		        int max = Math.max(maxHeight, height.get(i));
		        maxHeight = max;
		    }
		    //System.out.println(maxHeight);
		    return maxHeight;
		    
		}

     }
	
static public void main(String[] args) throws IOException {
	TreeHeight test = new TreeHeight();
	height test1 = test.new height(); 
	test1.read();
	System.out.println(test1.computeHeight());
	}}
