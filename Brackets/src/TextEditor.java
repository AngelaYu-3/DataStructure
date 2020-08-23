import java.util.Stack;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

/*2D array enter in i value into respective 2D array for
 * each different bracket (different row for different bracket)
 * then go through array if array not empty to find first index where there's discrepancy (lowest number i)
 */

public class TextEditor {
    
	Stack<Bracket> Brackets = new Stack<Bracket>();
	String input;
	/*Stack<Integer> leftOut = new Stack<Integer>();
	Stack<Integer> leftBlock = new Stack<Integer>();
	Stack<Integer> leftCurly = new Stack<Integer>();*/
	
	Scanner scan = new Scanner(System.in);
	
	public TextEditor() {
	    System.out.print("Please enter in a string with brackets or hit q to quit: ");
	    String result = scan.nextLine();
	    
	    if(result.equals("q")){
	    	System.out.printf("\nProcess finished with exit code 0");
    		System.exit(0);
	    }
	    
	    //!result.contains("(") is the same as result.contains("(") == false
	    while(!result.contains("(") && !result.contains(")") && !result.contains("[")
	    		&& !result.contains("]") && !result.contains("{") && !result.contains("}")) {	
	    	
	    	System.out.print("No brackets detected. Please enter in a string with brackets or hit q to quit: ");
	    	result = scan.nextLine();
	    }
	   
	    input = result;
	    
	}
	
	
	
	public void isSuccess() {
		boolean result = true;
		int i;
		
	    for(i = 0; i < input.length(); i++) {
	    	char inputC = input.charAt(i);
	    	
	    	switch(inputC) {
	    	case '(':
	    	    Bracket open = new Bracket(0,i);
	    	    Brackets.push(open);
	    	    break;
	    	    
	    	case '[':
	    		Bracket box = new Bracket(1,i);
	    		Brackets.push(box);
	    		break;
	    		
	    	case '{':
	    		Bracket curly = new Bracket(2,i);
	    		Brackets.push(curly);
	    		break;
	    		
	    	case ')':
	    		result = rightBracket(0,i);
	    		break;
	    		
	    	case ']':
	    		result = rightBracket(1,i);
	    		break;
	    		
	    	case '}':
	    		result = rightBracket(2,i);
	    		break;
	    	
	    	default:
	    		continue;
	    	} 
	    	
	    	if(result == false) {
	    		break;	
	    	}
	    } 
	    
	    if(result == false) {
	    	System.out.println("Error at: " + i);	
	    }
	    
	    else {
	    	if(Brackets.isEmpty() ) {
		    	System.out.println("Success");
		    }
		    else {
		    	int x = Brackets.firstElement().index;
		    	System.out.println("Error at: " + (x + 1));
		    }	
	    }
	    
	    
	}
	    
	    public boolean rightBracket(int target, int index){
	        if(Brackets.isEmpty()) {
	        	return false;
    		}
    		else {
    			Bracket peek = Brackets.peek();
	    		int type = peek.type;	
	    		
	    		if(type == target) {
	    			Brackets.pop();
	    			return true;
	    		}
	    		else {
	    			return false;
	    		}
    		}	
	   }
	    
		/*int result = 0;
		
		for(int i = 0; i < input.length(); i++) {
			
			if((input.charAt(i) == '(')) {
			    leftOut.push(i);	 
			}
			
			else if((input.charAt(i) == '[')) {
			    leftBlock.push(i);	
			}
			
			else if((input.charAt(i) == '{')) {
			    leftCurly.push(i);	
			}
			
			else if((input.charAt(i) == ')')) {				
			    if(leftOut.isEmpty()) {
			    	result = i + 1;
			    	System.out.println("Error at: " + i);
			    	break;
			    }
			    else {
			    	leftOut.pop();
			    }
				    
		    }
			
			else if((input.charAt(i) == ']')) {				
			    if(leftBlock.isEmpty()) {
			    	result = i + 1;
			    	System.out.println("Error at: " + i);
			    	break;
			    }
			    else {
			    	leftBlock.pop();
			    }
				    
		    }
			
			else if((input.charAt(i) == '}')) {				
			    if(leftCurly.isEmpty()) {
			    	result = i + 1;
			    	System.out.println("Error at: " + i);
			    	break;
			    }
			    else {
			    	leftCurly.pop();
			    }
				    
		    }
			
		}
		
		if(leftOut.isEmpty() && leftBlock.isEmpty() && leftCurly.isEmpty() && result == 0 ) {
		    System.out.println("Success");	
		}
		else if(result == 0){
		    //out brackets
			int open = -1;
			int block = -1;
			int curly = -1;
			
			if(!leftOut.isEmpty()) {
				open = leftOut.firstElement();	
			}
			if(!leftBlock.isEmpty()) {
				block = leftBlock.firstElement();	
			}
			if(!leftCurly.isEmpty()) {
				curly = leftCurly.firstElement();	
			}
			
			
			int min[] = {open, block, curly};
			
			int x = 0;
			if(open != -1) {
				x = open;	
			}
			else if(block != -1) {
				x = block;	
			}
			else {
				x = curly;
			}
			
			for (int i = 0; i < min.length; i++ ) {
				if(min[i] != -1 && min[i] < x ) {
					x = min[i];
				}
				else {
					continue;
				}
			}
			
			System.out.println("Error at: " + x);
			
		}
		
	}*/
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		do {
			 TextEditor test = new TextEditor();
			 test.isSuccess();
		}while(true);   
	}
}