import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/HW3_Homework_Help_Session.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Class 3 Homework help
    ## Boolean Logic and Conditionals

    **Goal:** Help you develop problem-solving approaches using if/elif/else

    **Duration:** 15 minutes

    **Structure:** For each technique, we'll:
    1. Think through the LOGIC together
    2. Write PSEUDOCODE in plain English
    3. CODE it in Python immediately

    **New this week:** if/elif/else statements for making decisions!

    **Make a copy** of this notebook so you can refer back to it later!

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Framework with Decisions

    Remember the 4-step framework:
    1. What information do I have?
    2. What do I need to find?
    3. What are the steps?
    4. How do I write it in Python?

    **NEW:** Step 3 now includes DECISIONS!
    - "IF this condition is true, THEN do this"
    - "OTHERWISE, do that"

    Let's practice with simplified versions of your homework problems...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 1: Simple if/else Decisions

    ## Problem: Compare Two Scores

    **Given:**
    ```python
    aliceScore = 85
    bobScore = 78
    ```

    **Task:** Determine if Alice has the higher score.

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** What comparison do we need to make?

    **Question 2:** What are the two possible outcomes?

    **Question 3:** How do we handle each outcome differently?

    ---

    ### ✍️ Pseudocode:

    ```
    COMPARING SCORES:
    1. Create Boolean: aliceWon = (Alice's score > Bob's score)
    2. IF aliceWon == True THEN
         winner = "Alice"
    3. ELSE
         winner = "Bob"
    4. Print winner
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _():
    # Given data
    aliceScore = 85
    bobScore = 78

    # Create a Boolean variable
    aliceWon = (aliceScore > bobScore)
    print(f"Alice wins?: {aliceWon}")  # See the Boolean value

    # Use if/else with explicit Boolean comparison
    if aliceWon == True:
        winner = "Alice"
    else:
        winner = "Bob"

    print(f"Winner: {winner}")

    (aliceWon, winner)
    return


@app.cell
def _():
    # Another example: Checking a threshold
    score = 88

    # Create Boolean for passing
    isPassing = (score >= 70)

    if isPassing == True:
        print(f"PASS: Score of {score} is passing")
    else:
        print(f"FAIL: Score of {score} is not passing")

    isPassing
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Key points:**
    - Use `==` for comparison (not `=`)
    - Remember the colon `:` after condition
    - Indent the code inside if/else
    - Always use explicit comparisons: `== True` or `== False`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 2: Finding Maximum Value

    ## Problem: Find Highest Score

    **Given:**
    ```python
    scores = [85, 92, 78, 90]
    ```

    **Task:** Find the highest score

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** Where should we start?

    **Question 2:** What do we check for each score?

    **Question 3:** What do we do if we find a higher one?

    ---

    ### ✍️ Pseudocode:

    ```
    FINDING THE MAXIMUM:
    1. Assume first score is highest
    2. Check second score:
         IF second > highest THEN
           highest = second
    3. Check third score:
         IF third > highest THEN
           highest = third
    4. Check fourth score:
         IF fourth > highest THEN
           highest = fourth
    5. Print highest
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _():
    # Given data
    scores = [85, 92, 78, 90]

    # Start by assuming first score is highest
    highestScore = scores[0]
    print(f"Starting with: {highestScore}")

    # Check second score
    if scores[1] > highestScore:
        highestScore = scores[1]
        print(f"Found higher: {highestScore}")

    # Check third score
    if scores[2] > highestScore:
        highestScore = scores[2]
        print(f"Found higher: {highestScore}")

    # Check fourth score
    if scores[3] > highestScore:
        highestScore = scores[3]
        print(f"Found higher: {highestScore}")

    print(f"\nHighest score: {highestScore}")

    highestScore
    return (scores,)


@app.cell
def _(scores):
    # Finding minimum uses same pattern with < instead of >
    # (reusing the same `scores` list from the maximum example above)

    # Start by assuming first score is lowest
    lowestScore = scores[0]

    # Check each other score with <
    if scores[1] < lowestScore:
        lowestScore = scores[1]

    if scores[2] < lowestScore:
        lowestScore = scores[2]

    if scores[3] < lowestScore:
        lowestScore = scores[3]

    print(f"Lowest score: {lowestScore}")

    lowestScore
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Key points:**
    - Start with first value as current max/min
    - Check each other value individually
    - Update if you find higher/lower
    - Yes, this is repetitive - loops will fix this next week!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 3: Counting with Conditions (Accumulator Pattern)

    ## Problem: Count High Scores

    **Given:**
    ```python
    scores = [85, 92, 78, 90]
    ```

    **Task:** Count how many scores are 85 or above

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** What do we need to keep track of?

    **Question 2:** What condition do we check?

    **Question 3:** What do we do when condition is met?

    ---

    ### ✍️ Pseudocode:

    ```
    COUNTING WITH CONDITIONS:
    1. Start with count = 0
    2. Check first score:
         IF score >= 85 THEN
           count = count + 1
    3. Check second score:
         IF score >= 85 THEN
           count = count + 1
    4. Check third score:
         IF score >= 85 THEN
           count = count + 1
    5. Check fourth score:
         IF score >= 85 THEN
           count = count + 1
    6. Print count
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _(scores):
    # (reusing the same `scores` list from Technique 2)
    threshold = 85

    # MUST initialize counter first!
    countHighScores = 0

    # Check first score
    if scores[0] >= threshold:
        countHighScores = countHighScores + 1
        print(f"Score {scores[0]} counts!")

    # Check second score
    if scores[1] >= threshold:
        countHighScores = countHighScores + 1
        print(f"Score {scores[1]} counts!")

    # Check third score
    if scores[2] >= threshold:
        countHighScores = countHighScores + 1
        print(f"Score {scores[2]} counts!")

    # Check fourth score
    if scores[3] >= threshold:
        countHighScores = countHighScores + 1
        print(f"Score {scores[3]} counts!")

    print(f"\nScores >= {threshold}: {countHighScores} out of {len(scores)}")

    # Calculate percentage
    percentage = (countHighScores / len(scores)) * 100
    print(f"Percentage: {percentage}%")

    (countHighScores, percentage)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Key points:**
    - MUST initialize counter to 0 before checking!
    - Increment with `count = count + 1`
    - This is the "accumulator pattern"
    - Check each item individually (for now)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 4: Multiple Conditions with elif

    ## Problem: Course Enrollment Logic

    **Given:**
    ```python
    course = "EK210"
    enrolledCourses = ["EK125", "MA226", "CH102"]
    maxCourses = 4
    ```

    **Task:** Decide if student can add the course

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** What reasons prevent adding a course?

    **Question 2:** What order should we check?

    **Question 3:** What if both conditions are false?

    ---

    ### ✍️ Pseudocode:

    ```
    CHECKING ENROLLMENT:
    1. IF course already in enrolledCourses THEN
         Print "Already enrolled"
    2. ELSE IF number of courses >= maxCourses THEN
         Print "Cannot add - would exceed maximum"
    3. ELSE (can add it!)
         Add course to enrolledCourses
         Print "Adding to schedule"
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _():
    # Given data
    course = "EK210"
    enrolledCourses = ["EK125", "MA226", "CH102"]
    maxCourses = 4

    print(f"Trying to add: {course}")
    print(f"Current courses: {enrolledCourses}")
    print()

    # Check conditions in order
    if course in enrolledCourses:
        print(f"{course}: Already enrolled")
    elif len(enrolledCourses) >= maxCourses:
        print(f"{course}: Cannot add - would exceed maximum of {maxCourses} courses")
    else:
        enrolledCourses.append(course)
        print(f"{course}: Adding to schedule")

    print(f"\nFinal courses: {enrolledCourses}")

    enrolledCourses
    return


@app.cell
def _():
    # Another example: Grade categorization
    examScore = 87

    # Check from highest to lowest
    if examScore >= 90:
        grade = "A"
    elif examScore >= 80:
        grade = "B"
    elif examScore >= 70:
        grade = "C"
    elif examScore >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Score {examScore} = Grade {grade}")

    grade
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Key points:**
    - Use `elif` (NOT "else if")
    - Only ONE branch executes
    - Order matters - check most specific first
    - `else` catches everything else
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 5: Boolean Variables with String Checking

    ## Problem: Check for Multiple Words

    **Given:**
    ```python
    text = "This movie was great and awesome!"
    ```

    **Task:** Check if text contains positive words, build list of found words

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** How do we check if a word is in text?

    **Question 2:** How do we check MULTIPLE words?

    **Question 3:** How do we know if ANY word was found?

    **Question 4:** How do we build a list of found words?

    ---

    ### ✍️ Pseudocode:

    ```
    CHECKING FOR WORDS:
    1. Convert text to lowercase
    2. Check each word:
         hasGreat = ("great" in lowerText)
         hasAwesome = ("awesome" in lowerText)
         hasWonderful = ("wonderful" in lowerText)
    3. Combine with OR:
         hasPositive = (hasGreat == True) or (hasAwesome == True) or ...
    4. Build list of found words:
         foundWords = []
         IF hasGreat == True THEN
           foundWords.append("great")
         IF hasAwesome == True THEN
           foundWords.append("awesome")
         ...
    5. Print results
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _():
    # Given data
    text = "This movie was great and awesome!"

    # Convert to lowercase for case-insensitive checking
    lowerText = text.lower()
    print(f"Checking: {lowerText}")
    print()

    # Check each word individually
    hasGreat = ("great" in lowerText)
    hasAwesome = ("awesome" in lowerText)
    hasWonderful = ("wonderful" in lowerText)
    hasExcellent = ("excellent" in lowerText)

    print(f"Has 'great': {hasGreat}")
    print(f"Has 'awesome': {hasAwesome}")
    print(f"Has 'wonderful': {hasWonderful}")
    print(f"Has 'excellent': {hasExcellent}")
    print()

    # Combine with OR (ANY word found?)
    hasPositiveContent = (hasGreat == True) or (hasAwesome == True) or \
                         (hasWonderful == True) or (hasExcellent == True)

    print(f"Has positive content: {hasPositiveContent}")
    print()

    # Build list of found words
    foundWords = []
    if hasGreat == True:
        foundWords.append("great")
    if hasAwesome == True:
        foundWords.append("awesome")
    if hasWonderful == True:
        foundWords.append("wonderful")
    if hasExcellent == True:
        foundWords.append("excellent")

    print(f"Found words: {foundWords}")

    foundWords
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Key points:**
    - Convert to lowercase first (case-insensitive)
    - Create Boolean variable for each word
    - Combine with `or` (ANY) or `and` (ALL)
    - Build list by checking each Boolean
    - Yes, this is repetitive - loops next week!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 6: Combining AND/OR Logic

    ## Problem: Age-Appropriate Content

    **Given:**
    ```python
    textLength = 150
    hasInappropriateWords = False
    targetAudience = "child"
    ```

    **Task:** Determine if content is approved for audience

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** What makes content appropriate for children?

    **Question 2:** How do we combine multiple conditions?

    **Question 3:** How do we check different audiences?

    ---

    ### ✍️ Pseudocode:

    ```
    CHECKING APPROPRIATENESS:
    1. Create conditions for each audience:
         isAppropriateForChildren = (no bad words) AND (short) AND (simple)
         isAppropriateForTeens = (no bad words) AND (not too long)
         isAppropriateForAdults = True (adults can read anything)
    2. Check target audience and corresponding condition:
         IF (audience is "child") AND (appropriate for children) THEN
           approved = True
         ELSE IF (audience is "teen") AND (appropriate for teens) THEN
           approved = True
         ELSE IF audience is "adult" THEN
           approved = True
    3. Print result
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _():
    # Given data
    textLength = 150
    hasInappropriateWords = False
    hasManyWords = False
    targetAudience = "child"

    print(f"Text length: {textLength}")
    print(f"Has inappropriate words: {hasInappropriateWords}")
    print(f"Target audience: {targetAudience}")
    print()

    # Create compound conditions with AND
    isAppropriateForChildren = (hasInappropriateWords == False) and \
                               (textLength <= 200) and \
                               (hasManyWords == False)

    isAppropriateForTeens = (hasInappropriateWords == False) and \
                            (textLength <= 1000)

    isAppropriateForAdults = True  # Adults can read anything

    print(f"Appropriate for children: {isAppropriateForChildren}")
    print(f"Appropriate for teens: {isAppropriateForTeens}")
    print(f"Appropriate for adults: {isAppropriateForAdults}")
    print()

    # Decide based on target audience
    isApproved = False
    if (targetAudience == "child") and (isAppropriateForChildren == True):
        isApproved = True
    elif (targetAudience == "teen") and (isAppropriateForTeens == True):
        isApproved = True
    elif targetAudience == "adult":
        isApproved = True

    if isApproved == True:
        print(f"APPROVED: Content approved for {targetAudience} audience")
    else:
        print(f"NOT APPROVED: Content not appropriate for {targetAudience} audience")

    (isApproved, isAppropriateForChildren, isAppropriateForTeens)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Key points:**
    - `and` = ALL conditions must be True
    - `or` = AT LEAST ONE must be True
    - Use parentheses for clarity
    - Always use explicit comparisons: `== True`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 🎯 How These Apply to Your Homework

    ### Problem 1: Grade Book
    - ✅ **Technique 1:** Compare averages (who won?)
    - ✅ **Technique 2:** Find max/min (check all 8 scores)
    - ✅ **Technique 3:** Count scores >= 85

    ### Problem 2: Course Registration
    - ✅ **Technique 4:** Multiple conditions with elif
    - Check: already enrolled? at max? then add
    - Repeat for each desired course

    ### Problem 3: Email Validator
    - ✅ **Technique 1:** Simple if/else for validation
    - ✅ **Technique 3:** Count valid emails
    - Repeat for each email

    ### Problem 4: Combined Practice
    - ✅ **Technique 5:** Check for multiple words
    - ✅ **Technique 6:** Complex AND/OR logic
    - All techniques together!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 📝 Quick Reference: if/elif/else Syntax

    ```python
    # Simple if/else
    if condition == True:
        # do this
    else:
        # do that

    # Multiple conditions
    if condition1 == True:
        # do this
    elif condition2 == True:
        # do that
    elif condition3 == True:
        # do something else
    else:
        # do default

    # Just if (no else needed)
    if condition == True:
        # do something
    # code continues regardless
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 📝 Quick Reference: Boolean Operators

    ```python
    # Comparison operators
    a == b    # Equal to
    a != b    # Not equal to
    a < b     # Less than
    a > b     # Greater than
    a <= b    # Less than or equal
    a >= b    # Greater than or equal

    # Logical operators
    a and b   # Both must be True
    a or b    # At least one must be True
    not a     # Opposite of a

    # Membership operators
    x in list        # Is x in the list?
    x not in list    # Is x NOT in the list?
    "word" in text   # Is word in the text?

    # ALWAYS use explicit Boolean comparisons
    if isValid == True:     # GOOD
    if isValid:             # BAD (avoid in this course)

    if hasError == False:   # GOOD
    if not hasError:        # BAD (avoid in this course)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## ⚠️ Common Mistakes to Avoid

    ### 1. Using = instead of ==
    ```python
    # WRONG:
    if score = 90:

    # RIGHT:
    if score == 90:
    ```

    ### 2. Forgetting the colon
    ```python
    # WRONG:
    if score >= 90
        grade = "A"

    # RIGHT:
    if score >= 90:
        grade = "A"
    ```

    ### 3. Not initializing counter
    ```python
    # WRONG:
    if score >= 85:
        count = count + 1  # count doesn't exist yet!

    # RIGHT:
    count = 0  # Initialize first!
    if score >= 85:
        count = count + 1
    ```

    ### 4. Wrong indentation
    ```python
    # WRONG:
    if score >= 90:
    grade = "A"  # Not indented!

    # RIGHT:
    if score >= 90:
        grade = "A"  # Indented 4 spaces
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 💡 Why So Repetitive?

    You'll notice Problems 4-6 (and 10) require repetitive code:

    ```python
    # Checking 8 scores individually:
    if score[0] >= 85:
        count = count + 1
    if score[1] >= 85:
        count = count + 1
    # ... 6 more times!
    ```

    **This is intentional!**

    Next week in Class 5, you'll learn **for loops**:

    ```python
    # What you'll learn next week:
    for score in scores:
        if score >= 85:
            count = count + 1
    ```

    Much shorter! The repetition helps you:
    1. Appreciate why loops are useful
    2. Understand what the loop does
    3. Practice conditional logic thoroughly

    Embrace the repetition!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## ✅ Remember for Tonight:

    1. **Write pseudocode first** - plan your decisions in English
    2. **Use the 4-step framework** - especially for complex problems
    3. **Be explicit with Booleans** - always `== True` or `== False`
    4. **Initialize counters** - start at 0 before checking!
    5. **Test frequently** - run code after each piece
    6. **Order matters with elif** - most specific first
    7. **The repetition teaches** - loops come next week!

    ---

    ## 🎉 You're Ready for Problems 4-10!

    **Office hours:** Sunday/Tuesday/Thursday evenings

    **You already did Problems 1-3** - halfway done!

    Good luck! 🚀
    """)
    return


if __name__ == "__main__":
    app.run()
