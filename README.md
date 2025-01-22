# selenium-network-log-analyzer
Network Log Analysis

## Project Overview
This project involves automating the process of capturing network logs from the website [ExactSpace](https://exactspace.co/), extracting the HTTP status codes, and providing a summary of the counts of different status code categories (2XX, 4XX, 5XX).

The solution is implemented in Python using Selenium and Chrome DevTools Protocol.

---

## Features
- Automatically navigates to the ExactSpace website.
- Captures network logs (`.har` format) containing HTTP request and response details.
- Parses the logs to extract and categorize HTTP status codes.
- Outputs the results as a JSON file with counts for:
  - Total status codes
  - 2XX (Success)
  - 4XX (Client Errors)
  - 5XX (Server Errors)

---

## File Structure
