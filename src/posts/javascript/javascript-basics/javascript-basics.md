---
title: Javascript Basics
description: Unlock the power of JavaScript with our in-depth tutorial! From navigating the browser console to grasping variable scopes and naming conventions, this post covers it all. Delve into the world of strings, numbers, and arrays, and gain a thorough understanding of boolean data types and comparison operators. Discover the nuances of loose vs. strict comparison, and explore the intricacies of type conversions using functions like parseInt and parseFloat. Elevate your JavaScript proficiency with this comprehensive guide.
date: 'Wed, 27 Dec 2023 01:35:27 GMT'
categories:
  - javascript
  - web dev
author_id: 1
image: /images/javascript-basics-banner-png.png
webp_image: /images/javascript-basics-banner.webp
image_thumb: /images/javascript-basics-banner-png_thumb.png
banner_alt: Picture of square toy-like robots waiting for the order to clean the messy area they surround.
show_banner: true
comments: true
published: true
---

## A. The Browser Console  

The browser console is an essential tool for debugging JavaScript code in the browser. It can be accessed across different browsers a few ways including right clicking the page and choose inspect in the menu, or press Ctrl + Shift + I key combo.

The console allows you to view any error messages that occur from your scripts, log custom messages and variable values using `console.log()`, test JavaScript code directly, and much more. It presents errors with their stack traces, line numbers, filenames, and other meta information to help you trace issues.

Some common console methods include:

- `console.log()` - prints a message to the console
- `console.error()` - logs an error message
- `console.warn()` - logs a warning message
- `console.clear()` - clears all messages from the console

You can use the browser console to quickly check variable values, function returns, and perform basic JavaScript debugging and testing without needing to run any web servers or HTML files locally. Proper use of the console can save tremendous time and headache when developing JavaScript code.

## B. Variables, Constants & Comments

**Variables and Constants**
Variables enable storing data (like strings, numbers, objects etc.) and making them available for reuse throughout your code. They are declared using the `var`, `let` or `const` keywords:

```js
// Declare variable with var
var age = 25; 

// Declare with let  
let name = "John";

// Declare with const
const pi = 3.14;
```

- `var` declarations are globally scoped or function scoped while `let` and `const` are block scoped
- `let` and `var` can be updated while `const` cannot be updated


@ds What are some best practices for choosing declaration keywords?

```js
// Var declarations are globally scoped or function scoped
var age = 25; // Can be accessed anywhere in this javascript file
            // Can also be accessed by any function 

function getAge() {
    return age; // Works even though var age is declared outside 
}

// Let and const are block scoped 
if (true) {
    let name = "John"; // Accessible only inside this block

    // Gives error outside block
    console.log(name); 
}

// Best practice is to use const by default
const pi = 3.14; 

// Use let only if the variable needs to change
let count = 0; // Count can update so let makes sense here
count++;

// Don't use var as it can cause unintended consequences 
if (true) {
    var test = 1; 
    // test is still available outside this block
}
console.log(test); // Works even though defined inside block
```

Some variable naming best practices include:

- Use camelCase (e.g. myVariableName)
- Start with a letter or underscore, not a number
- Use descriptive names (e.g. userAge vs age) 
- Constants are usually capitalized (e.g. PI)

@ds Want more variable naming best practices?
**Camel case (myVariableName)**
- Standard convention for variable and function names
- First word lowercase, subsequent words uppercase

**Pascal case (MyVariableName)** 
- Used for constructor functions and classes
- First letter of each word capitalized

**Snake case (my_variable_name)**
- Not commonly used in JavaScript 
- Can be seen in some legacy systems

**Screaming snake case (MY_VARIABLE_NAME)**
- Usually used for constants 
- Entirely uppercase with underscores

**Hungarian Notation (strName, intWidth)**
- Used to indicate type information
- Not that common in JavaScript

Besides camelCase being the standard, here are some other naming tips:

- Use full descriptive names 
- Avoid single letters like x, y 
- Constants like PI in all caps
- Prefix non-public methods and properties with `_`
- Use verbs for function names 

I'd recommend sticking to camelCase and PascalCase conventions for consistency with most JavaScript teams unless your codebase has other standards. The key is to make your names descriptive and easy to understand.
@ds Want more variable naming best practices?
@ds What are some best practices for choosing declaration keywords?

**Comments**

Comments allow you to leave explanatory notes without impacting any code. Single line comments start with `//` while multi-line comments are wrapped in `/* */`:

```js
// This is a single-line comment

/* 
This is 
a multi-line 
comment
*/
```

Adding quality comments helps other developers quickly understand what your code is doing. The browser ignores comments entirely.

## C. Data Types at a Glance

Data types in JavaScript describe the different kinds of values that can be stored and manipulated within your code. Some main data types include strings, numbers, booleans, arrays, objects and more. Understanding the built-in data types available is essential for properly accessing and working with data in JavaScript.

### 1. Strings

Strings represent textual data and are defined by enclosing content in single or double quotes:

```js
let email = 'john@test.com'; 
let name = "John";
```

You can use backticks `&#96;` to create multi-line strings and interpolate values using `&#36;{expression}`:

```js 
let text = &#96;Hello 
world!&#96;;

let name = "John";
let greeting = &#96;Hello &#36;{name}&#96;; // Hello John
```

Useful string methods include:

- `length` - Gets string length
- `indexOf()` - Returns index of substring 
- `slice()` - Extracts section of string
- `toUpperCase()` - Converts string to uppercase

And many more!

### 2. Numbers

JavaScript has one main numeric type - Number. It can represent both integers and decimals.

```js
let count = 10; // Integer
let price = 9.99; // Decimal 
```

You can perform all basic arithmetic operations like:

```js
let sum = 10 + 5; // 15
let diff = 10 - 5; // 5 

let product = 10 * 5; // 50
let quotient = 10 / 5; // 2
```

There are also useful number methods like toFixed() and Number() for type conversions.

### 3. Arrays

Arrays allow storing multiple values sequentially:

```js
let colors = ["red", "green", "blue"]; 
```

You access elements by index, starting at 0:

```js
let first = colors[0]; // "red"
```

They have very useful built-in methods like push(), pop(), shift(), unshift() etc. Arrays can hold any data types within them as well.


### 4. null & undefined

`null` and `undefined` are two distinct values in JavaScript that represent the absence of value:

**null**: Represents the intentional absence of a value

```js
let age = null; // Age is currently unknown

``` 

**undefined**: Represents a variable that has not been assigned a value

```js 
let name;
console.log(name); // undefined
```

Key Differences:

- null is an assigned value, while undefined is type returned when value undefined
- Set something to null explicitly, undefined is set automatically
- Check for null with strict equality as it can coerce with ==

They can often be used interchangeably but have important nuances.

### 5. Booleans

Boolean represents logical values of `true` or `false`:

```js
let completed = true;
let loggedIn = false; 
```

Very useful in conditional logic and evaluation:

```js
if (completed) {
// Do something  
} else {
// Do something else
} 
```

Comparisons evaluate to booleans:

```js
10 > 5; // true
10 == 5; // false
10 === 10 // true
```

Can also convert values like strings to booleans with Boolean() wrapper.

### 6. Loose vs Strict Comparison

In JavaScript, there are two ways to compare values:

**Loose equality `==`**: Compares values after converting to common type.

```js
"1" == 1; // true
null == undefined; // true 
```

**Strict equality `===`**: Compares both value AND type (no type coercion).

```js
1 === "1"; // false
null === undefined; // false
```

Best practice is to use strict equality by default as loose equality can cause unexpected results.

Some key differences:

- `==` coerces types before comparison (can cause bugs)
- `===` does not coerce types, compares as is 
- `===` is faster than `==`

When mixing types, be very careful with loose equality.

### 7. Type Conversions 

You may need to manually convert between data types like strings, numbers and booleans.

**String Conversion**

```js
let score = 10;

// Convert score to string
score.toString(); // "10"  
String(score); // "10"
```

**Numeric Conversion** 

```js
let value = "10";

// Convert value to number 
Number(value); // 10
parseInt(value); // 10
parseFloat(value); // 10
```

Can also convert to booleans, arrays etc. Type coercion happens automatically in some cases as well.

Understanding conversions helps prevent bugs!


@ds Why might we need to convert between types?
**1) Working with form data values**

Values submitted from HTML forms come in as strings. You may need to convert them to numbers to perform math:

```js
let num1 = "5";
let num2 = "10";

// Convert to numbers before adding
let sum = Number(num1) + Number(num2);
```

**2) Before storing values in variables**

You may receive value from API request or other source as string but need number:

```js
let apiValue = "12.5" // Numeric string 

let value = parseFloat(apiValue); // Convert to number
```

**3) Concatenating variables in strings**

When embedding variables in strings, may need conversion:

```js
let points = 10;
let msg = "You scored " + points.toString() + " points!";
```


The key motivation in summary is either to:

1. Manipulate values in desired way 
2. Validate input is expected type
@ds Why might we need to convert between types?

## Conclusion


And there you have it – the building blocks of Javascript. We covered the key basics including variables, data types, operators, arrays, conditionals and loops. These core concepts will provide a solid foundation as you continue to learn.

Javascript has its quirks, but by understanding things like loose typing, coercion and scope, you can avoid common pitfalls. Use strict equality operators when needed.

You now have the tools to start storing data, manipulating values, and controlling program flow. With practice, Javascript will become second nature. Don't be afraid to experiment! Making things is the best way to solidify knowledge.

This was just the tip of the iceberg. As you level up, dive deeper into Javascript’s rich ecosystem. But no matter how advanced you become, these basic principles will serve you well. Happy coding!
