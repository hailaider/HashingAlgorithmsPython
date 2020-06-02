import hashlib
import secrets 
import uuid

#Global constants
X = 0 

#message to encode
message=input("Input a message: ")

#encode the message
encoded_message = message.encode()

#pick your type of hash algorithm
while X == 0:
        hashh = input("Input hash type (SHA-2,SHA-3,BLAKE2): ")
#pick between 256 and 512 bytes
        hash_type = input ("Input byte size (256 or 512): ")
        
        #converts from bytes to hexadecimal        
        #SHA2
        if hashh == "SHA-2" and hash_type == "256":
                print("Your hash is: ", hashlib.sha256(encoded_message).hexdigest())
                break
        elif hashh == "SHA-2" and hash_type == "512":
                print("Your hash is: ", hashlib.sha512(encoded_message).hexdigest())
                break
        #SHA3
        elif hashh == "SHA-3" and hash_type == "256":
                print ("Your hash is ", hashlib.sha3_256(encoded_message).hexdigest())
                break
        elif hashh == "SHA-3" and hash_type == "512":
                print ("Your hash is ", hashlib.sha3_512(encoded_message).hexdigest())
                break
        #BLAKE2b(256) or BLAKE2s(512)
        elif hashh == "BLAKE2" and hash_type == "256":
                print ("Your hash is ", hashlib.blake2s(encoded_message).hexdigest())
                break
        elif hashh == "BLAKE2" and hash_type == "512":
                print ("Your hash is ", hashlib.blake2b(encoded_message).hexdigest())
                break
        

        
        
