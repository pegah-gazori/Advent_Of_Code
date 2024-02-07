**Automatic Data Retrieval**

In order to make this process automatic, you can use [advent-of-code-data](https://pypi.org/project/advent-of-code-data/) package. 
The steps to use this package are as follows:

1- Install the package using `pip install advent-of-code-data`.

2- Get the session ID from the browser. In order to do this, open [Advent of Code](https://adventofcode.com/) website in your browser. From settings, select **developer tools** and then in the **network** tab, click on a **post request**. Then, copy the **session** data from the cookie.

3- Now, change the directory to **.config** using `cd ~/.config`. (create if it does not exist). Then create a directory for advent of code using `mkdir aocd`. Inside of this directory, create a file using `cd aocd` and `touch token`. Finally, paste the session content (from previous step) to this file and save it.

