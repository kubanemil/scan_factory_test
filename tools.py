import re
from statistics import mean


def get_subdomain(domain):
    return domain.split('.')[0].lower()


def is_trash_domain(domain, regex):
    subdomain = get_subdomain(domain)
    return bool(re.match(regex, subdomain))


def get_regex(domains):
    subdomains = [get_subdomain(domain) for domain in domains]
    subdomains_len = [len(sub) for sub in subdomains]
    meany, maxy = int(mean(subdomains_len)) - 1, max(subdomains_len)
    return r'^.{%s,%s}$' % (meany, maxy)


# def insert_into_db(domain_id, regex):
