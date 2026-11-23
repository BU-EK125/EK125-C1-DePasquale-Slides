import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/DiceGames.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # The Same Dice Game, Eleven Ways

    ### From Python to Machine Code, and Beyond

    🧪 [Run the full interactive notebook in Colab](https://colab.research.google.com/github/BU-EK125/EK125-C1-DePasquale-Slides/blob/main/slides/DiceGames/dice_games_fortran_to_machine_code.ipynb)

    *(Same notebook the "Open in Colab" button above opens -- unlike
    most decks on this site, this one's button links to the real,
    runnable notebook, not a flattened read-only copy. Every
    language here actually compiles and runs there. Colab may open
    it in "playground mode" first -- click "Copy to Drive" to run
    cells.)*

    *Curious how these slides work? They're built with
    [marimo](https://marimo.io), a Python notebook that runs live,
    right in your browser.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    One tiny program, written at every level of the stack, so you
    can see what changes as you move closer to the hardware -- and
    what stays the same.

    **The game:** you and the computer each roll two dice per round.
    Higher total wins the round, ties score nothing. Five rounds,
    then a winner, then an optional rematch.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    | # | Version | Era | What it is |
    |---|---------|-----|-----------|
    | 1 | Python | 1991 | Readable, built-in random numbers |
    | 2 | Fortran 90 | 1990s | Modern, free-form, built-in random |
    | 3 | Fortran 77 | 1977 | Fixed-form, column-sensitive, `GO TO` |
    | 4 | BASIC | 1964+ | Line-numbered, interpreted |
    | 5 | C | 1970s | Compiled, close to the hardware |
    | 6 | x86-64 assembly | 1950s idea | One line per CPU instruction |
    | 7 | Machine code | the CPU's own language | The same program as raw bytes |
    | 8 | Brainfuck | 1993 | Eight commands and a tape of bytes |
    | 9 | Chef | 2002 | Programs that read like recipes |
    | 10 | Piet | 2001 | Programs that are abstract paintings |
    | 11 | Whitespace | 2003 | Written only in spaces, tabs, newlines |

    Versions 1-7 are a ladder from a high-level language down to the
    machine. Versions 8-11 are **esoteric languages**: the same game,
    on strange models of computation, to show how little a language
    actually needs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Abstraction Ladder
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
     Fortran / BASIC / C   <- describe WHAT to do
            |  compiler or interpreter
            v
        assembly           <- one line per instruction
            |  assembler
            v
         machine code      <- the bytes the CPU runs
            |  CPU decoder
            v
        logic gates and transistors
    ```

    Everything above machine code is a convenience for humans. The
    CPU only ever sees the bytes at the bottom.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Before We Start: How Does a Computer Run a Program?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Source code** is the text a person writes, like `print("hi")`.
    A CPU can't run that directly -- it only understands **machine
    code**: long lists of numbers, each one a tiny instruction such
    as "add these two numbers" or "jump to another instruction."

    So every program has to be **translated**. Which way a language
    does that explains most of the differences you'll see below.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Four words you'll need

    | Word | What it is | Everyday comparison |
    |------|-----------|---------------------|
    | **Compiler** | Translates *all* your source ahead of time into a file you can run any time | Translating a whole book once, then handing out copies |
    | **Interpreter** | Reads your source and does what it says *as it goes*, no separate file | A live interpreter at a meeting |
    | **Assembler** | A small compiler for assembly language (readable words instead of numbers) | Writing each number out in words |
    | **Linker** | Joins translated pieces, and library code, into one runnable file | Binding chapters into one book |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### A few more ideas

    - **Library:** code someone else wrote that you reuse -- like the
      code that prints text on screen
    - **Operating system (OS):** manages the computer; programs ask
      it for things ("print this", "read a key") via **system calls**
    - **Stack:** a pile where you only add or remove at the top, like
      a stack of plates. Several languages here work this way
    - **Pseudo-random numbers:** a computer can't truly roll dice --
      it uses a formula that turns one number into the next, looking
      random. The starting number is the **seed**: same seed, same
      "random" rolls
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### How to read the real notebook's cells

    Every notebook you've used in this course so far has been
    ordinary Python cells. The real notebook behind this deck adds
    three new kinds of cell -- all standard Colab/Jupyter features,
    not anything specific to this notebook:

    - **`%%writefile name`** as a cell's first line saves everything
      below it as a file called `name`. It does **not** run
      anything -- it's how each `dice_game.py`/`.f90`/`.c`/... source
      file gets created in the first place
    - **A line starting with `!`** runs a shell command, exactly as
      if you'd typed it into a terminal -- `!gcc dice_game.c -o
      dice_c` runs the C compiler the same way it would outside
      Colab
    - **`printf '\\n\\n\\n\\n\\nn\\n' | ./program`** feeds typed-out
      input into a program automatically. Colab's `!` cells can't
      pause and wait for you to type while they run, so each `\\n`
      stands in for one press of Enter, and the final `n` declines
      the rematch. The `|` is a **pipe**: it sends one command's
      output straight into the next command's input, instead of to
      the screen
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Setup
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    The real notebook installs:

    - `gfortran` -- compiles both Fortran versions
    - `bwbasic` -- a BASIC interpreter
    - `gcc`, `as`, `ld` -- C compiler, assembler, linker (preinstalled
      on Colab)
    - `xxd` -- converts between hex text and binary files
    - Pillow and numpy -- draw and read the Piet image

    **One hard requirement:** the assembly and machine-code sections
    are x86-64 Linux only. That's what Colab runs. They will *not*
    run on Apple Silicon Macs or on Windows.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 1. Python
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Python (Guido van Rossum, 1991) is the language most people meet
    first, and the easiest way to say what the game does. Everything
    below is the same game with more of the work done by hand.

    - `random.randint(1, 6)` rolls a die in one line
    - Indentation is the syntax -- no braces, no `end` keywords
    - **f-strings** put variables straight into text
    - `input()` waits for Enter, so this version can be played
      interactively, unlike everything below it
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```python
    import random

    def roll_die():
        return random.randint(1, 6)

    def play_game():
        p1, p2 = roll_die(), roll_die()
        c1, c2 = roll_die(), roll_die()
        p_total, c_total = p1 + p2, c1 + c2
        if p_total > c_total:
            p_wins += 1
        elif c_total > p_total:
            c_wins += 1
        # ... print results, loop 5 rounds
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **What we get:** no build step. Python is an **interpreter** --
    it reads the text file and carries out the instructions as it
    goes. (Internally it first compiles to *bytecode*, which a
    built-in engine then runs.) Quick to try and change, at the cost
    of some speed, because translating happens every time you run it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Verified output (seed fixed for a reproducible example)

    ```
    === Dice Game: You vs. Computer ===
    Best of 5 rounds; highest total wins.

    Round 1
    You rolled:      3 + 2 = 5
    Computer rolled: 4 + 6 = 10
    Computer wins this round.
    Score: You 0 - Computer 1
          ... (rounds 2-5) ...
    === Final Result ===
    The computer wins the game.
    Thanks for playing!
    ```

    This was actually run (`python3 dice_game.py`, seeded for
    reproducibility). The notebook's own run is unseeded, so yours
    will roll differently.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 2. Fortran 90
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Fortran** (FORmula TRANslation, IBM, 1957) was the first widely
    used high-level language, built for scientists and engineers.
    Fortran 90 modernized it with free-form layout, `do ... end do`
    loops, and `if / else if` blocks.

    - `random_number` / `random_seed` are built in -- rolling a die
      is one line
    - Arrays and loops count from **1** by default
    - A small function (`roll_die`) lives in a `contains` section
      inside the program

    **What we get:** a native executable, `dice_f90`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```fortran
    program dice_game
      implicit none
      integer :: p1, p2, c1, c2, p_total
      call random_seed()

      do round = 1, n_rounds
        p1 = roll_die()
        p2 = roll_die()
        ! ... read input, compare, print
      end do

    contains
      integer function roll_die()
        real :: r
        call random_number(r)
        roll_die = 1 + int(r * 6.0)
      end function roll_die
    end program dice_game
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Step 1: compile. Step 2: run.

    `gfortran` is a **compiler**: it reads the whole program ahead of
    time and translates it into machine code for this computer's
    processor, before anything runs.

    ```bash
    gfortran dice_game.f90 -o dice_f90
    printf '\\n\\n\\n\\n\\nn\\n' | ./dice_f90
    ```

    *Not independently re-run here -- this environment doesn't have
    `gfortran` installed. Relying on the author's own notebook
    (tested in a separate sandbox).*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 3. Fortran 77
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Fortran 77 is the version much of the world's scientific code was
    written in. It's **fixed-form**: the column you type in matters.

    | Columns | Meaning |
    |---------|---------|
    | 1 | `C` here comments out the whole line |
    | 1-5 | Statement label (`10`, `100`, ...) |
    | 6 | Any character means "continue previous line" |
    | 7-72 | The actual statement |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### What's different from Fortran 90

    - No `END DO` -- loops end on a labeled `CONTINUE`
    - No `CONTAINS` -- the die roller is a separate `FUNCTION`
    - Output layout uses numbered `FORMAT` statements
    - **No standard random routine**, so the program carries its own
      generator (Park-Miller, via Schrage's trick so it never
      overflows a 32-bit integer) -- and asks *you* for a seed
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```fortran
    C     COLUMN 1 = COMMENT, COLS 1-5 = LABEL
          PROGRAM DICE
          READ(*,*,ERR=900,END=900) ISEED

       10 CONTINUE
          DO 50 ROUND = 1, NROUND
             P1 = IROLL(ISEED)
             IF (PTOT .GT. CTOT) THEN
                PWINS = PWINS + 1
             END IF
       50 CONTINUE
          IF (AGAIN .EQ. 'y') GO TO 10
      900 STOP
          END

          INTEGER FUNCTION IROLL(ISEED)
          K = ISEED / 127773
          ISEED = 16807*(ISEED-K*127773) - 2836*K
          IROLL = 1 +
         &  INT(6.0D0*DBLE(ISEED)/2147483647.0D0)
          END
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```bash
    gfortran dice_game.f -o dice_f77
    printf '42\\n\\n\\n\\n\\n\\nn\\n' | ./dice_f77
    ```

    Same two steps as Fortran 90: compile, then run. Change the `42`
    seed and you get a different sequence of rolls -- same seed,
    same game.

    *Also not independently re-run here, for the same reason as
    Fortran 90.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 4. BASIC
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    BASIC (Dartmouth, 1964) was designed so students could program
    without being experts. Programs are **numbered lines**, run in
    order unless you jump with `GOTO`/`GOSUB`, and are usually
    **interpreted**.

    - `RND(1)` gives a number between 0 and 1;
      `INT(RND(1) * 6) + 1` turns that into a die roll
    - `GOSUB 900` calls a tiny subroutine that rolls one die
    - Several statements can share a line, separated by `:`
    - Like Fortran 77, it asks for a seed

    **What we get:** no executable at all -- `bwbasic` reads the
    text file fresh every time you run it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```basic
    30 N = 5
    40 INPUT "Enter a seed"; S
    50 RANDOMIZE S
    130 FOR R = 1 TO N
    170 GOSUB 900 : P1 = D
    210 PT = P1 + P2 : CT = C1 + C2
    240 IF PT>CT THEN PW=PW+1: PRINT "Win!": GOTO 280
    290 NEXT R
    370 IF A$ = "y" THEN 100
    390 END
    900 REM ROLL ONE DIE (1-6) INTO D
    910 D = INT(RND(1) * 6) + 1
    920 RETURN
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### No build step: the interpreter does the work

    `bwbasic` reads the BASIC file and does what each numbered line
    says, in order, with nothing saved to a separate executable.
    Easy to experiment with, but it re-reads and re-understands every
    line each time the program runs.

    > **Straight from the author's own notes:** "This section was
    > written for the widely compatible classic dialect and I
    > haven't been able to test it under `bwbasic`. If a line
    > misbehaves, it's most likely the multi-statement `IF ... THEN`
    > lines (240, 250, 320, 330)." Not independently re-run here
    > either -- `bwbasic` isn't installed in this environment.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 5. C
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    C (Bell Labs, early 1970s) was created to write the Unix
    operating system. It compiles straight to machine code, gives
    direct control over memory, and has almost no runtime overhead.

    - `rand()`/`srand()` come from the standard library, seeded from
      the clock with `time(NULL)`
    - Unlike Fortran, **C counts from 0**
    - The code is longer than Fortran 90's mostly because reading
      input carefully (`getchar`) takes more lines

    **What we get:** a native executable, `dice_c`, linked against
    the C standard library.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>

    static int roll_die(void) {
        return (int)(rand() / (RAND_MAX + 1.0)
                     * 6.0) + 1;
    }

    int main(void) {
        srand((unsigned)time(NULL));
        for (round = 1; round <= N_ROUNDS; round++) {
            p1 = roll_die(); p2 = roll_die();
            c1 = roll_die(); c2 = roll_die();
            if (p_total > c_total) p_wins++;
            else if (c_total > p_total) c_wins++;
        }
        return 0;
    }
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Compiling and linking

    `gcc` does two jobs in one command:

    1. **Compile:** translate text into machine code
    2. **Link:** attach library pieces the program borrows, like
       `printf` and `rand` -- you didn't write those yourself, the
       linker connects your program to the copy that ships with the
       system

    ```bash
    gcc -Wall -Wextra dice_game.c -o dice_c
    printf '\\n\\n\\n\\n\\nn\\n' | ./dice_c
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Verified output (actually compiled and run here)

    ```
    === Dice Game: You vs. Computer ===
    Best of 5 rounds; highest total wins.

    Round 1
    You rolled:      5 + 2 = 7
    Computer rolled: 5 + 5 = 10
    Computer wins this round.
          ... (rounds 2-5) ...
    === Final Result ===
    The computer wins the game.
    Thanks for playing!
    ```

    `gcc -Wall -Wextra` produced no warnings. Unseeded (clock-based),
    so your own run will roll differently.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 6. x86-64 Assembly
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Assembly has **one line per CPU instruction**. No loops, no `if`
    blocks, no variables -- only registers (`rax`, `rbx`, ...), memory
    addresses, jumps and compares. This version uses GNU assembler
    syntax (Intel flavor) and **doesn't touch the C library at all**
    -- it talks to Linux directly, through three raw syscalls:

    | Syscall | Number | Used for |
    |---------|--------|----------|
    | `read` | 0 | Waiting for Enter, reading y/n |
    | `write` | 1 | Printing text |
    | `exit` | 60 | Ending the program |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Everything else is written by hand

    - **Random numbers:** xorshift64 (shifts and XORs a 64-bit
      value), seeded from `rdtsc`, the CPU's own cycle counter
    - **Printing numbers:** divide by 10 repeatedly, turn each
      remainder into an ASCII digit
    - **Game logic:** the same compare-and-jump pattern every
      compiled language above produces behind the scenes -- just
      spelled out instead of hidden
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```asm
            .intel_syntax noprefix
    _start:
            rdtsc            # seed from CPU cycles
            shl     rdx, 32
            or      rax, rdx
            mov     [rip + seed], rax

    roll_die:                        # xorshift64
            mov     rax, [rip + seed]
            mov     rdx, rax
            shl     rdx, 13
            xor     rax, rdx
            shr     rdx, 7
            xor     rax, rdx
            shl     rdx, 17
            xor     rax, rdx
            mov     [rip + seed], rax
            shr     rax, 32
            xor     edx, edx
            mov     ecx, 6
            div     ecx              # edx = eax mod 6
            lea     eax, [rdx + 1]
            ret
    ```

    258 lines in all -- the full file is in the real notebook.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Assemble, then link

    `add eax, 1` means "add 1 to the number stored in `eax`."
    Names like `eax` are **registers**: tiny, very fast storage slots
    inside the CPU itself. Two programs turn text into something
    runnable:

    1. The **assembler** (`as`) translates each line into machine
       bytes and saves them in an *object file* (`.o`)
    2. The **linker** (`ld`) packages that into an **executable**,
       adding a header that tells the OS where to start

    ```bash
    as dice_game.s -o dice_game.o
    ld dice_game.o -o dice_asm
    printf '\\n\\n\\n\\n\\nn\\n' | ./dice_asm
    ```

    *Not independently re-run here -- this requires an x86-64 Linux
    environment, which this build session doesn't have (it's an
    arm64 Mac). The author verified this in their own sandbox.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 7. Machine Code
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Machine code is the real program: the bytes the CPU fetches and
    executes. Assembly is just a readable spelling of it. The whole
    dice game fits in **1,538 bytes of hex**, no assembler or linker
    involved.

    | Byte range | Contents |
    |-----------|----------|
    | 0-63 | **ELF header** -- 64-bit x86 executable, entry point |
    | 64-119 | **Program header** -- where to load it, how much to zero |
    | 120 onward | Instructions, then the text strings |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### What is hex, and how does a file become a program?

    Every file is just **bytes**, each a number from 0 to 255. People
    write bytes in **hexadecimal**: `00` is 0, `0f` is 15, `ff` is
    255. `xxd -r -p` (`r` for "reverse") turns hex text back into
    real bytes, then the file is marked runnable.

    The OS doesn't care how a file was made. It reads the first
    bytes (the ELF header), sees a valid program, copies the rest
    into memory, and starts running where the header says. That's
    how *every* program on Linux starts.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    7f454c4602010100000000000000000002003e0001
    0000007800400000000000400000000000000000
    0000000000000000000000000040003800010000
    0000000001000000070000000000000000000000
    0000400000000000000000400000000000000206
    000000000000400600000000000000001000000
    0000000000f3148c1e2204809d04883c801...
    ```

    `xxd` and `objdump` confirm this is real and self-consistent: the
    byte at offset 0x78 is where the header says code begins, and
    the first two bytes there are `0f 31` -- the `rdtsc` instruction,
    the very first line of the assembly above.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```bash
    xxd -r -p dice_game.hex dice_mc
    chmod +x dice_mc
    printf '\\n\\n\\n\\n\\nn\\n' | ./dice_mc
    ```

    **What we get:** `xxd -r -p` turns the hex text back into raw
    bytes. Making the file executable and running it executes those
    bytes directly -- no build step at all, because there's nothing
    left to translate.

    *The byte layout above was independently verified (decoded the
    hex, confirmed the offsets and `rdtsc` match). Running the binary
    itself needs x86-64 Linux, unavailable in this build session.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 2: Esoteric Languages
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    The next four languages were designed as puzzles, jokes, or art,
    not for getting work done. They compute the same things as
    everything above, but each one removes something you'd normally
    rely on.

    Writing these by hand is impractical, so each one is **produced
    by a short Python generator** you can read in the real notebook
    -- write the game once in readable form, the generator emits the
    esoteric program. One file, `esolang_runners.py`, interprets all
    four.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Words you'll need for this part

    - **Esoteric** means deliberately strange -- not for real work.
      Each one asks: how little do you need to write *any* program?
    - **Turing complete** means a language can compute anything any
      computer can, given enough time and memory. All four of these
      are -- that's why they can play the game at all
    - **Stack machine:** three of the four (Chef, Piet, Whitespace)
      work on a **stack**: `push` adds a number on top, `add` takes
      the top two off, adds them, pushes the result back
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 8. Brainfuck
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Brainfuck (Urban Müller, 1993) has **eight commands** and nothing
    else:

    | Command | Meaning |
    |---------|---------|
    | `>` `<` | Move the pointer along a tape of byte cells |
    | `+` `-` | Add/subtract 1 in the current cell (wraps at 256) |
    | `.` | Print the current cell as a character |
    | `,` | Read one character into the current cell |
    | `[` `]` | Loop while the current cell isn't zero |

    No variables, no numbers beyond what you count with `+`, no
    strings, no `if`, no random numbers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### A tiny example first

    ```
    ++++++++[>++++++++<-]>+.
    ```

    - `++++++++` adds 1 eight times -- cell 0 holds 8
    - `[>++++++++<-]` repeats 8 times: add 8 to cell 1, subtract 1
      from cell 0. Cell 1 ends up at 8 x 8 = 64
    - `>+.` moves to cell 1, adds 1 (65), prints it

    **Verified -- actually run:** this prints `A` (character code
    65), exactly as predicted.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### How the full game works anyway

    - **Variables** are tape positions -- the generator hands out
      cells by name and works out the `>`/`<` moves
    - **`if`/`else`** are loops that zero a flag cell on exit
    - **Printing text** adjusts a scratch cell by the difference
      between consecutive characters, then prints it
    - **Random numbers:** `seed = seed * 101 + 13`, relying on the
      cell wrapping at 256. A die is `seed / 43 + 1`, found by
      counting up to 43 and rolling over -- there's no divide
    - **Comparing totals** counts both down together until one hits 0

    **What we get:** 26,630 commands. Plays five rounds, no rematch.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Verified output (seed character: A)

    ```
    === Dice Game: You vs. Computer ===
    Best of 5 rounds; highest total wins.

    Round 1
    You rolled:      5 + 2 = 7
    Computer rolled: 1 + 3 = 4
    You win this round!
          ... (rounds 2-5) ...
    === Final Result ===
    You win the game!
    Thanks for playing!
    ```

    Actually run through the author's own interpreter
    (`esolang_runners.py bf`). Change the seed character and you get
    a different game.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 9. Chef
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Chef (David Morgan-Mar, 2002) makes programs look like **cooking
    recipes**. The parts of a recipe are the parts of the machine:

    | In the recipe | In the machine |
    |---------------|----------------|
    | Ingredients | Variables (dry prints as a number, liquid as a character) |
    | Mixing bowls | Stacks (`Put`, `Fold`, `Add`, `Combine`) |
    | Baking dishes | Output, printed by `Serves` |
    | `Verb the x. ... until verbed.` | A loop while `x` isn't 0 |

    There is **no `if`** -- only loops, so a conditional is a loop
    that runs once and leaves with `Set aside`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    Dice Game Casserole.

    You and the computer each roll two dice per
    round. Dice are rolled by shuffling a bowl of
    the numbers one to six. The higher total wins.

    Ingredients.
    1 g one
    2 g two
    3 g three
    4 g four
    5 g five
    6 g six
    0 g your first die
    0 g your total
    0 g your wins
    ```

    An actual excerpt of the generated recipe -- every game variable
    really is an ingredient.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### How the game works

    - **Dice:** Chef's one source of randomness is
      `Mix the mixing bowl well`. Put 1-6 in a bowl, shuffle, take
      the top one -- no generator or seed needed
    - **Text:** every printed character is a liquid ingredient with
      its character code. A bowl prints top-down, so each line is
      pushed in backwards
    - **Comparing totals:** subtract 1 from both repeatedly until one
      reaches zero
    - **Output order:** each round goes into its own baking dish;
      `Serves 7` prints all seven dishes at the end

    **What we get:** a ~52 KB recipe. Plays five rounds, no rematch.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Verified output (actually run)

    ```
    === Dice Game: You vs. Computer ===
    Best of 5 rounds; highest total wins.

    Round 1
    You rolled:      5 + 6 = 11
    Computer rolled: 6 + 1 = 7
    You win this round!
          ... (rounds 2-5) ...
    === Final Result ===
    You win the game!
    Thanks for playing!
    ```

    Run through `esolang_runners.py chef`. The bowl shuffles fresh
    every run, so your rolls will differ too.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 10. Piet
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Piet (David Morgan-Mar, 2001) programs are **images** -- named
    after the painter Piet Mondrian. No text at all.

    - The image is made of colored **blocks** of same-colored
      squares (codels). Execution walks from block to block
    - Which instruction runs is decided by **how the color changes**
      between two blocks: hue picks a row (add, divide, print, ...),
      lightness picks a column
    - `push` pushes the **size of the block you just left** -- to
      push 72 you must draw a block of 72 squares
    - A *direction pointer* says which way to travel; `pointer` turns
      it, which is how Piet branches. Black squares are walls
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### How the game works here

    - The main path runs along the top, with tall blocks for big
      numbers (letters are ASCII codes, like 72 or 111)
    - At the end, `greater` then `pointer` turns the path **down** --
      the win/lose messages hang below as long columns
    - Dice use `seed = (seed + 1) * 75 mod 65537 - 1`, with a few
      warm-up steps so small seeds don't start out low
    - Each ending is a 3-square block entered in the middle, so the
      pointer can't back out and the program stops

    **What we get:** an image of **968 x 379 codels** (verified -- I
    regenerated it and measured). Plays **one round** only.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Verified output (seed: 42)

    ```
    You rolled: 4 + 1 = 5
    Computer rolled: 5 + 1 = 6
    Computer wins!
    ```

    Actually run through `esolang_runners.py piet`, codel size
    auto-detected from the image. Try other seeds, like `7`, to see
    the other two endings (you win / a tie).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 11. Whitespace
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Whitespace (Edwin Brady and Chris Morris, 2003) uses only
    **space, tab, and newline**. Every other character is a comment
    -- a Whitespace program can hide inside ordinary text, or look
    completely blank.

    | Group | Prefix | Examples |
    |-------|--------|----------|
    | Stack | space | push, duplicate, swap, discard |
    | Arithmetic | tab space | add, subtract, multiply, divide |
    | Heap | tab tab | store, retrieve |
    | Flow control | newline | label, call, jump, return, end |
    | I/O | tab newline | print/read a character or number |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### How the game works

    - **Variables** are numbered heap slots (slot 0 is the seed,
      slot 1 your score, ...)
    - **Text** prints one character at a time -- why the file is
      large
    - **Random numbers** reuse Piet's generator,
      `seed = (seed + 1) * 75 mod 65537 - 1`
    - Numbers are written in **binary** (space = 0, tab = 1), ended
      by a newline

    **What we get:** 7,126 bytes of pure whitespace (verified).
    Plays all five rounds, with a rematch.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### The real file, made visible

    ```
       ^I   ^I ^I$
    ^I$
         ^I^I ^I^I^I $
    ^I$
         ^I^I^I ^I  $
    ```

    `^I` is a tab, `$` marks the end of a line, spaces are spaces.
    Verified -- actually generated and inspected (`cat -vte` on the
    real file).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Verified output (seed: 42)

    ```
    === Dice Game: You vs. Computer ===
    Best of 5 rounds; highest total wins.

    Round 1
    You rolled:      1 + 5 = 6
    Computer rolled: 5 + 6 = 11
    Computer wins this round.
          ... (rounds 2-5) ...
    === Final Result ===
    You win the game!
    Thanks for playing!
    ```

    Actually run through `esolang_runners.py ws` -- full game, with
    a working rematch loop, in a language with no visible characters.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 12. What We Ended Up With
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Source size (verified -- lines of text)

    | Version | Lines |
    |---------|-------|
    | Python | 63 |
    | Fortran 90 | 73 |
    | Fortran 77 | 82 |
    | BASIC | 36 |
    | C | 87 |
    | x86-64 assembly | 258 |
    | Machine code | 1,538 bytes, 0 lines (it's just bytes) |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Esoteric programs (verified -- bytes written, not hand-typed)

    | Version | Program size | Generator |
    |---------|--------------|-----------|
    | Brainfuck | 27,314 bytes (26,630 commands) | 134 lines |
    | Chef | 51,914 bytes | 124 lines |
    | Piet | 968 x 379 codels | 134 lines |
    | Whitespace | 7,126 bytes | 118 lines |

    All four generated, run, and measured directly for this deck.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### How each version got from text to a running program

    | Version | Who translated it | Steps |
    |---------|-------------------|-------|
    | Python | An interpreter (`python3`) | Run |
    | Fortran 90 / 77 | A compiler (`gfortran`) | Compile, run |
    | BASIC | An interpreter (`bwbasic`) | Run |
    | C | A compiler + linker (`gcc`) | Compile, link, run |
    | Assembly | An assembler + linker (`as`, `ld`) | Assemble, link, run |
    | Machine code | Nobody -- we wrote the bytes | Convert, run |
    | Esoteric x4 | An interpreter we wrote (`esolang_runners.py`) | Generate, run |

    The pattern: the higher a language sits on the ladder, the more
    translating happens between your text and the CPU.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Four Ideas Worth Remembering
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    1. **Every step down trades convenience for control.** The game
       logic never changes: roll, add, compare, update the score.
       What changes is how much work you do by hand to express it.

    2. **A compiler and an assembler do the same job at different
       levels.** Fortran, C and BASIC all end up as machine code --
       the hex section shows the exact bytes your instructions
       become.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    3. **The random numbers differ in every version.** Fortran's
       built-in generator, Park-Miller, BASIC's `RND`, C's `rand`,
       xorshift64, a bowl shuffle, and a small multiply-mod generator
       shared by Piet and Whitespace -- even with the same seed, the
       dice won't match across languages.

    4. **Computation needs very little.** Brainfuck has eight
       commands, Piet has no text, Whitespace has no visible
       characters, Chef has no `if`. All of them still ran the game.
       A language gives you not capability, but *how much work it
       takes to say something*.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Where to Go Next
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - Change the number of rounds and rebuild each version (the
      assembly and hex versions hardcode "Best of 5" in their text,
      so you'd edit that too)
    - Add a rule -- doubles winning outright -- and see how much code
      each language needs
    - Go one level *below* machine code: write the game as hardware
      in Verilog, a shift register for the dice and a comparator for
      the winner
    - Open `bf_gen.py`, change `rounds` or the printed strings,
      rerun the generator and the program
    - Try the generated `.bf`/`.chef`/`.ws` files and the Piet image
      in someone else's interpreter, and see whether they agree

    🧪 [Open the full notebook in Colab](https://colab.research.google.com/github/BU-EK125/EK125-C1-DePasquale-Slides/blob/main/slides/DiceGames/dice_games_fortran_to_machine_code.ipynb)
    """)
    return


if __name__ == "__main__":
    app.run()
