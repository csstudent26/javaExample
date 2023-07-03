package tests;

import java.util.Arrays;
import java.util.Collections;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;
import java.util.List;




import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.ArrayList;
class EncryptiontTestT {
	
	
    private EncryptionT encryption;


	@BeforeEach
	void setUp() throws Exception {
		
        encryption = new EncryptionT();
        encryption.newKey(); // Generate a new key for each test

		
	}
	
	
	

	
	
		@Test
		void testEncrypt() {
		    String message = "Hello";
		 //   String message = "Hello, World!";

		  //  String expectedEncryptedMessage = "}]00$";
		    String expectedEncryptedMessage = "elHHd";


		    EncryptionT encryption = new EncryptionT();
		    encryption.list = new ArrayList<>(Arrays.asList('H', 'e', 'l', 'l', 'o'));
		  //  encryption.shuffledList = new ArrayList<>(Arrays.asList('}', ']', '0', '0', '$'));
		    encryption.shuffledList = new ArrayList<>(Arrays.asList('e', 'l', 'H', 'H', 'd'));

		    
		    
		  
		  
		    
		    System.out.println(encryption.shuffledList);
		    



		    encryption.encrypt();

		    String actualEncryptedMessage = encryption.getEncryptedMessage();
		    

		    
		    System.out.println("Actual encrypted message: " + actualEncryptedMessage);

		    
		    assertEquals(expectedEncryptedMessage, actualEncryptedMessage);
		}

	

	
		
		@Test
		void testDecrypt() {
		    String encryptedMessage = "elHHd";
		    String expectedDecryptedMessage = "Hello";

		    EncryptionT encryption = new EncryptionT();
		    encryption.list = new ArrayList<>(Arrays.asList('H', 'e', 'l', 'l', 'o'));
		    encryption.shuffledList = new ArrayList<>(Arrays.asList('e', 'l', 'H', 'H', 'd'));

		    encryption.setEncryptedMessage(encryptedMessage);
		    encryption.decrypt();

		    String actualDecryptedMessage = encryption.getDecryptedMessage();

		    System.out.println("Actual decrypted message: " + actualDecryptedMessage);

		    assertEquals(expectedDecryptedMessage, actualDecryptedMessage);
		}


}
