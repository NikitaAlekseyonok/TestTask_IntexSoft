import pytest
from helpers.logger_helper import Logger
from steps import api_steps as steps
from config import test_data


@pytest.mark.parametrize("country_code", test_data.COUNTRY_CODES)
def test_borders_between_countries(api_tests, country_code) -> None:
    wrong_country_borders = []

    country_borders = steps.get_country_borders_data(country_code)

    for border_country_code in country_borders:
        Logger.info(f"Checking that the boundaries between the country with code {country_code} and the country"
                    f" with code {border_country_code} are reciprocal")
        border_country_borders = steps.get_country_borders_data(border_country_code)

        if country_code not in border_country_borders:
            Logger.warning(f"The boundaries between the country with code {country_code} and the country"
                           f" with code {border_country_code} are NOT reciprocal")
            wrong_country_borders.append(border_country_code)

    assert not wrong_country_borders, f"Border between {country_code} and {', '.join(wrong_country_borders)} is not mutual"
