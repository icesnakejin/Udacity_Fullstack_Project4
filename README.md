# Udacity_Fullstack_Project4

# App Engine application for the Udacity training course.

### Description:

This project is to improve upon and extend an existing Conference program written in Python using the Google App Engine Api.

###Udacity project goals completed:

### 1: Add Sessions to a Conference

Endpoints, Class, forms, and Indexes added to support multiple sessions per conference.
Sessions are implemented with an ancestor relationship to their conference.
Sessions are memcached for performance due to the probability that they will be queried often.

Endpoints added include:
* createSession,
* getConferenceSessions
* getConferenceSessionsByType
* getSessionsBySpeaker


### 2: Add sessions ot User Wishlist

Wishlist are stored in the user's profile.  The profile model was adjusted to add this functionality.

Endpoints added include:
* addSessionToWishlist
* getSessionsInWishlist

### 3: Work on indexes and queries

Indexes were created to allow for filtering.  A problem query related to pulling all sessions before 7pm and excluding workShop was implemented.  The key takeaway form this is that it can not be done a simple query due to the limitation of datastore allowing only a single inequality filter.  To work around this, the time filter is implemented in the query and the session type filter is done in the python on the results of the first query.

I implemented this in a slightly more flexible way than requested.  Instead of 7pm and workshop type, the endpoint added accepts an hour as an interval in 24 hour format and a session type to filter as a string.

Additionally, two queries to help find Sessions that have default values still were added.  One find sessions with unknown highlights and the other finds ones with a Generic session type.

Endpoints added include:
* getSessionsBeforeHourExcludingType
* getUnknownHighlightsSessions
* getGenericSessions


### 4: Add support for a feature speaker and an endpoint to get that speaker

Featured speaker was implemented somewhat similar to the existing announcement feature.  The featured speaker is stored only in memcache as it is not vital to have long term.  If a speaker has more than one session, they are added as the featured speaker at the time a new session is added for them.

Endpoints added include:
* getFeaturedSpeaker

### Setup Instructions:

Note: To deploy this API server locally the [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads) is required.

1. Clone the git repository (or download it from the submission)
2. Run `dev_appserver.py DIR` or launch the app from the GUI app launcher Google provides in their API download.  Ensure it's running by visiting your local server's address, which is likely to be [localhost:8080][5]].

Optionally you can follow these instructions to set it up for your own deplayment:

1. Update the value of `application` in `app.yaml` to the app ID you
   have registered in the App Engine admin console and would like to use to host
   your instance of this sample.
1. Update the values at the top of `settings.py` to
   reflect the respective client IDs you have registered in the
   [Developer Console][4].
1. Update the value of CLIENT_ID in `static/js/app.js` to the Web client ID
1. (Optional) Mark the configuration files as unchanged as follows:
   `$ git update-index --assume-unchanged app.yaml settings.py static/js/app.js`
1. Run the app with the devserver using `dev_appserver.py DIR`, and ensure it's running by visiting your local server's address (by default [localhost:8080][5].)
1. (Optional) Generate your client library(ies) with [the endpoints tool][6].
1. Deploy your application.

[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool
