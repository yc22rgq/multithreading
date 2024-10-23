import subprocess
import statistics

def controller():
    # Start Program A
    process = subprocess.Popen(['python3', 'randNumGen.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    # Send "Hi" command and verify response
    process.stdin.write("Hi\n")
    process.stdin.flush()
    response = process.stdout.readline().strip()
    if response != "Hi":
        process.terminate()
        return

    # Retrieve 100 random numbers
    random_numbers = []
    for _ in range(100):
        process.stdin.write("GetRandom\n")
        process.stdin.flush()
        random_numbers.append(int(process.stdout.readline().strip()))

    # Send "Shutdown" command
    process.stdin.write("Shutdown\n")
    process.stdin.flush()
    process.wait()

    # Sort the list of random numbers
    random_numbers.sort()

    # Print the sorted list
    print("Sorted Random Numbers:", random_numbers)

    # Calculate and print the median and average
    median = statistics.median(random_numbers)
    average = statistics.mean(random_numbers)
    print(f"Median: {median}")
    print(f"Average: {average}")


if __name__ == "__main__":
    controller()