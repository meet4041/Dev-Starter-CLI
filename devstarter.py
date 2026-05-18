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
    "README.md": "# {project_name}\n\nGenerated with Dev-Starter-CLI.\n",
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
        "dirs": [
            "lib",
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
            "requirements.txt": "",
            "pubspec.yaml": (
                "name: flutter_clean_architecture_app\n"
                "description: Generated with Dev-Starter-CLI\n"
                "publish_to: 'none'\n"
                "version: 1.0.0+1\n\n"
                "environment:\n"
                "  sdk: '>=3.0.0 <4.0.0'\n\n"
                "dependencies:\n"
                "  flutter:\n"
                "    sdk: flutter\n\n"
                "dev_dependencies:\n"
                "  flutter_test:\n"
                "    sdk: flutter\n"
            ),
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


def build_project(base_dir: Path, project_name: str, template_key: str) -> Path:
    template = TEMPLATES[template_key]
    project_dir = base_dir / project_name
    project_dir.mkdir(parents=True, exist_ok=True)

    for name, content in COMMON_FILES.items():
        create_file(project_dir / name, content.format(project_name=project_name))

    for directory in template["dirs"]:
        (project_dir / directory).mkdir(parents=True, exist_ok=True)

    for name, content in template["files"].items():
        create_file(project_dir / name, content)

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
    project_name = selected["project_name"]
    project_dir = build_project(Path.cwd(), project_name, choice)
    print()
    print(color(" Project created successfully.", GREEN))
    print(color(f" Location: {project_dir}", CYAN))
    print(color(f" Stack: {selected['label']}", DIM))


if __name__ == "__main__":
    main()
