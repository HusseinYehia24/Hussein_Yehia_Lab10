from pathlib import Path
import runpy
import shutil


def main():
    source = Path(__file__).resolve().parent / "app.py"
    destination = Path.home() / "jenkins_deploy" / "jenkins_project"
    destination.mkdir(parents=True, exist_ok=True)

    deployed_app = destination / "app.py"
    shutil.copy2(source, deployed_app)

    print(f"Deployed application to: {deployed_app}", flush=True)
    runpy.run_path(str(deployed_app), run_name="__main__")


if __name__ == "__main__":
    main()