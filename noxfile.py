"""All the nox related automation lives here."""

import nox

nox.options.sessions = ["lint"]
nox.options.reuse_venv = True
nox.options.default_venv_backend = "uv|virtualenv"


@nox.session()
def airflow_start(session: nox.Session) -> None:
    """Start Airflow with a local SQLite DB."""
    session.run("docker-compose", "up", "-d", external=True)


@nox.session()
def airflow_stop(session: nox.Session) -> None:
    """Stop Airflow."""
    session.run("docker-compose", "down", external=True)


@nox.session()
def lint(session: nox.Session) -> None:
    """lint the codebase"""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox.session()
def tests(session: nox.Session) -> None:
    """Run the tests."""
    session.install("pytest")
    session.run("pytest", "tests/")
