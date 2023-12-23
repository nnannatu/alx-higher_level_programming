# Hash Table Project README

## Project Overview

This project focuses on implementing a hash table data structure in the C programming language. The primary goal is to deepen your understanding of hash functions, hash tables, collision handling, and their applications. Upon completion of this project, you should be able to explain these concepts without relying on external sources.

## Learning Objectives

### General

1. **What is a hash function?**
   - A hash function is a method that takes an input (or 'key') and produces a fixed-size string of characters, which is typically a hash code. The key here is a string.

2. **What makes a good hash function?**
   - A good hash function should generate unique hash codes for distinct inputs and distribute these codes uniformly across the hash table array.

3. **What is a hash table, how do they work, and how to use them?**
   - A hash table is a data structure that maps keys to values using a hash function. It typically consists of an array of linked lists, and each list represents a bucket that stores key-value pairs.

4. **What is a collision, and what are the main ways of dealing with collisions in the context of a hash table?**
   - A collision occurs when two keys hash to the same index in the array. Main collision resolution methods include chaining (using linked lists in each array cell) and open addressing (finding the next available slot).

5. **What are the advantages and drawbacks of using hash tables?**
   - Advantages include fast data retrieval and insertion. Drawbacks may include increased memory usage due to potential collisions.

6. **What are the most common use cases of hash tables?**
   - Hash tables are often used in scenarios where quick data retrieval and insertion are crucial, such as database indexing, caches, and symbol tables.

### Copyright - Plagiarism

- You are responsible for creating solutions to the tasks independently, ensuring no plagiarism or unauthorized publication of content.

## Project Requirements

### General

- **Allowed Editors:** vi, vim, emacs
- **Compilation:** Ubuntu 20.04 LTS, gcc with options -Wall -Werror -Wextra -pedantic -std=gnu89
- **File Conventions:** Files should end with a new line.
- **README.md:** Mandatory at the root, containing project details.
- **Coding Style:** Follow the Betty style, checked using betty-style.pl and betty-doc.pl.
- **Global Variables:** Not allowed.
- **Functions per File:** No more than 5.
- **Header File:** Include prototypes in hash_tables.h and use include guards.
- **Library:** Use the C standard library.

### Data Structures

```c
typedef struct hash_node_s
{
     char *key;
     char *value;
     struct hash_node_s *next;
} hash_node_t;

typedef struct hash_table_s
{
     unsigned long int size;
     hash_node_t **array;
} hash_table_t;

