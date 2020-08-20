import java.util.Arrays;

public class mergeSort {
	
    public void mergeHelper(int[] left, int[] right, int[] array) {
        int leftIdx = 0;
        int rightIdx = 0;
        int sortIdx = 0;
        
    	while(leftIdx < left.length && rightIdx < right.length) {
    	    if(left[leftIdx] <= right[rightIdx]) {
    	    	array[sortIdx] = left[leftIdx];
    	    	leftIdx++;
    	    	sortIdx++;
    	    }
    	    else {
    	    	array[sortIdx] = right[rightIdx];
    	    	rightIdx++;
    	    	sortIdx++;
    	    }
    	}
    	
    	while(leftIdx < left.length) {
    		array[sortIdx] = left[leftIdx];
    		leftIdx++;
    		sortIdx++;
    	}
    	
    	while(rightIdx < right.length) {
    		array[sortIdx] = right[rightIdx];
    		rightIdx++;
    		sortIdx++;
    	}
    }
    
    public int[] merge(int[] array) {
    
    	int middle = array.length / 2;
    	int[] left = new int[middle];
    	int[] right = new int[array.length - middle];
    	
    	if(array.length == 1) {
    		return array;
    	}
    	
    	//left array
    	for(int i = 0; i < middle; i++) {
    	    left[i] = array[i];
    	}
    	
    	//right array
    	int i = 0;
    	for(int j = middle; j < array.length; j++) {   		
    		right[i] = array[j];  
    		i++;
    	}
    	
    	merge(left);
    	merge(right);
    	mergeHelper(left,right, array);
		return array;
    	
    }
    
    /*public static void main(String[] args) {
    	mergeSort test = new mergeSort();
    	int[] array = {5,5};
    	System.out.println(Arrays.toString(test.merge(array)));
    	
    }*/
}
