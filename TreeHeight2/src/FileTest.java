import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

public class FileTest {
  public static void main(String[] args) {
	//File file = new File(".");
	//for(String fileNames : file.list()) System.out.println(fileNames);
    try {
      File myObj = new File("test1.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        String[] arr = data.split(" ");
        for(String a : arr) {
        	int x = Integer.parseInt(a);
        	System.out.println(x);
        }
        //System.out.println(data);
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
}