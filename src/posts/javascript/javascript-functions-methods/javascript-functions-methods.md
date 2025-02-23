---
title: Javascript Functions and Methods
description: Learn how to use functions in JavaScript including declarations, arrow functions, callbacks and handy methods like forEach. Understand core concepts like scope, arguments and returns.
date: 'Sat, 30 Dec 2023 15:57:26 GMT'
categories:
  - javascript
  - web dev
author_id: 1
image: /images/javascript-functions-methods-banner-png.png
webp_image: /images/javascript-functions-methods-banner.webp
image_thumb: /images/javascript-functions-methods-banner-png_thumb.png
banner_alt: Image of to simple robots.
show_banner: true
comments: true
published: true
---

## I. What are Functions?

### Introduction to Functions

Functions are one of the core building blocks in JavaScript. A function is a reusable block of code designed to perform a particular task. 

Functions allow you to group one or more related statements together to perform a specific task. They promote the DRY (Don't Repeat Yourself) principle - this allows you to reuse code instead of repeating the same code in multiple places.

### Why Functions are Essential in JavaScript

Here are some reasons why functions are indispensable in JavaScript:
- **Organization** - Functions allow you to logically organize your code into reusable, modular blocks. This makes code easier to understand and maintain.
- **Reusability** - You can call the same function multiple times without having to rewrite the logic each time. This saves time and reduces duplication.
- **Abstraction** - Functions hide complex operations behind a simple interface. This helps manage complexity in large programs.
- **Scope** - Variables and state are localized to the function scope. This prevents unintended interactions of global data.

### Creating Functions 

There are mainly two ways to create functions in JavaScript:

1. Function Declarations
2. Function Expressions

Let's look at both in more detail:

## II. Function Declarations & Expressions

### Function Declarations

Function declarations define functions in the standard way using the `function` keyword:

```js
function greetUser() {
    console.log('Hello there!'); 
}

greetUser(); // Hello there!
```

Some key properties:
-Hoisted - Functions declared like this are hoisted to the top. That means you can call the function before declaring it.
-Named - Has an explicit named identifier after the `function` keyword.

### Function Expressions 

Functions can also be defined as expressions and assigned to variables:

```js 
const greet = function() {
    console.log('Hi!');
};

greet(); // Hi!
```

- Not hoisted - Only works after being defined.
- Anonymous - No specific name, commonly assigned to a variable.
- Can be named - e.g. `const greet = function displayGreeting() {...}`

Here is a table comparing function declarations and function expressions:
<script>

  import Group from '$lib/components/TabGroup/Group.svelte'
  import Tab from '$lib/components/TabGroup/Tab.svelte'
  import Table from '$lib/components/Table.svelte'
  let group_name = 'tab-group-' + Math.random().toString(36).substr(2, 9)

  let rows = [
    [ 'Definition', 'Uses `function` keyword', 'Created by assigning an anonymous function to a variable' ],
    [ 'Hoisting', 'Hoisted to the top, can be called before being declared', 'Not hoisted, must be defined before called' ],
    [ 'Naming', 'Requires a function name', 'Often anonymous but can be named' ],
    [ 'Syntax', '`function name() {...}`', '`const name = function() {...}`' ],
    [ 'Use Cases', 'Good for reusable helper functions to call generically', 'Useful for functions you may only need to call once' ],
    [ 'Invocations/Calls', 'Can be invoked using its function name', 'Must be invoked using the variable name' ],
    [ 'Best Practices ', 'Use for major functions you will reuse often', 'Use for smaller one-off functions not called often' ],
  ]
  let headers = ['Feature', 'Function Declarations', 'Function Expressions'];
</script>
<Table {headers} {rows} highlight_first_row={true} />

**Key Differences and Benefits:**
- Function declarations load before anything else in a JavaScript file, so you can call a function declaration before it appears in code. Function expressions must load before you call them.
- Function declarations are convenient when you want to refer to the function simply by name elsewhere. Function expressions require you to use variable names when calling it.
- Function expressions avoid using unnecessary global namespaces created by lots of function declarations. This promotes modular code.
- It's best practice to use function declarations for major important helper functions you will reuse often. Use function expressions for smaller one-off functions.

## III. Arguments & Parameters

### Understanding Parameters

Parameters are placeholder variables listed when defining a function. They act as local variables inside the function body:

```js
function greet(name) {
    console.log('Hello ' + name);
}

greet('John'); // Hello John
```
Here `name` is a parameter that will refer to the first argument passed to the `greet` function.

You can also set **default parameters** that initialize to a value if no argument is passed:

```js
function greet(name = 'stranger') {
    console.log('Hello ' + name); 
}

greet(); // Hello stranger
```

### Working with Arguments

Arguments are values passed to the function when it is invoked. They are assigned to the corresponding parameters:

```js
function sum(num1, num2) {
    return num1 + num2;
}

sum(2, 3); // 5
```

The `arguments` keyword also gives access to all arguments as array-like object:

```js
function sumAll() {
    let total = 0;
    for(let i = 0; i < arguments.length; i++){
        total += arguments[i]; 
    }
    return total;
}

sumAll(1, 2, 3); // 6
```

## IV. Returning Values

### The Return Statement

The return statement ends function execution and returns a value from the function:

```js 
function sum(num1, num2) {
    console.log('This console.log gets executed!');
    return num1 + num2; 
    console.log('This console.log is not executed due to the return from one line prior ending the function.');
}

let total = sum(5, 10); // Returns 15
```

Return is useful for processing data inside functions and returning the result.

### Multiple Returns

You can include multiple return statements conditionally:

```js
function authorize(role) {
    if (role === 'admin') {
        return 'Access granted';
    } else {
        return 'Unauthorized access'; 
    }
} 
```

You can also return objects and arrays. Generally aim to keep return logic simple and return single coherent data types.

## V. Arrow Functions

### Introduction to Arrow Functions

Arrow functions provide a more concise syntax for writing functions:

```js
const sum = (num1, num2) => {
    return num1 + num2;
}
```

The arrow `=>` replaces the `function` keyword. Useful for short functions.

They also lexically bind the `this` value, which can simplify usage in callbacks and promise handlers.

### When to Use Arrow Functions

- For short, single line functions:

```js 
const double = num => num * 2; 
```

- As callback functions to keep proper binding of `this`:

```js
const player_obj = {
    players: [
        { name: 'John', wins: 5 }, 
        { name: 'Mary', wins: 7}
    ],
    sport: 'baseball',
    printPlayers() {
        this.players.forEach(player => console.log(player.name + ' ' + this.sport));     
    }
};


```

<Group>
  <Tab label="Arrow Func" {group_name} checked={true}>

```js
const video = {
    title: 'Some Video',
    tags: ['javascript', 'webdev'],

    printTags() {
        this.tags.forEach(tag => {
        console.log(this.title, tag);   // this.title logs 'Some Video' as intended
        });
    }
}
```
  </Tab>
  <Tab label="Function Keyword" {group_name}>

```js
const video = {
    title: 'Some Video',
    tags: ['javascript', 'webdev'],

    printTags() {
        this.tags.forEach(function(tag) {
        console.log(this.title, tag);   // this.title logs undefined due to using this original function declaration style
        });
    }
}
```
  </Tab>
</Group>

- Generally best suited for callbacks, promise handlers, event handlers etc.

## VI. Functions vs Methods

### Distinguishing Functions and Methods

- **Functions** are reusable blocks of code that take inputs, process data, and return outputs. They usually serve one specific purpose.
- **Methods** are functions defined as object properties that can access data from the parent object.

```js
function greet(name) {
    return 'Hello ' + name; 
} 

const person = {
    name: 'John',

    greet() {
        return 'Hello ' + this.name; 
    }
}

``` 

### Use Cases and Best Practices

- Use generic reusable **functions** independent of objects.
- Use **methods** when functionality needs to modify or interact with an object instance.
- Strive for consistency within your codebase - don't mix up naming and approaches.

## VII. Foreach Method & Callbacks

### Introduction to `forEach` Method 

The `forEach()` method executes a callback function on each element in an array:

```js
const numbers = [1, 2, 3];

numbers.forEach(function(number) {
    console.log(number);
});

// Logs:
// 1 
// 2
// 3
```

This offers a simpler and cleaner way to iterate arrays vs a manual `for` loop.

### Callbacks Explained

A callback function is a function passed into another function as an argument and invoked inside the outer function:

```js 
function handleData(data, callback) {
    // do something with data
    callback(data);  
}
handleData("log this text", console.log);

``` 
This allows greater flexibility - the same function can call different callbacks to produce varying logic and effects.

### Benefits of Using Callbacks

Some benefits of using callbacks with objects:
- Keep related data and functions together 
- Reuse functions across different objects
- Ability to swap callbacks for different needs  
