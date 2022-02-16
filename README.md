# Shipp It
Welcome To Supply Chain App [ Shipp It ]

![image](https://user-images.githubusercontent.com/84222590/151915204-0edff92c-fbef-464b-87b3-aae40227dd50.png)


# Goal

To create a full solution[web+app] for the entire supply chain from receiving the order from an e-com/store to sending it to the end user .


# About

 "Shipp It" is a Full-scale logistic service. Using "Shipp It" big companies to individual small sellers anyone can deliver their product to their desired customer. This software will be ready to use, for any kind of users and at any scale - from the business class to startup and individual level. Different role based authentication and accesses will let individual seller get more clarity for their small business. It will also give real time updates of the products with location tracking.
Proper details for any kind of delay or late shipment will be conveyed directlty by the delivery personal from very interactive app.


# Features 

* Real time tracking with multi admin system 
* User friendly interactive platform
* Different permission based dashboard/ features for supporting startup 
* OTP based authentication 


# Languages & Tools 

* Python, Django, Django-Rest-Framework(DRF)
* Flutter, React
* HTML, CSS, Javascript
* PostgreSQL


# Contributors

• Saikat Mukherjee
• Soumalya Bhattacharya
• Shreshtha Sadhu


# Maintainers

• Saikat Mukherjee


# Participating under JWoC 2K22

# Mentor

Mentor for this project is Saikat Mukherjee. Github profille :- https://github.com/7saikat7

<table>
<tr>
 <td align="center"><a href="https://github.com/7saikat7"><img src="https://avatars.githubusercontent.com/u/65228695?v=4" width=150px height=150px /></a></br> <h4 style="color:red;">Saikat Mukherjee</h4>

</tr>
</table>

# Django app setup guidelines 🚀

### Development Environment Setup: Windows


**Step 1** : Downloading and Installing the Code Editor
<br>
<br/>
You can install any one of the following code editors.
<br>

- <a href="https://code.visualstudio.com/">Visual Studio Code</a>
- <a href="https://www.sublimetext.com/3">Sublime Text 3</a>
- <a href="https://atom.io/">Atom</a>


---


**Step 2** : Installing Python 3.9

<br>
Download <a href="https://www.python.org/downloads/">Python 3.9 </a>
<br><br>
<ul>
<li>Download the Windows x86-64 executable installer for the 64-bit version of Windows</li>
<li>Download the Windows x86 executable installer for the 32-bit version of Windows.</li>
<li>Make sure to check '<b>Add Python 3.9 to Path</b>' in the setup window of the Installer.</li>
</ul>

Verify the installation from the command prompt (Terminal) using the following command,

```bash
python --version
```

Installed version of python will be printed.


---


**Step 3**: Installing Git

<br>
Download <a href="https://git-scm.com/downloads">Git</a>


---


**Step 4**: Fork the Repository

<br>
Click on <a href="#" target="_self"> <img src="https://docs.github.com/assets/cb-6294/images/help/repository/fork_button.jpg" width="15%"> </img></a> to fork <a href="https://github.com/7saikat7/supply_chain">this</a> repsository


---

**Step 5**: Creating Project Directory

<br>
Note: We're creating project directory on the desktop for easy and fast access.
<br><br>

```bash
cd desktop
mkdir myprojects
cd myprojects
```


---


**Step 6**: Cloning Repository using Git

<br>

```bash
git clone https://github.com/'<your-github-username>'/supply_chain.git
```


---


**Step 7**: Change directory to supply_chain

<br>

```bash
cd supply_chain
```


---

**Step 8**: Add a reference to the original repository

<br>

```bash
git remote add upstream https://github.com/7saikat7/supply_chain.git
```


---

**Step 9**: Creating Virtual Environment

<br>
Install virtualenv
<br><br>

```bash
pip3 install virtualenv
```

Creating Virtual Environment named `myvenv`

```bash
virtualenv myvenv -p python3.9
```

To Activate `myvenv`

```bash
myvenv\Scripts\activate
```

To deactivate `myvenv`

```bash
deactivate
```


---


**Step 10**: Installing Requirements

<br>
Note: Before installing requirements, Make sure Virtual Environment is activated.
<br><br>

```bash
pip install -r requirements.txt
```


---


**Step 11**: Making database migrations

<br>

```bash
python manage.py makemigrations
python manage.py migrate
```


---

**Step 12**: Creating superuser to access Admin Panel

<br>

```bash
python manage.py createsuperuser
```


---

**Step 13**: Running the Project in local server

<br>
<b>Note:</b> Before running the project in local server, Make sure you activate the Virtual Environment.
<br><br>

```bash
python manage.py runserver
```
<br/>

---

# Contribution guidelines 🔐


Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

**1.**  To contribute to this project you first need to fork this repository
        Fork [this](https://github.com/7saikat7/supply_chain) repository.
        To fork it click on the fork
        ![image](https://docs.github.com/assets/cb-6294/images/help/repository/fork_button.jpg)


**2.**  Clone your forked copy of the project.
        To clone open git bash in your device and type the following command 

```
git clone https://github.com/<your github username>/supply_chain.git
```

**3.** Now open git bash in cloned repository folder


**4.** Add a reference(remote) to the original repository.

```
git remote add upstream https://github.com/7saikat7/supply_chain.git
```

**5.** Check the remotes for this repository.
```
git remote -v
```

**6.** Always take a pull from the upstream repository to your master branch to keep it at par with the main project(updated repository).

```
git pull upstream main
```

**7.** Create a new branch.

```
git checkout -b <your_branch_name>
```

**8.** Perform your desired changes to the code base.


**9.** Track your changes:heavy_check_mark: .

```
git add . 
```

**10.** Commit your changes .

```
git commit -m "Relevant message"
```

**11.** Push the committed changes in your feature branch to your remote repo.
```
git push -u origin <your_branch_name>
```

**12.** To create a pull request, click on `compare and pull requests`. Please ensure you compare your feature branch to the desired branch of the repository you are supposed to make a PR to.


**13.** Add appropriate title and description to your pull request explaining your changes and efforts done.


**14.** Click on `Create Pull Request`.

**Happy Contributing**

<br>

--- 

# ShippIt UI 

###  Take A Look Of Our Projects UI   **[Shipp It UI ](https://www.figma.com/file/1JMyodDjCK4SkiqXzHzkDK/Ship-It?node-id=0%3A1)** 







