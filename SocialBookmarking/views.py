from flask import render_template, url_for, redirect, flash

from datetime import datetime

from SocialBookmarking import app, db
from forms import BookmarkForm
from models import BookMark

bookmarks = []


def store_bookmark(url, description):
    bookmarks.append(dict(
        url=url,
        description=description,
        user="Kevin",
        date=datetime.utcnow()
    ))


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=BookMark.newest(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()

    if form.validate_on_submit():
        app.logger.debug('validate_on_submit')
        url = form.url.data
        description = form.description.data
        bm = BookMark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        flash("Stored bookmark '{}'".format(description))
        app.logger.debug('stored url: ' + url)
        return redirect(url_for('index'))
    app.logger.debug('navigating to add.html: ')
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
