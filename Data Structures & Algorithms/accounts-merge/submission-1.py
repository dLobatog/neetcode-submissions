class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # ["name", "name@gmail.com", "sada@gmail.com"]
        email_to_name = {}
        g = defaultdict(list)

        for row in accounts:
            name = row[0]
            first_email = row[1]
            for email in row[1:]:
                email_to_name[email] = row[0]
                g[email]
                if email != first_email:
                    g[first_email].append(email)
                    g[email].append(first_email)

        result = []
        visited = set()

        def dfs(node):
            visited.add(node)
            component.append(node)
            for neighbor in g[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for email_node in g.keys():
            component = []
            if email_node not in visited:
                dfs(email_node)
            if len(component) != 0:
                result.append([email_to_name[email_node]] + component)

        return result
