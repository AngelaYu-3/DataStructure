import java.lang.reflect.Array;
import java.util.Arrays;

public class insertionSort {
	
    public void sort(int[] x) {
        for(int i = 1; i < x.length; i++){
        	
            int possibleIndex = i;
            int temp = x[i];
            
            while((possibleIndex > 0) && (temp < x[i - 1])) {
            	x[i] = x[i - 1];
            	possibleIndex--;
            }
            x[possibleIndex] = temp;
        }
        
        System.out.println("Insertion Sort: " + Arrays.toString(x));
    }

}
