# Dev-Starter-CLI

Create starter project structures from one simple Python CLI.

Dev-Starter-CLI removes repetitive setup by generating ready-to-use project foundations for common stacks in seconds.

## Highlights

- Fast terminal-based project setup
- Clean starter structure for multiple stacks
- Good for learning, prototyping, and quick project bootstrapping
- No external packages required

## Templates

| Option | Project Type |
|--------|--------------|
| 1 | Python CLI project |
| 2 | Flask API project |
| 3 | FastAPI project |
| 4 | React project structure |
| 5 | Flutter clean architecture structure |
| 6 | Exit |

## What It Generates

Based on your selected option, the CLI creates a starter folder with common essentials such as:

- `README.md`
- `.gitignore`
- `.env.example`
- `requirements.txt`, `package.json`, or `pubspec.yaml`
- source, config, and test folders
- starter entry files like `main.py` or `main.dart`

Each generated project `README.md` includes:

- required tools and environment setup
- basic run commands
- troubleshooting hints if something breaks

## Run

```bash
python3 devstarter.py
```

The CLI also shows required environment setup before creation. If a required tool is missing, it stops early and tells the user what to install.

## Menu Preview

```text
1. Create Python CLI project
2. Create Flask API project
3. Create FastAPI project
4. Create React project structure
5. Create Flutter clean architecture structure
6. Exit
```

Select an option and press Enter. The matching starter structure is created in the current directory.

## Problem It Solves

Developers often waste time recreating the same base folders and starter files again and again. Dev-Starter-CLI gives you a quick, consistent starting point so you can begin building immediately.
