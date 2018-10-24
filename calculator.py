import shlex
import math
import random

# Used for the hello command
last_value = 0
_hello     = 0                         #downwithteam5

if __name__ == "__main__":
       
    print ("Calculator")

    # Defines a set of commands that
    # are used for the command interpreter
    commands = {
        "exit":      "closes the calculator",
        "sqrt":      "finds the square root of the given number",
        "abs":       "finds the absolute value of the given number",
        "fact":      "finds the factorial of the given number",
        "pow":       "raises argument one to the argument two power",
        "ln":        "finds the number '1' for now", # ln needs finishing
        "mod":       "unsure of", # needs finishing
        "log10":     "unsure of", # i don't understand how to word this
        "divide":    "divides argument one by argument two",
        "multiply":  "multiplies the two given numbers",
        "inverse":   "unsure of", # needs finishing
        "add":       "adds the two given numbers",
        "sub":       "subtracts argument two from argument one",
        "opp":       "switces the sign of the given number",
        "hello":     "try it and see",
        "help":      "shows this help dialog",
        "recall":    "recalls the last answer",
        #"convert":   "converts numbers between bases",
        "root":      "finds arg1 to the arg2 root"
    }

    def helpfile():
        print ("Commands:")
        for i,v in commands.items():
            print ("    "+i+" - "+v)
        
		
    helpfile()

    hellos = ["Ironman is the best"
    ]

    # Witty responses to leave hello alone
    leave_us_alone = ["Ironman is the best Avenger",
        "I HATE YOU"
    ]

    while True:
        command = shlex.split(input("> "))

        try:
            cmd = command[0]
        except:
            print ("Command failed!")

        for _cmd in commands.keys():
            if _cmd == cmd:
                try:
                    if cmd == "sqrt":
                        number = int(command[1])
                        last_value = pow(number,0.5)
                        print(last_value)
                    elif cmd == "exit":
                        exit(0)
                    elif cmd == "hello":
                        if _hello <= 10:
                            _hello += 1
                            print(hellos[random.randint(0, len(hellos) - 1)])
                        else:
                            print(colors.FAIL + leave_us_alone[random.randint(0, len(leave_us_alone) - 1)] + colors.ENDC)
                    elif cmd == "abs":
                        number = int(command[1])
                        last_value = abs(number)
                        print(last_value)
                    elif cmd == "help":
                    	helpfile()
                    elif cmd == "recall":
                        print ("Last value: %d" % last_value)
                    elif cmd == "add":
                        number1 = int(command[1])
                        number2 = int(command[2])
                        last_value = (number1+ number2)
                        print(last_value)
                    elif cmd == "sub":
                        number1 = int(command[1])
                        number2 = int(command[2])
                        last_value = number1-number2
                        print(last_value)
                    elif cmd == "opp":
                        number = int(command[1])
                        last_value = -(number)
                        print(last_value)
                    elif cmd == "pow":
                        number1 = int(command[1])
                        number2 = int(command[2])
                        last_value = pow(number1, number2)
                        print(last_value)
                    elif cmd == "root":
                        last_value=pow(int(command[1]),1/int(command[2]))
                        print(last_value)
                    elif cmd == "divide":
                        number1 = float(command[1])
                        number2 = float(command[2])
                        last_value = number1//number2
                        print(last_value)
                except:
                    print ("Command failed!")
