import csv


def write_to_csv(event_data, csv_file_name, start_idx = 1):
  with open(csv_file_name, 'w', newline="") as templog:
    csv_writer = csv.writer(templog)
    csv_writer.writerow([
      "ID", 
      "EventName", "EventDate", "StartDate", "EndDate", "Location",
      "HybridNotes", "EventLink", "Year"
    ])
    for idx, event in enumerate(event_data):
      csv_writer.writerow([
        idx, 
        event["EventName"], event["EventDate"], event["StartDate"],
        event["StartDate"], event["EndDate"], event["Location"],
        event["HybridNotes"], event["EventLink"], event["Year"]
      ])