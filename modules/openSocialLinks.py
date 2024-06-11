from subprocess import Popen

socials = {
    "youtube": "https://www.youtube.com/@OnelCrack",
    "github": "https://www.github.com/TechOGR",
    "instagram": "",
    "facebook": "",
    "telegram": ""
}

def openYoutube():
    Popen(["start", socials["youtube"]], shell=True)
    
def openInstagram():
    Popen(["start", socials["instagram"]], shell=True)
    
def openFacebook():
    Popen(["start", socials["facebook"]], shell=True)
    
def openGitHub():
    Popen(["start", socials["github"]], shell=True)
    
def openTelegram():
    Popen(["start", socials["telegram"]], shell=True)
    