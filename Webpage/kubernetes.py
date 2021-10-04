#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

kube = cgi.FieldStorage()
y = kube.getvalue("x").lower()

# Get Pods
if ('list' in y or 'show' in y or 'get' in y) and ('pod' in y or 'pods' in y):    
    cmd = "sudo kubectl get pods"
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Get all resourses
elif ('list' in y or 'show' in y or 'get' in y) and ('every' in y or 'all' in y) and ('resources' in y or 'resource' in y):    
    cmd = "sudo kubectl get all"
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Launch Pod
elif ('run' in y or 'create' in y or 'launch' in y) and ('pod' in y or 'pods' in y) and ('image' in y):
    str = y.split()
    if 'pod' in str:
        i = str.index(('pod')) + 1
    elif 'pods' in str:
        i = str.index('pods') + 1
    j = str.index('image') + 1
    cmd = "sudo kubectl run {0} --image={1}".format(str[i], str[j])
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Launch Deployment
elif ('deployment' in y or 'deploy' in y) and ('create' in y or 'launch' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index(('deployment')) + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    j = str.index('image') + 1
    cmd = "sudo kubectl create deployment {0} --image={1}".format(str[i], str[j])
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Expose deployment
elif ('deployment' in y or 'deploy' in y) and ('expose' in y or 'service' in y or 'services' in y) and ('port' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index(('deployment')) + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    port = str.index('port') + 1
    cmd = "sudo kubectl expose deployment {0} --port={1} --type=NodePort".format(str[i], str[port])
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Scale deployment
elif ('deployment' in y or 'deploy' in y) and ('scale' in y or 'replica' in y or 'replicas' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index('deployment') + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    j = str.index('to') + 1
    cmd = "sudo kubectl scale deployment {0} --replicas={1}".format(str[i], str[j])
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Delete deployment
elif ('deployment' in y or 'deploy' in y) and ('delete' in y or 'remove' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index(('deployment')) + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    cmd = "sudo kubectl delete deploy {}".format(str[i])
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Get all deployment
elif ('list' in y or 'show' in y or 'get' in y) and ('every' in y or 'all' in y) and ('deploy' in y or 'deployment' in y):    
    cmd = "sudo kubectl get deployment"
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# List Services
elif ('list' in y or 'show' in y or 'get' in y) and ('svc' in y or 'services' in y or 'service' in y):    
    cmd = "sudo kubectl get svc"
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# Delete Service
elif ('deployment' in y or 'deploy' in y) and ('expose' in y or 'service' in y or 'services' in y) and ('delete' in y or 'remove' in y):
    str = y.split()
    if 'deployment' in str:
        i = str.index(('deployment')) + 1
    elif 'deploy' in str:
        i = str.index('deploy') + 1
    cmd = "sudo kubectl delete svc {}".format(str[i])
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

# delete all resourses
elif ('delete' in y or 'terminate' in y) and ('every' in y or 'all' in y) and ('resources' in y or 'resource' in y):    
    cmd = "sudo kubectl delete all --all"
    output = subprocess.getoutput(cmd)
    print("<pre>{}</pre>".format(output))

else:
    print("Please enter right requirement !!")
