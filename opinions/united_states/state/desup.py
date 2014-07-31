#  Scraper for the Superior Court of Delaware
# CourtID: desup
# Court Short Name: De.
# Author: Andrei Chelaru
# Reviewer:
# Date created: 31 July 2014

from juriscraper.opinions.united_states.state import de


class Site(de.Site):
    def __init__(self):
        super(Site, self).__init__()
        self.url = 'http://courts.delaware.gov/opinions/List.aspx?ag=Superior%20Court'
        self.court_id = self.__module__

