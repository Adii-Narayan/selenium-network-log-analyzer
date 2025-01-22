import json

def parse_har(har_file):
    with open(har_file, 'r') as file:
        data = json.load(file)
    
    status_counts = {
        "total": 0,
        "2XX": 0,
        "4XX": 0,
        "5XX": 0
    }

    for entry in data:
        try:
            # Extract status code from the log entry
            status = entry['message']['params']['response']['status']
            if status:
                status_counts["total"] += 1
                if 200 <= status < 300:
                    status_counts["2XX"] += 1
                elif 400 <= status < 500:
                    status_counts["4XX"] += 1
                elif 500 <= status < 600:
                    status_counts["5XX"] += 1
        except KeyError:
            continue  # Skip entries without a valid status code

    output_file = "status_code_counts.json"
    with open(output_file, 'w') as outfile:
        json.dump(status_counts, outfile, indent=4)

    print(f"Status code counts saved to {output_file}")
    return status_counts

if __name__ == "__main__":
    har_file_path = "network_log.har"  # Replace with your file path
    parse_har(har_file_path)
