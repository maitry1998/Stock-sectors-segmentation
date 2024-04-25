import scrapy
from yahoo_finance.items import YahooFinanceItem
import re
from scrapy_splash import SplashRequest
import datetime

class SectorSpider(scrapy.Spider):
    name = 'sector_spider'
    
    start_urls = [
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_basic-materials/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_communication-services/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_consumer-cyclical/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_consumer-defensive/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_energy/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_financial-services/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_healthcare/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_industrials/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_real-estate/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_technology/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_utilities/?offset=0&count=100',
    ]
    def convert_to_number(self, value):
        multiplier = 1
        if 'B' in value:
            multiplier = 1e9
        elif 'M' in value:
            multiplier = 1e6
        elif 'K' in value:
            multiplier = 1e3
        elif 'T' in value:
            multiplier = 1e12

        # Remove any non-numeric characters except '.'
        numeric_value = ''.join(filter(lambda x: x.isdigit() or x == '.', value))
        return float(numeric_value) * multiplier if numeric_value else None
    

    def start_requests(self):
        for url in self.start_urls:
            print('I am waiting for 0.5 secs')
            sector_name = self.extract_sector_name(url)
            yield SplashRequest(url, self.parse, args={'wait': 0.5}, meta={'sector_name': sector_name})


    def extract_sector_name(self, url):
        match = re.search(r'sec-ind_sec-largest-equities_([^/?]*)', url)
        return match.group(1).replace('-', ' ').title() if match else None
  

    def parse(self, response):
        # Navigate to the table containing the data
        sector_name = self.extract_sector_name(response.url)
        rows = response.xpath('//table[contains(@class, "W(100%)")]/tbody/tr')
        for row in rows:
            item = YahooFinanceItem()
            item['sector_name'] = sector_name
            item['symbol'] = row.xpath('.//td[1]//text()').get()
            item['company_name'] = row.xpath('.//td[2]/text()').get()
            item['last_price'] = row.xpath('.//td[3]/fin-streamer/@value').get()
            item['change'] = row.xpath('.//td[4]/fin-streamer/span/text()').get()
            item['percent_change'] = row.xpath('.//td[5]/fin-streamer/span/text()').get()
            item['volume'] = row.xpath('.//td[6]/fin-streamer/@value').get()
            item['avg_vol_3m'] = row.xpath('.//td[7]/text()').get()
            item['market_cap'] = row.xpath('.//td[8]/fin-streamer/@value').get()
            item['pe_ratio_ttm'] = row.xpath('.//td[9]/text()').get()

            yield item

            # symbol = item['symbol']
            # history_url = f'https://finance.yahoo.com/quote/{symbol}/history?period1=1556037632&period2=1713889315&frequency=1mo'
            
            # # Store initial item in meta to pass to the next request
            # yield scrapy.Request(
            #     history_url,
            #     callback=self.parse_history,
            #     meta={'item': item}
            # )

    # def parse_history(self, response):
    #     # This function processes historical data to capture data from the 1st of each month in the last five years
    #     item = response.meta['item']
        
    #     # Current date for reference
    #     current_date = datetime.datetime.now()

    #     # Extract the table rows
    #     history_rows = response.xpath('//table[contains(@class, "table")]/tbody/tr')

    #     # Loop through rows to find data for the 1st of the month
    #     for row in history_rows:
    #         date_text = row.xpath('.//td[1]//text()').get()
        
    #         if date_text:
    #             date_object = datetime.datetime.strptime(date_text, '%b %d, %Y')

    #             # Check if the date is the 1st of the month and within the last 5 years
    #             if date_object.day == 1 and (current_date - date_object).days <= 5 * 365:
    #                 # if item.get(re.sub(r'[\s,]+', '_', date_text)):
    #                 item[re.sub(r'[\s,]+', '_', date_text)] = row.xpath('.//td[5]//text()').get()

    #     # Store the extracted data in the item
    #     yield item  # Yield the item to the pipeline or CSV
       
        
        



