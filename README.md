# University of Michigan Requests Client

A wrapper around the Python [Requests](http://www.python-requests.org/en/latest/) library
that allows you to access authenticated University of Michigan resources.

## Install

With pip:

    pip install umclient

If you don't have pip you can get it with:

    easy_install pip

## Quickstart

Create a new requests client:

    from umclient import AuthenticatedUMClient

    client = AuthenticatedUMClient(username, password)

Request the authenticated resource:

    resp = client.get('http://wolverineaccess.umich.edu')
    print resp # returns a requests response object
    <Response [200]>

The client automatically logged the user in and returned the
appropriate resource.

## License

Licensed under the MIT License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
