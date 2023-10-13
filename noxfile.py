# noxfile.py
import nox

@nox.session(python=["3.10"])
def tests(session):
    session.run("python", "-m", "coverage", "report")
