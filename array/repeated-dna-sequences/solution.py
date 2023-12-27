"""
https://github.com/eugenechevski
https://leetcode.com/problems/repeated-dna-sequences
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
            Can we find a way to create a unique key for each substring?
            DNA code will be stored as a 64-bit number
            where the first (from the right) 10 bits are used for 'A'
            nucleotide and all other ocupy the other 30. For instance the DNA sequence
            AAAAACCGGT is encoded as 1000000000 0110000000 0001100000 0000011111
                                         T          G           C         A
        """

        if len(s) < 10:
            return []

        def encode(nucl, i):
            base = 0  # A is default

            if nucl == 'C':
                base = 10
            elif nucl == 'G':
                base = 20
            elif nucl == 'T':
                base = 30

            return 1 << (base + i)

        def decode(i):
            res = 'A'
            base = i // 10
            if base == 1:
                res = 'C'
            elif base == 2:
                res = 'G'
            elif base == 3:
                res = 'T'

            return res

        # Build the first DNA sequence
        current = 0
        for i in range(10):
            current |= encode(s[i], i)

        # Find all sequences
        seen = set([current])
        result = set()
        for i in range(1, len(s) - 9):
            # Slide the window
            current ^= encode(s[i - 1], 0)
            current >>= 1
            current |= encode(s[i + 9], 9)

            if current in seen and current not in result:
                result.add(current)
            else:
                seen.add(current)

        # Decode the result
        final = []
        for encoded in list(result):
            decoded = [''] * 10
            count = 0
            for i in range(40):
                if (1 << i) & encoded:
                    decoded[i % 10] = decode(i)
                    count += 1
                if count == 10:
                    break
            final.append(''.join(decoded))

        return final
