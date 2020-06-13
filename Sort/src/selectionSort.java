/**
 * Basic Sorting Algorithms 
 * This program takes a string of numbers separated by commas from the user and
 * sorts the numbers in ascending order using selection, insertion, and merge sort algorithms.
 * 
 *  @date April 9, 2020
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class selectionSort {
	Scanner in = new Scanner(System.in);
	String[] values;
	static int[] array;
	int i = 0;
	
	
	/**
	 * passes in string from user with only integers and commas
	 * prompts user for another string if invalid string (not only integers and commas)
	 * changes string to array of integers (no commas)
	 * offers option to quit with "Q" or "q"
	 */
	
	public selectionSort() {
		System.out.print("\nPlease enter in a list of integers separated by commas only or enter q to quit: ");
		String input = in.nextLine();
		input = input.replaceAll("\\s+",""); //removes all white spaces in input
		
		String regex = "[\\d, /, /-]+"; //used to see if "0-9" and "," are only present in input
		
		if(input.contentEquals("q") || input.contentEquals("Q")) {
			System.out.printf("\nProcess finished with exit code 0");
			System.exit(0);
		}
		while(!input.matches(regex)) {
			if(input.contentEquals("q") || input.contentEquals("Q")) {
				System.out.printf("\nProcess finished with exit code 0");
				System.exit(0);
				//break;
			}
			System.out.print("Please enter in a list of integers separated by commas only or enter q to quit: ");
			input = in.nextLine();
		}
		
		input = input.replaceAll("\\s+","");
		values = input.split(",");
		array = new int[values.length];
		for(String str:values) {
			array[i] = Integer.parseInt(str);
			i++;
		}
		//System.out.print(Arrays.toString(array));
	}
	
	/**
	 * selectionSort logic
	 */
	public void sort() {	    
        
		for(int i = 0; i < array.length - 1; i++) {		
			int minIndex = i;
			
			for(int j = i + 1; j < array.length; j++) {
				
				if(array[j] < array[minIndex]) {
				    minIndex = j;	
				}
			}
			
			int temp = array[i];
			array[i] = array[minIndex];
			array[minIndex] = temp;
		}
		
		System.out.println("Selection Sort: " + Arrays.toString(array));
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		do{
			selectionSort sort1 = new selectionSort();
			insertionSort sort2 = new insertionSort();
			mergeSort sort3 = new mergeSort();
			
			sort1.sort();
			sort2.sort(array);
			System.out.println("Selection Sort: " + Arrays.toString(sort3.merge(array)));
			
		}while(true);
	}

}
