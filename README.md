# DuplicatePersonSearch

### Important Notes
Phonenumbers should be provided in the same state. The countrycode cant be matched reliable, if the country is not known. This is why it should always be provided with the countrycode or with the internal zone code.  
For example:  
012345 6789  
+4912345 6789  
They are both from germany, but wouldn't match, since we cant reliable say the '+49' is the german country code.  
For consistency parse one of them to match the same structure.

