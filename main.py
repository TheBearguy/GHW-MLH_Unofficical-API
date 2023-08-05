from scrape_events import scrape_events
from write_to_csv import write_to_csv
from write_to_json import write_to_json


def main():
  YEARS = [2021, 2022]
  all_event_data = []
  total_idx = 1
  for year in YEARS:
    print("Write to CSV Success!", "\n\n")
    new_event_data = scrape_events(year)
    #new_event_data_count = len(new_event_data)

    for event in new_event_data:
      event["ID"] = total_idx
      event["Year"] = year
      all_event_data.append(event)
      total_idx+=1
    
    new_csv_file_name = f"mlh_events_{year}.csv"
    write_to_csv(new_event_data, new_csv_file_name)

  new_merged_json_file = "merged_mlh_events.json"
  write_to_json(all_event_data, new_merged_json_file)


if __name__ == "__main__":
  main()
