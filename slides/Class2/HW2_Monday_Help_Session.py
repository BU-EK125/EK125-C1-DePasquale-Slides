import marimo

__generated_with = "0.24.0"
app = marimo.App(
    width="full",
    layout_file="layouts/HW2_Monday_Help_Session.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Homework 2 Help Session
    ## Problems 1-3: Strings and Lists

    **Goal:** Help you develop the problem-solving approach for tonight's homework

    **Duration:** 15 minutes

    **Structure:** For each technique, we'll:
    1. Think through the LOGIC together
    2. Write PSEUDOCODE in plain English
    3. CODE it in Python immediately

    **Make a copy** of this notebook so you can refer back to it later!

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Four-Step Problem-Solving Framework

    For EVERY problem in your homework, use this approach:

    1. **What information do I have?** (Inputs/Given data)
    2. **What do I need to find?** (Outputs/Goals)
    3. **What are the steps to get from inputs to outputs?** (Algorithm)
    4. **How do I write those steps in Python?** (Code)

    Let's practice with simplified versions of your homework problems...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 1: Splitting Strings and Accessing Parts

    ## Problem: Extract First, Middle, and Last Names

    **Given:**
    ```python
    fullName = "Jane Marie Smith"
    ```

    **Task:** Extract and print the first, middle, and last names separately

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** What tool do we have for breaking up strings by spaces?

    **Question 2:** Once we split the name, what do we get?

    **Question 3:** How do we access individual parts from a list?

    ---

    ### ✍️ Pseudocode:

    ```
    EXTRACTING NAMES:
    1. Split the full name by spaces → get a list of words
    2. Access index 0 → first name
    3. Access index 1 → middle name
    4. Access index 2 → last name
    5. Print each one
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _():
    # Given data
    fullName = "Jane Marie Smith"

    # Step 1: Split by spaces
    nameParts = fullName.split()
    print("Name parts:", nameParts)  # See what we got

    # Step 2-4: Access each part by index
    firstName = nameParts[0]
    middleName = nameParts[1]
    lastName = nameParts[2]

    # Step 5: Print results
    print(f"First: {firstName}")
    print(f"Middle: {middleName}")
    print(f"Last: {lastName}")

    (firstName, middleName, lastName)
    return firstName, lastName, middleName


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 2: Splitting on Different Characters

    ## Problem: Extract Username from Email

    **Given:**
    ```python
    email = "jane.smith@university.edu"
    ```

    **Task:** Extract just the username (part before @)

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** What character separates the username from the domain?

    **Question 2:** Can we split on that character?

    **Question 3:** Which part do we want - before or after the @?

    ---

    ### ✍️ Pseudocode:

    ```
    EXTRACTING USERNAME:
    1. Split email by "@" → get list with 2 parts
    2. First part (index 0) = username
    3. Second part (index 1) = domain (we don't need this)
    4. Print username
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _():
    # Given data
    email = "jane.smith@university.edu"

    # Split by @ to separate username and domain
    emailParts = email.split("@")
    print("Email parts:", emailParts)  # See what we got

    # Access the parts
    username = emailParts[0]
    domain = emailParts[1]

    print(f"Username: {username}")
    print(f"Domain: {domain}")

    (username, domain)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 3: Building Strings from Pieces

    ## Problem: Create Initials from Names

    **Given:**
    ```python
    firstName = "Jane"
    middleName = "Marie"
    lastName = "Smith"
    ```

    **Task:** Create initials like "J.M.S."

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** How do we get just the first letter of a word?

    **Question 2:** What do we need to add after each letter?

    **Question 3:** How do we combine strings together?

    ---

    ### ✍️ Pseudocode:

    ```
    CREATING INITIALS:
    1. Get first letter of firstName [0] → add "."
    2. Get first letter of middleName [0] → add "."
    3. Get first letter of lastName [0] → add "."
    4. Combine all pieces with +
    5. Print result
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _(firstName, lastName, middleName):
    # Given data — same firstName/middleName/lastName as Technique 1
    # (there they came from splitting; here they're literally "Jane"/"Marie"/"Smith")

    # Method 1: Using + to combine
    initials = firstName[0] + "." + middleName[0] + "." + lastName[0] + "."
    print(f"Initials: {initials}")

    # Method 2: Using f-string (also works!)
    initials2 = f"{firstName[0]}.{middleName[0]}.{lastName[0]}."
    print(f"Initials (f-string): {initials2}")

    (initials, initials2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 4: Cleaning Text (Multiple Replacements)

    ## Problem: Remove Punctuation from Text

    **Given:**
    ```python
    message = "Hello! How are you?"
    ```

    **Task:** Remove punctuation (! and ?) and convert to lowercase

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** How do we remove characters we don't want?

    **Question 2:** Can we replace them with nothing (empty string)?

    **Question 3:** What method makes everything lowercase?

    ---

    ### ✍️ Pseudocode:

    ```
    CLEANING TEXT:
    1. Replace "!" with "\" (empty string)
    2. Replace "?" with "\"
    3. Replace "." with "\"
    4. Replace "'" with "\"
    5. Convert to lowercase
    6. Split into words
    7. Get first and last words
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _():
    # Given data
    message = "Hello! How are you?"

    # Remove punctuation step by step
    cleaned = message.replace("!", "")
    cleaned = cleaned.replace("?", "")
    cleaned = cleaned.lower()

    print(f"Original: {message}")
    print(f"Cleaned: {cleaned}")

    # Split into words
    words = cleaned.split()
    print(f"Words: {words}")

    # Get first and last words
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")  # -1 gets the last item!

    words
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 5: Counting Characters in Strings

    ## Problem: Count Sentences

    **Given:**
    ```python
    text = "Hello! How are you? I'm fine."
    ```

    **Task:** Count how many sentences (count . ! ?)

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** What marks the end of a sentence?

    **Question 2:** Can we count each punctuation mark separately?

    **Question 3:** How do we add them all together?

    ---

    ### ✍️ Pseudocode:

    ```
    COUNTING SENTENCES:
    1. Count periods "." in text
    2. Count exclamations "!" in text
    3. Count questions "?" in text
    4. Add all three counts together
    5. Print total
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _():
    # Given data
    text = "Hello! How are you? I'm fine."

    # Count total characters
    charCount = len(text)
    print(f"Characters: {charCount}")

    # Count each type of punctuation
    periods = text.count(".")
    exclamations = text.count("!")
    questions = text.count("?")

    print(f"Periods: {periods}")
    print(f"Exclamations: {exclamations}")
    print(f"Questions: {questions}")

    # Add them up
    sentenceCount = periods + exclamations + questions
    print(f"Total sentences: {sentenceCount}")

    sentenceCount
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 6: List Modifications

    ## Problem: Build and Modify a Shopping List

    **Given:**
    ```python
    shoppingList = []
    ```

    **Tasks:**
    1. Add items
    2. Remove an item
    3. Insert at a specific position
    4. Sort alphabetically

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** What method adds to the END of a list?

    **Question 2:** What method removes a specific item by name?

    **Question 3:** What method puts something at a specific position?

    **Question 4:** What method sorts alphabetically?

    ---

    ### ✍️ Pseudocode:

    ```
    MODIFYING A LIST:
    1. Start with empty list []
    2. Append "milk"
    3. Append "bread"
    4. Append "eggs"
    5. Remove "bread"
    6. Insert "butter" at position 1
    7. Sort the list
    8. Print final list
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _():
    # Start with empty list
    shoppingList = []
    print(f"Start: {shoppingList}")

    # Add items to end
    shoppingList.append("milk")
    shoppingList.append("bread")
    shoppingList.append("eggs")
    print(f"After adding: {shoppingList}")

    # Remove an item
    shoppingList.remove("bread")
    print(f"After removing bread: {shoppingList}")

    # Insert at position 1
    shoppingList.insert(1, "butter")
    print(f"After inserting butter: {shoppingList}")

    # Sort alphabetically
    shoppingList.sort()
    print(f"After sorting: {shoppingList}")

    # Other useful operations
    print(f"Length: {len(shoppingList)}")
    print(f"Count of 'eggs': {shoppingList.count('eggs')}")

    shoppingList
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    # Technique 7: Calculating with Lists

    ## Problem: Calculate Total Cost

    **Given:**
    ```python
    prices = [2.50, 1.25, 3.00, 4.00]
    ```

    **Task:** Calculate total and average

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** How do we add up all the prices?

    **Question 2:** How do we calculate an average?

    ---

    ### ✍️ Pseudocode:

    ```
    CALCULATING TOTAL:
    1. Add prices[0] + prices[1] + prices[2] + prices[3]
    2. Store in total
    3. Divide total by number of items
    4. Store in average
    5. Print both
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _():
    # Given data
    prices = [2.50, 1.25, 3.00, 4.00]

    # Calculate total by adding each price
    total = prices[0] + prices[1] + prices[2] + prices[3]
    print(f"Total: ${total}")

    # Calculate average
    average = total / len(prices)
    print(f"Average: ${average}")

    # Note: Next week you'll learn loops to make this shorter!
    # For now, we add each item individually

    (total, average)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 🎯 How These Apply to Your Homework

    ### Problem 1: Personal Information Processor
    - ✅ **Technique 1:** Split name to get first/middle/last
    - ✅ **Technique 2:** Split email to get username
    - ✅ **Technique 3:** Build initials from first letters
    - ✅ **Technique 6:** Add to hobbies list and sort

    ### Problem 2: Shopping List Manager
    - ✅ **Technique 6:** All list operations (append, remove, insert, count)
    - ✅ **Technique 7:** Calculate total cost

    ### Problem 3: Text Message Analyzer
    - ✅ **Technique 4:** Clean text (remove punctuation)
    - ✅ **Technique 5:** Count characters and sentences
    - ✅ **Technique 1:** Split into words, get first/last
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 📝 Quick Reference: String Methods

    ```python
    # Changing case
    text.upper()      # "HELLO"
    text.lower()      # "hello"
    text.title()      # "Hello World"

    # Splitting and joining
    text.split()      # Split by spaces → list
    text.split("@")   # Split by specific character

    # Modifying
    text.replace("old", "new")  # Replace text
    text.strip()      # Remove leading/trailing spaces

    # Checking
    text.count("a")   # Count occurrences
    "@" in text       # Check if contains
    len(text)         # Length

    # Accessing
    text[0]           # First character
    text[-1]          # Last character
    text[0:5]         # Slice (first 5)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 📝 Quick Reference: List Methods

    ```python
    # Adding items
    myList.append(item)        # Add to end
    myList.insert(index, item) # Add at position
    myList.extend(otherList)   # Add multiple items

    # Removing items
    myList.remove(item)        # Remove by value
    myList.pop()               # Remove last item
    myList.pop(index)          # Remove by position

    # Organizing
    myList.sort()              # Sort in place
    myList.reverse()           # Reverse order

    # Checking
    myList.count(item)         # Count occurrences
    item in myList             # Check if contains
    len(myList)                # Length

    # Accessing
    myList[0]                  # First item
    myList[-1]                 # Last item
    myList[1:3]                # Slice
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## ✅ Remember for Tonight:

    1. **Always use the 4-step framework** - don't jump straight to code!
    2. **Write pseudocode first** - English before Python
    3. **Test frequently** - run your code after each small piece
    4. **Use good variable names** - `firstName` not `x`
    5. **Add comments** - explain your thinking
    6. **Problems 1-3 only use strings and lists** - no if/else needed!

    ---

    ## 🎉 You're Ready!

    **Office hours:** Sunday/Tuesday/Thursday evenings if you get stuck

    Good luck! 🚀
    """)
    return


if __name__ == "__main__":
    app.run()
