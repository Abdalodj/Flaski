from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

from .utils  import find_content

@app.route('/')
@app.route('/index/')
def index():
    if 'img' in request.args:
        img = request.args['img']
        og_image = url_for('static', filename=img, _external=True)
        og_url = url_for('index', img=img, _external=True)
    else:
        description = """
            Toi, tu n'as pas peur d'être seul ! Les grands espaces et les 
            aventures sont faits pour toi. D'ailleurs, Koh Lanta est ton 
            émission préférée ! Bientôt tu partiras les cheveux au vent 
            sur ton radeau. Tu es aussi un idéaliste chevronné. Quelle 
            chance ! 
        """
        og_image = url_for('static', filename='tmp/sample.jpg', _external=True)
        og_url = url_for('index', _external=True)

    return render_template('index.html', 
                            user_name="Tom",
                            user_image=url_for('static', filename='img/profile.png'),
                            description = description,
                            blur=True,
                            og_url=og_url,
                            og_image=og_image)


@app.route('/result/')
def result():
    gender = request.args.get('gender')
    description = find_content(gender).description
    user_name = request.args.get('first_name')
    uid = request.args.get('id')
    profil_pic = 'http://graph.facebook.com/' + uid + '/picture?type=large'
    img = 'tmp/sample.jpg'
    og_url = url_for('index', _external=True,img=img)
    return render_template('result.html', 
                            user_name=user_name,
                            user_image=profil_pic,
                            description = description,
                            og_url=og_url)

@app.route('/contents/<content_id>/')
def content(content_id):
   return '%s' % content_id

# if __name__ == "__main__":
#     app.run()
