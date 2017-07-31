
from flask_assets import Bundle, Environment
from .. import app
bundles = {
        'home_js': Bundle(
            'bower_components/jquery/dist/jquery.min.js',
            output='gen/home.js'),
        #'home_css': Bundle(
            #output='gen/home.css'),
        'react_js': Bundle(
            'bower_components/babel-standalone/babel.min.js',
            'bower_components/react/react.min.js',
            'bower_components/react/react-dom.min.js',
            output='gen/react.js'),
        'bootstrap_js': Bundle(
            'bower_components/bootstrap/dist/js/bootstrap.min.js',
            output='gen/bootstrap.js'),
        'bootstrap_css': Bundle(
            'bower_components/bootstrap/dist/css/bootstrap.min.css',
            output='gen/bootstrap.css'),
        }

assets = Environment(app)

assets.register(bundles)
