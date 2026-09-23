import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class3_GPP.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Class 3 Morning Assignment: Boolean Logic Practice (GPP)

        **Group Work (Teams of 3)**

        📖 [Full reading: Class 3](https://BU-EK125.github.io/EK125/class/Class3.html)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("## Part 1: Boolean Naming Practice and Expression Evaluation")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### Boolean Naming Exercise (5 minutes)

        Work together to improve these poorly named Boolean variables. Remember:
        Boolean names should ask questions!
        """
    )
    return


@app.cell
def _():
    # Poor names - discuss and rename them as a group
    weather = isRaining              # Better: ?
    user = currentUser is not None   # Better: ?
    data = (len(results) > 0)        # Better: ?
    time = (hour >= 9) and (hour <= 17)  # Better: ?
    access = (userRole == "admin")   # Better: ?
    validation = (email.count("@") == 1)  # Better: ?
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("**Group Discussion:** What makes a good Boolean variable name?")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### Boolean Expression Evaluation

        Work together to evaluate these expressions **by hand first**, then verify
        with Python:
        """
    )
    return


@app.cell
def _():
    # Expression 1
    result1 = (True and False) or True
    print(f"Expression 1: {result1}")

    # Expression 2
    result2 = not ((False or True) and True)
    print(f"Expression 2: {result2}")

    # Expression 3
    result3 = (5 > 3) and (2 < 4) or (10 == 10)
    print(f"Expression 3: {result3}")

    # Expression 4
    result4 = not (7 >= 7) or (3 != 4)
    print(f"Expression 4: {result4}")

    (result1, result2, result3, result4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "**Group Discussion:** Did your hand calculations match Python's results? "
        "If not, discuss why."
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("## Part 2: Weather Decision System")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Create a program that helps decide what to wear based on weather conditions.

        **Your Task:** Complete the TODO sections with appropriate Boolean
        expressions using parentheses.

        **Important:** Use explicit Boolean comparisons throughout!
        """
    )
    return


@app.cell
def _():
    # Get weather conditions
    temperature = 72.0  # originally: float(input("Enter temperature (°F): "))
    isRaining = False  # originally: input("Is it raining? (yes/no): ").lower() == "yes"
    isWindy = True  # originally: input("Is it windy? (yes/no): ").lower() == "yes"
    humidity = 55.0  # originally: float(input("Enter humidity percentage: "))

    # Decision logic - complete these conditions using explicit comparisons
    needsJacket = (temperature < 60) or isWindy
    needsUmbrella = None  # TODO: Complete this condition
    isComfortable = None  # TODO: Complete this condition (temp between 65-80, not raining, humidity < 70)
    stayInside = None  # TODO: Complete this condition (very cold OR very hot OR raining AND windy)

    # Output recommendations using explicit Boolean checks
    print("\n--- Weather Recommendations ---")
    if needsJacket == True:
        print("Bring a jacket!")

    if needsUmbrella == True:
        print("Take an umbrella!")

    if isComfortable == True:
        print("Perfect weather to be outside!")

    if stayInside == True:
        print("Maybe consider staying indoors today")

    (needsJacket, needsUmbrella, isComfortable, stayInside)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("## Part 3: Grade Calculator with Conditions")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Create a grade evaluation system using clear Boolean naming and explicit
        comparisons:

        **Your Task:** Complete the Boolean expressions using proper naming and
        parentheses.
        """
    )
    return


@app.cell
def _():
    # Student information
    homeworkScore = 85.0  # originally: float(input("Enter homework average (0-100): "))
    examScore = 78.0  # originally: float(input("Enter exam score (0-100): "))
    attendanceRate = 92.0  # originally: float(input("Enter attendance rate (0-100%): "))
    hasExtraCredit = True  # originally: input("Extra credit completed? (yes/no): ").lower() == "yes"

    # Grade calculations
    finalScore = (homeworkScore * 0.4) + (examScore * 0.6)
    if hasExtraCredit == True:
        finalScore = finalScore + 5  # 5 point bonus

    # Conditions to determine - work together on these using good Boolean naming
    isPassing = None  # TODO: final score >= 60 AND attendance >= 75%
    hasHonors = None  # TODO: final score >= 90 AND attendance >= 95%
    needsImprovement = None  # TODO: homework < 70 OR exam < 65 OR attendance < 80%
    isExcellent = None  # TODO: final score >= 95 AND attendance == 100 AND hasExtraCredit

    # Output results using explicit Boolean comparisons
    print(f"\nFinal Score: {finalScore:.1f}")
    print(f"Attendance: {attendanceRate}%")

    if isExcellent == True:
        print("Excellent work! You're a star student!")
    elif hasHonors == True:
        print("Honors achievement!")
    elif isPassing == True:
        print("Passing grade - well done!")
    else:
        print("Not passing - please see instructor")

    if needsImprovement == True:
        print("Areas for improvement identified")

    (finalScore, isPassing, hasHonors, needsImprovement, isExcellent)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("## Part 4: Login Validator with Truth Tables")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "**Challenge:** Create a truth table on paper for the `canLogin` logic "
        "before testing your code!"
    )
    return


@app.cell
def _():
    # User credentials
    username = "alice123"  # originally: input("Enter username: ")
    password = "Secret123"  # originally: input("Enter password: ")
    isWeekend = False  # originally: input("Is it weekend? (yes/no): ").lower() == "yes"
    hourOfDay = 14  # originally: int(input("Enter hour (0-23): "))

    # TODO: Check if password contains at least one uppercase letter
    # Hint: Use a for loop to check each character with char.isupper()
    hasUpperCase = False  # HINT: Start as false, then look for conditions where it will be true

    # Write your code here
    # .
    # .
    # .

    # TODO: Check if password contains at least one digit
    # Hint: Use a for loop and char.isdigit()

    hasDigit = False  # HINT: Start as false, then look for conditions where it will be true
    # Write your code here
    # .
    # .
    # .

    # Validation rules - figure these out together using explicit Boolean logic
    isValidUsername = (len(username) >= 5) and username.isalnum()
    isValidPassword = None  # TODO: length >= 8 AND contains both uppercase letters and numbers
    isBusinessHours = None  # TODO: hour between 9 and 17 (inclusive) AND not weekend
    hasAdminAccess = (username.lower() == "admin") and (password == "admin123")

    # Access decision using explicit Boolean checks
    canLogin = (isValidUsername and isValidPassword) or hasAdminAccess
    fullAccess = canLogin and isBusinessHours

    print(f"\nUsername valid: {isValidUsername}")
    print(f"Password valid: {isValidPassword}")
    print(f"Business hours: {isBusinessHours}")

    if fullAccess == True:
        print("Full access granted!")
    elif canLogin == True:
        print("Limited access granted (outside business hours)")
    else:
        print("Access denied")

    (isValidUsername, isValidPassword, isBusinessHours, hasAdminAccess, canLogin, fullAccess)
    return


if __name__ == "__main__":
    app.run()
