# saequus-flask-website-first-version
First version of a saequus.com website for poems.

Ready to upload and deploy Flask App for poem website.
This Flask App includes:
  1. Flask & Python Package with html and css templates with bootstrap technogoly include
  2. Instruction on how to deploy the App on the server
  3. Raw .jpg, .png files


# Deployment Flask Package on Digital Ocean server
Creating main folder in ~ folder (root or user), installing flask, python-pip, nginx
```sudo apt-get install nginx flask```
```mkdir main```
```apt-get install python-pip nginx```

Starting nginx 
```sudo /etc/init.d/nginx start```

Remove default nginx file 
```sudo rm /etc/nginx/sites-enabled/default```
Make new file instead of deleted

```sudo touch /etc/nginx/sites-available/flask_settings```

Make a link between these two
`sudo ln -s /etc/nginx/sites-available/flask_settings /etc/nginx/sites-enabled/flask_settings`

Open flask-settings file with vim (or nano if you'd prefer)
```vim /etc/nginx/sites-enabled/flask_settings```

Set configuration setttings
```
server {
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
}
}
```

Restart nginx
sudo /etc/init.d/nginx restart

Install virtualenv 
```pip install virtualenv```
Create `env` virtual environment in `main` folder
```cd main```
```virtualenv env```

Activate virtual environment
```source env/bin/activate```

Install gunicorn
```pip3 install flask gunicorn```

Run the app
```gunicorn run:app```



## Possible problems with deployment

If you see something like this:
`[20303] ERROR ` run
```ps -A```
and kill all gunicorn processes
```sudo kill 20303```
and if you root run gunicorn without sudo
```gunicorn run:app```



