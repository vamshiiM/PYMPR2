import time

# Function to execute after 2 days
def delayed_code():
    print("This code runs after 2 days.")

# Function to calculate time difference in seconds
def time_diff_in_seconds(timestamp):
    return timestamp - time.time()

# Main function
def main():
    # Calculate the timestamp for 2 days from now
    two_days_in_seconds = 1 * 60
    timestamp = time.time() + two_days_in_seconds

    # Wait until the specified time
    while True:
        time_remaining = time_diff_in_seconds(timestamp)
        if time_remaining <= 0:
            break
        time.sleep(time_remaining)

    # Execute the delayed code
    delayed_code()

# Run the main function
if __name__ == "__main__":
    main()
