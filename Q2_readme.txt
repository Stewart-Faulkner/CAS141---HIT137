# Chapter 2: The Chamber of Strings

This Python script processes strings and decrypts a cryptogram.

## String Processing

Input: `56aAww1984sktr235270aYmn145ss785fsq31D0`

Output:
- Numbers: 561984235270145785310
- Letters: aAwwsktraYmnssfsqD
- Even numbers (ASCII): [6, 8, 4, 2, 2, 0, 4, 8, 0] -> [54, 56, 52, 50, 50, 48, 52, 56, 48]
- Uppercase letters (ASCII): A, Y, D -> [65, 89, 68]

## Cryptogram Decryption

Input:
```
VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQ NG GVZRF UNEO GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYY QBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR
```

Output (Shift 13):
```
IM SELFISH IMPATIENT AND A LITTLE INSECURE I MAKE MISTAKES I AM OUT OF CONTROL AND AT TIMES HARB TO HANDLE BUT IF YOU CANT HANDLE ME AT MY WORST THEN YOU SURE AS HELL DONT DESERVE ME AT MY BEST MARILYN MONROE
```

Note: "HARB" should be "HARD" in the decrypted text.
