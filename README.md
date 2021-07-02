#	CNT 4713 Net-Centric Computing Class Project
<p align="center">
	<img src="./static/ClassLogo.png" alt="CNT4713 LOGO" />
</p>

This is a simple web application where I am hosting a static & live feed.
Pretty much you'll see a video of me back from 2006 when my band tried our luck at a Battle of the Bands.
I'm also live-streaming from my webcam with the help of VLC Player & Ngrok.

The website is <a href="https://newappv.herokuapp.com">here</a>.

I used for this project the following:
<ul>
	<li>Python</li>
	<li>Ananconda</li>
	<li>Flask Framework</li>
	<li>OAuth: Google</li>
	<li>VLC Player</li>
	<li>Ngrok</li>
	<li>Heroku</li>
</ul>

While developing this application, I had to learn Python fundamentals and
Web Development using the Flask Framework.

<h2>Recommended Courses:</h2>

<a href="https://www.udemy.com/share/1013nI2@FG5gV2FbSF0Kck5EBHBnVBRu/">Udemy: Python and Flask Bootcamp: Create Websites using Flask!</a>
<br>
<a href="https://www.udemy.com/share/101Wai2@Pm1gbFlSTlQGdUBAEmJOVD1HYA==/">Udemy: Learn Python Programming Masterclass</a>

#	Installation

<h6>Please note that this is not the best solution but most of these concepts were alien to me at the start of the project.</h6>

<h5>Step 1: Step Your Python Environment</h5>
<br>
<li>Download and install <a href="https://www.anaconda.com/">Ananconda</a></li>

After you download and install Ananconda, create a Python environement. Open your command prompt (Windows Key + r -> cmd)
and type the following: (you can replace "webstream" by whatever you wish)

```
	conda create -n webstream flask
```

This will start creating the environment and install the <a href="https://flask-doc.readthedocs.io/en/latest/"> Flask Framework </a>.
It will ask for your input to install other dependencies; enter 'y' to proceed. Once it finishes creating the environment it will show
you how to activate (and deactivate) the environment. Type the command:

```
	conda activate webstream
```

<h5>Step 2: Download the requirements<h5>

All the dependcies needed for this all to work are on the requirements.txt file. To install them, through your command prompt, you have to change to the directory
where you downloaded this project (the root directory of project).

```
	cd <path to project>
```

then type the following command:

```
	pip install -r requirements.txt
```

This will install everything.
