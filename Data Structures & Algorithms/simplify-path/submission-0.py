class Solution:
    def simplifyPath(self, path: str) -> str:
        # simplified canonical path -> 
        # '.' curdir
        # '..' prev dir
        # '/////' ignore and just do '/'
        # '...', '....'... treated as valid name
        # path must start with a single '/'
        # directories must be separated by exactly 1 slash
        # path must not end with a slash unless it's the root directory
        # no single or double periods
        # --------
        # if a slash is found - ok if stack[-1] doesn't contain any slashes. 
        #                           else, skip
        # if a char is found, keep reading and add to stack
        # if a dot is found, skip
        s = []
        for dir in path.split('/'):
            if dir == '' or dir == '.':
                continue
            elif dir == '..':
                if s:
                    s.pop()
            else:
                s.append(dir)
        return '/' + '/'.join(s)
