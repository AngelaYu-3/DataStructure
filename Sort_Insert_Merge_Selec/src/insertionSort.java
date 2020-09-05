import java.lang.reflect.Array;
import java.util.Arrays;

//hello
public class insertionSort {
	
    public void sort(int[] x) {
        for(int i = 1; i < x.length; i++){
        	
            int possibleIndex = i;
            int temp = x[i];
            
            while(temp < x[i - 1]) {
            	x[i] = x[i - 1];
            	x[possibleIndex] = temp;
            	possibleIndex--;
            }
        }
        
        System.out.println("Insertion Sort: " + Arrays.toString(x));
    }

}
