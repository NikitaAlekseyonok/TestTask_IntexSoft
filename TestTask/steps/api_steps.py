from config.status_codes import SUCCESS_CODE
from helpers.logger_helper import Logger
from models.country_model import Country
from typing import List


@Logger.step("Get border country list")
def get_country_borders_data(country_code: str) -> List[str]:

    Logger.info(f"Get country data response for {country_code}")
    county_data_response = Country.get_county_data_response(country_code)
    assert county_data_response.status_code == SUCCESS_CODE, f"Failed to get country information for {country_code}"

    Logger.info(f"Get border countries for {country_code}")
    country = Country(country_code, county_data_response.json())
    border_countries = country.border_countries

    return border_countries
