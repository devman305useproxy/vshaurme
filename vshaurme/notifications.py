from flask import url_for

from vshaurme.extensions import db
from vshaurme.models import Notification


def push_follow_notification(follower, receiver):
    message = 'Пользователь <a href="%s">%s</a> подписался на вас.' % \
              (url_for('user.index', username=follower.username), follower.username)
    notification = Notification(message=message, receiver=receiver)
    db.session.add(notification)
    db.session.commit()


def push_comment_notification(photo_id, receiver, page=1):
    message = 'Под <a href="%s#comments">этим</a> фото появился комментарий/ответ.' % \
              (url_for('main.show_photo', photo_id=photo_id, page=page))
    notification = Notification(message=message, receiver=receiver)
    db.session.add(notification)
    db.session.commit()


def push_collect_notification(collector, photo_id, receiver):
    message = 'Пользователь <a href="%s">%s</a> взял ваше фото <a href="%s">photo</a> в коллекцию.' % \
              (url_for('user.index', username=collector.username),
               collector.username,
               url_for('main.show_photo', photo_id=photo_id))
    notification = Notification(message=message, receiver=receiver)
