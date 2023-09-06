import re
from statistics import mean


class Tools:
    @staticmethod
    def get_subdomain(domain):
        """Gets subdomain of full domain."""
        return domain.split('.')[0].lower()

    def is_trash_domain(self, domain, regex):
        """Returns True if domain is trash."""
        subdomain = self.get_subdomain(domain)
        return bool(re.match(regex, subdomain))

    def get_regex(self, domains):
        """
        Returns Regular expression from data
        """
        subdomains = [self.get_subdomain(domain) for domain in domains]
        subdomains_len = [len(sub) for sub in subdomains]
        meany, maxy = int(mean(subdomains_len)) - 1, max(subdomains_len)
        return r'^.{%s,%s}$' % (meany, maxy)



