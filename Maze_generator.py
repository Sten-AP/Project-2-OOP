from colorama import init, Fore
import random
init()


class Maze:
    def __init__(self):
        self.maze = []

    def grid(self, breedte, hoogte):
        self.hoogte = hoogte
        self.breedte = breedte
        for i in range(self.hoogte):
            rij = []
            for j in range(self.breedte):
                rij.append('█')
            self.maze.append(rij)

    def in_en_uitgang(self):
        self.ingang = []
        self.uitgang = []
        self.rndX = []
        self.rndY = []
        self.kantIenU = []
        hetzelfde = True

        while (hetzelfde):
            for i in range(2):
                # kant van doolhof
                self.kantIenU.append(random.randrange(0, 4))

                # boven
                if self.kantIenU[i] == 0:
                    self.rndX.append(random.randrange(2, self.breedte-2))
                    self.rndY.append(0)
                # rechts
                elif self.kantIenU[i] == 1:
                    self.rndY.append(random.randrange(2, self.hoogte-2))
                    self.rndX.append(0)
                # onder
                elif self.kantIenU[i] == 2:
                    self.rndX.append(random.randrange(2, self.breedte-2))
                    self.rndY.append(0)
                # links
                elif self.kantIenU[i] == 3:
                    self.rndY.append(random.randrange(2, self.hoogte-2))
                    self.rndX.append(0)

            if self.rndY[0] != self.rndY[1] and self.rndX[0] != self.rndX[1]:
                hetzelfde = False
            else:
                self.kantIenU.clear()
                self.rndX.clear()
                self.rndY.clear()

        # ingang
        if self.kantIenU[0] == 0:
            self.ingang.append(0)
            self.ingang.append(self.rndX[0])
        elif self.kantIenU[0] == 1:
            self.ingang.append(self.rndY[0])
            self.ingang.append(self.breedte-1)
        elif self.kantIenU[0] == 2:
            self.ingang.append(self.hoogte-1)
            self.ingang.append(self.rndX[0])
        elif self.kantIenU[0] == 3:
            self.ingang.append(self.rndY[0])
            self.ingang.append(0)

        self.maze[self.ingang[0]][self.ingang[1]] = '▓'

        # uitgang
        if self.kantIenU[1] == 0:
            self.uitgang.append(0)
            self.uitgang.append(self.rndX[1])
        elif self.kantIenU[1] == 1:
            self.uitgang.append(self.rndY[1])
            self.uitgang.append(self.breedte-1)
        elif self.kantIenU[1] == 2:
            self.uitgang.append(self.hoogte-1)
            self.uitgang.append(self.rndX[1])
        elif self.kantIenU[1] == 3:
            self.uitgang.append(self.rndY[1])
            self.uitgang.append(0)

        self.maze[self.uitgang[0]][self.uitgang[1]] = '▒'

    def genereer_wegen(self):
        weg = '░'

        if self.kantIenU[0] == 0:
            self.maze[self.ingang[0]+1][self.ingang[1]] = weg
        elif self.kantIenU[0] == 1:
            self.maze[self.ingang[0]][self.ingang[1]-1] = weg
        elif self.kantIenU[0] == 2:
            self.maze[self.ingang[0]-1][self.ingang[1]] = weg
        elif self.kantIenU[0] == 3:
            self.maze[self.ingang[0]][self.ingang[1]+1] = weg

        if self.kantIenU[1] == 0:
            self.maze[self.uitgang[0]+1][self.uitgang[1]] = weg
        elif self.kantIenU[1] == 1:
            self.maze[self.uitgang[0]][self.uitgang[1]-1] = weg
        elif self.kantIenU[1] == 2:
            self.maze[self.uitgang[0]-1][self.uitgang[1]] = weg
        elif self.kantIenU[1] == 3:
            self.maze[self.uitgang[0]][self.uitgang[1]+1] = weg

        for i in range(5):
            # 0 = rechts, 1 = links, 2 = recht door
            rndWeg = random.randrange(0, 3)
            if i % 2 == 0:
                if rndWeg == 0:
                    if self.kantIenU[0] == 0:
                        self.maze[self.ingang[0]+1][self.ingang[1]+1] = weg
                    elif self.kantIenU[0] == 1:
                        self.maze[self.ingang[0]-1][self.ingang[1]-1] = weg
                    elif self.kantIenU[0] == 2:
                        self.maze[self.ingang[0]-1][self.ingang[1]+1] = weg
                    elif self.kantIenU[0] == 3:
                        self.maze[self.ingang[0]+1][self.ingang[1]+1] = weg
                elif rndWeg == 1:
                    if self.kantIenU[0] == 0:
                        self.maze[self.ingang[0]+1][self.ingang[1]-1] = weg
                    elif self.kantIenU[0] == 1:
                        self.maze[self.ingang[0]+1][self.ingang[1]-1] = weg
                    elif self.kantIenU[0] == 2:
                        self.maze[self.ingang[0]-1][self.ingang[1]-1] = weg
                    elif self.kantIenU[0] == 3:
                        self.maze[self.ingang[0]-1][self.ingang[1]+1] = weg
                elif rndWeg == 2:
                    if self.kantIenU[0] == 0:
                        self.maze[self.ingang[0]+2][self.ingang[1]] = weg
                    elif self.kantIenU[0] == 1:
                        self.maze[self.ingang[0]][self.ingang[1]-2] = weg
                    elif self.kantIenU[0] == 2:
                        self.maze[self.ingang[0]-2][self.ingang[1]] = weg
                    elif self.kantIenU[0] == 3:
                        self.maze[self.ingang[0]][self.ingang[1]+2] = weg
            elif i % 1 == 0:
                if rndWeg == 0:
                    if self.kantIenU[1] == 0:
                        self.maze[self.uitgang[0]+1][self.uitgang[1]+1] = weg
                    elif self.kantIenU[1] == 1:
                        self.maze[self.uitgang[0]-1][self.uitgang[1]-1] = weg
                    elif self.kantIenU[1] == 2:
                        self.maze[self.uitgang[0]-1][self.uitgang[1]+1] = weg
                    elif self.kantIenU[1] == 3:
                        self.maze[self.uitgang[0]+1][self.uitgang[1]+1] = weg
                elif rndWeg == 1:
                    if self.kantIenU[1] == 0:
                        self.maze[self.uitgang[0]+1][self.uitgang[1]-1] = weg
                    elif self.kantIenU[1] == 1:
                        self.maze[self.uitgang[0]+1][self.uitgang[1]-1] = weg
                    elif self.kantIenU[1] == 2:
                        self.maze[self.uitgang[0]-1][self.uitgang[1]-1] = weg
                    elif self.kantIenU[1] == 3:
                        self.maze[self.uitgang[0]-1][self.uitgang[1]+1] = weg
                elif rndWeg == 2:
                    if self.kantIenU[1] == 0:
                        self.maze[self.uitgang[0]+2][self.uitgang[1]] = weg
                    elif self.kantIenU[1] == 1:
                        self.maze[self.uitgang[0]][self.uitgang[1]-2] = weg
                    elif self.kantIenU[1] == 2:
                        self.maze[self.uitgang[0]-2][self.uitgang[1]] = weg
                    elif self.kantIenU[1] == 3:
                        self.maze[self.uitgang[0]][self.uitgang[1]+2] = weg

    def print_maze(self):
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[0])):
                if self.maze[i][j] == '█':
                    print(Fore.WHITE, f'{self.maze[i][j]}', end="")
                elif self.maze[i][j] == '▓':
                    print(Fore.YELLOW, f'{self.maze[i][j]}', end="")
                elif self.maze[i][j] == '▒':
                    print(Fore.GREEN, f'{self.maze[i][j]}', end="")
                else:
                    print(Fore.LIGHTBLACK_EX, f'{self.maze[i][j]}', end="")
            print('\n')
