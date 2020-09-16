# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class SurreyuniversityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #.course Name
    course_name=scrapy.Field()


    #.course Website
    course_website = scrapy.Field()

    #.duration
    duration = scrapy.Field()

    #6.duration term
    duration_term = scrapy.Field()




    #11.intake month
    intake_month = scrapy.Field()



    #.apply month
    apply_month = scrapy.Field()



    #.international fee
    international_fee = scrapy.Field()

    #.domestic fee
    domestic_fee = scrapy.Field()

    #.fee term
    fee_term = scrapy.Field()

    #.fee year
    fee_year = scrapy.Field()


    #.IELTS listening
    IELTS_listening = scrapy.Field()

    #.IELTS speaking
    IELTS_speaking = scrapy.Field()

    #.Ielts writing
    IELTS_writing = scrapy.Field()

    #.IELTS reading
    IELTS_reading = scrapy.Field()

    #.IELTS overall
    IELTS_overall = scrapy.Field()

    #.PTE listening
    PTE_listening = scrapy.Field()

    #.PTE speaking
    PTE_speaking = scrapy.Field()

    #.PTE writing
    PTE_writing = scrapy.Field()

    #.PTE reading
    PTE_reading = scrapy.Field()

    #.PTE overall
    PTE_overall = scrapy.Field()

    #.TOEFL Listening
    TOEFL_listening = scrapy.Field()

    #.TOEFL Speaking
    TOEFL_speaking = scrapy.Field()

    #.TOEFL Writing
    TOEFL_writing = scrapy.Field()

    #.TOEFL reading
    TOEFL_reading = scrapy.Field()

    #.TOEFL overall
    TOEFL_overall = scrapy.Field()



    #.reading
    reading = scrapy.Field()

    #.listening
    listening = scrapy.Field()

    #.speaking
    speaking = scrapy.Field()

    #.writing
    writing = scrapy.Field()

    #.overall
    overall = scrapy.Field()

    #.other requirements
    other_requirements = scrapy.py()

    #.course description
    course_description = scrapy.Field()

    #.course structure
    course_structure = scrapy.Field()

    #.career
    career = scrapy.Field()

    pass
