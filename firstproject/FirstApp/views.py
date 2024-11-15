from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function
	#ss ----> is html-data/code
	ss = '''		
			<center>
				<h2 style="color:Blue;">
					Hello User, Welcome to Django First-Project First-App
				</h2>
				<hr />
			</center>
		''';
	
	return HttpResponse(ss);

# Create your views here.
def display(request): #view-function (/welcome/)
	print("welcome/ url is requested & display() is executed");

def demo(request):   
	print("mulitple-Requests-URLs same respose");
	htmldata='''<center>
		<h1>Welcome Demo User!!!</h1>
		<hr />
		<h2>This is Same-Output for diff-mulitple-Requests-URLs</h2>
		<hr />
		<h3>Have a Great Day...</h3>
		</center>''';
	return HttpResponse(htmldata);

def homepage(request):
	hp='''<center>
	<h1>Welcome to Home Page</h1>
	<hr>
	<h2>Your Request Not Found</h2>
	<hr>
	<h3>Try Another URL</h3><hr>
	</center>'''
	return HttpResponse(hp)
