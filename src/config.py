#!/usr/bin/python2.7
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Configuration options for the application.

  OAuth 2.0 Client Settings:
    Visit the APIs Console (https://code.google.com/apis/console/) to create or
    obtain client details for a project.
    Authorized Redirect URIs for your client should include the hostname of your
    app with /admin/auth appended to the end.
    e.g. http://example.appspot.com/admin/auth

  XSRF Settings:
    This is used to generate a unique key for each user of the app.
    Replace this with a unique phrase or random set of characters.
    Keep this a secret.
"""

__author__ = 'pkeesey@gmail.com (Peter Keesey)'

# OAuth 2.0 Client Settings
AUTH_CONFIG = {
    'OAUTH_CLIENT_ID': '215262093087-dj6b6peu1immi7496efcon5ungejkuce.apps.googleusercontent.com',
    'OAUTH_CLIENT_SECRET': 'oGqRiolx38_Luu0dD75sI89X',

    # E.g. Local Dev Env on port 8080: http://localhost:8080
    # E.g. Hosted on App Engine: https://your-application-id.appspot.com
    'OAUTH_REDIRECT_URI': '%s%s' % (
        'https://ga-super-proxy-153816.appspot.com')
}

# XSRF Settings
XSRF_KEY = 'afhadslfkjhaeruiha'
