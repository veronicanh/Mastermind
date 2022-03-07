import random
import sys


class Mastermind:
    def __init__(self, codeLength):
        self._numOfguesses = 0
        self._codeLength = codeLength
        # Generate code
        self._code = []
        for i in range(self._codeLength):
            self._code.append(random.randint(0, 9))

    def getGuess(self):
        inpList = []
        inp = input(" ├ ").strip().replace(" ", "").replace(",", "")

        # Option to quit game
        if "q" in inp:
            sys.stdout.write("\033[F")
            return "q"

        # Uniform output
        inpStr = ""
        for s in inp:
            inpStr += s + " "
        sys.stdout.write("\033[F")
        print(" ├ " + inpStr + "┼", end=" ")

        for siffer in inp:
            inpList.append(int(siffer))
        return inpList

    def checkGuess(self, guess):
        if len(guess) != self._codeLength:
            raise IndexError()
        codeCopy = []
        for tall in self._code:
            codeCopy.append(tall)

        # Riktig tall og plass
        blackPegs = 0
        for i in range(self._codeLength):
            if guess[i] == self._code[i]:
                blackPegs += 1
                codeCopy.remove(guess[i])
                guess[i] = "x"  # To prevent counting in in next loop

        # Riktig tall, feil plass
        whitePegs = 0
        for i in range(len(guess)):
            if guess[i] in codeCopy:
                whitePegs += 1
                codeCopy.remove(guess[i])

        self.printHintString(blackPegs, whitePegs)
        return (blackPegs == self._codeLength)  #=All num in correct place

    def printHintString(self, blackPegs, whitePegs):
        hint = ""
        for i in range(blackPegs):
            hint += "● "
        for i in range(whitePegs):
            hint += "○ "
        print(hint)

    def spill(self):
        print("\nWelcome to Mastermind!")
        print("- Black circle = one guessed num is correct,")
        print("  and is in the right place")
        print("- White circle = one guessed num is correct,")
        print("  but is in the wrong place")
        print("- The code concists of 4 digits from 0-9")
        print("- Type 'q' to give up")

        #self._codeLength = int(input("Choose code length: "))

        print(" ┌─" + "──" * self._codeLength + "┐")
        print(" │ " + "¤ " * self._codeLength + "│")
        print(" ├─" + "──" * self._codeLength + "┤")

        vunnet = False
        ferdig = False
        while not ferdig:
            try:
                inp = self.getGuess()
                if inp == "q":
                    ferdig = True
                else:
                    vunnet = self.checkGuess(inp)
                    ferdig = vunnet
                self._numOfguesses += 1
            except Exception as e:
                self.writeErrorMessage(e)

        codeStr = ""
        for tall in self._code:
            codeStr += str(tall) + " "
        print(" ├─" + "──" * self._codeLength + "┤")
        print(" │ " + codeStr + "│")
        print(" └─" + "──" * self._codeLength + "┘")
        if vunnet:
            print("You guessed the code correctly!")
            print("You used", self._numOfguesses, "guesses.")
        else:
            print("You gave up")

    def writeErrorMessage(self, error):
        print()
        sys.stdout.write("\033[F")
        errorStr = "ERROR"
        msg = " ├ "
        for i in range(2 * self._codeLength - 1):
            if i < len(errorStr):
                msg += errorStr[i]
            else:
                msg += " "
        msg += " ┼ "

        if type(error) is IndexError:
            print(msg + "You need to type " + str(self._codeLength) +
                  " digits")
        elif type(error) is ValueError:
            print(msg + "You need to type only digits")
        else:
            print(msg + "Unown error, try again")


def main():
    codeLength = 4
    m = Mastermind(codeLength)
    m.spill()


if (__name__ == "__main__"):
    main()
