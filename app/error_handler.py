from flask import render_template


def handle_error(error):
    return render_template('templates/error.html', error=error), error.code
