# settings.py - list of global variables specific to our project

# Scrapy settings for comesg project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

## our scraper a name
BOT_NAME = 'comesg'

## where our spider module is located

SPIDER_MODULES = ['scraper_app.spiders']
NEWSPIDER_MODULE = 'comesg.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'comesg (+http://www.yourdomain.com)'

############################

ITEM_PIPELINES = ['scraper_app.pipelines.ComesgPipeline']

############################



# The username is your username for your machine. The password may not be needed (just an empty string, 'password': ''), or may be the password used when setting up Postgres initially.

# The database is the name of the database we created earlier, postgres=# create database scrape;.

DATABASE = {

	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'kristelteng',
	'password': '',
	'database': 'scrape'
}


############################

