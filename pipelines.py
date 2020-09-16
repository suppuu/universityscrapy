# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy import signal
from scrapy.exporters import CsvItemExporter
#from itemadapter import ItemAdapter


class SurreyuniversityPipeline:
    def __init__(self):
            self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        output_file = open(str(spider.name)+'.csv', 'a+b')
        self.files[spider] = output_file
        self.exporter = CsvItemExporter(output_file)
        self.exporter.fields_to_export = ['course_name','course_website','duration','duration_term','degree_level','intake_month','apply_day','international_fee','domestic_fee','fee_term','fee_year','ielts_listening','ielts_speaking','ielts_writing','ielts_reading','ielts_overall','pte_listening','pte_speaking','pte_writing','pte_reading','pte_overall','toefl_listening','toefl_speaking','toefl_writing','toefl_reading','toefl_overall','other_requirements','course_description','course_structure','career' ]
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        output_file = self.files.pop(spider)
        output_file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item