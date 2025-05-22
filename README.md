# About Restaurant-Management-System

A Python-based command-line application for managing restaurant operations, including customer orders, worker tasks, and table reservations.

## Features
### 1. Customer Functions:
* Request an empty table
* Place an order
* Ask for a bill
* Cancel an order

### 2. Worker Functions:
* Add, update, or delete menu items
* View the next order in the queue
* Check total pending orders
* View order history and total income

### Data Persistence: 
* Saves menu, table satus, and orders in .txt files

## Data Structures Used
### 1. Custom Array 
* Used for storing table statuses (True/False for availability)
* Dynamically resizable for flexible table management

### 2. Queue
* FIFO (First-In-First-Out) system for managing pending orders
* Workers process orders in the sequence they were received

### 3. Hash Map (Dictionary in Menu class)
* Stores menu items (key: dish name, value: price)
* Allows O(1) lookup for updating/deleting items

### 4. File I/O (.txt Storage)
* Persistent storage for:
  * Menu
  * Table Status
  * Order queue
  * Order history
 
## How to Run:
### 1. Clone the repository
```sh
git clone https://github.com/yourusername/Restaurant-Management.git 
```
### 2. Navigate to the project folder:
```sh
cd Restaurant-Management 
```

### 3. Run the program:
```sh
python main.py 
```

## License
This project is licensed under the MIT License – you are free to use, modify, and distribute this project with attribution.

## Contact
* Email: fckfelicia04@gmail.com
