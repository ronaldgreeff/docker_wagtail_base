$ mkvirtualenv {venv}
(with {venv} $ ....):

cd /example_site/webms/webpage_files/requirements
pip install -r base.txt
cd ../../
mkdir webpage
cp webpage_files/{Dockerfile,Dockerfile.production,Dockerfile.testing,entrypoint.sh,entrypoint.production.sh,wait-for-it.sh} webpage/
cp -R webpage_files/requirements/ webpage/
cd webpage
wagtail start webpage
rm webpage/Dockerfile webpage/requirements.txt
cd ..
cp -a webpage_files/webpage/settings/. webpage/webpage/webpage/settings/
cp -r webpage_files/webpage/templatetags/ webpage/webpage/webpage/
cp -r webpage_files/webpage/templatetags/ webpage/webpage/webpage/
cp webpage_files/webpage/cookielaw.css webpage/webpage/webpage/static/css/
cp webpage_files/webpage/cookielaw.js webpage/webpage/webpage/static/js/
cd ..
docker volume create webpage_postgres_volume
docker-compose -f docker-compose.yml -f docker-compose.development.yml build
docker-compose -f docker-compose.yml -f docker-compose.development.yml up
