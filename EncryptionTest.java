package tests;

import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class EncryptionTest {

	 private Encryption encryption;


		@BeforeEach
		void setUp() throws Exception {
			
	        encryption = new Encryption();
	        encryption.newKey(); // Generate a new key for each test

			
		}
		
		
		

		
		
			@Test
			void testEncrypt() {
			    String message = "Hello";
			 //   String message = "Hello, World!";

			  //  String expectedEncryptedMessage = "}]00$";
			    String expectedEncryptedMessage = "elHHd";


			    Encryption encryption = new Encryption();
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

			    Encryption encryption = new Encryption();
			    encryption.list = new ArrayList<>(Arrays.asList('H', 'e', 'l', 'l', 'o'));
			    encryption.shuffledList = new ArrayList<>(Arrays.asList('e', 'l', 'H', 'H', 'd'));

			    encryption.setEncryptedMessage(encryptedMessage);
			    encryption.decrypt();

			    String actualDecryptedMessage = encryption.getDecryptedMessage();

			    System.out.println("Actual decrypted message: " + actualDecryptedMessage);

			    assertEquals(expectedDecryptedMessage, actualDecryptedMessage);
			}


}
