# -*- coding: utf-8 -*-
import scrapy
from SurreyUniversity.items import UniversityItem
import logging, re, traceback


class SurreySpider(scrapy.Spider):
    name = 'surreySpider'
    allowed_domains = ["https://www.surrey.ac.uk/"]
    start_urls = ["https://www.surrey.ac.uk/undergraduate/accounting-and-finance"]

    def parse_base_url(self, response):
        courses = response.xpath('//div[@class="border border-top-0 border-mustard border-right-0 border-left-0 py-3"]/div/div/div/div[@class="col-12 col-md-6 mb-3 views-row"]').extract()
        logging.warn("SampleSpider; Scraping Courses Started....; url= %s", response.url)
        for course_url in courses:
            if Bsc(Hons) in course_url:
                yield scrapy.Request(course_url, callback=self.parse_course)

    def parse_course(self, response):
        try:
            item = UniversityItem()

            # 1 CourseName
            course_name = response.xpath('//div[@class="row justify-content-center"]/div/div/h1[@class="my-0"]').extract_first()
            item['course_name'] = course_name



            # 4 Course Website
            course_website = response.url
            item['course_website'] = course_website

            #5 degree level
            degree_level =  response.xpath('//div[@class="row justify-content-center"]/div[@class="col-12 col-lg-8 pt-gw"]/div[@class="table-container key-info text-white w-100"]/div/table/tbody/tr[@class="d-flex flex-column flex-md-row border-0"]/td[@class="d-block font-weight-normal border-0 align-top pl-4"]/p/span/span[@class="font-weight-bold"]').extract()
            item['degree_level'] = degree_level

            #instake_month
            intake_month = response.xpath('//div/table/caption/p[@class="mb-0 pt-2 pl-4"]').extract()
            item['intake_month'] = intake_month

            #course description
            course_description = response.xpath('//div[@class="body-content"]/p').extract()
            item['course_description'] = course_description

            #course_structure
            course_structure = response.xpath('//div[@class="tab-content"]/div[@class="tab-pane active"]').extract()
            item['course_structure'] = course_structure

            #careers
            career = response.xpath('//div[@class="col-12 col-lg-8"]/div/div/ul').extract()
            item['career'] = career


            #duration_term
            sentence = response.xpath('//table[@class="table course-options text-dark bg-transparent mb-0"]/tbody/tr/td/p').extract()
            sentence = sentence.split(" ")


            #other requirement
            other_requirement = response.xpath('//div[@class="jump-menu-unit"]/div/p').extract()
            item['other_requirement'] = other_requirement






            # 6 Duration Term
            duration_term = ""
            if duration:
                duration_term = duration.split(" ")[-1]

            item['duration_term'] = duration_term

            #domestic fee

            #fee
            domestic_fee = " "
            item['domestic_fee'] = domestic_fee

            international_fee = " "
            item['international_fee'] = international_fee


            #### IELTS Data
            ielts = panel_data["ielts"]
            ielts_listening = ielts_writing = ielts_speaking = ielts_reading = ielts_overall = ""
            if ielts:

                ielts_data = re.findall("\d+\.\d+", ielts)

                # 22 IELTS Listening
                ielts_listening = ielts_data[-1]

                # 23 IELTS Speaking
                ielts_speaking = ielts_data[-1]

                # 24 IELTS Writing
                if len(ielts_data) == 3:
                    ielts_writing = ielts_data[1]
                else:
                    ielts_writing = ielts_data[-1]

                # 25 IELTS Reading
                ielts_reading = ielts_data[-1]

                # 26 IELTS Overall
                ielts_overall = ielts_data[0]

            item["ielts_listening"] = ielts_listening
            item["ielts_writing"] = ielts_writing
            item["ielts_reading"] = ielts_reading
            item["ielts_speaking"] = ielts_speaking
            item["ielts_overall"] = ielts_overall

            yield item

        except Exception as e:
            logging.error("SampleSpider; msg=Crawling Failed > %s;url= %s", str(e), response.url)
            logging.error("SampleSpider; msg=Crawling Failed;url= %s;Error=%s", response.url, traceback.format_exc())

        panel_data = {}

        panel_data["ielts"] = ielts_data

        return panel_data




    def parse(self,response):
        url="https://www.surrey.ac.uk/apply/international/english-language-requirements"
        TOEFL = self._get_TOEFL_score(url)
        PTE = self._get_PTE_score(url)
        yield scrapy.Request(url,callback=self.parse)

    def __get__TOEFL_score(self,url):
        page = requests.get(url)
        response = html.fromstring(page.content)

        TOEFL = {}
        reading =12
        writing =23
        listening =11
        speaking =17
        overall = 88

    def __get__PTE_score(self,url ):
        page = requests.get(url)
        response = html.fromstring(page.content)

        PTE = {}
        reading=42
        writing =50
        listening =42
        speaking =42
        overall =58


        return TOEFL, PTE



