class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        tables = {}
        for e in emails:
            local, domain = e.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            if domain not in tables:
                tables[domain] = set()
            tables[domain].add(local)

        return sum([len(item) for item in tables.values()])
