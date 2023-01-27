#!/bin/bash

echo "Enter the location of the new folder:"
read folderLocation
echo "Enter a name for the new solution:"
read solutionName

solutionNameLower=`echo $solutionName | tr '[:upper:]' '[:lower:]' | tr ' ' '-'`
mkdir $folderLocation/$solutionNameLower
touch $folderLocation/$solutionNameLower/solution.py
echo '"""' > $folderLocation/$solutionNameLower/solution.py
echo 'https://github.com/eugenechevski' >> $folderLocation/$solutionNameLower/solution.py
echo "https://leetcode.com/problems/$solutionNameLower" >> $folderLocation/$solutionNameLower/solution.py
echo '"""' >> $folderLocation/$solutionNameLower/solution.py

# TODO: add to README.md