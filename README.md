# Mastermind
En tall-versjon av det populære gjette-spillet

## Hvordan bruke?
`$ python3 Mastermind.py`

## Eksempel-kjøring
Code: [# # # #]

Welcome to Mastermind!
- Black circle = one guessed num is correct,
  and is in the RIGHT place
- White circle = one guessed num is correct,
  but is in the WRONG place
- The code concists of 4 digits from 0-9
- Type 'q' to give up
 ┌─────────┐
 │ ¤ ¤ ¤ ¤ │
 ├─────────┤
 ├ ERROR   ┼ You need to type 4 digits
 ├ 1 2 3 4 ┼ ○ ○ 
 ├ 1 2 5 6 ┼ ○ 
 ├ 3 4 7 8 ┼ ● ○ 
 ├ 3 4 9 0 ┼ ● ○ 
 ├ 3 4 3 4 ┼ ● ○ ○ 
 ├ 3 3 4 4 ┼ ● ● ○ 
 ├ 3 9 4 4 ┼ ● ● 
 ├ 3 7 4 1 ┼ ● ● 
 ├ 3 3 4 8 ┼ ● ● ○ 
 ├ 3 4 4 8 ┼ ● ● 
 ├ 3 8 4 3 ┼ ● ● ● 
 ├ 1 1 1 1 ┼ 
 ├ 2 2 2 2 ┼ 
 ├ ERROR   ┼ You need to type 4 digits
 ├ 3 3 3 3 ┼ ● ● 
 ├ 4 4 4 4 ┼ ● 
 ├ 5 5 5 5 ┼ 
 ├ 6 6 6 6 ┼ ● 
 ├ 3 6 4 3 ┼ ● ● ● ● 
 ├─────────┤
 │ 3 6 4 3 │
 └─────────┘
You guessed the code correctly!
You used 18 guesses.
