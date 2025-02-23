---
title: Javascript Object Literals
description: Object literals are fundamental for managing data and configuration in JS apps. Read this in-depth guide on declarations, methods, prototypes, immutability best practices, and practical object usage!
date: 'Sun, 31 Dec 2023 15:25:57 GMT'
categories:
  - javascript
  - web dev
author_id: 1
image: /images/js-object-literals-banner-png.png
webp_image: /images/js-object-literals-banner.webp
image_thumb: /images/js-object-literals-banner-png_thumb.png
banner_alt: Picture of people at work in a shop with text along the bottom asking 'What is an Object in JS?'.
show_banner: true
comments: true
published: true
---

## Objects at a Glance 

Objects in JavaScript allow us to model real-world things with code. 

### Introduction to Objects

Objects are collections of related data and functionality. Think of objects as containers that have properties and methods.

For example, we could create an object to represent a person with properties like `name`, `age`, and `address` and methods like `walk()` and `talk()`.

### Key-Value Pairs

Objects contain key-value pairs. The keys (name, age, etc) are strings that act as identifiers for the values. Values can be any type in JavaScript - strings, numbers, booleans, arrays, functions, or other objects.

```js
const person = {
    name: "John",
    age: 30 
};
```
Here "name" and "age" are keys, while "John" and 30 are the values.

### Object Literal Notation 

**What it is:**

- It's a concise way to create objects in JavaScript, directly defining their properties and values within curly braces `{}`.
- It offers a more readable and maintainable approach compared to using the new `Object()` constructor.

**Syntax:**

```js
const objectName = {
    property1: value1,
    property2: value2,
    // ... more properties
};
```

**Key elements:**

- Curly braces `{}`: Enclose the object's properties and values.
- Property names: Strings that represent the names of the object's properties.
- Colon `:`: Separates property names from their corresponding values.
- Commas `,`: Separate multiple property-value pairs (except after the last pair).
- Values: Can be any valid JavaScript data type, including strings, numbers, booleans, arrays, other objects, or functions.

**Example:**

```js
const person = {
    name: "John Doe",
    age: 30,
    city: "New York",
    hobbies: ["reading", "coding", "hiking"],
    greet: function() {
        console.log("Hello, my name is " + this.name);
    }
};
```

**Key features:**

- **Dynamic property creation:** Add or modify properties after object creation:

```js
person.job = "Software Engineer";
```
- **Computed property names:** Use expressions for property names (enclosed in square brackets):

```js
const key = "address";
const person = {
    [key]: "123 Main St"
};
```
- **Shorthand property names:** If property name matches variable name, omit it:

```js
const firstName = "John";
const person = {
    firstName, // Equivalent to firstName: firstName
    lastName: "Doe"
};
```
- **Methods:** Define functions as properties:

```js
const person = {
    firstName: "John",
    lastName: "Doe",
    fullName() {
        return this.firstName + " " + this.lastName;
    }
};
```

**Benefits:**

- **Conciseness and readability:** Makes code easier to write and understand.
- **Maintainability:** Properties are clearly defined and organized.
- **Flexibility:** Dynamically add, modify, or remove properties.
- **Functionality:** Encapsulate data and behavior within objects.

## Creating an Object Literal

Let's look at how to create a basic object literal in JavaScript.

### Basic Syntax

The basic syntax for creating an object literal is:

```js
const objectName = {
    key1: value1,
    key2: value2
};
```
Replace `objectName` with the name for your object. Add key-value pairs inside the curly braces `{}`.

### Property Assignment 

We can assign values to keys in a few different ways:

```js
const person = {
    name: "John", 
    age: 30
};

// Same as above
const person = {
    "name": "John",
    "age": 30  
};

// Using variables
const nameKey = "name";
const ageKey = "age";

const person = {
    [nameKey]: "John",
    [ageKey]: 30    
};
```

In the first example, we assign values using `key: value` syntax. The property name does not need quotes unless it has spaces or dashes.

The second does the same but with quotes around the keys. This is also valid but not required if it's a valid identifier.

The third example uses variables for the keys. This can be useful to dynamically create keys. The square bracket syntax is required here.

## Adding Methods

Methods are functions that are properties of an object. When a function is declared using a declaration keyword like 'function', it becomes a method of the global object. In the case of browsers, the global object is 'window'. This means that functions declared in the global scope without being explicitly attached to another object are, by default, methods of the 'window' object in a browser environment. Here is how to add methods to JavaScript objects.

### Functions as Object Properties

We can assign function expressions as values to object properties to add methods:

```js
const person = {
    name: "John",
    sayHello: function() {
        console.log("Hello!"); 
    }
}

person.sayHello(); // Logs "Hello!"
```

The `sayHello` method can be invoked using `person.sayHello()`.

### Invoking Object Methods

To call an object method, use:

```js 
objectName.methodName();
```

Where `objectName` is the name of your object, and `methodName` is the method you want to invoke.

Methods have access to other properties on the same object using `this` (more on that below)!

### Best Practices for Method Definition  

Some best practices for methods include:
- Avoid using arrow functions which lexically bind `this`. Use regular functions instead.
- Use ES6 method shorthand syntax:

```js
sayHi() {
    // method code
}
```
\

## 'this' Keyword 

The special `this` keyword references the current object but can sometimes be confusing.

### Understanding 'this' in Objects

In object methods, `this` refers to the object itself:

```js
const person = {
    name: "John",
    sayName() {
        console.log(this); // person object
    }
};

person.sayName();

``` 
Whereas in regular functions, `this` refers to the global object (`window` in browsers).

### 'this' in Regular Functions vs. Arrow Functions

Arrow functions lexically bind `this` so they inherit `this` from the surrounding scope:

```js
const person = {
    name: "John",
    sayName: () => { 
        console.log(this); // window  
    }
};  

person.sayName(); 
```

So arrow functions should be avoided as object methods.

### Common 'this' Pitfalls and Solutions

Here are some common `this` pitfalls and how to avoid them:

- Losing `this` context: store `this` in a variable 
- Using arrow functions: stick to regular functions for methods
- Changing `this` (call/apply): leverage lexical `this` with arrow functions

## Objects in Arrays

We can store objects in arrays to organize related data.

### Storing Objects in Arrays

An array stores an ordered collection of items. We can store objects inside arrays like so:

```js
const todos = [
    { 
        id: 1,
        text: "Take out trash",
        completed: false
    },
    {
        id: 2, 
        text: "Doctor's appointment",
        completed: true 
    }
];
```
This `todos` array contains two todo objects representing tasks.

### Iterating Over Object Arrays  

We can use loops to iterate over arrays of objects:

```js
for (let i = 0; i < todos.length; i++) {
    console.log(todos[i].text); // Log text property  
} 
```
We can access object properties inside the loop on each iteration.

The `forEach` array method is also useful for looping over object arrays.

### Use Cases for Objects in Arrays

Some examples of storing objects in arrays include:

- User objects stored in an array as a simple database
- Todo/task objects for a todo list web app 
- Product objects in a shopping cart array

This is a very common pattern in JavaScript apps.

## Math Object   

The built-in Math object has useful methods and properties for mathematical operations.

### Overview of the Math Object

- Static properties and methods (not constructable with `new`) 
- Useful for common math tasks in programming
- Helps avoid issues with numbers in JS  

```js
Math.PI; // 3.14159... 
Math.floor(3.14); // 3
Math.ceil(3.14); // 4 
Math.min(1,3,2); // 1
Math.random(); // Random number  
```

### Common Math Operations 

Here are some common math operations with `Math`:  

- `Math.round()`, `Math.floor()`, `Math.ceil()` - round to integer
- `Math.min()/Math.max()` - find min/max value
- `Math.random()` - generate random number 
- Many more!

### Math Object Use Cases

Some example use cases:

- Generate random ID numbers for objects
- Calculate distances/physics in games 
- Formulas/operations across app  

The `Math` object helps avoid issues with representing numbers in JS and supports many common math functions out of the box.

## Primitive vs. Reference Types

In JavaScript, data types can be either primitive or reference types. This affects how they are stored and interacted with.

### Understanding Primitive Types

Primitive types include:

- Strings
- Numbers  
- Booleans
- null and undefined

Primitives store only a single value directly in the variable itself. 

For example: 

```js
let name = "John";

```  

The string "John" is stored directly in the `name` variable.

### Understanding Reference Types

Reference types include:

- Arrays
- Functions  
- Objects

References don't store the value directly. They point to a location in memory where the object is stored.

For example:

```js  
const person = {
    name: "John"   
};
```

`person` doesn't contain the object directly. It points to a memory location storing the object data.

### Implications in Object Literals

In practice, this means:

- Primitives are copied by value
- Objects are copied by reference 

This becomes very relevant when passing functions arguments or assigning objects to new variables.

```js
let name = "John";
let name2 = name; 

name2 = "Jane";

console.log(name); // "John"
```

Here the string is copied by value - `name2` gets a copy of the value in `name`.

Objects behave differently:  

```js  
let person = {
    name: "John"
};
let person2 = person;  

person2.name = "Jane"; 

console.log(person.name); // "Jane"  
```

`person` and `person2` point to the same object location. Changing one also affects the other!

To truly copy objects, we need to manually create a copy with destructuring or `Object.assign()`:

```js
// Destructuring copy  
let {name: name2} = person;  

name2 = "Jane";

console.log(person.name); // "John"
```

So because objects are stored by reference, modifications can unexpectedly change variables. Destructuring allows true copies of object data.

## Object Destructuring

Destructuring allows us to extract data from objects and arrays into distinct variables.

### Extracting Values from Objects 

With object destructuring we can extract values like this:  

```js
const person = {
    firstName: "John",
    lastName: "Doe",
    age: 32
}

// Object destructuring  
const {firstName, age} = person; 

console.log(firstName); // "John"
console.log(age); // 32
```
This pulls properties out into separate variables.

### Simplifying Code with Object Destructuring

Destructuring objects can simplify code by reducing redundant access:

```js 
// Without destructuring
function printDetails(user) {
    console.log(user.firstName, user.lastName);  
}

// With destructuring
function printDetails({firstName, lastName}) {
    console.log(firstName, lastName);   
}
```
By destructuring in the function argument, we skip redundant `user.` references.

### Use Cases for Object Destructuring 

Object destructuring shines anytime we need to access multiple properties of an object. Some examples:

- Initializing variables 
- Function arguments
- Pulling API response data

## Object Spread Operator

The spread syntax (...) allows us to expand objects into other objects very useful for combining data.

### Introduction to the Spread Operator

The spread operator unpacks elements:

```js
const numbers = [1,2,3];
Math.max(...numbers); 
```
We spread an iterable like an array into individual arguments.

### Copying Objects with Spread 

We can create shallow copies of objects with the spread syntax:

```js
const person = { 
    name: "John",
    age: 30
}

const copiedPerson = {...person}; 
```
This quickly copies all key-value pairs into a new object.

### Merging Objects Using Spread

The spread operator can also merge objects together:  

```js
const person = {  
    name: "John"
};

const job = {
    role: "Teacher"
}

// Merge objects  
const employee = {...person, ...job};  

console.log(employee);  
// {name: "John", role: "Teacher"}
```
This allows easily combining data from multiple sources.


## Object Methods & Properties 

JavaScript objects come with useful built-in methods we can use.

Common methods include:

- `Object.keys()` – Returns array of keys 
- `Object.values()` – Returns array of values
- `Object.entries()` – Returns keys & values  

Consider this object:

```js  
const person = {
    name:"John",
    age: 30 
}; 

Object.keys(person); // ["name", "age"]  
Object.values(person); // ["John", 30]
Object.entries(person); // [["name", "John"], ["age", 30]]
```
These provide different views into the object data.

### Iterating Over Object Properties 

We can also use these methods to iterate (loop) over objects:

```js
// Loop over keys 
for (let key of Object.keys(person)) {
    console.log(key); // Prints name, age
}
```
They enable easily looping without having to manually access properties.

### Use Cases for Object Methods

Here are some example use cases for these methods:

- Convert objects into maps/arrays
- Iterate over objects in loops 
- Access all values or keys easily

## Immutability in Objects

Immutable objects cannot be changed after creation. This provides several benefits.

### Understanding Immutability

An immutable object can't be modified after it's created. Consider this:

```js
const person = {
    name: 'John'  
};

person.name = 'Jane'; // Can be modified!
```
This `person` object is mutable - it can be changed after creation.

An immutable object could not have its properties changed like this.

### Techniques for Achieving Immutability

There are a few ways to achieve immutability in JavaScript:
**Const**

Declaring an object as `const` only prevents reassignment of the variable. The properties can still change:

```js
const person = {
    name: 'John'
};

person.name = 'Jane'; // Allowed!
```

**Object.freeze()**

The `Object.freeze()` method prevents new properties from being added and existing properties changed: 

```js 
const person = {
    name: 'John'  
};

Object.freeze(person); 

person.name = 'Jane'; // Throws an error
```
Now the object is immutable!

**Spread operator**

We can use the spread syntax to create a new copy whenever an object changes:

```js
let person = {...originalPerson}; 

person = {...person, name: 'Jane'}; // Create updated copy
```
This ensures modifications create a new object instead.


### Benefits of Immutable Objects

Benefits include:

- Avoid unexpected side effects from modifying objects
- Help manage shared data  
- Enable useful patterns like redux 
Overall, immutability leads to safer and more predictable code.

## Object Prototypes

When you create an object in JavaScript, that object is linked to another object called its "prototype". This prototype linkage allows objects to inherit features from other objects.

### The Prototype Chain

All JavaScript objects have a private `[[Prototype]]` property that's either another object or `null`. When you try to access a property on an object:

1. JavaScript first looks for the property on the object itself 
2. If it's not found, it then searches the object's prototype object, 
3. And keeps going up the prototype chain until the property is found or it reaches `null`.
This is the prototype chain.

So the prototype acts as a fallback for properties that don't exist on the object itself.

### Inheriting from Object.prototype

By default, all custom objects inherit properties and methods from the base `Object.prototype`:

```js
const user = { name: "John" }; 

user.toString(); // Works even though we didn't define it 
```
Here `user` inherits the `toString()` method from `Object.prototype`.

We can access an object's prototype using `Object.getPrototypeOf()`:

```js
Object.getPrototypeOf(user); // Object.prototype
```

### Setting the Prototype

Every function has a `prototype` property that allows setting the prototype for objects created with that function:

```js
function User(name) {
    this.name = name;
}

User.prototype.sayHi = function() {
    alert(&#96;Hi, I am &#36;{this.name}&#96;);
}

const me = new User("John");
me.sayHi(); // Works!

``` 
Now `User` objects inherit from the custom `User.prototype` object.

Prototypes allow objects to share and extend functionality in a dynamic, modular way. It's a key aspect of OOP in JavaScript.

## Common Mistakes and Best Practices

When working with object literals, there are some best practices we can follow to write optimized, maintainable code.

### Avoiding Common Pitfalls in Object Literal Usage

Here are some common mistakes to avoid:
**Modifying object literals incorrectly**

```js
const person = {
    name: "John" 
};

person = {}; // Re-assigning loses reference 

person.name = "Jane";  // Modifying non-existent property
```
Don't re-assign the object variable or try to change properties on an undefined object.

**Using reserved words as keys** 

```js
const person = {
    class: "Computer Science" // Causes syntax error
};
```
Avoid using reserved words and symbols as key names.

**Mixing up declaring and invoking**

```js
let user = {
    name: "John",
    print: printDetails(); // Runs instantly!
}

function printDetails() {
    // Prints undefined  
    // Because print() already ran above
} 
```
Don't invoke functions in objects, simply refer to them.

### Best Practices for Object-oriented JavaScript

Some best practices include:  

- Use descriptive key names
- Create objects with same properties grouped 
- Store methods on prototypes instead of instances

This leads to clean, readable code. 

### Writing Maintainable and Readable Object Literals

Some tips for writing good object literals:

- Be consistent and predictable in naming 
- Use comments for complex object literals
- Format code neatly into semantic blocks

Your future self and other developers will thank you!

## Conclusion

Object literals are the bread and butter of working with data and config in JavaScript. By following best practices of descriptive declaration, correct method assignment, reusing prototypes, immutable data and prudent manipulation, we build robust, maintainable and performant code. Becoming an expert in literal JavaScript objects pays huge dividends towards mastering the language paradigms.
