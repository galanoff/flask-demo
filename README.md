# Flask Demo App
## Description
### Directory structure
```
|-- build_rpm.sh             # script for quick rpm build
|-- package                  # directory with package metadata
|   `-- task.spec
|-- playbook
|   |-- install.yml          # main ansible playbook
`-- src                      # application sources
    |-- application.py       # main app code
    |-- manager.py           # app sell utility
    |-- settings.py          # app configuration
    `-- tests                # unit test for application
        |-- __init__.py
        `-- unit.py
```
### Run application from CLI
```
$ cd src/
$ ./manager.py runserver
```
### Ansible playbook
It works with Centos, however it could be extended to support Ubuntu as well.
The playbook installs:
* mongodb without auth
* httpd apache as a uwsgi server for the application with default number of threads equal to 5
* test task application from rpm and pushes configuration
```
cd playbook
ansible-playbook -i <inventory> install.yml
```
## Tests
### Unit Tests
TODO:
### Smoke Tests
```
$ curl -i -X POST  -H "Content-Type: application/json" --data '[{"date": "2015-05-12T14:36:00.451765", "uid": "1", "md5checksum": "e8c83e232b64ce94fdd0e4539ad0d44f", "name": "John Doe"}]' http://127.0.0.1:8080/v1/store

$ curl -i http://127.0.0.1:8080/v1/payloads/1/20150512
```
