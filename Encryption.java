package tests;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Random;
import java.util.Scanner;

import org.junit.jupiter.api.Test;

public class Encryption {
	
	

	//Adding for the getEncryptedMessage() method
    private String encryptedMessage; 
    private String decryptedMessage; 




	
	public Scanner scanner;
	public Random random;
	
	public ArrayList<Character> list;
	public ArrayList<Character> shuffledList;
	
	public char character;
	public String line;
	
	public char[] letters;
	public char[] secretLetters;
	
	ArrayList<Character> aar  = new ArrayList<Character>();
	
	
	
	Encryption(){
		
		  scanner = new Scanner(System.in);
		  random = new Random();
		  list = new ArrayList();
		  shuffledList = new ArrayList();
		  character = ' ';
		  line = " ";
		  
	//	askQuestion();
	//	getKey();
	}

	
	
	
	
	
		
	public void askQuestion() {
			char response = ' ';
			while(response != 'Q') {
			System.out.println("++++++++++++++++++++++++++++++++++++");
            System.out.println("What do you want to do? ");
            System.out.println("(N)ewKey, (G)etKey. (E)ncrypt, (D)crypt, (Q)uit");
             response = Character.toUpperCase(scanner.nextLine().charAt(0));
            
            switch(response) {
            
            case 'N' :
            	
            	newKey();
            	break;
            	
            case 'G' :
            	
            	getKey();
            	break;
            	
            case 'E' :
            	
            	encrypt();
            	break;
            	
            case 'D' :
            	
            	decrypt();
            	break;
            	
            case 'Q' :
            	
            	quit();
            	break;
            	
            default:
            	
            	System.out.println("Not a valid Answer");
            	
            	
            	
            }
            
			}
            	
            	
          
}
	
	public void newKey() {
		
		System.out.println("This is newKey");
		
		character = ' '+ 1;
		list.clear();
		shuffledList.clear();
		
		for(int i = 32; i< 127; i++) {
			
			list.add(Character.valueOf(character));
			character++;
		}
		
		    shuffledList = new ArrayList(list);
		    Collections.shuffle(shuffledList);
		    
		    System.out.println("A new key has being Generated");
	}
	      
	
	public void getKey() {
		
		System.out.println("The Key is: ");
		
			for(Character x : list) {
				System.out.print(x);
			}
		
			System.out.println();

		System.out.println("The new Key is: ");
		
		    for(Character x : shuffledList) {
				System.out.print(x);
			}
		
		System.out.println();
		
	}
	

	
	public void encrypt() {
		
		System.out.println("Enter a message to br Encrypted");
	
		String message = scanner.nextLine();
		       letters = message.toCharArray();
		for(int i = 0; i < letters.length;i++) {
			
			for(int j = 0; j < list.size(); j++) {
			if(letters[i]== list.get(j)) {
				letters[i]= shuffledList.get(j);
				//Here we are INTITIONALLY Commenting-out the 'break' Statement
				//break;
				
			}
		}
	 }
        encryptedMessage = new String(letters); // Store the encrypted message

		System.out.println("The encrypted message is : ");
		
		for(char x : letters) {
			System.out.print(x);
		}
	}//End of encrypt()
	     
	
	public void decrypt() {
		
		System.out.println("Enter a message to be Decrypted");
		
		String message = scanner.nextLine();
		       letters = message.toCharArray();
		for(int i = 0; i < letters.length;i++) {
			
			for(int j = 0; j < shuffledList.size(); j++) {
			if(letters[i]== shuffledList.get(j)) {
				letters[i]= list.get(j);
				
				//Here we are INTITIONALLY Commenting-out the 'break' Statement
				//break;
			}
		}
	 }
	    decryptedMessage = new String(letters);

		System.out.println("The decrypted message is : ");
		
		for(char x : letters) {
			System.out.print(x);
		}
		
}//End of decrypt()
	
	public void quit() {
		System.out.println("Ok that was the Endrypton Program. \n Hope you enjoyed");
		
		System.exit(0);
	}

	public String getEncryptedMessage() {
		// TODO Auto-generated method stub
	    return encryptedMessage;

	}
	
	  public void setEncryptedMessage(String encryptedMessage) {
	        this.encryptedMessage = encryptedMessage;
	    }
	  
	  public String getDecryptedMessage() {
	        return decryptedMessage;
	    }

	
	
	
	
	

}





