###	Brute force password break to 7zip with perl
##	Disclaimer
This script has the single pourpose of education. Its only to learn more about computing and cyber security.
Author does not take responsability for (neither agree to) any other application of this work.
##	Goals
- Show how a 7zip password may be broken using brute force
##	Software in use
- p7zip: It may compress and extract the files from zip, support encryptation
- perl
##	How it works
1.	Create a 7zip encrypted file, with an easy password (otherwise it may take days!). I may let another script to do it automaticly.
2.	Use the bruteforce algorithm to break it.
##	Best practice
- Longer passwords takes exponencial more time for each characters lenght added: pick very short passwords (max 4 chars)
- Only-numbers passwords break much faster also
