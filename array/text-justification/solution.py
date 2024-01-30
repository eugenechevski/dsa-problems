"""
https://github.com/eugenechevski
https://leetcode.com/problems/text-justification
"""


class Solution:
    def fullJustify(self, words, maxWidth):
        lines = []  # all lines
        currentWidth = -1  # the minimum width of the current line
        newLineStart = 0  # index of the start of the current line
        for i, w in enumerate(words):
            currentWidth += len(w) + 1

            if currentWidth > maxWidth:
                currentWidth -= len(w) + 1  # subtract the last word

                # Calculate the space count
                spaceCount = i - newLineStart - 1
                line = ''
                if spaceCount == 0:
                    word = words[newLineStart]
                    line += word + ' ' * (maxWidth - len(word))
                else:
                    currentWidth -= spaceCount
                    spaceWidth = (maxWidth - currentWidth) // spaceCount
                    spaceRemainder = (maxWidth - currentWidth) % spaceCount
                    for j in range(newLineStart, i):
                        line += words[j]
                        if j < i - 1:
                            line += ' ' * spaceWidth
                            if spaceRemainder > 0:
                                line += ' '
                                spaceRemainder -= 1

                # Add the new line
                lines.append(line)

                # Start the new line
                currentWidth = len(w)
                newLineStart = i

        # Add the last line
        # Justify to the left
        line = ''
        for i in range(newLineStart, len(words)):
            line += words[i]
            if i < len(words) - 1:
                line += ' '
        line += ' ' * (maxWidth - len(line))
        lines.append(line)

        return lines
