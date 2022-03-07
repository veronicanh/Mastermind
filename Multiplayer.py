from Mastermind import Mastermind
import sys


class Multiplayer(Mastermind):
    def __init__(self):
        super().__init__(4)

        # Get code as input from player 1
        self._code = []
        inp = input("Type in secret code: ").strip().replace(" ", "").replace(",", "")
        for siffer in inp:
            self._code.append(int(siffer))


        # Hide typed code
        sys.stdout.write("\033[F")
        print("Type in secret code: # # # #")

def main():
    m = Multiplayer()
    m.spill()

if (__name__ == "__main__"):
    main()
