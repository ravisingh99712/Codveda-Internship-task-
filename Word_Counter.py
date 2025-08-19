sample.txt : Hello Codveda Internship
This is my Python task
Word counter project

def word_counter(filename):
    try:
        # File open karke read karna
        with open(sample.txt, 'r') as file:
            content = file.read()

        # Words split karna (space ke basis par)
        words = content.split()
        word_count = len(words)

        print(f"✅ The file '{sample.txt}' has {word_count} words.")

    except FileNotFoundError:
        print(f"⚠️ Error: The file '{sample.txt}' was not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


# Run program
filename = "sample.txt"   # yaha apna file ka naam likhna
word_counter(filename)
