
__author__ = 'wesc+api@google.com (Wesley Chun)'

import webapp2
import logging
from google.appengine.api import app_identity
from google.appengine.api import mail
from conference import ConferenceApi

class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        ConferenceApi._cacheAnnouncement()
        self.response.set_status(204)


class FeaturedSpeakerHandler(webapp2.RequestHandler):
    def post(self):
        """Set featured speaker in Memcache if appropriate"""
        logging.info("HELLO!") 
        ConferenceApi._cacheFeaturedSpeaker(self.request.get('speaker'))
        self.response.set_status(204)


class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created a following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )

app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/check_and_add_featured_speaker', FeaturedSpeakerHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
], debug=True)
