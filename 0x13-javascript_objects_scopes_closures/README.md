# JavaScript - Objects, Scopes and Closures

## Introduction
This project focuses on mastering various aspects of JavaScript, particularly objects, scopes, and closures. It aims to provide a comprehensive understanding of these concepts through practical examples and exercises.

## Learning Objectives
At the end of this project, you will be able to:
- Understand why JavaScript programming is versatile and powerful.
- Create objects in JavaScript using different approaches.
- Explain the meaning of `this` in JavaScript and how it is used.
- Understand the concept of `undefined` and its implications.
- Appreciate the importance of variable type and scope in JavaScript.
- Define what closures are and how they work in JavaScript.
- Explain the concept of prototypes and their role in inheritance.
- Inherit objects from others using constructor functions, prototypes, or ES6 classes.

## Requirements
- Allowed editors: vi, vim, emacs
- Code should be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- Code should be semistandard compliant with rules of Standard + semicolons on top
- All files must be executable
- The length of files will be tested using wc
- Not allowed to use var

## Installation
1. Install Node.js 14:
   ```sh
   $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
   $ sudo apt-get install -y nodejs
   ```

2. Install semistandard:
   ```sh
   $ sudo npm install semistandard --global
   ```

## Usage
1. Clone this repository:
   ```sh
   $ git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```sh
   $ cd <project_directory>
   ```

3. Run the JavaScript files using Node.js:
   ```sh
   $ node <filename.js>
   ```

## Examples
- **Creating an object in JavaScript:**
  ```javascript
  const person = {
    name: 'John',
    age: 30,
    greet() {
      console.log(`Hello, my name is ${this.name} and I'm ${this.age} years old.`);
    }
  };
  person.greet(); // Output: Hello, my name is John and I'm 30 years old.
  ```

- **Understanding `this` in JavaScript:**
  ```javascript
  const person = {
    name: 'John',
    greet() {
      console.log(`Hello, my name is ${this.name}.`);
    }
  };
  person.greet(); // Output: Hello, my name is John.
  ```

- **Using closures in JavaScript:**
  ```javascript
  function outer() {
    const x = 10;
    function inner() {
      console.log(x);
    }
    return inner;
  }

  const closure = outer();
  closure(); // Output: 10
  ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to Guillaume for providing guidance and resources for this project.
```
