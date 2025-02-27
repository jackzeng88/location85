# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Location85Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country_id = scrapy.Field()
    country_name = scrapy.Field()
    country_slug = scrapy.Field()

    city_id = scrapy.Field()
    city_name = scrapy.Field()
    city_slug = scrapy.Field()

    location_id = scrapy.Field()
    location_name = scrapy.Field()
    location_slug = scrapy.Field()
