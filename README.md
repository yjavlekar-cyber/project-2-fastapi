# Project 2: Instructions for Automation

You have the code files (`main.py` and `requirements.txt`). Now, you need to create the automation files yourself.

---

## Task 1: Create the `Dockerfile`
Create a file named `Dockerfile` in this folder. It should follow this logic:
1. **Base Image**: Start with `python:3.12-slim`.
2. **Workdir**: Set it to `/app`.
3. **Copy Dependencies**: Copy `requirements.txt` into the current directory.
4. **Install**: Run `pip install` for the requirements.
5. **Copy Code**: Copy the `main.py` file.
6. **Port**: The app runs on port `8000`. You need an instruction to document this.
7. **Entrypoint**: Use `uvicorn` to run the app. 
    - *Hint*: The command should look like `uvicorn main:app --host 0.0.0.0 --port 8000`.

---

## Task 2: Create the `Jenkinsfile`
Create a file named `Jenkinsfile`. Use a `pipeline { ... }` block with these stages:

### Stage 1: Build
- **Goal**: Turn your code and Dockerfile into an image.
- **Action**: Use the `sh` command to run `docker build`. Don't forget to tag it (e.g., `-t my-project-2`).

### Stage 2: Deploy
- **Goal**: Run the container so you can see it on your browser.
- **Action**: 
    1. Use `docker rm -f` to clear any old container with the same name.
    2. Use `docker run` to start the new one.
    - *Hint*: You'll need `-d` for background, and `-p 8085:8000` to see it on your laptop.

---

## Validation
Once your files are created and the pipeline runs:
- Check the Jenkins logs for a "Success" message.
- Visit `http://localhost:8085` to see the JSON response from your Python code.
