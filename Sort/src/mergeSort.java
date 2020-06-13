import java.util.Arrays;

public class mergeSort {
	
    public void mergeHelper(int[] left, int[] right, int[] x) {
        int i = 0;
        int j = 0;
        int k = 0;
        
    	while(i < left.length && j < right.length) {
    	    if(left[i] <= right[j]) {
    	    	x[k] = left[i];
    	    	i++;
    	    	k++;
    	    }
    	    else {
    	    	x[k] = right[j];
    	    	j++;
    	    	k++;
    	    }
    	}
    	
    	while(i < left.length) {
    		x[k] = left[i];
    		i++;
    		k++;
    	}
    	
    	while(j < right.length) {
    		x[k] = right[j];
    		j++;
    		k++;
    	}
    }
    
    public int[] merge(int[] x) {
    
    	int middle = x.length / 2;
    	int[] left = new int[middle];
    	int[] right = new int[x.length - middle];
    	
    	if(x.length == 1) {
    		return x;
    	}
    	
    	//left array
    	for(int i = 0; i < middle; i++) {
    	    left[i] = x[i];
    	}
    	
    	//right array
    	int i = 0;
    	for(int j = middle; j < x.length; j++) {   		
    		right[i] = x[j];  
    		i++;
    	}
    	
    	merge(left);
    	merge(right);
    	mergeHelper(left,right, x);
		return x;
    	
    }
    
    /*public static void main(String[] args) {
    	mergeSort test = new mergeSort();
    	int[] array = {-1,7,5};
    	System.out.println(Arrays.toString(test.merge(array)));
    	
    }*/
}
