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
    'OAUTH_CLIENT_ID': '108665138304118945677',
    'OAUTH_CLIENT_SECRET': 'MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDGYQcfSI2B9yHk\nqWXL2TAYPLOEKwwFMrpq2N7qpC6gJSztTGziXEaRywgiuE+MJQvM/W6rRmWT6fR8\nH76KvZc2ytcU3jnT7L2igRFymEAvNxfNvdVaMzSSCOCvJUdYyta+/y/MVYszXPAj\nOqbVMvtYdcYLmaDqCUdpAsMLKVovXrITx065YgpPswqmDWmji8niOTSpRqMatqjJ\nYoTsHCsaP/b87kS7D37NnCM0Y1o8MMMZ/vLH/Qg0STO9pQxmTjnoHsV3wRj7TbAK\nBqMbtD4JR3vd/wcJ4Ge0UHV4BabhPvFQORO+8oMPWXYPEw62iMk3HjMuP98SJl3A\npBzUdkopAgMBAAECggEAUdJ9VIrhSuS6xwyTnxOywZxv0qjKqW4185IFx7P2Qzly\nIWIvWuICfWnHrkJlFQHGr0MsnVpI1Uxe+b9CIQl30DKzqbjLEz0HLnqbzq87cf4A\nRGzzDeQm38Dno3X1yorHLjok5du2sXW42l77pt4DS4YwLGKuOzmeiZKJDhZ9SyHC\n0WPJqJmUZ+pCAD5urDU8Y+9sQdDvOOGKgX0uJ293ZHtO7hgovUZ9brxPxsw9ew+H\nRCsNMkVSxFJV4nG9O62PjMdkAq9yotB0D58ZIOwre2qNORMGimhedl9cQRsHwczD\nrsgBn5q67HQ3M+fw8N5Wr6mUJEQFBY0qhFxOtFapXQKBgQDmXux36jJS6ITwBUa9\nFKu5QPDLIArFmwtrXQ+jQahQ0Iy4pf4KMIAheBmPo+1I7oyM1V0Fg43HQpsS8VJw\nS3OBo1xdp44Zln4tPl9E/kPwtFr67elOUKJJIM5IvZAfD3Ij03dbHeJOArkiOH3M\nUMPLInW32JWaTM/NCGqoLrNuawKBgQDccvZLPyyQCdwi/svRQCp4SMDd+ZT0cp7i\n+BWhBenvESAmz5CO5E+QWZz+nAspJb3fzefuG25wWQqbTXLSh03jw41tzrU+bXwd\nKmy1hN+zdQw+OvxL8KpepbZyUGBKDcgqv6tlKK3XKlprMQuAWLnP2spLMAIpodTA\nRD1UGbJmuwKBgGRnDKK6xJIT2xSNCCaSYsGLxyaQYYF8MH7rgUxC6mvGaP51AgJI\n3x83K9TJujomFcWvnCoyCtHEerfHy4k7qSzgGPqMc0c9quJnI7h7JPs8b8abeCp0\nxDYhASb8z1pqLfHlUUi5/o7Haw66FkG9FYhsDWhCEfm87nhK6clBCVzfAoGBAJOA\nzLGejKe4ITa9PA1AHOqs63fbRsKlaxC9JGPAvD19PQEbA0PJGj+g5n4qVQFsQnbc\npGJasnOz8Hfnw3uAkypiL2CY3gbuZQxy1ZhDVxcRq2Z8O1JoruZzhPdKNpN2U0ff\nRcSDCoaczTFJ+MMhGvssDw1uCxRmNx+KyWpbY1Z/AoGBANAml9F8waeDzLPheqHB\n04HVqyi8KDQz1H79767k9OjZdMab6ZPf1x+Dj+ZFecQ/G+IyFqZBgGYYgcjZdAHZ\nnXRMVKKdUkPLLUnr8JbEnc8hA123YEB117BYI9RXK+kIUSo52l7n+nwWTW+W6HxT\nD7npum/C4x2l4g+UhIO7mKi+',

    # E.g. Local Dev Env on port 8080: http://localhost:8080
    # E.g. Hosted on App Engine: https://your-application-id.appspot.com
    'OAUTH_REDIRECT_URI': '%s%s' % (
        https://ga-super-proxy-153816.appspot.com)
}

# XSRF Settings
XSRF_KEY = 'REPLACE THIS WITH A SECRET PHRASE THAT SHOULD NOT BE SHARED'
