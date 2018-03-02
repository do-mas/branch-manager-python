import urllib2
import os
from jinja2 import Template
import jinja2
from string import Template

import sys
import subprocess
from profile import run

from subprocess import Popen, PIPE

from jinja2 import Environment, FileSystemLoader

#Import YAML module


def buildPipelineTemplate():
    pass


def create_pipeline(concourse_url, branch, git_repo):
    create_pipeline_config(branch, git_repo)
    # push_pipeline(concourse_url)


def push_pipeline(concourse_url, branch):
    print("downloading fly cli ...")

    fly = urllib2.urlopen(concourse_url)
    with open("fly", "wb") as code:
        code.write(fly.read())
    print("fly downloaded")
    os.system("fly -version")
    os.system("fly -t ci login -c http://104.196.14.231:8080 -u admin -p admin")
    os.system("fly -t ci set-pipeline -p ruby-pipe3 -c pipeline-test.yml -n")


def create_pipeline_config(branch, git_repo):
    s = Template('pipelines/pipeline-${pipe_name}.yml')
    string = s.safe_substitute(pipe_name='pipe1')

    print(string)
    # print("creating pipeline config")
    # context = {
    #     'branch': branch,
    #     'git_repo': git_repo
    # }
    # result = render('pipeline-template.yml', context)
    # os.system("mkdir pipelines")
    # f = open(s, 'a')
    # f.write(result)
    # f.close()


def render(template_path, context):
    path, filename = os.path.split(template_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(context)


create_pipeline("http://104.196.14.231:8080/api/v1/cli?arch=amd64&platform=linux", "test", "repo")
