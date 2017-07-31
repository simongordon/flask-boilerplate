
from flask_assets import Bundle, Environment
from .. import app
bundles = {
        'home_js': Bundle(
            #'bower_components/jquery/dist/jquery.js',
            'bower_components/jquery/dist/jquery.min.js',
            output='gen/home.js')
        }

assets = Environment(app)

assets.register(bundles)
