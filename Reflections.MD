### Questions (Reflection)

> [!IMPORTANT]
> 1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest issues to fix where the ones which were marked as styling conventions, such as spacing between operators, newline at the end of the code, etc. The hardest to do was to handle global instances, as the code had to be re-written to implement classes instead of just plain functions.

> [!IMPORTANT]
> 2. Did the static analysis tools report any false positives? If so, describe one example.
The pylint_report.txt included reports of generalized `except` statements, which can be used to catch certain errors which can be otherwise looked over. That, in my opinion, would be a false positive.

> [!IMPORTANT]
> 3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
Local integration uses **`pre-commit` hooks** to run quick checks like **Flake8** and **Bandit** on staged files for instant developer feedback. CI integration runs a full analysis, including **Pylint**, as a **mandatory Quality Gate** that blocks Pull Requests if new issues or drops in quality standards are detected.

> [!IMPORTANT]
> 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes? `docstrings` helped in deciphering what a function does just by glancing at it, making it perfectly documented. Shorter lines, proper spaces between functions, newline at the end of the program also helps in proper readability of any code. Using classes, keeping all affected objects contained in a neatly typed manner helps in handling errors as one does not need to go over the entire codebase trying to find a bug.

