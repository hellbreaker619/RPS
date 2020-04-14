import random, time, sys, os.path, math
class PPoints:
    x=0

class Cpoints:
    y=0

Pscoret = PPoints()
Cscoret = Cpoints()

if os.path.isfile('Scoresheet.txt'):

    pass
else:
    f = open('Scoresheet.txt','w+')
    f.write("Scores")
    f.close()
    f = open('Scoresheet.txt','a')
    f.write("\n")
    f.write("=============================================")
    f.close()

options = ["rock","paper","scissors"]
def start():
    name = input("Whats your name? ")
    if name == "admin":
        replace = input("reset game? ".lower())

        if replace == "yes" or "y":
                f = open('Scoresheet.txt','w+')
                f.write("Scores")
                f.close()
                f = open('Scoresheet.txt','a')
                f.write("\n")
                f.write("=============================================")
                f.close()
                start()
        else:
            start()

    print ("welcome", name,"to ROCK PAPER SCISSORS SHOWDOWN!!!")
    def main():
        Ready = input("Are you ready? (y/n)\n")

        if Ready =="y" :

            def game():

                your_choice=input("Choose your fighter: ".lower())
                My_choice= random.choice(options)
                print("I chose: ",My_choice)

                if My_choice==your_choice :
                    print("It's a tie!")
                    again = input("want to continue? y/n\n")
                    if again == "y":
                        game()
                    else:
                        if Pscoret.x==0 and Cscoret.y==0:
                            exit()

                        else:

                            f=open('Scoresheet.txt','a')
                            f.write("\n")
                            f.write("Com")
                            f.write(".....")
                            f.write(str(Cscoret.y))
                            f.write(" ")
                            f.write(name)
                            f.write(".....")
                            f.write(str(Pscoret.x))

                            f.close()
                            exit()

                elif My_choice=="rock" and your_choice=="paper":
                    print("YOU WIN!!")
                    Pscoret.x = Pscoret.x + 1
                    Cscoret.y = Cscoret.y + 0
                    Ptext = (name," ",Pscoret.x ," wins")
                    Ctext = ("com",Cscoret.y," wins")
                    print("you have ",Pscoret.x ," points\n","I have ",Cscoret.y," points")

                    again = input("want to continue? y/n\n")
                    if again == "y":
                        game()
                    else:
                        if Pscoret.x==0 and Cscoret.y==0:
                            exit()

                        else:

                            f=open('Scoresheet.txt','a')
                            f.write("\n")
                            f.write("Com")
                            f.write(".....")
                            f.write(str(Cscoret.y))
                            f.write(" ")
                            f.write(name)
                            f.write(".....")
                            f.write(str(Pscoret.x))

                            f.close()
                            exit()


                elif My_choice=="scissors" and your_choice=="rock":
                        print("YOU WIN!!")
                        Pscoret.x  = Pscoret.x + 1
                        Cscoret.y = Cscoret.y+ 0
                        Ptext = (name," ",Pscoret.x ," wins")
                        Ctext = ("com",Cscoret.y," wins")
                        print("you have ",Pscoret.x ," points\n","I have ",Cscoret.y," points")

                        again = input("want to continue? y/n\n")
                        if again == "y":
                            game()
                        else:
                            if Pscoret.x==0 and Cscoret.y==0:
                                exit()

                            else:

                                f=open('Scoresheet.txt','a')
                                f.write("\n")
                                f.write("Com")
                                f.write(".....")
                                f.write(str(Cscoret.y))
                                f.write(" ")
                                f.write(name)
                                f.write(".....")
                                f.write(str(Pscoret.x))

                                f.close()
                                exit()


                elif My_choice=="paper" and your_choice=="scissors":
                    print("YOU WIN!!")
                    Pscoret.x  = Pscoret.x + 1
                    Cscoret.y = Cscoret.y+ 0
                    Ptext = (name," ",Pscoret.x ," wins")
                    Ctext = ("com",Cscoret.y," wins")
                    print("you have ",Pscoret.x ," points\n","I have ",Cscoret.y," points")

                    again = input("want to continue? y/n\n")
                    if again == "y":
                        game()
                    else:
                        if Pscoret.x==0 and Cscoret.y==0:
                            exit()

                        else:

                            f=open('Scoresheet.txt','a')
                            f.write("\n")
                            f.write("Com")
                            f.write(".....")
                            f.write(str(Cscoret.y))
                            f.write(" ")
                            f.write(name)
                            f.write(".....")
                            f.write(str(Pscoret.x))

                            f.close()
                            exit()


                elif My_choice=="scissors" and your_choice=="paper":
                    print("YOU LOSE!!")
                    Cscoret.y = Cscoret.y+ 1
                    Pscoret.x  = Pscoret.x + 0
                    Ptext = (name," ",Pscoret.x ," wins")
                    Ctext = ("com",Cscoret.y," wins")
                    print("you have ",Pscoret.x ," points\n","I have ",Cscoret.y," points")

                    again = input("want to continue? y/n\n")
                    if again == "y":
                        game()
                    else:
                        if Pscoret.x==0 and Cscoret.y==0:
                            exit()

                        else:

                            f=open('Scoresheet.txt','a')
                            f.write("\n")
                            f.write("Com")
                            f.write(".....")
                            f.write(str(Cscoret.y))
                            f.write(" ")
                            f.write(name)
                            f.write(".....")
                            f.write(str(Pscoret.x))

                            f.close()
                            exit()


                elif My_choice=="rock" and your_choice=="scissors":
                    print("YOU LOSE!!")
                    Cscoret.y = Cscoret.y+ 1
                    Pscoret.x  = Pscoret.x + 0
                    Ptext = (name," ",Pscoret.x ," wins")
                    Ctext = ("com",Cscoret.y," wins")
                    print("you have ",Pscoret.x ," points\n","I have ",Cscoret.y," points")

                    again = input("want to continue? y/n\n")
                    if again == "y":
                        game()
                    else:
                        if Pscoret.x==0 and Cscoret.y==0:
                            exit()

                        else:

                            f=open('Scoresheet.txt','a')
                            f.write("\n")
                            f.write("Com")
                            f.write(".....")
                            f.write(str(Cscoret.y))
                            f.write(" ")
                            f.write(name)
                            f.write(".....")
                            f.write(str(Pscoret.x))

                            f.close()
                            exit()


                elif My_choice=="paper" and your_choice=="rock":
                    print("YOU LOSE!!")
                    Cscoret.y = Cscoret.y+ 1
                    Pscoret.x  = Pscoret.x + 0
                    Ptext = (name," ",Pscoret.x ," wins")
                    Ctext = ("com",Cscoret.y," wins")
                    print("you have ",Pscoret.x ," points\n","I have ",Cscoret.y," points")

                    again = input("want to continue? y/n\n")
                    if again == "y":
                        game()
                    else:
                        if Pscoret.x==0 and Cscoret.y==0:
                            exit()

                        else:

                            f=open('Scoresheet.txt','a')
                            f.write("\n")
                            f.write("Com")
                            f.write(".....")
                            f.write(str(Cscoret.y))
                            f.write(" ")
                            f.write(name)
                            f.write(".....")
                            f.write(str(Pscoret.x))

                            f.close()
                            exit()

            game()


        else :
            print(":(")
            EXIT=input("Do you want to exit? (y/n)\n")
            if EXIT=="y":
                exit()


            else:
                print(":)")
                main()

    main()
start()
