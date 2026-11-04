class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []

        for n in nums:
            if len(pre) == 0:
                pre.append(n)
            else:
                pre.append(pre[-1] * n)

        for n in reversed(nums):
            if len(post) == 0:
                post.append(n)
            else:
                post.append(post[-1] * n)

        post = post[::-1]
        # print(pre, post)
        results = []
        pre_i = -1
        post_i = 1
        for i, n in enumerate(nums):
            if post_i >= len(nums):
                results.append(pre[pre_i])
            elif pre_i < 0:
                results.append(post[post_i])
            else:
                results.append(pre[pre_i] * post[post_i])
            pre_i += 1
            post_i += 1

        return results 

