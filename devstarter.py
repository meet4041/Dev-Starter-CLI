import subprocess
from shutil import which
from pathlib import Path


RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"


COMMON_FILES = {
    ".gitignore": "__pycache__/\n*.pyc\n.env\n.venv/\nvenv/\nnode_modules/\ndist/\nbuild/\ncoverage/\n.dart_tool/\n.flutter-plugins\n.flutter-plugins-dependencies\n",
    ".env.example": "# Add environment variables here\n",
}


def color(text: str, tone: str) -> str:
    return f"{tone}{text}{RESET}"


def clear_screen() -> None:
    print("\033[2J\033[H", end="")


def line(char: str = "─", width: int = 64) -> str:
    return char * width


def banner() -> str:
    return "\n".join(
        [
            color(line("═"), BLUE),
            color(f"{BOLD} Dev-Starter-CLI".ljust(64), CYAN),
            color(line("═"), BLUE),
        ]
    )


def menu_item(key: str, title: str, description: str) -> str:
    prefix = color(f" {key} ", BOLD + BLUE)
    return f"{prefix} {color(title, BOLD)}\n    {color(description, DIM)}"


TEMPLATES = {
    "1": {
        "label": "Create Python CLI project",
        "project_name": "python-cli-project",
        "description": "CLI app with src, commands, tests, config, and main entry point",
        "requirements": [
            "Python 3 installed",
            "pip available if you want to add packages later",
        ],
        "creation_checks": [],
        "run_steps": [
            "python3 main.py",
        ],
        "troubleshooting": [
            "If python3 is not found, install Python 3 and add it to PATH.",
            "If imports fail, run commands from the project root.",
        ],
        "dirs": [
            "src",
            "src/commands",
            "tests",
            "config",
        ],
        "files": {
            "requirements.txt": "",
            "src/__init__.py": "",
            "src/commands/__init__.py": "",
            "main.py": (
                'def main() -> None:\n'
                '    print("Hello from Python CLI project")\n\n'
                'if __name__ == "__main__":\n'
                "    main()\n"
            ),
            "tests/test_main.py": (
                "from main import main\n\n\n"
                "def test_main_runs() -> None:\n"
                "    main()\n"
            ),
            "config/settings.py": "APP_NAME = \"python-cli\"\n",
        },
    },
    "2": {
        "label": "Create Flask API project",
        "project_name": "flask-api-project",
        "description": "Flask API starter with routes, tests, settings, and health endpoint",
        "requirements": [
            "Python 3 installed",
            "pip installed",
        ],
        "creation_checks": [],
        "run_steps": [
            "python3 -m pip install -r requirements.txt",
            "python3 main.py",
        ],
        "troubleshooting": [
            "If Flask is missing, install dependencies with pip.",
            "If port 5000 is busy, stop the other process or change the port in main.py.",
        ],
        "dirs": [
            "src",
            "src/routes",
            "tests",
            "config",
        ],
        "files": {
            "requirements.txt": "Flask>=3.0.0\n",
            "src/__init__.py": "",
            "src/routes/__init__.py": "",
            "src/routes/api.py": (
                "from flask import Blueprint, jsonify\n\n"
                "api = Blueprint(\"api\", __name__)\n\n\n"
                "@api.get(\"/health\")\n"
                "def health():\n"
                "    return jsonify({\"status\": \"ok\"})\n"
            ),
            "main.py": (
                "from flask import Flask\n"
                "from src.routes.api import api\n\n"
                "app = Flask(__name__)\n"
                "app.register_blueprint(api, url_prefix=\"/api\")\n\n\n"
                "if __name__ == \"__main__\":\n"
                "    app.run(debug=True)\n"
            ),
            "tests/test_api.py": (
                "from main import app\n\n\n"
                "def test_health() -> None:\n"
                "    client = app.test_client()\n"
                "    response = client.get(\"/api/health\")\n"
                "    assert response.status_code == 200\n"
            ),
            "config/settings.py": "DEBUG = True\n",
        },
    },
    "3": {
        "label": "Create FastAPI project",
        "project_name": "fastapi-project",
        "description": "FastAPI service structure with router, tests, config, and app setup",
        "requirements": [
            "Python 3 installed",
            "pip installed",
        ],
        "creation_checks": [],
        "run_steps": [
            "python3 -m pip install -r requirements.txt",
            "uvicorn main:app --reload",
        ],
        "troubleshooting": [
            "If uvicorn is missing, install dependencies with pip.",
            "If the server does not start, confirm you are inside the project folder.",
        ],
        "dirs": [
            "src",
            "src/routes",
            "tests",
            "config",
        ],
        "files": {
            "requirements.txt": "fastapi>=0.115.0\nuvicorn>=0.30.0\n",
            "src/__init__.py": "",
            "src/routes/__init__.py": "",
            "src/routes/api.py": (
                "from fastapi import APIRouter\n\n"
                "router = APIRouter()\n\n\n"
                "@router.get(\"/health\")\n"
                "def health() -> dict[str, str]:\n"
                "    return {\"status\": \"ok\"}\n"
            ),
            "main.py": (
                "from fastapi import FastAPI\n"
                "from src.routes.api import router\n\n"
                "app = FastAPI()\n"
                "app.include_router(router, prefix=\"/api\")\n"
            ),
            "tests/test_api.py": (
                "from fastapi.testclient import TestClient\n"
                "from main import app\n\n\n"
                "client = TestClient(app)\n\n\n"
                "def test_health() -> None:\n"
                "    response = client.get(\"/api/health\")\n"
                "    assert response.status_code == 200\n"
            ),
            "config/settings.py": "APP_NAME = \"fastapi-app\"\n",
        },
    },
    "4": {
        "label": "Create React project structure",
        "project_name": "react-project",
        "description": "React frontend layout with public, pages, components, assets, and config",
        "requirements": [
            "Node.js installed",
            "npm installed",
        ],
        "creation_checks": [],
        "run_steps": [
            "npm install react react-dom react-scripts",
            "npm start",
        ],
        "troubleshooting": [
            "If npm is not found, install Node.js which includes npm.",
            "If react-scripts is missing, run npm install first.",
        ],
        "dirs": [
            "src",
            "src/components",
            "src/pages",
            "src/assets",
            "public",
            "tests",
            "config",
        ],
        "files": {
            "requirements.txt": "",
            "package.json": (
                "{\n"
                '  "name": "react-app",\n'
                '  "version": "1.0.0",\n'
                '  "private": true,\n'
                '  "scripts": {\n'
                '    "start": "react-scripts start",\n'
                '    "build": "react-scripts build",\n'
                '    "test": "react-scripts test"\n'
                "  }\n"
                "}\n"
            ),
            "public/index.html": (
                "<!DOCTYPE html>\n"
                "<html lang=\"en\">\n"
                "  <head>\n"
                "    <meta charset=\"UTF-8\" />\n"
                "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n"
                "    <title>React App</title>\n"
                "  </head>\n"
                "  <body>\n"
                "    <div id=\"root\"></div>\n"
                "  </body>\n"
                "</html>\n"
            ),
            "src/index.js": (
                "import React from \"react\";\n"
                "import ReactDOM from \"react-dom/client\";\n"
                "import App from \"./App\";\n\n"
                "ReactDOM.createRoot(document.getElementById(\"root\")).render(\n"
                "  <React.StrictMode>\n"
                "    <App />\n"
                "  </React.StrictMode>\n"
                ");\n"
            ),
            "src/App.js": (
                "function App() {\n"
                "  return <h1>Hello from React project</h1>;\n"
                "}\n\n"
                "export default App;\n"
            ),
            "src/components/.gitkeep": "",
            "src/pages/.gitkeep": "",
            "src/assets/.gitkeep": "",
            "tests/.gitkeep": "",
            "config/.gitkeep": "",
        },
    },
    "5": {
        "label": "Create Flutter clean architecture structure",
        "project_name": "flutter-clean-architecture-project",
        "description": "Flutter clean architecture folders for core, data, domain, and presentation",
        "flutter_app_name": "flutter_clean_architecture_app",
        "requirements": [
            "Flutter SDK installed",
            "Flutter added to PATH",
            "Desktop support enabled if you want to run on PC",
        ],
        "creation_checks": [
            {
                "command": "flutter",
                "message": "Flutter SDK is required. Install Flutter and add it to PATH.",
            },
        ],
        "run_steps": [
            "flutter pub get",
            "flutter run -d windows",
        ],
        "troubleshooting": [
            "If flutter is not found, install Flutter and add it to PATH.",
            "If no desktop device appears, run flutter config --enable-windows-desktop or enable your target desktop platform.",
            "If packages fail to resolve, run flutter pub get.",
        ],
        "dirs": [
            "lib/core",
            "lib/core/error",
            "lib/core/network",
            "lib/features",
            "lib/features/sample/domain/entities",
            "lib/features/sample/domain/repositories",
            "lib/features/sample/domain/usecases",
            "lib/features/sample/data/datasources",
            "lib/features/sample/data/models",
            "lib/features/sample/data/repositories",
            "lib/features/sample/presentation/bloc",
            "lib/features/sample/presentation/pages",
            "lib/features/sample/presentation/widgets",
            "test",
            "config",
        ],
        "files": {
            "lib/main.dart": (
                "import 'package:flutter/material.dart';\n\n"
                "void main() {\n"
                "  runApp(const MyApp());\n"
                "}\n\n"
                "class MyApp extends StatelessWidget {\n"
                "  const MyApp({super.key});\n\n"
                "  @override\n"
                "  Widget build(BuildContext context) {\n"
                "    return MaterialApp(\n"
                "      title: 'Flutter Clean Architecture',\n"
                "      home: Scaffold(\n"
                "        appBar: AppBar(title: const Text('Home')),\n"
                "        body: const Center(child: Text('Hello from Flutter project')),\n"
                "      ),\n"
                "    );\n"
                "  }\n"
                "}\n"
            ),
            "lib/core/error/failures.dart": "class Failure {}\n",
            "lib/core/network/network_info.dart": "abstract class NetworkInfo {}\n",
            "lib/features/sample/domain/entities/sample.dart": "class Sample {}\n",
            "lib/features/sample/domain/repositories/sample_repository.dart": "abstract class SampleRepository {}\n",
            "lib/features/sample/domain/usecases/get_sample.dart": "class GetSample {}\n",
            "lib/features/sample/data/datasources/sample_remote_data_source.dart": "abstract class SampleRemoteDataSource {}\n",
            "lib/features/sample/data/models/sample_model.dart": "class SampleModel {}\n",
            "lib/features/sample/data/repositories/sample_repository_impl.dart": "class SampleRepositoryImpl {}\n",
            "lib/features/sample/presentation/bloc/sample_bloc.dart": "class SampleBloc {}\n",
            "lib/features/sample/presentation/pages/sample_page.dart": "class SamplePage {}\n",
            "lib/features/sample/presentation/widgets/sample_card.dart": "class SampleCard {}\n",
            "test/.gitkeep": "",
            "config/.gitkeep": "",
        },
    },
}


def create_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_readme(project_name: str, template: dict[str, object]) -> str:
    requirements = "\n".join(f"- {item}" for item in template["requirements"])
    run_steps = "\n".join(f"```bash\n{step}\n```" for step in template["run_steps"])
    troubleshooting = "\n".join(f"- {item}" for item in template["troubleshooting"])
    return (
        f"# {project_name}\n\n"
        "Generated with Dev-Starter-CLI.\n\n"
        "## Requirements\n\n"
        f"{requirements}\n\n"
        "## Run\n\n"
        f"{run_steps}\n\n"
        "## Troubleshooting\n\n"
        f"{troubleshooting}\n"
    )


def create_project_readme(project_dir: Path, project_name: str, template: dict[str, object]) -> None:
    create_file(project_dir / "README.md", build_readme(project_name, template))


def missing_creation_requirements(template: dict[str, object]) -> list[str]:
    missing = []
    for check in template.get("creation_checks", []):
        command = str(check["command"])
        if which(command) is None:
            missing.append(str(check["message"]))
    return missing


def print_stack_info(template: dict[str, object]) -> None:
    print()
    print(color(" Requirements:", CYAN))
    for item in template["requirements"]:
        print(color(f"  - {item}", DIM))
    print(color(" If something breaks, check the generated README for run steps and troubleshooting.", DIM))


def build_flutter_project(base_dir: Path, project_name: str, template: dict[str, object]) -> Path:
    project_dir = base_dir / project_name
    flutter_app_name = str(template["flutter_app_name"])
    try:
        result = subprocess.run(
            ["flutter", "create", "--project-name", flutter_app_name, str(project_dir)],
            capture_output=True,
            text=True,
        )
    except FileNotFoundError as error:
        raise RuntimeError("Flutter SDK not found in PATH.") from error

    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or "Unknown Flutter error"
        raise RuntimeError(message)

    create_file(project_dir / ".env.example", COMMON_FILES[".env.example"])

    for directory in template["dirs"]:
        (project_dir / str(directory)).mkdir(parents=True, exist_ok=True)

    for name, content in template["files"].items():
        create_file(project_dir / str(name), str(content))

    create_project_readme(project_dir, project_name, template)
    return project_dir


def build_project(base_dir: Path, project_name: str, template_key: str) -> Path:
    template = TEMPLATES[template_key]
    if template_key == "5":
        return build_flutter_project(base_dir, project_name, template)

    project_dir = base_dir / project_name
    project_dir.mkdir(parents=True, exist_ok=True)
    for name, content in COMMON_FILES.items():
        create_file(project_dir / name, content.format(project_name=project_name))

    for directory in template["dirs"]:
        (project_dir / directory).mkdir(parents=True, exist_ok=True)

    for name, content in template["files"].items():
        create_file(project_dir / name, content)

    create_project_readme(project_dir, project_name, template)
    return project_dir


def print_menu() -> None:
    clear_screen()
    print(banner())
    print()
    for key, template in TEMPLATES.items():
        print(menu_item(key, template["label"], template["description"]))
        print()
    print(menu_item("6", "Exit", "Close Dev-Starter-CLI without creating a project"))
    print()
    print(color(line(), BLUE))
    print(color(" Select a stack or exit.", DIM))


def main() -> None:
    print_menu()
    choice = input(color(" > Select an option (1-6): ", YELLOW)).strip()
    if choice == "6":
        print(color(" Exiting Dev-Starter-CLI.", CYAN))
        return

    if choice not in TEMPLATES:
        print(color(" Invalid option. Please choose a number from 1 to 6.", RED))
        return

    selected = TEMPLATES[choice]
    print_stack_info(selected)
    missing = missing_creation_requirements(selected)
    if missing:
        print()
        print(color(" Missing required setup for project creation:", RED))
        for item in missing:
            print(color(f"  - {item}", YELLOW))
        return

    project_name = selected["project_name"]
    try:
        project_dir = build_project(Path.cwd(), project_name, choice)
    except RuntimeError as error:
        print()
        print(color(" Project creation failed.", RED))
        print(color(f" Reason: {error}", YELLOW))
        print(color(" Open the generated README requirements/troubleshooting after fixing the environment.", DIM))
        return

    print()
    print(color(" Project created successfully.", GREEN))
    print(color(f" Location: {project_dir}", CYAN))
    print(color(f" Stack: {selected['label']}", DIM))
    print(color(" Open README.md inside the project for install, run, and troubleshooting help.", DIM))


if __name__ == "__main__":
    main()
