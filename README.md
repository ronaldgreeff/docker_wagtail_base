<!-- To run as a shell script -->
echo What should this virtualenv be called?
read venv
mkvirtualenv $venv

mkdir /webms/webpage
cp /webms/webpage_files/{Dockerfile,Dockerfile.production,Dockerfile.testing,entrypoint.sh,entrypoint.production.sh,wait-for-it.sh} webms/webpage/
cp -R /webms/webpage_files/requirements/ webms/webpage/
pip install -r /webms/webpage_files/requirements/base.txt
cd /webms/webpage
wagtail start webpage
rm webpage/Dockerfile webpage/requirements.txt
cd ../../
cp -a webms/webpage_files/webpage/settings/. webms/webpage/webpage/webpage/settings/
cp -r webms/webpage_files/webpage/templatetags/ webms/webpage/webpage/webpage/
cp webms/webpage_files/webpage/cookielaw.css webms/webpage/webpage/webpage/static/css/
cp webms/webpage_files/webpage/cookielaw.js webms/webpage/webpage/webpage/static/js/