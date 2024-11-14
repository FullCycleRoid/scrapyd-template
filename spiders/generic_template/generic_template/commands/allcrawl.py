import urllib
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from scrapy.commands import ScrapyCommand
from scrapyd.app import log


class AllCrawlCommand(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED': False}

    def short_desc(self):
        return "Schedule a run for all available spiders"

    # def run(self, args, opts):
    #     url = 'http://localhost:6800/schedule.json'
    #     for s in self.s.list():
    #         values = {'project': 'YOUR_PROJECT_NAME', 'spider': s}
    #         data = urlencode(values)
    #         req = Request(url, data)
    #         response = urlopen(req)
    #         log.msg(response)
