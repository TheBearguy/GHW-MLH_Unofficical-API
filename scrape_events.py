from requests_html import HTMLSession
import time


def scrape_events(year):
  URL = f"https://mlh.io/seasons/{year}/events"
  SLEEP_TIME = 10
  session = HTMLSession()
  response = session.get(URL)
  eventWrapperList = response.html.find(".event-wrapper")
  event_data = []

  for eventWrapper in eventWrapperList:
    eventName = eventWrapper.find(".event-name", first=True).text
    eventDate = eventWrapper.find(".event-date", first=True).text.strip()
    eventStartDate = eventWrapper.find("meta[itemprop = 'startDate']",
                                       first=True).attrs['content']
    
    eventEndDate = eventWrapper.find("meta[itemprop = 'endDate']",
                                     first=True).attrs['content']
    
    eventLogo = eventWrapper.find(".event-logo img", first=True).attrs['src']
    eventCity = eventWrapper.find("span[itemprop = 'city']", first=True).text
    eventState = eventWrapper.find("span[itemprop = 'state']", first=True).text
    eventLocation = f"{eventCity}, {eventState}"
    eventHybridNotes = eventWrapper.find(".event-hybrid-notes span",
                                         first=True).text
    
    eventLink = eventWrapper.find(".event-link", first=True).attrs['href']
    event_data.append({
      "EventName": eventName,
      "EventDate": eventDate,
      "StartDate": eventStartDate,
      "EndDate": eventEndDate,
      "Location": eventLocation,
      "HybridNotes": eventHybridNotes,
      "EventLink": eventLink
    })
  time.sleep(2)

  return event_data
