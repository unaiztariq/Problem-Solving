# Suggestions for Optimization & Improvement

This file lists potential improvements for each problem. These are recommendations only — no code has been changed.

---

## 01 - Vigenere Cipher Encryption

- **Deduplicate helper functions**: `addcut_key`, `logic_num`, and `text_back` are duplicated between encryption and decryption. Extract them as shared module-level functions.
- **Use `ord()`/`chr()`** instead of a manual letter-index lookup list for cleaner character-to-index mapping.
- **Add input validation**: Check that raw_text and keyword contain only alphabetic characters.
- **Avoid `input()` at module level**: Move the demo call into a `if __name__ == "__main__"` block.

## 02 - Hourglass Asterisk

- **Separate concerns**: The `odd_allowed` nested function uses try/except but the exception path is unreachable since `isinstance` is checked first. Simplify the validation.
- **Return the pattern as a string** instead of printing directly, making the function more reusable and testable.

## 03 - Denomination Optimization

- **Simplify with integer division**: Replace the `while True` loop with `num_of_notes = amount // note` and `amount %= note` for a cleaner greedy approach.
- **Return both the note dictionary and total notes count** for complete output.
- **Handle edge cases**: Negative amounts, zero.

## 04 - Highest Streak

- **Simplify streak logic**: The current approach uses string-keyed dictionaries (`f"{key}.{no}"`) which is fragile. Use a simple counter variable to track current streak and max streak.
- **Separate the two problems**: Highest Streak and Run-Length Encoding are in the same file. Consider splitting or clearly delineating them.
- **Use `itertools.groupby`** for a cleaner consecutive grouping approach.

## 05 - Matrix Sequence

- **Use list comprehension**: The nested loops with dictionary storage can be replaced with a single list comprehension using `min(row+1, col+1, m-row, n-col)`.
- **Remove the v1 function**: It references undefined variable `w` and doesn't work correctly. Either fix it or remove it.
- **Return a proper 2D list** instead of building a dictionary of rows.

## 06 - Anagrams

- **`group_anagrams_brute_force` has a bug**: It compares characters positionally, not by count. `"aab"` would match `"aba"` but the letter-by-letter check could fail on edge cases.
- **Use `collections.defaultdict`** in `group_anagrams_dict` for cleaner grouping.
- **The brute-force version should be fixed or removed**: It's O(n^3) and the dict version is O(n*k*log(k)).

## 07 - Country Service

- **Fix `get_population` method**: It shadows the `name` parameter with a local variable on line 15, making the function unreliable.
- **Use a dictionary lookup** instead of linear search for each query.
- **Add error handling**: Methods return `None` silently when a country is not found.

## 08 - Diagonal Sort Matrix

- **Handle rectangular matrices**: Currently assumes 5x5. Generalize to m x n.
- **Use `zip(*matrix)`** for secondary diagonal extraction.
- **Return a dictionary** `{primary: [...], secondary: [...]}` for cleaner output.

## 09 - Filter & Validate Matrix

- **`filter_validate_v2` has a bug**: Removing elements from a list while iterating over it causes skipped elements. Use list comprehension instead.
- **The `a` variable is modified in-place** in v2, which is a side effect. The optimized version avoids this.
- **Add sorting by row sum** as specified in the problem statement but missing from implementations.

## 10 - Flatten List (Advanced)

- **`flatten_string_eval` uses `eval()`** which is a security risk and fragile. Remove or replace with `ast.literal_eval`.
- **The recursive version has `print(add)`** on line 18 which is a debug statement. Remove it.
- **Consider using `collections.abc.Iterable`** instead of `isinstance(i, list)` to handle tuples and other iterables.

## 11 - Merge Sorted Lists

- **Add boundary check**: If one list is empty, return the other immediately.
- **Consider Pythonic approach**: `heapq.merge()` from the standard library does this efficiently.
- **The commented-out merge sort snippets** (lines 46-58) are incomplete and reference undefined variables. Clean up.

## 12 - Butterfly Asterisk

- **Return pattern as string** instead of printing, for reusability.
- **Handle edge case**: Input of 1 or 2 produces garbled output.

## 13 - Camel Case Break

- **Handle consecutive uppercase**: `"HTMLParser"` becomes `"H T M L Parser"` which may not be desired. Consider treating consecutive uppercase as one word.
- **Handle digits**: Currently digits are treated as uppercase (they pass `i == i.upper()`).

## 14 - Character Frequency

- **Use `collections.Counter`** for a one-liner: `return dict(Counter(s))`.
- **No issues otherwise**: Clean and correct implementation.

## 15 - Digital Power Sum

- **Use list comprehension**: `sum(int(d)**(p+i) for i, d in enumerate(str(n)))` is cleaner.
- **Return type inconsistency**: Returns `int` on success, `str` on failure. Consider returning `-1` or `None` for consistency.

## 16 - Digit Separation

- **Use `divmod()`** for cleaner modulus/division: `num, last_num = divmod(num, 10)`.
- **Print in correct order**: Currently prints digits in reverse (least significant first). The problem says "each digit in a separate line" which is ambiguous.

## 17 - Fibonacci Sequence

- **`fibonacci_comma_output` and `fibonacci_with_limit` have a bug**: They use `a += 1` and `b += 1` instead of `a, b = b, a+b`. The Fibonacci values won't be correct.
- **Use a generator** for memory-efficient large sequences.
- **The basic version works correctly** and is the best implementation.

## 18 - FizzBuzz

- **Use string concatenation**: `("Fizz" if i%3==0 else "") + ("Buzz" if i%5==0 else "") or str(i)` is more concise.
- **No issues otherwise**: Clean and correct.

## 19 - Flatten List (Basic)

- **Hardcoded range**: `range(0,4)` should be `range(len(a))` to handle different list sizes.
- **Use list comprehension**: `return [item for sublist in a for item in sublist]`.

## 20 - Longest Consecutive String

- **Add boundary check**: If `k > len(strarr)`, return empty string.
- **Use `range(len(strarr) - k + 1)`** for cleaner slicing without manual index tracking.
- **The comparison between first/second is unnecessary**: The loop already checks all windows.

## 21 - Max & Min Number

- **`max_min_interactive` and `max_min_space_separated` use `input()`** which blocks execution. Keep `max_min_from_list` as the primary function.
- **Use built-in `min()` and `max()`** for simplicity, or return a tuple `(min, max)`.

## 22 - Order Correct

- **Missing error handling**: If input is empty string, `a.split()` returns `[]` and works fine, but `b.insert(j-1, i)` could fail if numbers are non-consecutive.
- **Use `sorted()` with a key**: `sorted(words, key=lambda w: int(''.join(c for c in w if c.isdigit())))`.

## 23 - Palindrome

- **Use `re.sub`** to strip non-alphanumeric characters: `re.sub(r'[^a-zA-Z0-9]', '', s).lower()`.
- **One-liner possible**: `return s == s[::-1]` after cleaning.
- **The current approach is correct** but verbose.

## 24 - Parenthesis Validation

- **Bug**: Only checks if first char is `(` and last is `)`. This fails for `()(())` type patterns and accepts `())((` if wrapped in parens.
- **Use a counter approach**: Increment on `(`, decrement on `)`, and return False if counter goes negative.
- **Use a stack** for full validation of nested parentheses.

## 25 - Prime Number

- **Only check up to sqrt(n)**: `range(2, int(pn**0.5) + 1)` is sufficient and much faster for large numbers.
- **Handle edge cases**: Numbers less than 2 are not prime.
- **Return a boolean** instead of printing.

## 26 - Reverse Words

- **Use Python slicing**: `return ' '.join(word[::-1] for word in s.split(' '))`.
- **Preserve original spacing**: The current approach normalizes multiple spaces to single spaces.

## 27 - Rock Paper Scissors

- **Missing case-insensitive comparison**: The `user` variable is lowercased but the win conditions compare against lowercase only. Add `.lower()` to be safe.
- **Add score tracking**: Track wins/losses/ties across rounds.
- **The win conditions have operator precedence issues**: The `or` chains should be grouped with parentheses.

## 28 - Transpose Matrix

- **Fix typo**: Function was originally named `trasnpose` (fixed to `transpose`).
- **Use list comprehension**: `return [list(row) for row in zip(*matrix)]`.
- **Handle non-rectangular matrices**: Currently assumes all rows have equal length.

## 29 - Two Sum

- **Use a hash map** for O(n) solution: `{num: i for i, num in enumerate(nums)}` and check `target - num` in the map.
- **Return indices, not values**: The problem says "return a pair of indices" but the function returns the actual numbers.
- **The current O(n^2) solution works** but is suboptimal.

## 30 - Unique in Order

- **Handle empty input**: `seq[len(seq)-1]` will crash on empty input.
- **Use `itertools.groupby`**: `return [k for k, _ in groupby(seq)]` is a one-liner.
- **Works for both strings and lists**: Good design choice.
