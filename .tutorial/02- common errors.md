# Common Errors

## Syntax Error

👉 What is wrong with the code below?

Tip: remove any other other code from your screen. Copy and paste this in and hit the `RUN` button.

```python
tvShow = input("What is your favourite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favourite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
else:
  print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
```

<details><summary> Answer 👀 </summary>

```python
else:
  print("Nah, Daddy Pig's the greatest")
  ```
  
is not indented properly. 

- This `else` statement is referring to `faveCharacter` and therefore, both the above `else` and `print` statements need to be indented one time. Highlight them both and click 'tab' one time.
</details>

