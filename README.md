# MindCanvas Database Collector

This project is designed to collect the database content of the web application "[MindCanvas](https://github.com/indrajit912/MindCanvas)" developed by [Indrajit Ghosh](https://github.com/indrajit912). It utilizes the MindCanvas API endpoint to retrieve data and stores it locally in JSON format.

## Author
- **Author:** Indrajit Ghosh

## Usage
To use this project, follow these steps:
1. Clone this repository.
2. Set up the `.env` file with appropriate configurations for `MINDCANVAS_HOST` and `BEARER_TOKEN`.
3. Run the script `main.py` by executing `python main.py`.
4. The fetched data will be saved to a JSON file in the local directory.

## Dependencies
- Python 3.x
- requests
- dotenv


## Scheduled Execution
To schedule the execution of this script using a cronjob at 6-hour intervals, add the following line to your crontab (to open crontab use `crontab -e`):
```bash
0 */6 * * * /path/env/bin/python3 /path/to/main.py
```