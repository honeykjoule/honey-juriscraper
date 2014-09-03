"""
Scraper for Indiana Supreme Court
CourtID: ind
Court Short Name: Ind.
Auth: Jon Andersen <janderse@gmail.com>
Reviewer:
History:
    2014-09-03: Created by Jon Andersen
"""
from juriscraper.OpinionSite import OpinionSite
import time
from datetime import date


class Site(OpinionSite):
    def __init__(self):
        super(Site, self).__init__()
        self.url = 'http://www.in.gov/judiciary/opinions/supreme.html'
        self.court_id = self.__module__
        self.my_precedential_statuses = []

    def _get_case_names(self):
        raw_case_names = [s for s in self.html.xpath('//dl/dt/a/text()')]
        case_names = []
        self.my_precedential_statuses = []
        for case_name in raw_case_names:
            if case_name.find("(NFP)") >= 0:
                case_names.append(case_name.replace("(NFP)", "").strip())
                self.my_precedential_statuses.append("Unpublished")
            else:
                case_names.append(case_name)
                self.my_precedential_statuses.append("Published")
        return case_names

    def _get_download_urls(self):
        return [s for s in self.html.xpath('//dl/dt/a/@href')]

    def _get_case_dates(self):
        dates = []
        for date_string in self.html.xpath('//dl/dd/dd/dd/text()'):
            val = date_string.strip()
            if val == '':
                dates.append('')
            else:
                dates.append(date.fromtimestamp(
                    time.mktime(time.strptime(val, '%m/%d/%y'))))
        return dates

    def _get_docket_numbers(self):
        return [s for s in self.html.xpath('//dl/dd/text()')]

    def _get_lower_court_numbers(self):
        return [e if e.strip() != "N/A" else "" for e in self.html.xpath('//dl/dd/dd/text()')]

    def _get_precedential_statuses(self):
        return self.my_precedential_statuses
