# String Calculator

## Instructions

- Create a simple String calculator with a method signature:
    ```python
    add(str numbers) -> int
    ```

- The method can take up to two numbers, separated by commas, and will return their sum. 
    - for example `''` or `'1'` or `'1,2'` as inputs.
    - for an empty string it will return `0`

- Allow the `add` method to handle an unknown amount of numbers

- Allow the `add` method to handle new lines between numbers (instead of commas).
    - The following input is ok: `'1\n2,3'` (will equal 6)
    - The following input is NOT ok: `'1,\n'` (not need to prove it - just clarifying)

- Support different delimiters
    - To change a delimiter, the beginning of the string will contain a separate line that looks like this:
    ```python
        '//[delimiter]\n[numbers…]'
    ```
    for example `'//;\n1;2'` should return `3` where the default delimiter is `';'`.
    - The first line is optional. All existing scenarios should still be supported

- Calling `add` with a negative number will throw an exception "negatives not allowed" - and the negative that was passed.
- If there are multiple negatives, show all of them in the exception message.

STOP HERE if you are a beginner. Continue if you can finish the steps so far in less than 30 minutes.

### Advanced Features
- Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2
- Delimiters can be of any length with the following format:
    ```python
    '//[delimiter]\n'
    ```
    for example: `'//[***]\n1***2***3'` should return `6`

    Allow multiple delimiters like this:
    ```python
    '//[delim1][delim2]\n'
    ```
    for example `'//[*][%]\n1*2%3'` should return `6`.
- Make sure you can also handle multiple delimiters with length longer than one character
