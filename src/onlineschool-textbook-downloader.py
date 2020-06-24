"""
MIT License

Copyright (c) 2019-2020 Lee Kyung-ha <i_am@nulleekh.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from requests import get  


def download(downloading_file_url, downloaded_file_name = None):
    with open(downloaded_file_name, "wb") as file:
        response = get(downloading_file_url)
        file.write(response.content)


if __name__ == '__main__':
    # Following variables are example for this[http://bf2009down.kedicdn.re.kr/2015hs/for2/spa1/webbook_01.zip].
    # Please modify it to suit your situation.

    curriculum = "2015"
    # Enter the year of your curriculum
    school_type = "hs"
    # Enter type of your school
    subject_type = "for2"
    # Enter type of your subject
    subject_name = "spa1"
    # Enter name of your subject
    file_name = "webbook"
    # Enter name of your textbook
    file_type = "zip"
    # Enter type of your textbook

    endpoint = 17
    # Enter number of your lessons

    for i in range (1, endpoint+1):
        if i < 10:
            url = "http://bf2009down.kedicdn.re.kr/" + curriculum + school_type + "/" + subject_type + "/" + subject_name + "/" + file_name + "_0" + str(i) + "." + file_type
            download(url, file_name + "_0" + str(i) + "." + file_type)

        else:
            url = "http://bf2009down.kedicdn.re.kr/" + curriculum + school_type + "/" +subject_type + "/" + subject_name + "/" + file_name + "_" + str(i) + "." + file_type
            download(url, file_name + "_" + str(i) + "." + file_type)
