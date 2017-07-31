
from flask_assets import Bundle, Environment
from .. import app
bundles = {
        'home_js': Bundle(
            #'bower_components/jquery/dist/jquery.js',
            'bower_components/jquery/dist/jquery.min.js',
            output='gen/home.js'),
        'react_js': Bundle(
            'bower_components/babel-standalone/babel.min.js',
            'bower_components/react/react.min.js',
            'bower_components/react/react-dom.min.js',
            output='gen/react.js')
        }

assets = Environment(app)

assets.register(bundles)
