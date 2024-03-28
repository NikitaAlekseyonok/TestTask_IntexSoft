import requests
from typing import List, Dict


class Country:
    COUNTRY_ENDPOINT = "https://restcountries.com/v2/alpha/{country_code}"

    def __init__(self, country_code: str, county_data: Dict[str, str]) -> None:
        self._county_code = country_code
        self._country_data = county_data

    @property
    def border_countries(self) -> List[str]:
        return self._country_data.get('borders', [])

    @property
    def country_code(self) -> str:
        return self._county_code

    @classmethod
    def get_county_data_response(cls, country_code: str) -> requests.Response:
        return requests.get(cls.COUNTRY_ENDPOINT.format(country_code=country_code))
