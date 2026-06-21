class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num_of_seniors = 0

        for string in details:
            age = int(string[11:13])

            if age > 60:
                num_of_seniors += 1


        return (num_of_seniors)

        