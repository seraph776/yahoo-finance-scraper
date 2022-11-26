# Welcome to the Contributing Guide docs

Thank you for investing your time in contributing to our project! Any contribution you make will be reflected on [docs.github.com](https://docs.github.com/en) :sparkles:. 
Read our [Code of Conduct](https://github.com/seraph776/QuickStartTemplate/blob/main/docs/CODE-OF-CONDUCT.md) to keep our community approachable and respectable. In this guide you will get an overview of the contribution workflow from opening an issue, creating a PR, reviewing, and merging the PR.


##  New contributor guide

To get an overview of the project, read the [README](README.md). Here are some resources to help you get started with open source contributions:

- [Finding ways to contribute to open source on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github)
- [Set up Git](https://docs.github.com/en/get-started/QuickStartTemplate/set-up-git)
- [GitHub flow](https://docs.github.com/en/get-started/QuickStartTemplate/github-flow)
- [Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)


## Getting started 

To navigate our codebase with confidence, see [the introduction to working in the docs repository](https://docs.github.com/en) :confetti_ball:. For more information on how we write our markdown files, see [the GitHub Markdown reference](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). Check to see what [types of contributions](https://github.com/github/docs/blob/main/contributing/types-of-contributions.md) we accept before making changes.
Some of them don't even require writing a single line of code :sparkles:.


## Issues

If you spot a problem with the docs, search if an issue already exists. If a related issue doesn't exist, you can open a new issue using a relevant issue form.


## Bug Reporting 

We encourage people to report bugs. Please read [How to Submit a Good Bug Report](https://github.com/theopensourceway/guidebook/blob/main/bug_report.adoc) before submitting your report. The most important advice from there is: 1) do as thorough a search as you can to see whether the bug has already been reported, and 2) be as precise and complete as you can when reporting a new bug.
To report a bug:

1. Go to the appropriate project.
2. Click the Issues button on the left of the window.
3. Click the "New issue" button.
4. Fill out the Title and Description. You don't need to fill out the other fields. (Shall we encourage readers to use the Label field?)


## Reporting security flaws
If you find a flaw in our project that can hurt users or provide unauthorized access, please contact our maintainer privately, as follows.
Chat channel:
Contact: @
See [SECURITY.md]() for more information on security.

✨ Look at our commit history for more examples: We'll still work with your contributions even if they don't follow these guidelines so don't let that stop you.


## Project Work Flow 


1. On Github, fork the repository. ℹ️ [reference](https://docs.github.com/en/get-started/QuickStartTemplate/fork-a-repo#forking-a-repository).
2. Clone the repository to your local machine using the command below. ℹ️[reference](https://docs.github.com/en/get-started/QuickStartTemplate/fork-a-repo#cloning-your-forked-repository).
```
$ git clone https://github.com/<YOUR_USERNAME>/TheArtofPython.git
```
3. Create a new branch using the command below. ℹ️[reference](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/making-changes-in-a-branch/managing-branches#creating-a-branch). 
```
$ git checkout -b <BRANCH_NAME>
```
4. Add your contribution using the following command, ensuring that the code passes the corresponding test cases (_see the Testing section_).
```
$ git add <FILE_NAME>
```
5. Commit your changes with a message. ℹ️[reference](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project).
```
$ git commit -m "Adding <FILE_NAME>
```
6. Push Changes to Folked Repo. ℹ️[reference](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository).
```
$ git push -u origin <BRANCH_NAME>
```
7. Submit a pull request. ℹ️[reference](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button. Then submit your pull request. Thank you for any contributions!

## Submission Requirments 

**Code submissions should follow  the following guidlines:**

- Python 3+
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) Style Guide for Python Code.
- Follow the [Python Naming Conventions](https://peps.python.org/pep-0008/#naming-conventions) so variable_names and function_names should be `snake_case`, CONSTANTS in `UPPERCASE`, and ClassNames should be `CamelCase`.
- Have a clean commit history. Ideally following the [angular commit message convention](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#type)
and including the problem being worked on in parenthesis. Look at our [commit history](https://github.com/careercup/QuickStartTemplate/commits/master) for more examples.
- Maintain the following directory structure with your submissions:
- **Plagiarism** is strictly not allowed. Any work that is found to be suspicious of plagiarized work will not be merged.
- Please follow Chris Beam's seven rules for writing a good commit messages:
  - Separate subject from body with a blank line.
  - Limit the subject line to 50 characters.
  - Capitalize the subject line.
  - Do not end the subject line with a period.
  - Use the imperative mood in the subject line.
  - Wrap the body at 72 characters.
  - Use the body to explain what and why versus how.

For examples and additional explanation of these seven rules, please read [Chris Beam's blog post](https://cbea.ms/git-commit/).



## Directory Structure 
Our content is divided by programming category. Please create an issue if you wish to add code in a category that we don't currently have here.
**Do not create folders in your submissions.** 

```
MyProject/
|_ app/
│  |_ app.py
|  |_ app_functions.py
|
|_ assets/
│  |_ images.jpg
|  |_ images.png
|
|_ test/
│     ├─ test_app_functions.py
|
|─ CODE-OF_CONDUCT.md
|─ CONTRIBUTING.md
|─ LICENSE.md|  
|─ README.md

```

## Testing 

Testing is optional; however, to test a specific function, do the following: first, ensure you are in the testing subdirectory by running cd testing from the root of the project. Then, run python [function-name]_test.py to test the code.
