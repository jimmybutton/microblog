from datetime import datetime, timedelta
import pytest
from app.models import User, Post

def test_password_hashing():
    u = User(username='susan')
    u.set_password('cat')
    assert not u.check_password('dog')
    assert u.check_password('cat')

def test_avatar():
    u = User(username='john', email='john@example.com')
    assert u.avatar(128) == 'https://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?d=identicon&s=128'

def test_follow(app_fixure):
    app, db = app_fixure
    u1 = User(username='john', email='john@example.com')
    u2 = User(username='susan', email='susan@example.com')
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()
    assert u1.followed.all() == []
    assert u1.followers.all() == []

    u1.follow(u2)
    db.session.commit()
    assert u1.is_following(u2)
    assert u1.followed.count() ==  1
    assert u1.followed.first().username == 'susan'
    assert u2.followers.count() == 1
    assert u2.followers.first().username == 'john'

    u1.unfollow(u2)
    db.session.commit()
    assert not u1.is_following(u2)
    assert u1.followed.count() == 0
    assert u2.followers.count() == 0
