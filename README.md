# Log Analyzer with Search, Statistics, and Export to CSV

This Python script provides a way to parse and analyze web server access logs. Users can search for specific log entries based on different parameters (e.g., IP address, date, HTTP method), generate statistics, and export the results to a CSV file.

---

## Features

- Search logs by:
  - IP Address
  - Date and Time
  - HTTP Method
  - Requested Resource
  - HTTP Version
  - Status Code
  - Response Size
  - User-Agent
- Generate statistics for a chosen parameter (e.g., count occurrences of each HTTP method).
- Export matching log entries to a CSV file.
- Error handling for invalid inputs and file-related issues.

---

## Requirements

- Python 3.7 or higher

No external libraries are required as the script uses built-in Python modules such as `re`, `csv`, and `tkinter` for the GUI.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/log-analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd logparser
   ```

---

## Usage

### Run the Script

```bash
python main.py
```

### Interactive Options

When you run the script, you will be prompted to:

1. Choose a parameter to search for (e.g., IP address, date).
2. Enter the value you want to search for.
3. View the matching results directly in the console.
4. Optionally, export the results to a CSV file for further analysis.
5. Generate statistics for a specific parameter to analyze patterns in the logs.

### Example Log Entry

The script is designed to parse logs in the following format:

```
172.16.0.2 - - [22/Dec/2024:06:19:59 +0000] "GET /index.html HTTP/1.1" 404 773 "Safari/537.36"
```

### Example Search

- **Search by IP Address:** Enter `1` and type an IP (e.g., `172.16.0.2`).
- **Search by Date:** Enter `2` and type a date (e.g., `22/Dec/2024`).

### Example Statistics

- **Generate Statistics by HTTP Method:** Select the option for statistics and choose `HTTP Method`. The script will output the count of each HTTP method (e.g., `GET: 150, POST: 30`).

---

## Export to CSV

If matching results are found, you will be asked if you want to save them to a CSV file. Provide a filename, and the results will be saved in the specified file in the same directory.

---

## Project Structure

```
log-analyzer/
├── access.log        # Example log file (not included in this repo)
├── log_search.py     # Main Python script
├── README.md         # Project description
```

---

## Future Improvements

- Add support for other log formats.
- Include advanced search options (e.g., regex-based searching).
- Develop a graphical user interface (GUI).
- Expand statistical analysis with more detailed visualizations.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any ideas or bug fixes.

---

## Contact

For any questions or feedback, reach out to [your_email@example.com](mailto:your_email@example.com).

