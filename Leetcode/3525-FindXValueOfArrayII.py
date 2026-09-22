class Solution:
    def resultArray(self, nums, k, queries):

        n = len(nums)

        # Each node:
        # [product of segment, count of each remainder]
        tree = [[1, [0] * k] for _ in range(4 * n)]

        def merge(left, right):

            left_prod, left_cnt = left
            right_prod, right_cnt = right

            # Start with prefixes completely inside left
            cnt = left_cnt[:]

            # Add prefixes that use all of left + prefix of right
            for r in range(k):
                new_r = (left_prod * r) % k
                cnt[new_r] += right_cnt[r]

            prod = (left_prod * right_prod) % k

            return [prod, cnt]

        def build(node, l, r):

            if l == r:
                value = nums[l] % k

                tree[node] = [
                    value,
                    [1 if i == value else 0 for i in range(k)]
                ]

                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, value):

            if l == r:

                value %= k

                tree[node] = [
                    value,
                    [1 if i == value else 0 for i in range(k)]
                ]

                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):

            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

            # Update
            nums[index] = value

            update(1, 0, n - 1, index, value)

            # Query nums[start ... n-1]
            result = query(
                1, 0, n - 1,
                start,
                n - 1
            )

            # Number of prefixes with remainder x
            ans.append(result[1][x])

        return ans
