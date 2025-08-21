# 🧮 Arithmetic Formatter

This project is an **arithmetic formatter** that can format up to five addition and subtraction math problems with numbers of up to four digits.  

It was created as part of my **Scientific Computing with Python Certification** from freeCodeCamp.  
👉 [View my certification here](https://freecodecamp.org/certification/lucawaldvogel/scientific-computing-with-python-v7)

---

## 🚀 Features
- Formats up to **5 math problems** at once  
- Supports **addition (+)** and **subtraction (-)**  
- Numbers with up to **4 digits**  
- Optionally shows the **answers**  
- Returns helpful **error messages**:
  - Too many problems  
  - Invalid operator (`*` or `/` not allowed)  
  - Non-digit input  
  - Numbers too long (>4 digits)  

---

## 📖 Example

### Input
```python
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
```

### Output
```python
  3801      123
-    2    +  49
-----    -----
```
