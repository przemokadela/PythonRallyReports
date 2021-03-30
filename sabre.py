import pyral
from IPython.display import display, Markdown



rally_server = "rally1.rallydev.com"
rally_user = "przemyslaw.kadela@sabre.com"
rally_workspace = "Sabre Production Workspace"
rally_apikey = "_HD3HAAWlR4KiB63cDdlYzssaKrhSEEyv6N325XjKEw"
rally_project = "Sabre"

def open_rally_connection(project=rally_project, server=rally_server, user=rally_user, workspace=rally_workspace, apikey=rally_apikey):
    return pyral.Rally(server,user, apikey=apikey, workspace=workspace, project=project)

def markdown(txt):
    display(Markdown(txt))