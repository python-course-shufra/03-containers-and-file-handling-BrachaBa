import sys
import random


def main():
    # TODO: your code here

    # 1. Get the command line arguments via sys.argv
    profession = sys.argv[1]
    num_questions = int(sys.argv[2])
    count = 0

    # 2. Open the correct file open(rf'questions\<filename>.txt)'
    with open(f'questions\{profession}.txt', mode='r') as file:
    
    # 3. Iterate over the file
        for _ in range(num_questions):
    #       3.1. Parse the line (use s.split())
            line = file.readline().strip()
            l = line.split(';')

    #       3.2 Create a list of options
            options = l[2].split(',')
            options.append(l[1])

    #       3.3 random.shuffle(l)
            random.shuffle(options)

    #       3.4 Display the question
            print(f"Question: {l[0]}")
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")

    #       3.5 Get user input
            user_answer = int(input("Your answer (enter the number): "))

    #       3.6 Check if the answer is correct
            if options[user_answer - 1] == l[1]:
                # print("Correct!\n")
                count += 1
            # else:
                # print(f"Wrong! The correct answer is: {l[1]}\n")
        print(f"You answered {count}/{num_questions} correct answers. Well done!")

if __name__ == '__main__':
    main()
