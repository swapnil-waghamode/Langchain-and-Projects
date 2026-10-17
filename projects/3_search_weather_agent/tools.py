from langchain_nimble import NimbleSearchTool
from langchain.tools import tool
import os

import requests

# creating object of Nimble search tool

search_tool = NimbleSearchTool(
  k = 5,               # Top 5 searches
  deep_search = True,   # Go deeper inside top searches
  parsing_type ="markdown"  # search results in markdown
)

# Google search Tool
@tool
def google_search(query: str):
  """
  Search anything on google for realtime information.

  Args:
      query - user search query for google search
  
  Return - result from google search
  """
  res = search_tool.invoke(query)
  return res


# Weather Tool
@tool
def weather_tool(city:str):
  """
   Get realtime weather details like temperature, humidity and others.
   Args:
      - city name for weather details
   
   Return -> Wether data from the api response.
  """

  WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
  API_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={WEATHER_API_KEY}"

  response = requests.get(API_URL)

  if response.status_code == 200:
    return response.json()

  return f"Unable to find the details for this city."


ALL_TOOLS = [google_search, weather_tool]