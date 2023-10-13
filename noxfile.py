# noxfile.py
import nox

@nox.session(python=["3.10"])
def tests(session):
    session.install("-r", "requirements.txt") 
    session.run("python", "-m", "coverage", "report")
