# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YahooFinanceItem(scrapy.Item):
    # define the fields for your item here
    symbol = scrapy.Field()
    sector_name = scrapy.Field()
    company_name = scrapy.Field()  # Full company name, e.g., "Amazon.com, Inc."
    last_price = scrapy.Field()  # Price (Intraday)
    change = scrapy.Field()  # Change in price
    percent_change = scrapy.Field()  # Percentage change in price
    volume = scrapy.Field()  # Volume
    avg_vol_3m = scrapy.Field()  # Average Volume (3 months)
    market_cap = scrapy.Field()  # Market Cap
    pe_ratio_ttm = scrapy.Field()  # PE Ratio (TTM)
    # The 52-week range is typically represented visually on websites and might not be directly scrapeable as text. You may need to handle this differently or exclude it if not essential.
    # week_52_range = scrapy.Field() 
    # Apr_1_2024 = scrapy.Field()
    # Mar_1_2024 = scrapy.Field()
    # Feb_1_2024 = scrapy.Field()
    # Jan_1_2024 = scrapy.Field()
    # Dec_1_2023 = scrapy.Field()
    # Nov_1_2023 = scrapy.Field()
    # Oct_1_2023 = scrapy.Field()
    # Sep_1_2023 = scrapy.Field()
    # Aug_1_2023 = scrapy.Field()
    # Jul_1_2023 = scrapy.Field()
    # Jun_1_2023 = scrapy.Field()
    # May_1_2023 = scrapy.Field()
    # Apr_1_2023 = scrapy.Field()
    # Mar_1_2023 = scrapy.Field()
    # Feb_1_2023 = scrapy.Field()
    # Jan_1_2023 = scrapy.Field()
    # Dec_1_2022 = scrapy.Field()
    # Nov_1_2022 = scrapy.Field()
    # Oct_1_2022 = scrapy.Field()
    # Sep_1_2022 = scrapy.Field()
    # Aug_1_2022 = scrapy.Field()
    # Jul_1_2022 = scrapy.Field()
    # Jun_1_2022 = scrapy.Field()
    # May_1_2022 = scrapy.Field()
    # Apr_1_2022 = scrapy.Field()
    # Mar_1_2022 = scrapy.Field()
    # Feb_1_2022 = scrapy.Field()
    # Jan_1_2022 = scrapy.Field()
    # Dec_1_2021 = scrapy.Field()
    # Nov_1_2021 = scrapy.Field()
    # Oct_1_2021 = scrapy.Field()
    # Sep_1_2021 = scrapy.Field()
    # Aug_1_2021 = scrapy.Field()
    # Jul_1_2021 = scrapy.Field()
    # Jun_1_2021 = scrapy.Field()
    # May_1_2021 = scrapy.Field()
    # Apr_1_2021 = scrapy.Field()
    # Mar_1_2021 = scrapy.Field()
    # Feb_1_2021 = scrapy.Field()
    # Jan_1_2021 = scrapy.Field()
    # Dec_1_2020 = scrapy.Field()
    # Nov_1_2020 = scrapy.Field()
    # Oct_1_2020 = scrapy.Field()
    # Sep_1_2020 = scrapy.Field()
    # Aug_1_2020 = scrapy.Field()
    # Jul_1_2020 = scrapy.Field()
    # Jun_1_2020 = scrapy.Field()
    # May_1_2020 = scrapy.Field()
    # Apr_1_2020 = scrapy.Field()
    # Mar_1_2020 = scrapy.Field()
    # Feb_1_2020 = scrapy.Field()
    # Jan_1_2020 = scrapy.Field()
    # Dec_1_2019 = scrapy.Field()
    # Nov_1_2019 = scrapy.Field()
    # Oct_1_2019 = scrapy.Field()
    # Sep_1_2019 = scrapy.Field()
    # Aug_1_2019 = scrapy.Field()
    # Jul_1_2019 = scrapy.Field()
    # Jun_1_2019 = scrapy.Field()
    # May_1_2019 = scrapy.Field()
