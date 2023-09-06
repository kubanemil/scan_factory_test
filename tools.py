import re
from statistics import mean


class Tools:
    @staticmethod
    def get_subdomain(domain):
        return domain.split('.')[0].lower()

    def is_trash_domain(self, domain, regex):
        subdomain = self.get_subdomain(domain)
        return bool(re.match(regex, subdomain))

    def get_regex(self, domains):
        subdomains = [self.get_subdomain(domain) for domain in domains]
        subdomains_len = [len(sub) for sub in subdomains]
        meany, maxy = int(mean(subdomains_len)) - 1, max(subdomains_len)
        return r'^.{%s,%s}$' % (meany, maxy)



