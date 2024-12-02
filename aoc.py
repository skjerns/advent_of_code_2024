import requests
import joblib

mem = joblib.Memory('.')

# Constants
AOC_URL = "https://adventofcode.com"
YEAR = 2024  # Change this to the desired year
with open('session', 'r') as f:
    SESSION_COOKIE = f.read().strip()  # Replace with your session cookie

def get_lines(day, year=YEAR, session_cookie=SESSION_COOKIE):
    return get_input(day, year, session_cookie).split('\n')

@mem.cache
def get_input(day, year=YEAR, session_cookie=SESSION_COOKIE):
    """
    Downloads the puzzle input for a specific day from Advent of Code.

    Args:
        day (int): The day of the puzzle (1-25).
        year (int): The year of the Advent of Code event.
        session_cookie (str): Your session cookie for authentication.

    Returns:
        str: The puzzle input as a string.
    """
    # Validate day
    day = int(day)
    if not (1 <= day <= 25):
        raise ValueError("Day must be between 1 and 25.")

    # Construct the URL for the puzzle input
    url = f"{AOC_URL}/{year}/day/{day}/input"

    # Set up cookies for authentication
    cookies = {"session": session_cookie}

    # Make the request
    response = requests.get(url, cookies=cookies)

    # Check for errors
    if response.status_code == 200:
        print(f"Successfully downloaded input for Day {day}, {year}.")
        return response.text.strip()
    elif response.status_code == 404:
        raise Exception(f"Puzzle for Day {day}, {year} is not available yet.")
    else:
        raise Exception(f"Failed to fetch puzzle input: {response.status_code} - {response.reason}")
