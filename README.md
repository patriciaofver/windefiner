# WinDefiner

WinDefiner is a Python program that allows users to create custom dictionary terms and shortcuts for faster typing on Windows. It enables users to define shortcuts that automatically expand into longer phrases or sentences, helping to improve typing efficiency and reduce repetitive tasks.

## Features

- Create custom shortcuts and corresponding text replacements.
- Save and load definitions from a JSON file for persistence.
- Listen for defined shortcuts and automatically replace them with the full text.
- Simple command-line interface for adding, removing, and managing shortcuts.

## Requirements

- Python 3.x
- `keyboard` library (`pip install keyboard`)

## Installation

1. Clone the repository or download the `WinDefiner.py` file.
2. Ensure Python 3.x is installed on your system.
3. Install the required library by running:
   ```
   pip install keyboard
   ```

## Usage

1. Run the program using Python:
   ```
   python WinDefiner.py
   ```

2. Follow the on-screen prompts to:
   - Add a new shortcut by entering a shortcut term and its replacement text.
   - Remove an existing shortcut.
   - Start listening for shortcuts. The program will replace the defined shortcuts with their corresponding text when detected.

3. Press `ESC` to stop the listening mode.

## Example

- Add a shortcut:
  - Shortcut: `omw`
  - Replacement: `On my way!`
- Type `omw` followed by a space or enter, and it will automatically replace with `On my way!`.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any bug fixes or enhancements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.