"""
A script to get the crontab entry str.

Author: Indrajit Ghosh
Created on: Apr 24, 2024
"""

from pathlib import Path

def generate_cronjob_entry(hours_interval: int, main_script: Path, env_path: Path=None):
    """
    Generate a string for cronjob entry based on provided parameters.

    Args:
        hours_interval (int): Interval in hours for the cronjob.
        main_script (Path): Path to the main script.
        env_path (Path): Path to the virtualenv dir.

    Returns:
        str: Cronjob entry string.
    """
    if env_path is None:
        env_path = main_script.resolve().parent / 'env'
    cronjob_entry = f"0 */{hours_interval} * * * {env_path}/bin/python {main_script.resolve()}"

    return cronjob_entry
def main():
    try:
        hours_interval = int(input("Enter hours interval for cronjob: "))
        main_script = Path(input("Enter the path to the main script: "))
        env_path_input = input("Enter the path to the virtualenv (leave empty for default to `env`): ")
        env_path = None if env_path_input == '' else Path(env_path_input).resolve()

        cronjob_entry = generate_cronjob_entry(hours_interval, main_script, env_path)
        print("Cronjob entry:")
        print(cronjob_entry)
    except ValueError:
        print("Error: Please enter a valid integer for hours interval.")

if __name__ == "__main__":
    main()
