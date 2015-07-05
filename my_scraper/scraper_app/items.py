from scrapy.item import Item, Field

class ComesgItem(Item):

## define the fields for your item here like:
    name = Field()
    address = Field()
    contact = Field()
    hours = Field()
    website = Field()
    photo = Field()
    desc = Field()
    video = Field()	 