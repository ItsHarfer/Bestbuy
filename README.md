# Bestbuy 🛒📦

A command-line inventory management application for a fictional electronics store. 
Features include product listing, quantity overview, and an interactive ordering system ...powered by clean OOP architecture and robust validation logic.
 
---

## ✨ Features

- 📦 Product inventory with name, price, and quantity tracking  
- 🧮 Stock validation and auto-deactivation on depletion  
- 🛒 Interactive ordering with product selection and quantity prompts  
- 🧪 Unit-tested with `pytest` and 100% functional coverage  

---

## 🛠️ Tech Stack

- Python 3.11+
- Standard Library (no external dependencies)
- `pytest` for unit testing

---

## 🧱 Project Structure
```
.
├── main.py                      # CLI entry point and user interaction loop
├── dispatcher.py                # Command dispatcher for CLI routing
├── products.py                  # Product class with validation logic
├── store.py                     # Store class for managing inventory and orders
└── tests
    ├── test_products.py         # Unit tests for Product class
    └── test_store.py            # Unit tests for Store class
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ItsHarfer/Bestbuy.git
cd Bestbuy
```

### 2. Run the App

```bash
python main.py
```
Follow the menu to interact with the store via terminal.

---

## 📋 Requirements
  - Python 3.11 or higher
  - pytest (only for testing)

To install pytest:

```bash
pip install pytest
```

---
## 🧪 Run Tests

```bash
pytest
```

All test cases are written using assert statements and cover:
- Product creation and validation
- Stock handling and quantity updates
- Store behavior and order processing
- Edge cases for invalid input

---
 
## 👤 Author

Martin Haferanke  
GitHub: [@ItsHarfer](https://github.com/ItsHarfer)  
Email: `martin.haferanke@gmail.com`

---

## 📄 License

Licensed under the MIT License.  
This project is intended for educational purposes and small-scale simulations.
